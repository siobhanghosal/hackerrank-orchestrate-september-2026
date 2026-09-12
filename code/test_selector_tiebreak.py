"""Synthetic checks for the literal payment-candidate selector order."""

import unittest
from datetime import date
from decimal import Decimal as D

import main as m


class SelectorTieBreakTests(unittest.TestCase):
    request = m.Request("request", "user", date(2026, 1, 1), "purchase", D("100"), date(2026, 1, 10), False, "")

    def candidate(self, *, total="100", start=date(2026, 1, 1), completion=date(2026, 1, 1),
                  payments=1, option_id=None, method="full_payment"):
        schedule = ((completion, D(total)),) if payments == 1 else tuple(
            (start if index == 0 else completion, D(total) / payments) for index in range(payments))
        return m.PaymentCandidate("affordable_now", method, schedule, start, option_id, "synthetic")

    def test_completion_by_deadline_precedes_lower_cost(self):
        late = self.candidate(total="1", start=date(2026, 1, 11), completion=date(2026, 1, 11))
        on_time = self.candidate(total="100", start=date(2026, 1, 10), completion=date(2026, 1, 10))
        self.assertIs(m.choose_payment_candidate([late, on_time], self.request), on_time)

    def test_lower_cost_precedes_earlier_start(self):
        cheaper_later = self.candidate(total="99", start=date(2026, 1, 2), completion=date(2026, 1, 2))
        dearer_earlier = self.candidate(total="100", start=date(2026, 1, 1), completion=date(2026, 1, 1))
        self.assertIs(m.choose_payment_candidate([dearer_earlier, cheaper_later], self.request), cheaper_later)

    def test_earlier_start_then_fewer_payments_then_option_id(self):
        later = self.candidate(start=date(2026, 1, 2), completion=date(2026, 1, 2))
        many = self.candidate(start=date(2026, 1, 1), completion=date(2026, 1, 1), payments=2, option_id="option_01")
        option_b = self.candidate(option_id="option_02")
        option_a = self.candidate(option_id="option_01")
        self.assertIs(m.choose_payment_candidate([later, many, option_b, option_a], self.request), option_a)


if __name__ == "__main__":
    unittest.main()
