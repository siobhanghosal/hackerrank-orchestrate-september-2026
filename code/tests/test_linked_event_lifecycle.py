"""Synthetic linked-event chains for the Milestone 2 lifecycle resolver."""

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class LinkedEventLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.as_of = date(2025, 1, 10)
        self.profile = m.Profile(
            "user", "USD", Decimal("100"), Decimal("20"),
            frozenset(), frozenset(), frozenset(), frozenset(), frozenset(), None,
        )

    def event(self, event_id, *, event_type="expense", direction="debit", status="pending",
              offset=1, linked=None, amount="10", description="Synthetic lifecycle record"):
        event_date = self.as_of + timedelta(days=offset)
        return m.FinancialEvent(
            event_id, "user", event_type, description, "test", direction, Decimal(amount), "USD",
            event_date, event_date, status, linked, "fixed", None,
        )

    def dataset(self, *events):
        return m.Dataset({"user": self.profile}, {}, {}, {}, tuple(events), {}, {}, (), ())

    def normalized(self, *events):
        return m.normalize_events(self.dataset(*events), "user")

    def test_settlement_supersedes_linked_pending_representation(self):
        pending = self.event("pending", status="pending", offset=1)
        settled = self.event("settled", status="settled", offset=2, linked="pending")
        normalized = self.normalized(pending, settled)
        by_id = {item.source.event_id: item for item in normalized}
        flows = m.future_explicit_flows(normalized, self.as_of)

        self.assertFalse(by_id["pending"].include_in_cash_flow)
        self.assertEqual(by_id["pending"].lifecycle_rule, "lifecycle_settlement_supersedes_open")
        self.assertEqual([flow.source_id for flow in flows], ["settled"])
        self.assertEqual(flows[0].source_event_ids, ("settled", "pending"))

    def test_refund_or_reversal_is_a_distinct_cash_leg(self):
        pending = self.event("authorization", status="pending", offset=1)
        reversal = self.event(
            "reversal", event_type="refund", direction="credit", status="settled", offset=2,
            linked="authorization", description="Settled authorization reversal",
        )
        normalized = self.normalized(pending, reversal)
        flows = m.future_explicit_flows(normalized, self.as_of)

        self.assertEqual([(flow.source_id, flow.amount) for flow in flows],
                         [("authorization", Decimal("-10")), ("reversal", Decimal("10"))])
        self.assertIn("distinct cash", flows[0].trace_reason)
        self.assertIn("linked refund", flows[1].trace_reason)

    def test_pending_refund_is_not_available_and_does_not_erase_original_charge(self):
        charge = self.event("charge", status="settled", offset=-2)
        refund = self.event("refund", event_type="refund", direction="credit", status="pending",
                            offset=2, linked="charge")
        normalized = self.normalized(charge, refund)
        by_id = {item.source.event_id: item for item in normalized}

        self.assertTrue(by_id["charge"].include_in_cash_flow)
        self.assertFalse(by_id["refund"].include_in_cash_flow)
        self.assertIn("pending credit", by_id["refund"].reason)
        self.assertEqual(m.future_explicit_flows(normalized, self.as_of), [])

    def test_ambiguous_possible_duplicate_debit_is_conservatively_retained(self):
        original = self.event("original", status="settled", offset=-2)
        possible_duplicate = self.event("possible_duplicate", status="pending", offset=2,
                                        linked="original", description="Possible duplicate card charge")
        normalized = self.normalized(original, possible_duplicate)
        by_id = {item.source.event_id: item for item in normalized}
        flows = m.future_explicit_flows(normalized, self.as_of)

        self.assertEqual(by_id["possible_duplicate"].lifecycle_rule, "lifecycle_ambiguous_debit")
        self.assertTrue(by_id["possible_duplicate"].include_in_cash_flow)
        self.assertEqual([(flow.source_id, flow.amount) for flow in flows],
                         [("possible_duplicate", Decimal("-10"))])

    def test_failed_debit_is_replaced_by_linked_scheduled_retry(self):
        failed = self.event("failed", event_type="debt_payment", status="failed", offset=-2)
        retry = self.event("retry", event_type="debt_payment", status="scheduled", offset=2,
                           linked="failed")
        normalized = self.normalized(failed, retry)
        flows = m.future_explicit_flows(normalized, self.as_of)

        self.assertEqual([flow.source_id for flow in flows], ["retry"])
        self.assertIn("active linked replacement", flows[0].trace_reason)

    def test_unrealized_valuation_does_not_suppress_purchase_or_enter_cash(self):
        purchase = self.event("purchase", event_type="investment_purchase", status="settled", offset=-2)
        valuation = self.event(
            "valuation", event_type="investment_valuation", direction="non_cash", status="unrealized",
            offset=2, linked="purchase", amount="15",
        )
        normalized = self.normalized(purchase, valuation)
        by_id = {item.source.event_id: item for item in normalized}

        self.assertTrue(by_id["purchase"].include_in_cash_flow)
        self.assertFalse(by_id["valuation"].include_in_cash_flow)
        self.assertEqual(by_id["valuation"].lifecycle_rule, "lifecycle_non_cash_child")
        self.assertEqual(m.future_explicit_flows(normalized, self.as_of), [])


if __name__ == "__main__":
    unittest.main()
