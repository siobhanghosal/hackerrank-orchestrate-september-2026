"""Regression checks for the optional local-model explanation boundary."""

import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m
import ollama_explanations as oe


def packet():
    return {
        "request": {"request_id": "request_x", "home_currency": "USD"},
        "decision": {
            "request_date": "2025-01-01", "desired_completion_date": "2025-01-10",
            "requested_amount": "100", "amount_safe_to_pay": "60",
            "affordability_status": "affordable_now", "recommended_payment_method": "full_payment",
            "payment_plan": "2025-01-01:100", "earliest_date_for_full_payment": "2025-01-01",
            "spending_changes_needed": "none", "payment_dates": ["2025-01-01"],
            "payment_count": "1", "total_payment_amount": "100",
        },
        "forecast": {
            "current_available_balance": "300", "minimum_balance_to_keep": "50",
            "minimum_projected_balance": "180", "minimum_projected_balance_date": "2025-01-04",
        },
        "resolved_evidence": [],
    }


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class FixedGenerator:
    def __init__(self, text):
        self.text = text
        self.packets = []

    def generate(self, supplied_packet):
        self.packets.append(supplied_packet)
        return self.text


class FailingGenerator:
    def generate(self, supplied_packet):
        raise oe.ExplanationError("offline")


class OllamaExplanationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dataset = m.load_dataset(Path(__file__).resolve().parents[2] / "dataset")

    def test_ollama_request_is_schema_constrained_and_records_usage(self):
        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["timeout"] = timeout
            captured["body"] = json.loads(request.data.decode("utf-8"))
            return FakeResponse({
                "message": {"content": '{"decision_explanation":"Full payment of 100 USD on 2025-01-01 stays above the 50 USD minimum."}'},
                "prompt_eval_count": 120,
                "eval_count": 20,
            })

        generator = oe.OllamaExplanationGenerator("qwen3:4b-instruct", timeout_seconds=15)
        with patch("ollama_explanations.urlopen", fake_urlopen):
            explanation = generator.generate(packet())

        self.assertIn("100 USD", explanation)
        self.assertEqual(captured["url"], "http://127.0.0.1:11434/api/chat")
        self.assertEqual(captured["timeout"], 15)
        self.assertFalse(captured["body"]["stream"])
        self.assertEqual(captured["body"]["format"], oe.EXPLANATION_SCHEMA)
        self.assertEqual(captured["body"]["options"]["temperature"], 0)
        self.assertEqual(generator.usages[0].prompt_tokens, 120)
        self.assertEqual(generator.usages[0].completion_tokens, 20)

    def test_unsupported_numeric_claim_is_rejected(self):
        with self.assertRaises(oe.ExplanationError):
            oe.validate_explanation("Payment of 999 USD is safe.", packet())

    def test_model_can_change_only_the_explanation(self):
        request = next(iter(self.dataset.samples.values()))
        deterministic = m.predict_baseline(self.dataset, request)
        generator = FixedGenerator("The selected payment plan follows the validated forecast.")
        enriched = m.predict_baseline(self.dataset, request, generator)

        self.assertEqual({key: value for key, value in enriched.items() if key != "decision_explanation"},
                         {key: value for key, value in deterministic.items() if key != "decision_explanation"})
        self.assertEqual(enriched["decision_explanation"], "The selected payment plan follows the validated forecast.")
        self.assertEqual(set(generator.packets[0]["request"]), {"request_id", "home_currency"})
        self.assertNotIn("message_text", json.dumps(generator.packets[0]))
        self.assertNotIn("request_text", json.dumps(generator.packets[0]))

    def test_model_failure_preserves_the_deterministic_explanation(self):
        request = next(iter(self.dataset.samples.values()))
        self.assertEqual(m.predict_baseline(self.dataset, request, FailingGenerator()),
                         m.predict_baseline(self.dataset, request))


if __name__ == "__main__":
    unittest.main()
