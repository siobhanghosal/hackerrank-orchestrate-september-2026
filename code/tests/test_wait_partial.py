"""Synthetic Milestone 5 checks for future full and two-payment plans."""

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class WaitAndPartialTests(unittest.TestCase):
    def setUp(self):
        self.day = date(2026, 2, 1)
        self.request = m.Request("request", "user", self.day, "purchase", Decimal("70"),
                                 self.day + timedelta(days=10), True, "Synthetic request")
        self.profile = m.Profile("user", "USD", Decimal("100"), Decimal("40"), frozenset(),
                                 frozenset(), frozenset(), frozenset(),
                                 frozenset({"full_payment", "partial_payment"}), None)

    def dataset(self, profile=None):
        profile = profile or self.profile
        return m.Dataset({"user": profile}, {self.request.request_id: self.request}, {}, {}, (), {}, {}, (), ())

    def test_unsafe_now_full_payment_becomes_safe_after_confirmed_credit(self):
        flows = [
            m.ForecastFlow(self.day + timedelta(days=1), Decimal("-40"), "bill", "test", "Bill", "explicit"),
            m.ForecastFlow(self.day + timedelta(days=2), Decimal("100"), "salary", "test", "Salary", "explicit"),
        ]
        # Same-day debits precede credits, so the credit date itself is unsafe.
        self.assertEqual(m.earliest_safe_full_payment(self.dataset(), self.request, flows), self.day + timedelta(days=3))

    def test_safe_first_payment_requires_a_safe_second_payment_date(self):
        flows = [
            m.ForecastFlow(self.day + timedelta(days=1), Decimal("-40"), "bill", "test", "Bill", "explicit"),
            m.ForecastFlow(self.day + timedelta(days=2), Decimal("100"), "salary", "test", "Salary", "explicit"),
        ]
        second = m.earliest_safe_partial_remainder(self.request, self.profile, flows, Decimal("20"))
        self.assertEqual(second, self.day + timedelta(days=3))

    def test_safe_first_payment_with_unsafe_remainder_is_not_a_candidate(self):
        profile = m.Profile("user", "USD", Decimal("120"), Decimal("50"), frozenset(),
                            frozenset(), frozenset(), frozenset(),
                            frozenset({"full_payment", "partial_payment"}), None)
        flows = [m.ForecastFlow(self.day + timedelta(days=1), Decimal("-50"), "bill", "test", "Bill", "explicit")]
        self.assertIsNone(m.earliest_safe_partial_remainder(self.request, profile, flows, Decimal("20")))

    def test_partial_payment_is_not_constructed_when_method_is_disallowed(self):
        profile = m.Profile("user", "USD", Decimal("100"), Decimal("40"), frozenset(),
                            frozenset(), frozenset(), frozenset(), frozenset({"full_payment"}), None)
        flows = [
            m.ForecastFlow(self.day + timedelta(days=1), Decimal("-40"), "bill", "test", "Bill", "explicit"),
            m.ForecastFlow(self.day + timedelta(days=2), Decimal("100"), "salary", "test", "Salary", "explicit"),
        ]
        candidates = m.payment_candidates(self.dataset(profile), self.request, flows, Decimal("20"),
                                          self.day + timedelta(days=2))
        self.assertFalse(any(candidate.method == "partial_payment" for candidate in candidates))


if __name__ == "__main__":
    unittest.main()
