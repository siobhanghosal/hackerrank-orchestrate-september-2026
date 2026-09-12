"""Deterministic, Python-first Buy or Wait baseline.

This module deliberately supplies the financial foundation before a complete
recommendation policy: typed CSV loading, event normalization, a 90-day cash
simulator, output validation, a small generic baseline, and sample evaluation.
It uses only participant-facing files under ``dataset/`` and no model/API key.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import defaultdict
from dataclasses import dataclass, field, replace
from datetime import date, timedelta
from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_FLOOR
from itertools import combinations, permutations
from pathlib import Path
from statistics import median
from typing import Iterable, Mapping, Sequence


MONEY_ZERO = Decimal("0")
FORECAST_DAYS = 90
OUTPUT_COLUMNS = (
    "request_id",
    "amount_safe_to_pay",
    "affordability_status",
    "recommended_payment_method",
    "payment_plan",
    "earliest_date_for_full_payment",
    "spending_changes_needed",
    "decision_explanation",
)
STATUSES = frozenset({"affordable_now", "affordable_with_plan", "affordable_later", "not_affordable"})
METHODS = frozenset({"full_payment", "partial_payment", "installments", "wait", "not_recommended"})
IGNORED_EVENT_STATUSES = frozenset({"cancelled", "failed", "unrealized"})
NON_CASH_EVENT_TYPES = frozenset({"investment_value"})


class DatasetError(ValueError):
    """Raised when a participant-facing CSV is malformed or incomplete."""


def parse_decimal(value: str | None, *, field_name: str, allow_blank: bool = False) -> Decimal | None:
    """Parse money without float rounding; blank amounts are never silently zero."""
    raw = (value or "").strip()
    if not raw:
        if allow_blank:
            return None
        raise DatasetError(f"Missing required money field: {field_name}")
    try:
        return Decimal(raw)
    except InvalidOperation as exc:
        raise DatasetError(f"Invalid decimal in {field_name}: {value!r}") from exc


def parse_date(value: str | None, *, field_name: str, allow_blank: bool = False) -> date | None:
    raw = (value or "").strip()
    if not raw:
        if allow_blank:
            return None
        raise DatasetError(f"Missing required date field: {field_name}")
    try:
        return date.fromisoformat(raw)
    except ValueError as exc:
        raise DatasetError(f"Invalid ISO date in {field_name}: {value!r}") from exc


def parse_bool(value: str | None, *, field_name: str) -> bool:
    raw = (value or "").strip().lower()
    if raw in {"true", "1", "yes"}:
        return True
    if raw in {"false", "0", "no"}:
        return False
    raise DatasetError(f"Invalid boolean in {field_name}: {value!r}")


def split_values(value: str | None) -> frozenset[str]:
    return frozenset(part.strip() for part in (value or "").split("|") if part.strip())


def money_text(value: Decimal) -> str:
    """Render Decimal CSV money without exponent notation or redundant zeroes."""
    rendered = format(value, "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


@dataclass(frozen=True)
class Profile:
    user_id: str
    home_currency: str
    current_available_balance: Decimal
    minimum_balance_to_keep: Decimal
    financial_priorities: frozenset[str]
    protected_categories: frozenset[str]
    reducible_categories: frozenset[str]
    stoppable_categories: frozenset[str]
    payment_methods: frozenset[str]
    max_installment_months: int | None


@dataclass(frozen=True)
class Request:
    request_id: str
    user_id: str
    request_date: date
    request_type: str
    requested_amount: Decimal
    desired_completion_date: date
    allows_partial_payment: bool
    request_text: str


@dataclass(frozen=True)
class FinancialEvent:
    event_id: str
    user_id: str
    event_type: str
    description: str
    category: str
    direction: str
    amount: Decimal | None
    currency: str
    event_date: date
    settlement_date: date | None
    status: str
    linked_event_id: str | None
    flexibility: str
    minimum_allowed_amount: Decimal | None


@dataclass(frozen=True)
class PaymentOption:
    payment_option_id: str
    request_id: str
    payment_method: str
    payment_amount: Decimal
    number_of_payments: int
    first_payment_date: date
    payment_frequency_days: int | None
    financing_fee: Decimal
    total_payable_amount: Decimal


@dataclass(frozen=True)
class ExchangeRate:
    rate_date: date
    from_currency: str
    to_currency: str
    rate: Decimal


@dataclass(frozen=True)
class NormalizedEvent:
    """An event classified for the cash forecast, with money in home currency."""
    source: FinancialEvent
    amount_home: Decimal | None
    cash_date: date | None
    include_in_cash_flow: bool
    reason: str
    evidence_sources: tuple[str, ...] = ()


@dataclass(frozen=True)
class EvidenceFact:
    source_id: str
    source_kind: str
    user_id: str
    action: str
    effective_date: date
    target_event_id: str | None
    amount: Decimal | None
    currency: str | None
    confidence: str
    reason: str


@dataclass(frozen=True)
class EvidenceResolution:
    facts: tuple[EvidenceFact, ...]

    def facts_for_event(self, event_id: str) -> tuple[EvidenceFact, ...]:
        return tuple(fact for fact in self.facts if fact.target_event_id == event_id)

    def facts_for_salary(self) -> tuple[EvidenceFact, ...]:
        return tuple(fact for fact in self.facts if fact.action in {"amend_salary", "remove_salary"})


@dataclass(frozen=True)
class CashFlow:
    flow_date: date
    amount: Decimal
    source_id: str
    category: str
    description: str
    kind: str  # explicit, recurring, or requested_payment


@dataclass(frozen=True)
class RecurringRule:
    description: str
    category: str
    direction: str
    amount: Decimal
    interval_days: int
    next_date: date
    source_event_ids: tuple[str, ...]
    flexibility: str
    evidence_sources: tuple[str, ...] = ()


@dataclass
class SimulationResult:
    ending_balance: Decimal
    minimum_balance: Decimal
    minimum_balance_date: date
    daily_balances: dict[date, Decimal]
    applied_flows: list[CashFlow]

    @property
    def is_safe(self) -> bool:
        return self.minimum_balance >= MONEY_ZERO  # replaced by caller's profile threshold


@dataclass(frozen=True)
class Dataset:
    profiles: Mapping[str, Profile]
    requests: Mapping[str, Request]
    samples: Mapping[str, Request]
    sample_labels: Mapping[str, Mapping[str, str]]
    events: tuple[FinancialEvent, ...]
    payment_options: Mapping[str, tuple[PaymentOption, ...]]
    exchange_rates: Mapping[tuple[date, str, str], Decimal]
    messages: tuple[Mapping[str, str], ...]
    images: tuple[Mapping[str, str], ...]


def read_csv(path: Path, required_columns: Iterable[str]) -> list[dict[str, str]]:
    """Read a UTF-8 CSV and reject missing headers/duplicate headers early."""
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if not reader.fieldnames:
                raise DatasetError(f"CSV has no header: {path}")
            fields = [name.strip() for name in reader.fieldnames]
            if len(set(fields)) != len(fields):
                raise DatasetError(f"CSV has duplicate headers: {path}")
            missing = set(required_columns) - set(fields)
            if missing:
                raise DatasetError(f"CSV {path} is missing columns: {sorted(missing)}")
            return [{key.strip(): (value or "").strip() for key, value in row.items()} for row in reader]
    except OSError as exc:
        raise DatasetError(f"Unable to read {path}: {exc}") from exc


def require_unique(rows: Iterable[object], key_name: str) -> dict[str, object]:
    indexed: dict[str, object] = {}
    for row in rows:
        key = getattr(row, key_name)
        if not key or key in indexed:
            raise DatasetError(f"Duplicate or blank {key_name}: {key!r}")
        indexed[key] = row
    return indexed


def load_dataset(dataset_dir: Path) -> Dataset:
    """Load every participant-facing CSV once, preserving all money as Decimal."""
    profile_rows = read_csv(dataset_dir / "financial_profiles.csv", {
        "user_id", "home_currency", "current_available_balance", "minimum_balance_to_keep",
        "financial_priorities", "expense_categories_to_protect",
        "expense_categories_user_is_willing_to_reduce", "expense_categories_user_is_willing_to_stop",
        "payment_methods_user_will_consider", "max_installment_months",
    })
    profiles = require_unique((Profile(
        user_id=row["user_id"], home_currency=row["home_currency"],
        current_available_balance=parse_decimal(row["current_available_balance"], field_name="current_available_balance") or MONEY_ZERO,
        minimum_balance_to_keep=parse_decimal(row["minimum_balance_to_keep"], field_name="minimum_balance_to_keep") or MONEY_ZERO,
        financial_priorities=split_values(row["financial_priorities"]),
        protected_categories=split_values(row["expense_categories_to_protect"]),
        reducible_categories=split_values(row["expense_categories_user_is_willing_to_reduce"]),
        stoppable_categories=split_values(row["expense_categories_user_is_willing_to_stop"]),
        payment_methods=split_values(row["payment_methods_user_will_consider"]),
        max_installment_months=int(row["max_installment_months"]) if row["max_installment_months"] else None,
    ) for row in profile_rows), "user_id")

    request_columns = {"request_id", "user_id", "request_date", "request_type", "requested_amount", "desired_completion_date", "allows_partial_payment", "request_text"}
    def parse_request(row: Mapping[str, str]) -> Request:
        return Request(
            request_id=row["request_id"], user_id=row["user_id"],
            request_date=parse_date(row["request_date"], field_name="request_date") or date.min,
            request_type=row["request_type"],
            requested_amount=parse_decimal(row["requested_amount"], field_name="requested_amount") or MONEY_ZERO,
            desired_completion_date=parse_date(row["desired_completion_date"], field_name="desired_completion_date") or date.min,
            allows_partial_payment=parse_bool(row["allows_partial_payment"], field_name="allows_partial_payment"),
            request_text=row["request_text"],
        )
    request_rows = read_csv(dataset_dir / "requests.csv", request_columns)
    sample_rows = read_csv(dataset_dir / "sample_requests.csv", request_columns | set(OUTPUT_COLUMNS[1:]))
    requests = require_unique((parse_request(row) for row in request_rows), "request_id")
    samples = require_unique((parse_request(row) for row in sample_rows), "request_id")
    for request in list(requests.values()) + list(samples.values()):
        if request.user_id not in profiles:
            raise DatasetError(f"Unknown profile user_id on {request.request_id}: {request.user_id}")

    event_rows = read_csv(dataset_dir / "financial_events.csv", {
        "event_id", "user_id", "event_type", "description", "category", "direction", "amount", "currency",
        "event_date", "settlement_date", "status", "linked_event_id", "flexibility", "minimum_allowed_amount",
    })
    events = tuple(FinancialEvent(
        event_id=row["event_id"], user_id=row["user_id"], event_type=row["event_type"], description=row["description"],
        category=row["category"], direction=row["direction"].lower(),
        amount=parse_decimal(row["amount"], field_name=f"{row['event_id']}.amount", allow_blank=True), currency=row["currency"],
        event_date=parse_date(row["event_date"], field_name=f"{row['event_id']}.event_date") or date.min,
        settlement_date=parse_date(row["settlement_date"], field_name=f"{row['event_id']}.settlement_date", allow_blank=True),
        status=row["status"].lower(), linked_event_id=row["linked_event_id"] or None,
        flexibility=row["flexibility"].lower(),
        minimum_allowed_amount=parse_decimal(row["minimum_allowed_amount"], field_name=f"{row['event_id']}.minimum_allowed_amount", allow_blank=True),
    ) for row in event_rows)
    require_unique(events, "event_id")

    option_rows = read_csv(dataset_dir / "request_payment_options.csv", {
        "payment_option_id", "request_id", "payment_method", "payment_amount", "number_of_payments",
        "first_payment_date", "payment_frequency_days", "financing_fee", "total_payable_amount",
    })
    options = tuple(PaymentOption(
        payment_option_id=row["payment_option_id"], request_id=row["request_id"], payment_method=row["payment_method"],
        payment_amount=parse_decimal(row["payment_amount"], field_name="payment_amount") or MONEY_ZERO,
        number_of_payments=int(row["number_of_payments"]),
        first_payment_date=parse_date(row["first_payment_date"], field_name="first_payment_date") or date.min,
        payment_frequency_days=int(row["payment_frequency_days"]) if row["payment_frequency_days"] else None,
        financing_fee=parse_decimal(row["financing_fee"], field_name="financing_fee") or MONEY_ZERO,
        total_payable_amount=parse_decimal(row["total_payable_amount"], field_name="total_payable_amount") or MONEY_ZERO,
    ) for row in option_rows)
    require_unique(options, "payment_option_id")
    options_by_request: dict[str, list[PaymentOption]] = defaultdict(list)
    for option in options:
        options_by_request[option.request_id].append(option)

    rate_rows = read_csv(dataset_dir / "exchange_rates.csv", {"rate_date", "from_currency", "to_currency", "rate"})
    exchange_rates: dict[tuple[date, str, str], Decimal] = {}
    for row in rate_rows:
        key = (parse_date(row["rate_date"], field_name="rate_date") or date.min, row["from_currency"], row["to_currency"])
        if key in exchange_rates:
            raise DatasetError(f"Duplicate exchange-rate row: {key}")
        exchange_rates[key] = parse_decimal(row["rate"], field_name="rate") or MONEY_ZERO

    messages = tuple(read_csv(dataset_dir / "messages.csv", {"message_id", "user_id", "request_id", "related_event_id", "sent_at", "source_type", "message_text"}))
    images = tuple(read_csv(dataset_dir / "images.csv", {"image_id", "user_id", "request_id", "related_event_id"}))
    labels = {row["request_id"]: {column: row[column] for column in OUTPUT_COLUMNS[1:]} for row in sample_rows}
    return Dataset(profiles, requests, samples, labels, events, {key: tuple(value) for key, value in options_by_request.items()}, exchange_rates, messages, images)


MONEY_IN_TEXT = re.compile(r"\b(?P<currency>INR|IDR|EUR|USD|ZAR)\s?(?P<amount>[0-9][0-9,]*(?:\.\d+)?)\b", re.IGNORECASE)
DATE_IN_TEXT = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")


def text_amount(text: str) -> tuple[Decimal, str] | None:
    match = MONEY_IN_TEXT.search(text)
    if not match:
        return None
    try:
        return Decimal(match.group("amount").replace(",", "")), match.group("currency").upper()
    except InvalidOperation:
        return None


def text_date(text: str, fallback: date) -> date:
    match = DATE_IN_TEXT.search(text)
    return date.fromisoformat(match.group(1)) if match else fallback


def credit_is_confirmed(event: FinancialEvent, override: EvidenceFact | None) -> bool:
    """Return true only for settled or explicitly attributable future credits."""
    if event.direction != "credit":
        return False
    if event.status == "settled" or (override is not None and override.action == "confirm_credit"):
        return True
    # The supplied scheduled-salary records identify themselves as confirmed and
    # include a settlement date.  Do not treat an arbitrary scheduled income row
    # as confirmed merely because it is categorised as salary.
    return (event.status == "scheduled" and event.event_type == "income" and event.category == "salary"
            and "confirmed" in event.description.casefold() and event.settlement_date is not None)


def resolve_evidence(dataset: Dataset, user_id: str) -> EvidenceResolution:
    """Extract only explicit, high-confidence textual evidence; never infer from a vague notice."""
    events = {event.event_id: event for event in dataset.events if event.user_id == user_id}
    facts: list[EvidenceFact] = []
    for message in dataset.messages:
        if message["user_id"] != user_id:
            continue
        source_id = message["message_id"]
        body = message["message_text"]
        text = body.lower()
        sent_date = date.fromisoformat(message["sent_at"][:10])
        target_id = message["related_event_id"] or None
        target = events.get(target_id or "")
        amount_info = text_amount(body)
        effective_date = text_date(body, sent_date)
        unavailable = any(phrase in text for phrase in (
            "not reached your account", "not been credited", "not withdrawable", "not available", "still pending",
            "still in payment processing", "no cash proceeds", "belum masuk", "belum dapat ditarik", "belum disetujui",
        ))
        cancelled = any(phrase in text for phrase in ("has been cancelled", "was cancelled", "voided", "reversed and posted"))
        available = any(phrase in text for phrase in ("has reached your account", "credit is settled", "now available"))
        salary_notice = message["source_type"] == "employer" and any(word in text for word in ("salary", "payroll", "gaji"))
        if target is not None and cancelled:
            facts.append(EvidenceFact(source_id, "message", user_id, "cancel_event", effective_date, target_id, None, None, "high", "explicit cancellation/reversal of the related event"))
        elif target is not None and unavailable and target.direction == "credit":
            facts.append(EvidenceFact(source_id, "message", user_id, "exclude_credit", effective_date, target_id, None, None, "high", "explicit statement that the related credit is not yet available"))
        elif target is not None and available and target.direction == "credit":
            facts.append(EvidenceFact(source_id, "message", user_id, "confirm_credit", effective_date, target_id, None, None, "high", "explicit statement that the related credit has reached the account"))
        elif target is not None and amount_info is not None and (DATE_IN_TEXT.search(body) or "amend" in text or "updated" in text):
            amount, currency = amount_info
            facts.append(EvidenceFact(source_id, "message", user_id, "amend_event", effective_date, target_id, amount, currency, "high", "explicit amount/date amendment tied to the related event"))
        elif salary_notice and ("no off-season income" in text or "employment has ended" in text or "income that has ended should be removed" in text):
            facts.append(EvidenceFact(source_id, "message", user_id, "remove_salary", effective_date, None, None, None, "high", "employer explicitly states future regular income is absent"))
        elif salary_notice and amount_info is not None and any(phrase in text for phrase in (
            "effective from", "applies from", "berlaku mulai", "next salary", "first salary", "regular salary", "monthly pay", "gaji bulanan", "gaji pokok", "gaji pertama",
        )):
            amount, currency = amount_info
            facts.append(EvidenceFact(source_id, "message", user_id, "amend_salary", effective_date, None, amount, currency, "high", "employer explicitly states a salary amount and effective/next-pay context"))
        elif salary_notice and ("expected on" in text or "replaces the payroll date" in text or "diperkirakan masuk pada" in text):
            facts.append(EvidenceFact(source_id, "message", user_id, "amend_salary", effective_date, None, None, None, "high", "employer explicitly states a replacement salary date"))
        else:
            facts.append(EvidenceFact(source_id, "message", user_id, "ignore", sent_date, target_id, None, None, "low", "does not meet an explicit high-confidence resolver pattern"))
    return EvidenceResolution(tuple(facts))


def normalize_events(dataset: Dataset, user_id: str, resolution: EvidenceResolution | None = None) -> list[NormalizedEvent]:
    """Classify events conservatively; missing/foreign unconvertible money is excluded, never zeroed."""
    profile = dataset.profiles[user_id]
    resolution = resolution or resolve_evidence(dataset, user_id)
    events = [event for event in dataset.events if event.user_id == user_id]
    child_ids = {event.linked_event_id for event in events if event.linked_event_id}
    normalized: list[NormalizedEvent] = []
    for event in events:
        cash_date = event.settlement_date or event.event_date
        evidence = resolution.facts_for_event(event.event_id)
        override = next((fact for fact in reversed(evidence) if fact.action in {"cancel_event", "exclude_credit", "confirm_credit", "amend_event"}), None)
        if override is not None and override.action in {"cancel_event", "exclude_credit"}:
            normalized.append(NormalizedEvent(event, None, cash_date, False, f"{override.reason}; evidence {override.source_id}", (override.source_id,)))
            continue
        if event.event_type in NON_CASH_EVENT_TYPES:
            normalized.append(NormalizedEvent(event, None, cash_date, False, "unavailable investment value"))
            continue
        if event.status in IGNORED_EVENT_STATUSES:
            normalized.append(NormalizedEvent(event, None, cash_date, False, f"{event.status} event"))
            continue
        effective_amount = override.amount if override is not None and override.action == "amend_event" and override.amount is not None else event.amount
        effective_currency = override.currency if override is not None and override.action == "amend_event" and override.currency else event.currency
        if override is not None and override.action in {"amend_event", "confirm_credit"}:
            cash_date = override.effective_date
        if effective_amount is None:
            normalized.append(NormalizedEvent(event, None, cash_date, False, "amount requires linked image review"))
            continue
        if event.direction not in {"credit", "debit"}:
            normalized.append(NormalizedEvent(event, None, cash_date, False, "unknown cash direction"))
            continue
        if effective_currency == profile.home_currency:
            amount_home = effective_amount
        else:
            rate = dataset.exchange_rates.get((cash_date, effective_currency, profile.home_currency))
            if rate is None:
                normalized.append(NormalizedEvent(event, None, cash_date, False, "missing dated exchange rate"))
                continue
            amount_home = effective_amount * rate
        confirmed_credit = credit_is_confirmed(event, override)
        if event.direction == "credit" and not confirmed_credit:
            reason = ("pending credit is not available"
                      if event.status == "pending" else "unconfirmed scheduled credit is unavailable")
            normalized.append(NormalizedEvent(event, amount_home, cash_date, False, reason,
                                              (override.source_id,) if override is not None else ()))
        elif event.event_id in child_ids and event.status != "scheduled":
            normalized.append(NormalizedEvent(event, amount_home, cash_date, False, "superseded transaction lifecycle record"))
        else:
            if event.status == "pending" and event.direction == "debit":
                reason = "pending debit retained as a conservative liability"
            else:
                reason = f"cash event; evidence {override.source_id}" if override is not None else "cash event"
            normalized.append(NormalizedEvent(event, amount_home, cash_date, True, reason, (override.source_id,) if override is not None else ()))
    return normalized


def future_explicit_flows(normalized: Iterable[NormalizedEvent], as_of: date) -> list[CashFlow]:
    flows: list[CashFlow] = []
    for item in normalized:
        event = item.source
        if not item.include_in_cash_flow or item.cash_date is None or item.cash_date <= as_of or item.amount_home is None:
            continue
        signed_amount = item.amount_home if event.direction == "credit" else -item.amount_home
        flows.append(CashFlow(item.cash_date, signed_amount, event.event_id, event.category, event.description, "explicit"))
    return flows


def is_terminal_salary_record(item: NormalizedEvent) -> bool:
    """A settled final/last payroll is explicit evidence that a prior salary stream ends."""
    return (item.include_in_cash_flow and item.cash_date is not None
            and item.source.category == "salary" and item.source.direction == "credit"
            and re.search(r"\b(final|last)\b", item.source.description, re.IGNORECASE) is not None
            and re.search(r"\b(payroll|salary|pay)\b", item.source.description, re.IGNORECASE) is not None)


def recurring_rules(normalized: Iterable[NormalizedEvent], as_of: date, resolution: EvidenceResolution | None = None) -> list[RecurringRule]:
    """Infer recurrence only from 3+ settled events with the same recurring obligation."""
    normalized = tuple(normalized)
    groups: dict[tuple[str, str, str], list[NormalizedEvent]] = defaultdict(list)
    for item in normalized:
        event = item.source
        if not item.include_in_cash_flow or item.amount_home is None or item.cash_date is None:
            continue
        if event.status != "settled" or item.cash_date >= as_of or event.event_type in NON_CASH_EVENT_TYPES:
            continue
        # A category alone is insufficient evidence: different grocery merchants or
        # restaurants are not automatically the same recurring commitment.
        groups[(event.description, event.category, event.direction)].append(item)
    rules: list[RecurringRule] = []
    for (description, category, direction), members in groups.items():
        members.sort(key=lambda item: item.cash_date or date.min)
        salary_facts: list[EvidenceFact] = []
        # Settlement dates normally determine cash timing.  A confirmed employer
        # replacement date is stronger evidence when a delayed prior settlement
        # would otherwise make a regular payroll cadence look irregular.  In that
        # narrow case, use the supplied intended payroll dates to establish the
        # fixed-day interval, then anchor future cash flow on the confirmation.
        if category == "salary" and direction == "credit" and resolution is not None:
            salary_facts = [fact for fact in resolution.facts_for_salary()
                            if fact.action == "amend_salary" and fact.effective_date > as_of]
        dates = ([item.source.event_date for item in members]
                 if salary_facts else [item.cash_date for item in members if item.cash_date])
        if len(dates) < 3:
            continue
        intervals = [(later - earlier).days for earlier, later in zip(dates, dates[1:]) if (later - earlier).days > 0]
        if len(intervals) < 2:
            continue
        typical_interval = int(round(median(intervals[-4:])))
        if not 5 <= typical_interval <= 35:
            continue
        # A three-occurrence sequence needs a tight cadence.  A 14-then-21 day
        # merchant pattern is ordinary variable spending, not a commitment.
        if max(abs(interval - typical_interval) for interval in intervals[-4:]) > max(2, typical_interval // 5):
            continue
        amounts = [item.amount_home for item in members[-3:] if item.amount_home is not None]
        amount = max(amounts) if direction == "debit" else min(amounts)
        last_date = dates[-1]
        next_date = last_date + timedelta(days=typical_interval)
        while next_date <= as_of:
            next_date += timedelta(days=typical_interval)
        evidence_sources: tuple[str, ...] = ()
        if category == "salary" and direction == "credit" and resolution is not None:
            terminal_records = [item for item in normalized if is_terminal_salary_record(item)
                                and last_date < item.cash_date <= as_of]
            if terminal_records:
                continue
            salary_facts = [fact for fact in resolution.facts_for_salary() if fact.effective_date <= as_of + timedelta(days=FORECAST_DAYS)]
            removal = [fact for fact in salary_facts if fact.action == "remove_salary" and fact.effective_date <= next_date]
            if removal:
                continue
            amendments = [fact for fact in salary_facts if fact.action == "amend_salary"]
            if amendments:
                amendment = amendments[-1]
                if amendment.amount is not None and amendment.currency:
                    if amendment.currency == members[-1].source.currency:
                        amount = amendment.amount
                    # A foreign-currency payroll change is only used if the stated
                    # home-currency amount can be converted on its effective date.
                    elif amendment.currency == "":
                        continue
                if amendment.effective_date > as_of:
                    next_date = amendment.effective_date
                evidence_sources = (amendment.source_id,)
        rules.append(RecurringRule(description, category, direction, amount, typical_interval, next_date,
                                   tuple(item.source.event_id for item in members[-3:]), members[-1].source.flexibility, evidence_sources))
    return rules


def recurring_flows(rules: Iterable[RecurringRule], as_of: date, horizon_days: int) -> list[CashFlow]:
    horizon = as_of + timedelta(days=horizon_days)
    flows: list[CashFlow] = []
    for rule in rules:
        flow_date = rule.next_date
        while flow_date <= horizon:
            signed_amount = rule.amount if rule.direction == "credit" else -rule.amount
            flows.append(CashFlow(flow_date, signed_amount, f"recurring:{rule.category}", rule.category,
                                  f"Inferred recurring {rule.description}", "recurring"))
            flow_date += timedelta(days=rule.interval_days)
    return flows


@dataclass(frozen=True)
class RecurrenceReconciliation:
    """Audit-only representation after the rejected hybrid candidate was reverted."""
    generated_before: tuple[CashFlow, ...]
    generated_after: tuple[CashFlow, ...]
    suppressions: tuple[object, ...] = ()


def reconcile_recurring_flows(rules: Sequence[RecurringRule], explicit_flows: Sequence[CashFlow], as_of: date, horizon_days: int) -> RecurrenceReconciliation:
    """Current active policy has no explicit-event suppression; retained for audit compatibility."""
    generated = tuple(recurring_flows(rules, as_of, horizon_days))
    return RecurrenceReconciliation(generated, generated)


def simulate_cash_flow(profile: Profile, flows: Iterable[CashFlow], as_of: date, horizon_days: int = FORECAST_DAYS) -> SimulationResult:
    """Run a daily forecast, processing debits before credits on each date conservatively."""
    horizon = as_of + timedelta(days=horizon_days)
    by_day: dict[date, list[CashFlow]] = defaultdict(list)
    for flow in flows:
        if as_of <= flow.flow_date <= horizon:
            by_day[flow.flow_date].append(flow)
    balance = profile.current_available_balance
    lowest, lowest_date = balance, as_of
    balances: dict[date, Decimal] = {}
    applied: list[CashFlow] = []
    current_day = as_of
    while current_day <= horizon:
        for flow in sorted(by_day[current_day], key=lambda item: (item.amount >= MONEY_ZERO, item.source_id)):
            balance += flow.amount
            applied.append(flow)
            if balance < lowest:
                lowest, lowest_date = balance, current_day
        balances[current_day] = balance
        current_day += timedelta(days=1)
    return SimulationResult(balance, lowest, lowest_date, balances, applied)


def base_flows(dataset: Dataset, request: Request) -> tuple[list[NormalizedEvent], list[CashFlow], list[RecurringRule]]:
    resolution = resolve_evidence(dataset, request.user_id)
    normalized = normalize_events(dataset, request.user_id, resolution)
    explicit = future_explicit_flows(normalized, request.request_date)
    rules = recurring_rules(normalized, request.request_date, resolution)
    return normalized, explicit + recurring_flows(rules, request.request_date, FORECAST_DAYS), rules


def is_safe(result: SimulationResult, profile: Profile) -> bool:
    return result.minimum_balance >= profile.minimum_balance_to_keep


def payment_schedule(option: PaymentOption) -> list[tuple[date, Decimal]]:
    if option.number_of_payments < 1:
        return []
    if option.number_of_payments > 1 and not option.payment_frequency_days:
        return []
    return [(option.first_payment_date + timedelta(days=(option.payment_frequency_days or 0) * index), option.payment_amount)
            for index in range(option.number_of_payments)]


def plan_flows(schedule: Iterable[tuple[date, Decimal]]) -> list[CashFlow]:
    return [CashFlow(day, -amount, "request_payment", "requested_payment", "Requested payment", "requested_payment")
            for day, amount in schedule]


PAYMENT_ENTRY = re.compile(r"^(\d{4}-\d{2}-\d{2}):(-?\d+(?:\.\d+)?)$")


def parse_payment_plan(value: str) -> list[tuple[date, Decimal]] | None:
    if value == "none":
        return []
    parsed: list[tuple[date, Decimal]] = []
    for entry in value.split("|"):
        match = PAYMENT_ENTRY.fullmatch(entry)
        if not match:
            return None
        try:
            parsed.append((date.fromisoformat(match.group(1)), Decimal(match.group(2))))
        except (InvalidOperation, ValueError):
            return None
    return parsed


def validate_spending_changes(value: str, dataset: Dataset, request: Request) -> list[str]:
    try:
        bind_spending_actions(value, dataset, request)
        return []
    except DatasetError as exc:
        return [str(exc)]


def schedule_matches_option(schedule: Sequence[tuple[date, Decimal]], option: PaymentOption) -> bool:
    expected = payment_schedule(option)
    return list(schedule) == expected and sum((amount for _, amount in schedule), MONEY_ZERO) == option.total_payable_amount


def validate_output_row(row: Mapping[str, str], dataset: Dataset, request: Request) -> list[str]:
    """Validate all row-level contract constraints independently of prediction policy."""
    errors: list[str] = []
    if tuple(row.keys()) != OUTPUT_COLUMNS:
        errors.append("output columns are missing, extra, or out of order")
    if row.get("request_id") != request.request_id:
        errors.append("request_id does not match input request")
    try:
        safe_amount = Decimal(row.get("amount_safe_to_pay", ""))
        if not MONEY_ZERO <= safe_amount <= request.requested_amount:
            errors.append("amount_safe_to_pay is outside [0, requested_amount]")
    except InvalidOperation:
        errors.append("amount_safe_to_pay is not a Decimal")
        safe_amount = MONEY_ZERO
    status = row.get("affordability_status", "")
    method = row.get("recommended_payment_method", "")
    if status not in STATUSES:
        errors.append("invalid affordability_status")
    if method not in METHODS:
        errors.append("invalid recommended_payment_method")
    if not row.get("decision_explanation", "").strip():
        errors.append("decision_explanation must not be blank")
    schedule = parse_payment_plan(row.get("payment_plan", ""))
    if schedule is None:
        errors.append("payment_plan has invalid syntax")
        schedule = []
    if any(amount <= MONEY_ZERO for _, amount in schedule):
        errors.append("payment plan payments must be positive")
    if any(later < earlier for (earlier, _), (later, _) in zip(schedule, schedule[1:])):
        errors.append("payment_plan is not chronological")
    earliest_raw = row.get("earliest_date_for_full_payment", "")
    try:
        earliest = parse_date(earliest_raw, field_name="earliest_date_for_full_payment", allow_blank=True)
    except DatasetError:
        errors.append("earliest_date_for_full_payment is not ISO formatted")
        earliest = None
    if status == "affordable_now" and earliest != request.request_date:
        errors.append("affordable_now requires request_date as earliest full-payment date")
    if status == "not_affordable" and earliest is not None:
        errors.append("not_affordable requires an empty earliest full-payment date")
    if method == "not_recommended" and schedule:
        errors.append("not_recommended must use payment_plan=none")
    profile = dataset.profiles[request.user_id]
    if method in {"full_payment", "partial_payment", "installments"} and method not in profile.payment_methods:
        errors.append(f"{method} is not accepted by the user")
    if method == "wait" and "full_payment" not in profile.payment_methods:
        errors.append("wait requires that the user accepts full_payment")
    if method == "wait":
        if earliest is None or len(schedule) != 1 or schedule[0] != (earliest, request.requested_amount):
            errors.append("wait must schedule the full payment on earliest_date_for_full_payment")
    if schedule and schedule[-1][0] > request.desired_completion_date:
        errors.append("payment plan completes after desired_completion_date")
    if method == "full_payment":
        if len(schedule) != 1 or schedule[0] != (request.request_date, request.requested_amount):
            errors.append("full_payment must contain the full amount on request_date")
    if method == "partial_payment":
        if status != "affordable_with_plan" or not request.allows_partial_payment or "partial_payment" not in profile.payment_methods:
            errors.append("partial_payment is not permitted")
        if len(schedule) != 2 or earliest is None:
            errors.append("partial_payment requires exactly two payments and an earliest date")
        elif (schedule[0] != (request.request_date, safe_amount) or safe_amount <= MONEY_ZERO or safe_amount >= request.requested_amount
              or schedule[1] != (earliest, request.requested_amount - safe_amount) or earliest > request.desired_completion_date):
            errors.append("partial payment schedule violates the request contract")
    if method == "installments":
        matching_options = [option for option in dataset.payment_options.get(request.request_id, ()) if option.payment_method == "installments" and schedule_matches_option(schedule, option)]
        if "installments" not in profile.payment_methods or not matching_options:
            errors.append("installment schedule does not match an eligible supplied option")
        elif profile.max_installment_months is not None and matching_options[0].number_of_payments > profile.max_installment_months:
            errors.append("installment option exceeds max_installment_months")
    changes = row.get("spending_changes_needed", "")
    change_errors = validate_spending_changes(changes, dataset, request)
    errors.extend(change_errors)
    if changes != "none" and (status != "affordable_with_plan" or not schedule):
        errors.append("spending changes require a completed affordable_with_plan schedule")
    if schedule and not change_errors:
        _, flows, _ = base_flows(dataset, request)
        if changes != "none":
            actions = bind_spending_actions(changes, dataset, request)
            if is_safe(simulate_cash_flow(profile, [*flows, *plan_flows(schedule)], request.request_date), profile):
                errors.append("spending changes are unnecessary for this safe no-change schedule")
            flows = apply_spending_actions(flows, actions, request)
        if not is_safe(simulate_cash_flow(profile, [*flows, *plan_flows(schedule)], request.request_date), profile):
            errors.append("payment plan breaches minimum_balance_to_keep in the 90-day simulation")
    return errors


def validate_output_rows(rows: Sequence[Mapping[str, str]], dataset: Dataset, requests: Mapping[str, Request]) -> list[str]:
    """Check file-level coverage/uniqueness plus every row-level constraint."""
    errors: list[str] = []
    ids = [row.get("request_id", "") for row in rows]
    if len(ids) != len(set(ids)):
        errors.append("output contains duplicate request_id values")
    if set(ids) != set(requests):
        errors.append("output request_id coverage differs from requests.csv")
    for row in rows:
        request = requests.get(row.get("request_id", ""))
        if request is not None:
            errors.extend(f"{request.request_id}: {error}" for error in validate_output_row(row, dataset, request))
    return errors


def earliest_safe_full_payment(dataset: Dataset, request: Request, base: Sequence[CashFlow]) -> date | None:
    profile = dataset.profiles[request.user_id]
    for offset in range(FORECAST_DAYS + 1):
        day = request.request_date + timedelta(days=offset)
        result = simulate_cash_flow(profile, [*base, *plan_flows([(day, request.requested_amount)])], request.request_date)
        if is_safe(result, profile):
            return day
    return None


@dataclass(frozen=True)
class PaymentCandidate:
    """One safe, permitted no-change plan, ranked only by the published selector order."""
    status: str
    method: str
    schedule: tuple[tuple[date, Decimal], ...]
    earliest_full_date: date | None
    payment_option_id: str | None
    explanation: str

    @property
    def total_paid(self) -> Decimal:
        return sum((amount for _, amount in self.schedule), MONEY_ZERO)

    @property
    def completion_date(self) -> date:
        return self.schedule[-1][0]

    @property
    def start_date(self) -> date:
        return self.schedule[0][0]


def candidate_rank(candidate: PaymentCandidate, request: Request) -> tuple[object, ...]:
    """Literal `Choosing Between Safe Plans` order; all candidates here need no changes."""
    return (
        candidate.completion_date > request.desired_completion_date,
        False,  # This no-change selector never attaches spending changes.
        candidate.total_paid,
        candidate.start_date,
        len(candidate.schedule),
        candidate.payment_option_id or "",
    )


def choose_payment_candidate(candidates: Sequence[PaymentCandidate], request: Request) -> PaymentCandidate | None:
    return min(candidates, key=lambda candidate: candidate_rank(candidate, request), default=None)


def payment_candidates(dataset: Dataset, request: Request, baseline_flows: Sequence[CashFlow],
                       safe_amount: Decimal, earliest: date | None) -> list[PaymentCandidate]:
    """Construct all eligible safe no-change plans before applying the selector."""
    profile = dataset.profiles[request.user_id]
    candidates: list[PaymentCandidate] = []

    full_schedule = ((request.request_date, request.requested_amount),)
    if "full_payment" in profile.payment_methods and is_safe(simulate_cash_flow(
            profile, [*baseline_flows, *plan_flows(full_schedule)], request.request_date), profile):
        option_ids = sorted(option.payment_option_id for option in dataset.payment_options.get(request.request_id, ())
                            if option.payment_method == "full_payment" and schedule_matches_option(full_schedule, option))
        candidates.append(PaymentCandidate("affordable_now", "full_payment", full_schedule, request.request_date,
                                           option_ids[0] if option_ids else None,
                                           "Baseline forecast keeps the balance above the minimum after full payment."))

    if "installments" in profile.payment_methods:
        for option in dataset.payment_options.get(request.request_id, ()):
            schedule = tuple(payment_schedule(option))
            if (option.payment_method != "installments" or not schedule
                    or (profile.max_installment_months is not None and option.number_of_payments > profile.max_installment_months)
                    or schedule[-1][0] > request.desired_completion_date):
                continue
            if is_safe(simulate_cash_flow(profile, [*baseline_flows, *plan_flows(schedule)], request.request_date), profile):
                candidates.append(PaymentCandidate("affordable_with_plan", "installments", schedule, earliest,
                                                   option.payment_option_id,
                                                   f"Baseline selected supplied installment option {option.payment_option_id}."))

    if (request.allows_partial_payment and "partial_payment" in profile.payment_methods
            and MONEY_ZERO < safe_amount < request.requested_amount and earliest is not None
            and earliest <= request.desired_completion_date):
        schedule = ((request.request_date, safe_amount), (earliest, request.requested_amount - safe_amount))
        if is_safe(simulate_cash_flow(profile, [*baseline_flows, *plan_flows(schedule)], request.request_date), profile):
            candidates.append(PaymentCandidate("affordable_with_plan", "partial_payment", schedule, earliest, None,
                                               "Baseline splits the request across two safe payments."))

    if (earliest is not None and request.request_date < earliest <= request.desired_completion_date
            and "full_payment" in profile.payment_methods):
        schedule = ((earliest, request.requested_amount),)
        if is_safe(simulate_cash_flow(profile, [*baseline_flows, *plan_flows(schedule)], request.request_date), profile):
            candidates.append(PaymentCandidate("affordable_later", "wait", schedule, earliest, None,
                                               "Baseline forecast finds a later safe full-payment date."))
    return candidates


def predict_no_change(dataset: Dataset, request: Request) -> dict[str, str]:
    """A deliberately small generic policy used only to exercise the foundation."""
    profile = dataset.profiles[request.user_id]
    _, baseline_flows, _ = base_flows(dataset, request)
    base_result = simulate_cash_flow(profile, baseline_flows, request.request_date)
    safe_amount = min(request.requested_amount, max(MONEY_ZERO, base_result.minimum_balance - profile.minimum_balance_to_keep))
    earliest = earliest_safe_full_payment(dataset, request, baseline_flows)
    none = {
        "request_id": request.request_id,
        "amount_safe_to_pay": money_text(safe_amount),
        "affordability_status": "",
        "recommended_payment_method": "",
        "payment_plan": "none",
        "earliest_date_for_full_payment": "",
        "spending_changes_needed": "none",
        "decision_explanation": "",
    }
    selected = choose_payment_candidate(payment_candidates(dataset, request, baseline_flows, safe_amount, earliest), request)
    if selected is not None:
        return {**none, "affordability_status": selected.status, "recommended_payment_method": selected.method,
                "payment_plan": "|".join(f"{day.isoformat()}:{money_text(amount)}" for day, amount in selected.schedule),
                "earliest_date_for_full_payment": selected.earliest_full_date.isoformat() if selected.earliest_full_date else "",
                "decision_explanation": selected.explanation}
    return {**none, "affordability_status": "not_affordable", "recommended_payment_method": "not_recommended",
            "earliest_date_for_full_payment": "", "decision_explanation": "Baseline found no eligible safe plan within 90 days."}


@dataclass(frozen=True)
class SpendingAction:
    event_id: str
    kind: str
    new_amount: Decimal
    occurrence_indices: tuple[int, ...]
    upper_amount: Decimal

    def serialize(self) -> str:
        if self.kind == "stop":
            return f"stop:{self.event_id}"
        return f"reduce_to:{self.event_id}:{money_text(self.new_amount)}"


@dataclass
class SpendingSearch:
    output: dict[str, str]
    notes: list[str]
    simulations: int = 0


def eligible_spending_actions(dataset: Dataset, request: Request, flows: Sequence[CashFlow],
                              rules: Sequence[RecurringRule]) -> list[SpendingAction]:
    """Map authorized source events to unambiguous existing generated occurrences."""
    profile = dataset.profiles[request.user_id]
    events = {event.event_id: event for event in dataset.events if event.user_id == request.user_id}
    memberships: dict[int, list[int]] = defaultdict(list)
    for rule_index, rule in enumerate(rules):
        generated = set(recurring_flows([rule], request.request_date, FORECAST_DAYS))
        for index, flow in enumerate(flows):
            if flow in generated and flow.kind == "recurring" and flow.flow_date > request.request_date:
                memberships[index].append(rule_index)
    actions: list[SpendingAction] = []
    cent = Decimal("0.01")
    for rule_index, rule in enumerate(rules):
        if rule.direction != "debit" or rule.category in profile.protected_categories:
            continue
        event = events.get(rule.source_event_ids[-1]) if rule.source_event_ids else None
        if (event is None or event.direction != "debit" or event.status != "settled"
                or event.currency != profile.home_currency or event.amount is None
                or not event.amount.is_finite() or event.amount <= 0):
            continue
        indices = tuple(index for index, owners in memberships.items() if owners == [rule_index])
        if not indices or any(rule_index in owners and len(owners) != 1 for owners in memberships.values()):
            continue
        upper = min(event.amount, rule.amount)
        if event.flexibility in {"stoppable", "reducible_or_stoppable"} and rule.category in profile.stoppable_categories:
            actions.append(SpendingAction(event.event_id, "stop", MONEY_ZERO, indices, upper))
        floor = event.minimum_allowed_amount
        if (event.flexibility in {"reducible", "reducible_or_stoppable"}
                and rule.category in profile.reducible_categories and floor is not None
                and floor.is_finite() and floor >= 0):
            # Output reductions use a cent grid; never round below the authorized floor.
            floor = floor.quantize(cent, rounding=ROUND_CEILING)
            if floor < upper:
                actions.append(SpendingAction(event.event_id, "reduce_to", floor, indices, upper))
    return sorted(actions, key=lambda action: (action.event_id, action.kind))


def apply_spending_actions(flows: Sequence[CashFlow], actions: Sequence[SpendingAction],
                           request: Request) -> list[CashFlow]:
    """Change only future generated debits; keep explicit events and all dates intact."""
    updated = list(flows)
    touched: set[int] = set()
    for action in actions:
        for index in action.occurrence_indices:
            flow = flows[index]
            if index in touched:
                raise DatasetError("Two spending actions target the same occurrence")
            if flow.kind != "recurring" or flow.amount >= 0 or flow.flow_date <= request.request_date:
                raise DatasetError("Spending change targets a non-future recurring debit")
            if not action.new_amount.is_finite() or not MONEY_ZERO <= action.new_amount < -flow.amount:
                raise DatasetError("Spending change is not a strict reduction")
            touched.add(index)
            updated[index] = replace(flow, amount=-action.new_amount)
    return updated


def bind_spending_actions(value: str, dataset: Dataset, request: Request) -> list[SpendingAction]:
    """Validate serialized actions against the same input permissions used by search."""
    if value == "none":
        return []
    entries = value.split("|")
    if not 1 <= len(entries) <= 3:
        raise DatasetError("spending_changes_needed requires one to three actions")
    _, flows, rules = base_flows(dataset, request)
    eligible = {(action.event_id, action.kind): action for action in eligible_spending_actions(dataset, request, flows, rules)}
    bound: list[SpendingAction] = []
    seen: set[str] = set()
    for entry in entries:
        parts = entry.split(":")
        if not ((len(parts) == 2 and parts[0] == "stop") or (len(parts) == 3 and parts[0] == "reduce_to")):
            raise DatasetError(f"Invalid spending change: {entry}")
        action = eligible.get((parts[1], parts[0]))
        if action is None:
            raise DatasetError(f"No authorized future recurring stream for {entry}")
        if action.event_id in seen:
            raise DatasetError("Cannot stop and reduce, or repeat, the same event")
        seen.add(action.event_id)
        if action.kind == "reduce_to":
            try:
                amount = Decimal(parts[2])
            except InvalidOperation as exc:
                raise DatasetError(f"Invalid reduced amount: {entry}") from exc
            if not amount.is_finite() or not action.new_amount <= amount < action.upper_amount:
                raise DatasetError(f"Reduced amount violates input bounds: {entry}")
            action = replace(action, new_amount=amount)
        bound.append(action)
    return bound


def spending_schedules(dataset: Dataset, request: Request, unchanged: Mapping[str, str],
                       earliest: date | None) -> list[tuple[str, list[tuple[date, Decimal]]]]:
    """Bounded schedules: full today, supplied installments, contract-defined partial."""
    profile = dataset.profiles[request.user_id]
    schedules: list[tuple[str, list[tuple[date, Decimal]]]] = []
    if "full_payment" in profile.payment_methods:
        schedules.append(("full_payment", [(request.request_date, request.requested_amount)]))
    if "installments" in profile.payment_methods and profile.max_installment_months is not None:
        for option in sorted(dataset.payment_options.get(request.request_id, ()), key=lambda option: option.payment_option_id):
            schedule = payment_schedule(option)
            if (option.payment_method == "installments" and schedule
                    and option.number_of_payments <= profile.max_installment_months
                    and schedule_matches_option(schedule, option)):
                schedules.append(("installments", schedule))
    safe = Decimal(unchanged["amount_safe_to_pay"])
    if ("partial_payment" in profile.payment_methods and request.allows_partial_payment
            and MONEY_ZERO < safe < request.requested_amount and earliest is not None):
        schedules.append(("partial_payment", [(request.request_date, safe), (earliest, request.requested_amount - safe)]))
    end = min(request.desired_completion_date, request.request_date + timedelta(days=FORECAST_DAYS))
    return [(method, schedule) for method, schedule in schedules if schedule
            and all(request.request_date <= day <= end and amount > 0 for day, amount in schedule)]


def plan_spending_changes(dataset: Dataset, request: Request,
                          unchanged: dict[str, str]) -> SpendingSearch:
    """Search <=3 actions, <=512 action sets, <=12000 simulations; no sample labels."""
    result = SpendingSearch(dict(unchanged), [])
    profile = dataset.profiles[request.user_id]
    _, flows, rules = base_flows(dataset, request)

    def simulate(actions: Sequence[SpendingAction], schedule: Sequence[tuple[date, Decimal]]) -> SimulationResult:
        result.simulations += 1
        return simulate_cash_flow(profile, [*apply_spending_actions(flows, actions, request), *plan_flows(schedule)], request.request_date)

    current_schedule = parse_payment_plan(unchanged["payment_plan"])
    if current_schedule:
        current = simulate([], current_schedule)
        shortfall = max(MONEY_ZERO, profile.minimum_balance_to_keep - current.minimum_balance)
        result.notes.append(f"Existing no-change plan shortfall: {money_text(shortfall)} {profile.home_currency}.")
        if shortfall == 0:
            result.notes.append("Preserved existing safe no-change output; spending changes are unnecessary.")
            return result

    actions = eligible_spending_actions(dataset, request, flows, rules)
    if not actions:
        result.notes.append("No authorized changes to supported future recurring streams.")
        return result
    earliest = earliest_safe_full_payment(dataset, request, flows)
    schedules = spending_schedules(dataset, request, unchanged, earliest)
    for method, schedule in schedules:
        minimum = simulate([], schedule).minimum_balance
        shortfall = max(MONEY_ZERO, profile.minimum_balance_to_keep - minimum)
        result.notes.append(f"Baseline {method} ending {schedule[-1][0]} shortfall: {money_text(shortfall)}.")
        if shortfall == 0:
            result.notes.append("An eligible schedule needs no spending changes; preserve existing output.")
            return result

    winner = None
    sets_tried = 0
    bounded = False
    for count in range(1, 4):
        for group in combinations(actions, count):
            if len({action.event_id for action in group}) != count:
                continue
            if sets_tried >= 512 or result.simulations >= 12000:
                bounded = True
                break
            sets_tried += 1
            for method, schedule in schedules:
                if result.simulations >= 12000:
                    bounded = True
                    break
                endpoint = simulate(group, schedule)
                updated = apply_spending_actions(flows, group, request)
                savings = sum((new.amount - old.amount for new, old in zip(updated, flows)), MONEY_ZERO)
                result.notes.append(f"Candidate {'|'.join(a.serialize() for a in group)} / {method}: "
                                    f"90-day savings {money_text(savings)}, minimum {money_text(endpoint.minimum_balance)}; "
                                    f"{'safe' if is_safe(endpoint, profile) else 'insufficient or too late'}.")
                if not is_safe(endpoint, profile):
                    continue
                reduction_indices = [index for index, action in enumerate(group) if action.kind == "reduce_to"]
                for order in permutations(reduction_indices):
                    optimized = list(group)
                    # Raise each permitted new amount as far as safety permits, trying
                    # every coordinate order (at most 3!); cents are integer search units.
                    for index in order:
                        action = optimized[index]
                        low = int(action.new_amount * 100)
                        high = int((action.upper_amount * 100).to_integral_value(rounding=ROUND_CEILING)) - 1
                        while low < high and result.simulations < 11999:
                            mid = (low + high + 1) // 2
                            trial = list(optimized)
                            trial[index] = replace(action, new_amount=Decimal(mid) / 100)
                            if is_safe(simulate(trial, schedule), profile):
                                low = mid
                            else:
                                high = mid - 1
                        optimized[index] = replace(action, new_amount=Decimal(low) / 100)
                    if result.simulations >= 12000:
                        bounded = True
                        break
                    final = simulate(optimized, schedule)
                    if not is_safe(final, profile):
                        continue
                    updated = apply_spending_actions(flows, optimized, request)
                    savings = sum((new.amount - old.amount for new, old in zip(updated, flows)), MONEY_ZERO)
                    serialized = "|".join(action.serialize() for action in optimized)
                    rank = (count, savings, schedule[-1][0], sum((amount for _, amount in schedule), MONEY_ZERO), serialized, method)
                    if winner is None or rank < winner[0]:
                        winner = (rank, method, schedule, serialized, final.minimum_balance)
        if winner is not None or bounded:
            break
    if bounded:
        result.notes.append("Bound reached; ranking covers enumerated candidates only.")
    if winner is None:
        result.notes.append("No safe authorized candidate found; preserved existing output.")
    else:
        rank, method, schedule, serialized, minimum = winner
        result.output.update(affordability_status="affordable_with_plan", recommended_payment_method=method,
                             payment_plan="|".join(f"{day}:{money_text(amount)}" for day, amount in schedule),
                             earliest_date_for_full_payment=earliest.isoformat() if earliest else "",
                             spending_changes_needed=serialized,
                             decision_explanation=f"Apply {serialized} to future recurring expenses; {method} then keeps "
                             f"at least {money_text(minimum)} {profile.home_currency} (minimum {money_text(profile.minimum_balance_to_keep)}).")
        result.notes.append(f"Selected {serialized}: necessary because every eligible no-change schedule breaches the minimum; "
                            f"{rank[0]} changes, {money_text(rank[1])} spending reduction, completes {rank[2]}, cost {money_text(rank[3])}.")
    return result


def predict_baseline(dataset: Dataset, request: Request) -> dict[str, str]:
    return plan_spending_changes(dataset, request, predict_no_change(dataset, request)).output


def trace_request(dataset: Dataset, request: Request) -> str:
    """Produce an auditable Markdown trace without relying on solved sample labels."""
    normalized, flows, rules = base_flows(dataset, request)
    resolution = resolve_evidence(dataset, request.user_id)
    explicit = future_explicit_flows(normalized, request.request_date)
    lines = [
        f"# Trace: {request.request_id}", "",
        f"As of `{request.request_date}`, current balance is `{money_text(dataset.profiles[request.user_id].current_available_balance)}` {dataset.profiles[request.user_id].home_currency}.",
        "", "## Supplied post-request events counted", "",
    ]
    if explicit:
        lines.extend(f"- `{flow.source_id}` — {flow.flow_date}: {money_text(flow.amount)} ({flow.description}; {flow.kind})." for flow in explicit)
    else:
        lines.append("- None.")
    lines.extend(["", "## Inferred recurring commitments counted", ""])
    if rules:
        for rule in rules:
            sign = "credit" if rule.direction == "credit" else "debit"
            resolver_evidence = f"; resolver evidence: {', '.join(rule.evidence_sources)}" if rule.evidence_sources else ""
            lines.append(f"- `{rule.description}` (`{rule.category}`): {sign} {money_text(rule.amount)} every {rule.interval_days} days, starting {rule.next_date}; evidence: {', '.join(rule.source_event_ids)}{resolver_evidence}.")
    else:
        lines.append("- None; fewer than three consistent settled historical events supported recurrence.")
    ignored = [item for item in normalized if item.cash_date and item.cash_date <= request.request_date and item.source.status in IGNORED_EVENT_STATUSES]
    if ignored:
        lines.extend(["", "## Lifecycle records excluded", ""])
        lines.extend(f"- `{item.source.event_id}` — {item.reason}." for item in ignored)
    evidence_overrides = [item for item in normalized if item.evidence_sources]
    applied_facts = [fact for fact in resolution.facts if fact.action != "ignore"]
    if applied_facts or evidence_overrides:
        lines.extend(["", "## Evidence resolutions", ""])
        lines.extend(f"- `{fact.source_id}`: `{fact.action}` effective {fact.effective_date}; {fact.reason}." for fact in applied_facts)
        lines.extend(f"- `{item.source.event_id}`: {'included' if item.include_in_cash_flow else 'excluded'} by `{', '.join(item.evidence_sources)}` under {item.reason}." for item in evidence_overrides)
    terminal_records = [item for item in normalized if is_terminal_salary_record(item) and item.cash_date <= request.request_date]
    if terminal_records:
        lines.extend(["", "## Explicit terminal income records", ""])
        lines.extend(f"- `{item.source.event_id}` on {item.cash_date}: {item.source.description}; "
                     "suppresses a prior inferred salary stream after this settled final payment." for item in terminal_records)
    profile = dataset.profiles[request.user_id]
    base_result = simulate_cash_flow(profile, flows, request.request_date)
    safe_amount = min(request.requested_amount, max(MONEY_ZERO, base_result.minimum_balance - profile.minimum_balance_to_keep))
    earliest = earliest_safe_full_payment(dataset, request, flows)
    candidates = payment_candidates(dataset, request, flows, safe_amount, earliest)
    selected = choose_payment_candidate(candidates, request)
    lines.extend(["", "## Safe no-change payment candidates", ""])
    if candidates:
        for candidate in sorted(candidates, key=lambda candidate: candidate_rank(candidate, request)):
            rank = candidate_rank(candidate, request)
            option = candidate.payment_option_id or "no supplied option"
            lines.append(f"- `{candidate.method}`: completes {candidate.completion_date}, starts {candidate.start_date}, "
                         f"total {money_text(candidate.total_paid)}, payments {len(candidate.schedule)}, option {option}; "
                         f"selector rank {rank}{' — selected' if candidate == selected else ''}.")
    else:
        lines.append("- None; no safe permitted no-change payment candidate completes by the desired date.")
    spending = plan_spending_changes(dataset, request, predict_no_change(dataset, request))
    lines.extend(["", "## Authorized spending-change search", ""])
    lines.extend(f"- {note}" for note in spending.notes)
    lines.append(f"- Candidate/guard simulations: {spending.simulations}.")
    lines.extend(["", "## Baseline 90-day result", "", f"- Minimum projected balance before this request: {money_text(base_result.minimum_balance)} on {base_result.minimum_balance_date}."])
    return "\n".join(lines) + "\n"


def compare_samples(dataset: Dataset) -> tuple[list[dict[str, str]], str]:
    predictions = [predict_baseline(dataset, request) for request in dataset.samples.values()]
    fields = OUTPUT_COLUMNS[1:]
    matches = {field: 0 for field in fields}
    validation_errors: list[str] = []
    request_mismatches = 0
    for prediction in predictions:
        request_id = prediction["request_id"]
        label = dataset.sample_labels[request_id]
        field_mismatch = False
        for field in fields:
            actual, expected = prediction[field], label[field]
            if field == "amount_safe_to_pay":
                same = Decimal(actual) == Decimal(expected)
            else:
                same = actual == expected
            matches[field] += int(same)
            if field != "decision_explanation":
                field_mismatch = field_mismatch or not same
        if field_mismatch:
            request_mismatches += 1
        validation_errors.extend(f"{request_id}: {error}" for error in validate_output_row(prediction, dataset, dataset.samples[request_id]))
    total = len(predictions)
    report_lines = [f"Samples evaluated: {total}", f"Requests with at least one structured-field discrepancy: {request_mismatches}/{total}"]
    report_lines.extend(f"{field}: {matches[field]}/{total} exact" for field in fields)
    report_lines.append(f"Baseline validation errors: {len(validation_errors)}")
    report_lines.extend(validation_errors[:20])
    return predictions, "\n".join(report_lines) + "\n"


def evidence_regression_checks(dataset: Dataset) -> str:
    """Check high-confidence evidence effects across all public sample contexts, without labels."""
    checked_facts = 0
    for request in dataset.samples.values():
        resolution = resolve_evidence(dataset, request.user_id)
        normalized = normalize_events(dataset, request.user_id, resolution)
        normalized_by_id = {item.source.event_id: item for item in normalized}
        rules = recurring_rules(normalized, request.request_date, resolution)
        for fact in resolution.facts:
            if fact.confidence != "high":
                continue
            checked_facts += 1
            if fact.action in {"cancel_event", "exclude_credit"} and fact.target_event_id:
                item = normalized_by_id.get(fact.target_event_id)
                if item is None or item.include_in_cash_flow:
                    raise DatasetError(f"Evidence regression: {fact.source_id} did not exclude {fact.target_event_id}")
            if fact.action == "amend_salary" and any(rule.category == "salary" and rule.direction == "credit" for rule in rules):
                if not any(fact.source_id in rule.evidence_sources for rule in rules if rule.category == "salary" and rule.direction == "credit"):
                    raise DatasetError(f"Evidence regression: {fact.source_id} did not reach the salary rule")
            if fact.action == "remove_salary" and fact.effective_date <= request.request_date:
                if any(rule.category == "salary" and rule.direction == "credit" for rule in rules):
                    raise DatasetError(f"Evidence regression: {fact.source_id} did not suppress future salary")
    return f"Evidence regression checks passed: {checked_facts} high-confidence facts across {len(dataset.samples)} samples.\n"


def build_recurrence_reconciliation_audit(dataset: Dataset) -> str:
    """Audit cadence inference and explicit-event reconciliation for every public sample context."""
    sections: list[str] = [
        "# Recurrence reconciliation audit", "",
        "This audit is derived from deterministic forecast inputs. It does not use solved output fields.", "",
    ]
    for request in dataset.samples.values():
        resolution = resolve_evidence(dataset, request.user_id)
        normalized = normalize_events(dataset, request.user_id, resolution)
        explicit = future_explicit_flows(normalized, request.request_date)
        rules = recurring_rules(normalized, request.request_date, resolution)
        reconciliation = reconcile_recurring_flows(rules, explicit, request.request_date, FORECAST_DAYS)
        sections.extend([f"## {request.request_id} — {request.user_id}", "", "### Inferred cadence and anchor", "", "| Stream | Category | Direction | Cadence | Anchor | Historical evidence |", "| --- | --- | --- | --- | --- | --- |"])
        sections.extend(f"| {markdown_cell(rule.description)} | {rule.category} | {rule.direction} | day-based ({rule.interval_days}d estimate) | {rule.next_date} | {', '.join(f'`{event_id}`' for event_id in rule.source_event_ids)} |" for rule in rules)
        if not rules:
            sections.append("| — | — | — | — | — | No supported recurrence |")
        sections.extend(["", "### Generated occurrences before reconciliation", "", "| Date | Stream | Amount |", "| --- | --- | ---: |"])
        sections.extend(f"| {flow.flow_date} | {markdown_cell(flow.description)} | {money_text(flow.amount)} |" for flow in reconciliation.generated_before)
        if not reconciliation.generated_before:
            sections.append("| — | — | — |")
        sections.extend(["", "### Explicit future events that supersede recurrence", "", "| Generated stream/date | Explicit event/date | Matching reason |", "| --- | --- | --- |"])
        sections.extend(f"| {markdown_cell(suppression.rule_description)} / {suppression.generated_date} | `{suppression.explicit_event_id}` / {suppression.explicit_date} | {markdown_cell(suppression.reason)} |" for suppression in reconciliation.suppressions)
        if not reconciliation.suppressions:
            sections.append("| — | — | No matching explicit future event |")
        final_flows = sorted([*explicit, *reconciliation.generated_after], key=lambda flow: (flow.flow_date, flow.source_id))
        sections.extend(["", "### Final occurrences used in forecast", "", "| Date | Source | Kind | Category | Amount |", "| --- | --- | --- | --- | ---: |"])
        sections.extend(f"| {flow.flow_date} | `{flow.source_id}` | {flow.kind} | {flow.category} | {money_text(flow.amount)} |" for flow in final_flows)
        if not final_flows:
            sections.append("| — | — | — | — | — |")
        sections.append("")
    return "\n".join(sections) + "\n"


def write_csv(path: Path, rows: Sequence[Mapping[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_COLUMNS, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def read_prediction_csv(path: Path) -> dict[str, dict[str, str]]:
    """Read an already-produced evaluation artifact without executing prediction."""
    rows = read_csv(path, OUTPUT_COLUMNS)
    predictions: dict[str, dict[str, str]] = {}
    for row in rows:
        request_id = row["request_id"]
        if not request_id or request_id in predictions:
            raise DatasetError(f"Prediction CSV has duplicate or blank request_id: {request_id!r}")
        predictions[request_id] = {column: row[column] for column in OUTPUT_COLUMNS}
    return predictions


def values_match(field: str, expected: str, actual: str) -> bool:
    if field == "amount_safe_to_pay":
        return Decimal(expected) == Decimal(actual)
    return expected == actual


def sample_metrics(dataset: Dataset, predictions: Mapping[str, Mapping[str, str]]) -> tuple[dict[str, int], int]:
    """Return exact-match counts and structured-request failures for a supplied artifact."""
    fields = OUTPUT_COLUMNS[1:]
    matches = {field: 0 for field in fields}
    structured_failures = 0
    for request_id, request in dataset.samples.items():
        prediction = predictions.get(request_id)
        if prediction is None:
            continue
        label = dataset.sample_labels[request_id]
        differs = False
        for field in fields:
            same = values_match(field, label[field], prediction[field])
            matches[field] += int(same)
            if field != "decision_explanation":
                differs = differs or not same
        structured_failures += int(differs)
    return matches, structured_failures


def markdown_cell(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def excluded_event_reason(item: NormalizedEvent, request: Request) -> str:
    if not item.include_in_cash_flow:
        return item.reason
    if item.cash_date is None:
        return "no usable cash date"
    if item.cash_date <= request.request_date:
        return f"cash date {item.cash_date} is already reflected in the as-of balance; retained only as potential recurrence evidence"
    return "not selected for the current forecast"


def relevant_messages_and_images(dataset: Dataset, request: Request) -> tuple[list[Mapping[str, str]], list[Mapping[str, str]]]:
    event_ids = {event.event_id for event in dataset.events if event.user_id == request.user_id}
    messages = [message for message in dataset.messages if message["user_id"] == request.user_id or message["request_id"] == request.request_id or message["related_event_id"] in event_ids]
    images = [image for image in dataset.images if image["user_id"] == request.user_id or image["request_id"] == request.request_id or image["related_event_id"] in event_ids]
    return messages, images


def diagnose_sample_difference(dataset: Dataset, request: Request, expected: Mapping[str, str], actual: Mapping[str, str]) -> tuple[str, str]:
    """Assign one evidence-led, reusable primary diagnosis; labels are diagnostic only."""
    messages, images = relevant_messages_and_images(dataset, request)
    message_text = " ".join(message["message_text"].lower() for message in messages)
    normalized = normalize_events(dataset, request.user_id)
    has_foreign_cash = any(item.source.currency != dataset.profiles[request.user_id].home_currency and item.source.amount is not None for item in normalized)
    has_lifecycle_evidence = any(item.source.linked_event_id or item.source.status in {"pending", "cancelled", "failed"} for item in normalized)
    expected_method, actual_method = expected["recommended_payment_method"], actual["recommended_payment_method"]
    if expected["spending_changes_needed"] != "none":
        return ("flexible spending changes", "The solved plan changes flexible recurring spending, while the baseline never models authorized stop/reduce actions or their resulting forecast cash flows.")
    if expected_method == "partial_payment":
        return ("partial-payment eligibility and timing", "The solved plan uses a two-payment schedule; the baseline needs a payment-date-specific capacity calculation for both the first amount and the remaining amount.")
    if expected_method == "wait" and actual_method == "wait" and expected["payment_plan"] != actual["payment_plan"]:
        return ("earliest-date computation", "The baseline finds a later date but represents wait with payment_plan=none instead of the solved future full-payment commitment, and its daily date is not conservative enough.")
    if expected_method == "installments" and actual_method == "installments":
        return ("earliest-date computation", "Both results select installments; the discrepancy is capacity/earliest-full-payment timing rather than an option-selection failure.")
    if expected_method == "installments" or actual_method == "installments":
        return ("payment-option schedule or financing fee handling", "The baseline does not rank all safe supplied offers against the solved plan's completion date, total payable amount, and financing fee semantics.")
    if messages or images:
        if "reduced" in message_text and "salary" in message_text:
            return ("cancellations or amendments from messages", "A payroll message supplies a reduced next-salary amount. The baseline does not apply dated salary amendments to the matching future income event or inferred salary recurrence.")
        if "replaces" in message_text and "salary" in message_text:
            return ("cancellations or amendments from messages", "A payroll message explicitly replaces an earlier salary date. The baseline must supersede the prior future income date before computing capacity and earliest payment date.")
        if any(token in message_text for token in ("bonus", "commission", "refund", "prize", "payout")) and any(token in message_text for token in ("pending", "not credited", "not withdrawable", "processing")):
            return ("pending debit or credit handling", "The supporting message says a bonus, commission, refund, prize, or payout is not yet cash. The forecast must reserve its absence until an explicit settlement/credit record exists.")
        return ("cancellations or amendments from messages", "Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.")
    if has_foreign_cash:
        return ("dated currency conversion", "At least one relevant cash event needs a dated conversion; the baseline's direct-rate-only handling can exclude valid events when a supplied reverse pair is required.")
    if has_lifecycle_evidence:
        return ("duplicate / linked-event handling", "The request has pending or linked lifecycle evidence; the baseline's child-ID suppression is not a complete lifecycle resolver and can omit or double reserve cash.")
    if expected_method == "wait" or expected["affordability_status"] == "affordable_later":
        return ("recurrence detection / forecasting frequency", "The solved result is later-safe while the baseline is now-safe or uses a different date, indicating that recurring essential commitments or their cadence are under-forecast.")
    if expected["affordability_status"] == "not_affordable" and actual["affordability_status"] != "not_affordable":
        return ("recurrence detection / forecasting frequency", "The baseline permits a plan that the solved sample rejects, which points to omitted conservative recurring commitments or an incorrectly counted future debit.")
    return ("earliest-date computation", "The output differs after the same broad affordability conclusion; payment-date simulation and conservative intra-day ordering need refinement.")


def metric_markdown(matches: Mapping[str, int], structured_failures: int, heading: str) -> list[str]:
    return [
        heading, "", f"- Structured failures: **{structured_failures}/25** (decision explanation excluded from this failure count).",
        f"- Exact explanation matches: **{matches['decision_explanation']}/25**; baseline explanations are intentionally generic.", "",
        "| Field | Exact matches |", "| --- | ---: |",
        *(f"| `{field}` | {matches[field]}/25 |" for field in OUTPUT_COLUMNS[1:]), "",
    ]


def build_discrepancy_report(dataset: Dataset, predictions: Mapping[str, Mapping[str, str]], before_metrics: list[str] | None = None) -> str:
    """Create an evidence-complete audit of structured sample failures from an existing artifact."""
    matches, structured_failures = sample_metrics(dataset, predictions)
    fields = OUTPUT_COLUMNS[1:]
    grouped: dict[str, list[str]] = defaultdict(list)
    sections: list[str] = []
    for request_id, request in dataset.samples.items():
        actual = predictions.get(request_id)
        if actual is None:
            continue
        expected = dataset.sample_labels[request_id]
        structured_differences = [field for field in fields[:-1] if not values_match(field, expected[field], actual[field])]
        if not structured_differences:
            continue
        category, diagnosis = diagnose_sample_difference(dataset, request, expected, actual)
        grouped[category].append(request_id)
        profile = dataset.profiles[request.user_id]
        normalized, flows, rules = base_flows(dataset, request)
        included = sorted(flows, key=lambda flow: (flow.flow_date, flow.amount, flow.source_id))
        excluded = sorted((item for item in normalized if item not in [] and (not item.include_in_cash_flow or item.cash_date is None or item.cash_date <= request.request_date)), key=lambda item: (item.cash_date or date.min, item.source.event_id))
        messages, images = relevant_messages_and_images(dataset, request)
        options = dataset.payment_options.get(request.request_id, ())
        difference_rows = []
        for field in fields:
            if not values_match(field, expected[field], actual[field]):
                difference_rows.append(f"| `{field}` | {markdown_cell(expected[field])} | {markdown_cell(actual[field])} |")
        included_rows = [f"| {flow.flow_date} | {markdown_cell(flow.source_id)} | {markdown_cell(flow.kind)} | {markdown_cell(flow.category)} | {money_text(flow.amount)} | {markdown_cell(flow.description)} |" for flow in included]
        excluded_rows = [f"| `{item.source.event_id}` | {item.cash_date or ''} | {markdown_cell(item.source.status)} | {markdown_cell(item.source.category)} | {money_text(item.amount_home) if item.amount_home is not None else ''} | {markdown_cell(excluded_event_reason(item, request))} |" for item in excluded]
        message_rows = [f"| `{message['message_id']}` | {markdown_cell(message['sent_at'])} | `{message['related_event_id'] or ''}` | {markdown_cell(message['source_type'])} | {markdown_cell(message['message_text'])} |" for message in messages]
        image_rows = [f"| `{image['image_id']}` | `{image['related_event_id'] or ''}` | {markdown_cell(image['request_id'])} |" for image in images]
        option_rows = []
        for option in options:
            schedule = "|".join(f"{day}:{money_text(amount)}" for day, amount in payment_schedule(option)) or "invalid schedule"
            option_rows.append(f"| `{option.payment_option_id}` | {option.payment_method} | {markdown_cell(schedule)} | {money_text(option.financing_fee)} | {money_text(option.total_payable_amount)} |")
        source_links = [item.source for item in normalized if item.source.linked_event_id]
        link_rows = [f"| `{event.event_id}` | `{event.linked_event_id}` | {event.status} | {event.event_type} |" for event in source_links]
        sections.extend([
            f"## {request_id} — {request.user_id}", "",
            f"Primary category: **{category}**", "", diagnosis, "",
            "### Expected vs actual", "", "| Field | Solved sample | Existing baseline artifact |", "| --- | --- | --- |", *difference_rows, "",
            "### Financial profile", "", f"- Home currency: `{profile.home_currency}`", f"- Current balance: `{money_text(profile.current_available_balance)}`", f"- Minimum balance: `{money_text(profile.minimum_balance_to_keep)}`",
            f"- Protected: `{ '|'.join(sorted(profile.protected_categories)) }`; reduce: `{ '|'.join(sorted(profile.reducible_categories)) }`; stop: `{ '|'.join(sorted(profile.stoppable_categories)) }`.",
            f"- Payment methods: `{ '|'.join(sorted(profile.payment_methods)) }`; max installment months: `{profile.max_installment_months or ''}`.", "",
            "### Included 90-day forecast cash flows", "", "| Date | Source | Kind | Category | Home-currency amount | Detail |", "| --- | --- | --- | --- | ---: | --- |", *(included_rows or ["| — | — | — | — | — | No flows |"]), "",
            "### Excluded source events", "", "| Event | Cash date | Status | Category | Home-currency amount | Reason |", "| --- | --- | --- | --- | ---: | --- |", *(excluded_rows or ["| — | — | — | — | — | No exclusions |"]), "",
            "### Relevant evidence", "", "#### Messages", "", "| Message | Sent | Related event | Source | Text |", "| --- | --- | --- | --- | --- |", *(message_rows or ["| — | — | — | — | None |"]), "",
            "#### Images", "", "| Image | Related event | Request |", "| --- | --- | --- |", *(image_rows or ["| — | — | None |"]), "",
            "#### Linked events", "", "| Event | Linked event | Status | Type |", "| --- | --- | --- | --- |", *(link_rows or ["| — | — | — | None |"]), "",
            "#### Payment options", "", "| Option | Method | Schedule | Fee | Total payable |", "| --- | --- | --- | ---: | ---: |", *(option_rows or ["| — | — | None | — | — |"]), "",
        ])
    category_rows = [f"| {category} | {len(request_ids)} | {', '.join(f'`{request_id}`' for request_id in request_ids)} |" for category, request_ids in sorted(grouped.items())]
    metrics = metric_markdown(matches, structured_failures, "## Before-fix metrics") if before_metrics is None else before_metrics + metric_markdown(matches, structured_failures, "## After latest fix metrics")
    return "\n".join([
        "# Sample discrepancy report", "",
        "This audit reads the supplied `sample_baseline_predictions.csv`; report generation does not run prediction. Solved rows are used only to compare public samples, never as prediction inputs.", "",
        *metrics,
        "## Reusable failure categories", "", "| Category | Failures | Requests |", "| --- | ---: | --- |", *category_rows, "",
        "## Per-request evidence", "", *sections,
    ]) + "\n"


def original_metric_block(report_path: Path) -> list[str] | None:
    """Preserve the first report's baseline block when refreshing after a fix."""
    if not report_path.exists():
        return None
    content = report_path.read_text(encoding="utf-8")
    match = re.search(r"(## Before-fix metrics\n.*?)(?=## (?:After latest fix metrics|Reusable failure categories))", content, flags=re.DOTALL)
    return match.group(1).rstrip().splitlines() + [""] if match else None


