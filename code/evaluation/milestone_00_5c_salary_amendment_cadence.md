# Milestone 00.5c — Confirmed Salary-Date Cadence

## Scope

When an employer explicitly confirms a future replacement payroll date, that
confirmation may repair one delayed settlement that would otherwise prevent a
well-supported salary stream from being forecast. The engine uses historical
`event_date` values only to establish the fixed-day cadence in that narrow
case, then anchors the forecast on the confirmed future date. All other
streams continue to use settlement dates.

## Evidence and guardrails

- The rule applies only to `salary` credits with three or more settled records.
- It requires an existing high-confidence `amend_salary` evidence fact whose
  effective date is after the request date.
- It does not create salary income where no settled salary stream exists.
- Without that confirmation, the normal cash-date cadence remains unchanged.
- The trace identifies the employer message as resolver evidence on the rule.

## Validation

```text
python -m unittest discover -s code/tests -p "test*.py" -v
python code/main.py --evaluate-samples
git diff --check
```

All 19 tests passed and output validation remained clean.

## Sample-only metrics

| Field | Before | After |
| --- | ---: | ---: |
| `amount_safe_to_pay` | 4/25 | 4/25 |
| `affordability_status` | 18/25 | 19/25 |
| `recommended_payment_method` | 20/25 | 21/25 |
| `payment_plan` | 15/25 | 16/25 |
| `earliest_date_for_full_payment` | 12/25 | 12/25 |
| `spending_changes_needed` | 22/25 | 22/25 |
| `decision_explanation` | 0/25 | 0/25 |

The change restores a safe supplied installment option for the public context
with a confirmed replacement payday. No reported structured metric regressed.
