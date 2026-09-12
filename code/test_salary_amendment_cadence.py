"""Regression checks for employer-confirmed replacement salary dates."""

import unittest
from datetime import date
from decimal import Decimal as D

import main as m


class SalaryAmendmentCadenceTests(unittest.TestCase):
    def salary(self, event_id, intended_date, settled_date):
        event = m.FinancialEvent(
            event_id, "user", "income", "Payroll credit", "salary", "credit", D("100"), "USD",
            intended_date, settled_date, "settled", None, "fixed", None,
        )
        return m.NormalizedEvent(event, D("100"), settled_date, True, "cash event")

    def test_confirmed_future_payday_repairs_one_delayed_settlement(self):
        records = [
            self.salary("one", date(2024, 6, 15), date(2024, 6, 15)),
            self.salary("two", date(2024, 7, 15), date(2024, 7, 15)),
            self.salary("three", date(2024, 8, 15), date(2024, 8, 23)),
        ]
        fact = m.EvidenceFact(
            "message", "message", "user", "amend_salary", date(2024, 9, 23), None,
            None, None, "high", "employer explicitly replaces the payroll date",
        )
        rules = m.recurring_rules(records, date(2024, 9, 5), m.EvidenceResolution((fact,)))
        salary_rules = [rule for rule in rules if rule.category == "salary"]
        self.assertEqual(len(salary_rules), 1)
        self.assertEqual(salary_rules[0].interval_days, 30)
        self.assertEqual(salary_rules[0].next_date, date(2024, 9, 23))
        self.assertEqual(salary_rules[0].evidence_sources, ("message",))

    def test_delayed_settlement_without_confirmation_keeps_cash_date_cadence(self):
        records = [
            self.salary("one", date(2024, 6, 15), date(2024, 6, 15)),
            self.salary("two", date(2024, 7, 15), date(2024, 7, 15)),
            self.salary("three", date(2024, 8, 15), date(2024, 8, 23)),
        ]
        rules = m.recurring_rules(records, date(2024, 9, 5), m.EvidenceResolution(()))
        salary_rules = [rule for rule in rules if rule.category == "salary"]
        self.assertEqual(len(salary_rules), 1)
        self.assertEqual(salary_rules[0].interval_days, 34)
        self.assertEqual(salary_rules[0].next_date, date(2024, 9, 26))


if __name__ == "__main__":
    unittest.main()
