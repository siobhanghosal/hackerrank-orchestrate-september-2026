"""Deterministic OCR extraction for linked financial-event documents.

The extractor intentionally knows nothing about requests or sample answers.  It
returns a value only when OCR finds a strong financial label immediately beside
one amount.  Callers must still verify that the document is linked to the event
and that its currency is compatible with the event record.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Protocol


class ImageEvidenceError(RuntimeError):
    """Raised when the optional local OCR dependency is unavailable."""


@dataclass(frozen=True)
class ImageAmountExtraction:
    amount: Decimal
    label: str
    ocr_confidence: Decimal
    detected_currency: str | None
    reason: str


class ImageAmountExtractor(Protocol):
    def extract(self, image_path: Path, *, direction: str, currency: str,
                description: str) -> ImageAmountExtraction | None:
        """Return one high-confidence financial amount, or ``None`` when ambiguous."""


NUMBER = re.compile(r"(?<![\d.-])(?P<value>\d{1,3}(?:,\d{2,3})+(?:\.\d{1,2})?|\d+(?:\.\d{1,2})?)(?![\d.-])")
DATE_LIKE = re.compile(r"\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b|\b\d{4}[-/]\d{1,2}[-/]\d{1,2}\b")
DOCUMENT_CURRENCY = re.compile(r"\b(?P<currency>INR|IDR|EUR|USD|ZAR)\b", re.IGNORECASE)

# Ordered from the most specific financial obligation to more general document
# totals.  A direction-specific choice avoids treating a previous balance on a
# debit bill as its current amount due, or a gross amount as salary net pay.
DEBIT_LABELS = (
    ("amount due after", 100),
    ("total amount due", 95),
    ("amount due", 90),
    ("balance due", 85),
    ("invoice total", 80),
    ("cash paid", 75),
    ("total payable", 70),
    ("net amount", 65),
    ("item bill", 65),
)
CREDIT_LABELS = (
    ("net pay", 100),
    ("net salary", 100),
    ("amount credited", 90),
    ("cash received", 85),
)


def _compact(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.casefold())


def _label_score(text: str, direction: str) -> tuple[str, int] | None:
    compact = _compact(text)
    labels = CREDIT_LABELS if direction == "credit" else DEBIT_LABELS
    for label, score in labels:
        if _compact(label) in compact:
            return label, score
    return None


def _money_in_line(text: str) -> Decimal | None:
    """Accept a single plausible money value, never a date or a bare year."""
    if DATE_LIKE.search(text):
        return None
    matches = list(NUMBER.finditer(text))
    if len(matches) != 1:
        return None
    source_value = matches[0].group("value")
    raw = source_value.replace(",", "")
    try:
        amount = Decimal(raw)
    except InvalidOperation:
        return None
    if (not amount.is_finite() or amount <= 0
            or ("," not in source_value and "." not in source_value and amount >= Decimal("1900"))):
        return None
    return amount


class RapidOcrImageAmountExtractor:
    """Offline OCR adapter.  Model files are distributed with the package."""

    def __init__(self, minimum_ocr_confidence: Decimal = Decimal("0.80")) -> None:
        try:
            from rapidocr_onnxruntime import RapidOCR
        except ImportError as exc:  # pragma: no cover - depends on installation
            raise ImageEvidenceError(
                "rapidocr-onnxruntime is required for --image-evidence-provider rapidocr"
            ) from exc
        self._ocr = RapidOCR()
        self.minimum_ocr_confidence = minimum_ocr_confidence

    def extract(self, image_path: Path, *, direction: str, currency: str,
                description: str) -> ImageAmountExtraction | None:
        if not image_path.is_file() or direction not in {"credit", "debit"}:
            return None
        try:
            result, _ = self._ocr(str(image_path))
        except Exception as exc:  # pragma: no cover - package/native failures
            raise ImageEvidenceError(f"OCR failed for {image_path.name}: {exc}") from exc
        lines: list[tuple[str, Decimal]] = []
        for row in result or []:
            if not isinstance(row, (tuple, list)) or len(row) < 3:
                continue
            text = str(row[1]).strip()
            try:
                confidence = Decimal(str(row[2]))
            except InvalidOperation:
                continue
            if text and confidence.is_finite():
                lines.append((text, confidence))

        candidates: list[tuple[int, Decimal, Decimal, str]] = []
        for index, (label_text, label_confidence) in enumerate(lines):
            label = _label_score(label_text, direction)
            if label is None or label_confidence < self.minimum_ocr_confidence:
                continue
            label_name, score = label
            # OCR normally emits labels and values on consecutive lines.  Three
            # lines permits an intervening date but prevents a distant unrelated
            # document total being joined to this label.
            for offset in range(0, 4):
                value_index = index + offset
                if value_index >= len(lines):
                    break
                value_text, value_confidence = lines[value_index]
                if value_confidence < self.minimum_ocr_confidence:
                    continue
                amount = _money_in_line(value_text)
                if amount is None:
                    continue
                candidates.append((score - offset, amount, min(label_confidence, value_confidence), label_name))
                break

        if not candidates:
            return None
        candidates.sort(key=lambda item: (-item[0], item[1], item[3]))
        best_score, best_amount, confidence, label = candidates[0]
        # Equal strongest labels with distinct values mean the document cannot be
        # resolved safely without understanding the layout.
        if any(score == best_score and amount != best_amount for score, amount, _, _ in candidates[1:]):
            return None
        currencies = {match.group("currency").upper() for match in DOCUMENT_CURRENCY.finditer("\n".join(text for text, _ in lines))}
        # Several document currencies are a conflict; no inferred conversion is
        # permitted. A missing visible currency is acceptable because the linked
        # event's CSV currency remains the authoritative source.
        if len(currencies) > 1:
            return None
        return ImageAmountExtraction(
            best_amount,
            label,
            confidence,
            next(iter(currencies), None),
            f"offline OCR found '{label}' adjacent to one amount for {description}",
        )
