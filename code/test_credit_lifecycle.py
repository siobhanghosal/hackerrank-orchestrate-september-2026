"""Synthetic lifecycle checks for conservative future-credit handling."""

import unittest
from datetime import date
from decimal import Decimal as D

import main as m


class CreditLifecycleTests(unittest.TestCase):
    profile = m.Profile("user", "USD", D("1000"), D("100"), frozenset(), frozenset(), frozenset(), frozenset(), frozenset(), None)

    def event(self, event_id, *, event_type="income", description="Credit", category="salary", direction="credit", status="pending"):
        return m.FinancialEvent(event_id, "user", event_type, description, category, direction, D("100"), "USD",
                                date(2025, 1, 10), date(2025, 1, 10), status, None, "fixed", None)

    def normalize(self, event, facts=()):
        dataset = m.Dataset({"user": self.profile}, {}, {}, {}, (event,), {}, {}, (), ())
        return m.normalize_events(dataset, "user", m.EvidenceResolution(tuple(facts)))[0]

    def test_pending_credit_is_excluded_without_attributable_confirmation(self):
        result = self.normalize(self.event("pending"))
        self.assertFalse(result.include_in_cash_flow)
        self.assertEqual(result.reason, "pending credit is not available")

    def test_confirmation_fact_includes_pending_credit_on_effective_date(self):
        fact = m.EvidenceFact("message", "message", "user", "confirm_credit", date(2025, 1, 15), "pending", None, None,
                              "high", "explicitly confirmed credit")
        result = self.normalize(self.event("pending"), (fact,))
        self.assertTrue(result.include_in_cash_flow)
        self.assertEqual(result.cash_date, date(2025, 1, 15))
        self.assertIn("message", result.evidence_sources)

    def test_only_explicitly_confirmed_scheduled_salary_is_included(self):
        confirmed = self.normalize(self.event("confirmed", description="Next confirmed salary", status="scheduled"))
        estimated = self.normalize(self.event("estimated", description="Estimated salary", status="scheduled"))
        self.assertTrue(confirmed.include_in_cash_flow)
        self.assertFalse(estimated.include_in_cash_flow)
        self.assertEqual(estimated.reason, "unconfirmed scheduled credit is unavailable")

    def test_conservative_fallback_retains_pending_debit(self):
        result = self.normalize(self.event("debit", event_type="expense", category="utilities", direction="debit", status="pending"))
        self.assertTrue(result.include_in_cash_flow)
        self.assertEqual(result.reason, "pending debit retained as a conservative liability")

    def test_unrealized_investment_value_never_enters_cash_ledger(self):
        result = self.normalize(self.event("investment", event_type="investment_value", category="investment", status="unrealized"))
        self.assertFalse(result.include_in_cash_flow)
        self.assertEqual(result.reason, "unavailable investment value")


if __name__ == "__main__":
    unittest.main()