def main() -> None:
    parser = argparse.ArgumentParser(description="Run deterministic Buy or Wait baseline diagnostics.")
    parser.add_argument("--dataset-dir", type=Path, default=Path(__file__).resolve().parents[1] / "dataset")
    parser.add_argument("--trace", metavar="REQUEST_ID", help="Print an auditable cash-flow trace for a request or sample.")
    parser.add_argument("--write-trace", type=Path, help="Write the trace Markdown to this path.")
    parser.add_argument("--evaluate-samples", action="store_true", help="Compare baseline structured output to public solved samples.")
    parser.add_argument("--predictions-path", type=Path, default=Path(__file__).resolve().parent / "evaluation" / "sample_baseline_predictions.csv")
    parser.add_argument("--write-discrepancy-report", type=Path, help="Audit an existing sample prediction CSV without running prediction.")
    parser.add_argument("--check-evidence-regressions", action="store_true", help="Run generic evidence-resolution invariants on public sample contexts.")
    parser.add_argument("--write-recurrence-audit", type=Path, help="Write cadence and explicit-event reconciliation audit for sample contexts.")
    args = parser.parse_args()
    dataset = load_dataset(args.dataset_dir)
    if args.trace:
        request = dataset.samples.get(args.trace) or dataset.requests.get(args.trace)
        if request is None:
            raise DatasetError(f"Unknown request_id: {args.trace}")
        trace = trace_request(dataset, request)
        print(trace, end="")
        if args.write_trace:
            args.write_trace.parent.mkdir(parents=True, exist_ok=True)
            args.write_trace.write_text(trace, encoding="utf-8", newline="\n")
    if args.evaluate_samples:
        predictions, report = compare_samples(dataset)
        write_csv(args.predictions_path, predictions)
        print(report, end="")
    if args.write_discrepancy_report:
        predictions = read_prediction_csv(args.predictions_path)
        before_metrics = original_metric_block(args.write_discrepancy_report)
        report = build_discrepancy_report(dataset, predictions, before_metrics)
        args.write_discrepancy_report.parent.mkdir(parents=True, exist_ok=True)
        args.write_discrepancy_report.write_text(report, encoding="utf-8", newline="\n")
        print(f"Wrote discrepancy report: {args.write_discrepancy_report}")
    if args.check_evidence_regressions:
        print(evidence_regression_checks(dataset), end="")
    if args.write_recurrence_audit:
        args.write_recurrence_audit.parent.mkdir(parents=True, exist_ok=True)
        args.write_recurrence_audit.write_text(build_recurrence_reconciliation_audit(dataset), encoding="utf-8", newline="\n")
        print(f"Wrote recurrence reconciliation audit: {args.write_recurrence_audit}")
    if not args.trace and not args.evaluate_samples and not args.write_discrepancy_report and not args.check_evidence_regressions and not args.write_recurrence_audit:
        parser.print_help()


if __name__ == "__main__":
    main()
