"""Synthetic invariants for the Milestone 1 forecast-ledger contract."""

from dataclasses import FrozenInstanceError
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class ForecastLedgerTests(unittest.TestCase):
    def setUp(self):
        self.as_of = date(2025, 1, 10)
        self.profile = m.Profile(
            "user", "USD", Decimal("100"), Decimal("40"),
            frozenset(), frozenset(), frozenset(), frozenset(), frozenset(), None,
        )

    def event(self, *, event_id="event", direction="debit", status="settled", event_date=None,
              settlement_date=None, amount="10"):
        return m.FinancialEvent(
            event_id, "user", "expense" if direction == "debit" else "income", "Synthetic event",
            "test", direction, Decimal(amount), "USD", event_date or self.as_of,
            settlement_date, status, None, "fixed", None,
        )

    def dataset(self, *events):
        return m.Dataset({"user": self.profile}, {}, {}, {}, tuple(events), {}, {}, (), ())

    def test_flow_is_immutable_and_requires_finite_decimal(self):
        flow = m.ForecastFlow(self.as_of, Decimal("1.25"), "source", "test", "Flow", "explicit")
        with self.assertRaises(FrozenInstanceError):
            flow.amount = Decimal("2")
        with self.assertRaises(m.DatasetError):
            m.ForecastFlow(self.as_of, Decimal("NaN"), "source", "test", "Flow", "explicit")

    def test_same_day_order_is_debits_then_credits_with_stable_ties(self):
        flows = [
            m.ForecastFlow(self.as_of, Decimal("100"), "z_credit", "test", "Credit", "explicit"),
            m.ForecastFlow(self.as_of, Decimal("-20"), "b_debit", "test", "Debit B", "explicit"),
            m.ForecastFlow(self.as_of, Decimal("-30"), "a_debit", "test", "Debit A", "explicit"),
        ]
        result = m.simulate_cash_flow(self.profile, reversed(flows), self.as_of, horizon_days=0)
        self.assertEqual([flow.source_id for flow in result.applied_flows],
                         ["a_debit", "b_debit", "z_credit"])
        self.assertEqual([step.closing_balance for step in result.ledger_steps],
                         [Decimal("70"), Decimal("50"), Decimal("150")])

    def test_decimal_money_has_no_binary_rounding_drift(self):
        flows = [
            m.ForecastFlow(self.as_of, Decimal("-0.30"), "debit", "test", "Debit", "explicit"),
            m.ForecastFlow(self.as_of, Decimal("0.10"), "credit", "test", "Credit", "explicit"),
        ]
        result = m.simulate_cash_flow(self.profile, flows, self.as_of, horizon_days=0)
        self.assertEqual(result.ending_balance, Decimal("99.80"))
        self.assertEqual(m.money_text(result.ending_balance), "99.8")

    def test_past_settled_event_is_not_reapplied_to_current_balance(self):
        settled = self.event(event_date=self.as_of - timedelta(days=2),
                             settlement_date=self.as_of - timedelta(days=1))
        normalized = m.normalize_events(self.dataset(settled), "user")
        self.assertTrue(normalized[0].include_in_cash_flow)
        self.assertEqual(m.future_explicit_flows(normalized, self.as_of), [])

    def test_pending_debit_is_retained_as_future_liability_with_trace(self):
        pending = self.event(status="pending", event_date=self.as_of + timedelta(days=2),
                             settlement_date=self.as_of + timedelta(days=3))
        normalized = m.normalize_events(self.dataset(pending), "user")
        flows = m.future_explicit_flows(normalized, self.as_of)
        self.assertEqual(len(flows), 1)
        self.assertEqual(flows[0].amount, Decimal("-10"))
        self.assertEqual(flows[0].source_event_ids, ("event",))
        self.assertIn("pending debit retained", flows[0].trace_reason)


if __name__ == "__main__":
    unittest.main()
