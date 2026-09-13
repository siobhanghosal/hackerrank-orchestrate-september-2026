"""Synthetic Milestone 4 checks for supplied payment-option semantics."""

from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class PaymentOptionTests(unittest.TestCase):
    def setUp(self):
        self.day = date(2026, 1, 5)
        self.profile = m.Profile(
            "user", "USD", Decimal("100"), Decimal("40"), frozenset(), frozenset(),
            frozenset(), frozenset(), frozenset({"installments", "full_payment"}), 3,
        )
        self.request = m.Request(
            "request", "user", self.day, "purchase", Decimal("60"), self.day + timedelta(days=45),
            False, "Synthetic request",
        )

    def option(self, *, option_id="option", amount="20", payments=3, first=None, frequency=14,
               fee="0", total="60"):
        return m.PaymentOption(
            option_id, self.request.request_id, "installments", Decimal(amount), payments,
            first or self.day, frequency if payments > 1 else None, Decimal(fee), Decimal(total),
        )

    def dataset(self, *options):
        return m.Dataset(
            {"user": self.profile}, {self.request.request_id: self.request}, {}, {}, (),
            {self.request.request_id: tuple(options)}, {}, (), (),
        )

    def test_fee_bearing_schedule_requires_exact_total(self):
        option = self.option(amount="22", payments=3, fee="6", total="66")
        self.assertEqual(m.payment_option_validation_errors(option, self.request), [])
        malformed = self.option(amount="22", payments=3, fee="6", total="65")
        self.assertIn("scheduled payments do not equal total_payable_amount",
                      m.payment_option_validation_errors(malformed, self.request))

    def test_unsafe_intermediate_installment_is_rejected(self):
        option = self.option(amount="20", payments=3, total="60")
        second_date = self.day + timedelta(days=14)
        baseline = [m.ForecastFlow(second_date, Decimal("-45"), "essential", "test", "Essential", "explicit")]
        evaluation = m.evaluate_installment_options(self.dataset(option), self.request, baseline)[0]
        self.assertFalse(evaluation.accepted)
        self.assertIn("minimum balance breaches", evaluation.reason)

    def test_safe_later_installment_option_is_accepted(self):
        option = self.option(amount="20", payments=3, total="60")
        evaluation = m.evaluate_installment_options(self.dataset(option), self.request, [])[0]
        self.assertTrue(evaluation.accepted)
        self.assertEqual(evaluation.schedule[-1][0], self.day + timedelta(days=28))

    def test_deadline_and_profile_term_limit_reject_options(self):
        late = self.option(payments=3, frequency=30, total="60")
        late_evaluation = m.evaluate_installment_options(self.dataset(late), self.request, [])[0]
        self.assertIn("desired_completion_date", late_evaluation.reason)
        over_limit = self.option(payments=4, frequency=10, amount="15", total="60")
        limit_evaluation = m.evaluate_installment_options(self.dataset(over_limit), self.request, [])[0]
        self.assertIn("max_installment_months", limit_evaluation.reason)


if __name__ == "__main__":
    unittest.main()
