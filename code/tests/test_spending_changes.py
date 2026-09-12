"""Independent synthetic cash-flow cases plus public-context preservation checks."""

import unittest
from dataclasses import replace
from datetime import date
from decimal import Decimal as D
from pathlib import Path
import sys
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class SpendingTests(unittest.TestCase):
    def fixture(self, balance="200", amount="80", streams=None, explicit=()):
        start = date(2026, 1, 1)
        profile = m.Profile("person", "USD", D(balance), D("100"), frozenset(),
                            frozenset(), frozenset({"optional"}), frozenset({"optional"}),
                            frozenset({"full_payment"}), None)
        request = m.Request("purchase", "person", start, "purchase", D(amount), start, False, "")
        events, rules = [], []
        for name, cost, flexibility, floor in (streams or [("service", "30", "stoppable", None)]):
            source = m.FinancialEvent(name, "person", "subscription", name, "optional", "debit", D(cost),
                                      "USD", date(2025, 12, 2), date(2025, 12, 2), "settled", None,
                                      flexibility, D(floor) if floor is not None else None)
            events.append(source)
            rules.append(m.RecurringRule(name, "optional", "debit", D(cost), 30, date(2026, 1, 2),
                                         (name,), flexibility))
        dataset = m.Dataset({"person": profile}, {"purchase": request}, {}, {}, tuple(events), {}, {}, (), ())
        flows = list(explicit) + m.recurring_flows(rules, start, 90)
        return dataset, request, flows, rules

    def search(self, case):
        dataset, request, flows, rules = case
        with patch.object(m, "base_flows", return_value=([], flows, rules)):
            before = m.predict_no_change(dataset, request)
            result = m.plan_spending_changes(dataset, request, before)
            self.assertEqual(m.validate_output_row(result.output, dataset, request), [])
            return before, result

    def test_required_stop_covers_shortfall_without_changing_safe_amount(self):
        case = self.fixture()
        before, result = self.search(case)
        self.assertEqual(before["recommended_payment_method"], "not_recommended")
        self.assertEqual(result.output["spending_changes_needed"], "stop:service")
        self.assertEqual(result.output["amount_safe_to_pay"], before["amount_safe_to_pay"])
        self.assertEqual(result.output["earliest_date_for_full_payment"], before["earliest_date_for_full_payment"])
        self.assertTrue(any("necessary" in note for note in result.notes))

    def test_reduce_only_as_much_as_needed_and_respect_floor(self):
        before, result = self.search(self.fixture(streams=[("service", "30", "reducible", "5")]))
        # Three payments must total <=20: 6.66 each is safe, 6.67 is not.
        self.assertEqual(result.output["spending_changes_needed"], "reduce_to:service:6.66")

    def test_fewest_changes_then_least_total_spending_reduction(self):
        _, result = self.search(self.fixture(balance="300", amount="100", streams=[
            ("larger", "30", "stoppable", None), ("smaller", "10", "stoppable", None)]))
        # Deficit is20; either stop works, but smaller stop saves30 instead of90.
        self.assertEqual(result.output["spending_changes_needed"], "stop:smaller")

    def test_multiple_changes_when_no_single_action_suffices(self):
        _, result = self.search(self.fixture(streams=[
            ("first", "20", "stoppable", None), ("second", "20", "stoppable", None)]))
        self.assertEqual(result.output["spending_changes_needed"], "stop:first|stop:second")

    def test_savings_cannot_pay_a_shortfall_before_the_occurrence(self):
        before, result = self.search(self.fixture(balance="170"))
        self.assertEqual(result.output, before)  # Paying80 immediately leaves90 <100.

    def test_safe_plan_preserved_exactly(self):
        before, result = self.search(self.fixture(balance="400"))
        self.assertEqual(result.output, before)
        self.assertEqual(result.simulations, 1)

    def test_no_permission_protected_or_foreign_stream_is_ineligible(self):
        dataset, request, flows, rules = self.fixture()
        for profile in [replace(dataset.profiles["person"], stoppable_categories=frozenset()),
                        replace(dataset.profiles["person"], protected_categories=frozenset({"optional"}))]:
            modified = replace(dataset, profiles={"person": profile})
            self.assertEqual(m.eligible_spending_actions(modified, request, flows, rules), [])
        foreign = replace(dataset, events=(replace(dataset.events[0], currency="EUR"),))
        self.assertEqual(m.eligible_spending_actions(foreign, request, flows, rules), [])

    def test_explicit_and_same_day_occurrences_untouched(self):
        dataset, request, flows, rules = self.fixture()
        same_day_rule = replace(rules[0], next_date=request.request_date)
        same_day = m.recurring_flows([same_day_rule], request.request_date, 90)[0]
        explicit = replace(flows[0], source_id="pending", kind="explicit")
        flows = [same_day, explicit, *flows]
        actions = m.eligible_spending_actions(dataset, request, flows, rules)
        changed = m.apply_spending_actions(flows, actions, request)
        self.assertEqual(changed[:2], flows[:2])
        self.assertTrue(all(flow.amount == 0 for flow in changed[2:]))

    def test_ambiguous_streams_are_rejected(self):
        dataset, request, flows, rules = self.fixture()
        self.assertEqual(m.eligible_spending_actions(dataset, request, flows, rules * 2), [])

    def test_malformed_and_unauthorized_reductions_rejected(self):
        dataset, request, flows, rules = self.fixture(streams=[("service", "30", "reducible_or_stoppable", "5")])
        with patch.object(m, "base_flows", return_value=([], flows, rules)):
            for value in ["reduce_to:service:4.99", "reduce_to:service:NaN", "reduce_to:service:Infinity",
                          "reduce_to:service:30", "stop:service|reduce_to:service:6", "stop:unknown"]:
                self.assertTrue(m.validate_spending_changes(value, dataset, request), value)

    def test_changed_output_is_simulated_by_validator(self):
        dataset, request, flows, rules = self.fixture(streams=[("service", "30", "reducible", "5")])
        with patch.object(m, "base_flows", return_value=([], flows, rules)):
            row = m.predict_baseline(dataset, request)
            row["spending_changes_needed"] = "reduce_to:service:6.67"
            self.assertTrue(any("breaches" in error for error in m.validate_output_row(row, dataset, request)))

    def test_all_public_safe_decisions_unchanged_and_core_contexts_eligible(self):
        dataset = m.load_dataset(Path(__file__).resolve().parents[2] / "dataset")
        for request in dataset.samples.values():
            before = m.predict_no_change(dataset, request)
            after = m.predict_baseline(dataset, request)
            if before["payment_plan"] != "none":
                self.assertEqual(before, after, request.request_id)
        # IDs belong only to regression checks, never the implementation.
        for request_id, event_id in [("request_06", "event_476"), ("request_11", "event_948"),
                                     ("request_21", "event_1816")]:
            request = dataset.samples[request_id]
            _, flows, rules = m.base_flows(dataset, request)
            self.assertIn(event_id, {a.event_id for a in m.eligible_spending_actions(dataset, request, flows, rules)})


if __name__ == "__main__":
    unittest.main()
