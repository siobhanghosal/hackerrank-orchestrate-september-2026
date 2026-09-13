"""Synthetic checks for exact-date direct and inverse foreign-exchange resolution."""

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class DatedFxTests(unittest.TestCase):
    def setUp(self):
        self.day = date(2025, 2, 3)

    def test_direct_rate_is_selected_on_the_exact_cash_date(self):
        rates = {
            (self.day, "EUR", "USD"): Decimal("1.25"),
            (self.day + timedelta(days=1), "EUR", "USD"): Decimal("1.30"),
        }
        resolution = m.resolve_dated_fx_rate(rates, self.day, "EUR", "USD")
        self.assertEqual(resolution.rate, Decimal("1.25"))
        self.assertEqual(resolution.rule_id, "fx_direct_pair")
        self.assertEqual(resolution.source_pair, ("EUR", "USD"))

    def test_inverse_rate_is_inverted_with_decimal_math(self):
        rates = {(self.day, "USD", "EUR"): Decimal("1.25")}
        resolution = m.resolve_dated_fx_rate(rates, self.day, "EUR", "USD")
        self.assertEqual(resolution.rate, Decimal("0.8"))
        self.assertEqual(resolution.rule_id, "fx_inverse_pair")
        self.assertEqual(resolution.source_pair, ("USD", "EUR"))

    def test_same_currency_uses_identity_without_rate_row(self):
        resolution = m.resolve_dated_fx_rate({}, self.day, "USD", "USD")
        self.assertEqual(resolution.rate, Decimal("1"))
        self.assertEqual(resolution.rule_id, "fx_identity")

    def test_missing_rate_never_uses_a_nearby_date(self):
        rates = {(self.day + timedelta(days=1), "EUR", "USD"): Decimal("1.25")}
        resolution = m.resolve_dated_fx_rate(rates, self.day, "EUR", "USD")
        self.assertIsNone(resolution.rate)
        self.assertEqual(resolution.rule_id, "fx_missing_pair")

    def test_direct_pair_is_authoritative_when_inverse_is_independently_rounded(self):
        rates = {
            (self.day, "EUR", "USD"): Decimal("1.25"),
            (self.day, "USD", "EUR"): Decimal("0.70"),
        }
        resolution = m.resolve_dated_fx_rate(rates, self.day, "EUR", "USD")
        self.assertEqual(resolution.rate, Decimal("1.25"))
        self.assertEqual(resolution.rule_id, "fx_direct_pair")

    def test_normalization_carries_inverse_rate_provenance_to_forecast_flow(self):
        profile = m.Profile("user", "USD", Decimal("100"), Decimal("10"), frozenset(),
                            frozenset(), frozenset(), frozenset(), frozenset(), None)
        event = m.FinancialEvent(
            "income", "user", "income", "Settled foreign income", "salary", "credit", Decimal("10"), "EUR",
            self.day, self.day, "settled", None, "fixed", None,
        )
        dataset = m.Dataset({"user": profile}, {}, {}, {}, (event,), {},
                            {(self.day, "USD", "EUR"): Decimal("1.25")}, (), ())
        normalized = m.normalize_events(dataset, "user")
        flow = m.future_explicit_flows(normalized, self.day - timedelta(days=1))[0]
        self.assertEqual(flow.amount, Decimal("8"))
        self.assertEqual(flow.original_amount, Decimal("10"))
        self.assertEqual(flow.original_currency, "EUR")
        self.assertEqual(flow.conversion_rate, Decimal("0.8"))
        self.assertEqual(flow.fx_rule, "fx_inverse_pair")


if __name__ == "__main__":
    unittest.main()
