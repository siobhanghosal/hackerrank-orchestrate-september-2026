"""Regression checks for explicit terminal salary records."""

import unittest
from datetime import date
from decimal import Decimal as D
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main as m


class TerminalSalaryTests(unittest.TestCase):
    def settled_salary(self, event_id, when, description="Regular payroll"):
        event = m.FinancialEvent(event_id, "user", "income", description, "salary", "credit", D("100"), "USD",
                                 when, when, "settled", None, "fixed", None)
        return m.NormalizedEvent(event, D("100"), when, True, "cash event")

    def test_later_final_payroll_terminates_prior_salary_recurrence(self):
        records = [self.settled_salary("one", date(2025, 1, 15)), self.settled_salary("two", date(2025, 2, 15)),
                   self.settled_salary("three", date(2025, 3, 15)),
                   self.settled_salary("final", date(2025, 4, 15), "Final employer payroll")]
        rules = m.recurring_rules(records, date(2025, 5, 1), m.EvidenceResolution(()))
        self.assertEqual([rule for rule in rules if rule.category == "salary"], [])

    def test_nonterminal_later_salary_does_not_stop_the_stream(self):
        records = [self.settled_salary("one", date(2025, 1, 15)), self.settled_salary("two", date(2025, 2, 15)),
                   self.settled_salary("three", date(2025, 3, 15)),
                   self.settled_salary("later", date(2025, 4, 15), "Correction payroll")]
        rules = m.recurring_rules(records, date(2025, 5, 1), m.EvidenceResolution(()))
        self.assertEqual(len([rule for rule in rules if rule.category == "salary"]), 1)


if __name__ == "__main__":
    unittest.main()
