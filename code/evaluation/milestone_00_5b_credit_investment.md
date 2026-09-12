# Milestone 00.5b — Credit Lifecycle: Terminal Salary

## Scope and hypothesis

This is one isolated credit-lifecycle rule discovered from a mismatch-ledger trace. A recurring `Payroll credit` stream in request_05 was projected after a later settled event explicitly described as `Final employer payroll`. The source record is stronger than recurrence inference, so it must terminate the prior inferred salary stream.

No pending-credit, linked-event, investment, FX, payment-option, or spending-change rule is changed by this candidate.

## Files/behaviour changed

- `code/main.py`
  - Adds `is_terminal_salary_record` for settled salary credits whose source description explicitly states `final` or `last` payroll/salary/pay.
  - Suppresses only an earlier same-category inferred salary stream after such a record.
  - Adds the suppressing source event and rule to `--trace`.
- `code/tests/test_terminal_salary.py`
  - Confirms a later final payroll terminates recurrence.
  - Confirms a non-terminal later payroll does not terminate recurrence.

## Commands run

```text
python -m unittest discover -s code/tests -p "test*.py" -v
python code/main.py --evaluate-samples
python code/main.py --trace request_05
git diff --check
```

## Validation result

- 17 synthetic and regression tests passed.
- Sample-output validation errors: 0.
- Trace for request_05 names `event_390` (`Final employer payroll`) as the source suppressing the inferred salary stream.

## Sample metrics: before → after

| Field | Before | After |
| --- | ---: | ---: |
| `amount_safe_to_pay` | 4/25 | 4/25 |
| `affordability_status` | 17/25 | 18/25 |
| `recommended_payment_method` | 19/25 | 20/25 |
| `payment_plan` | 14/25 | 15/25 |
| `earliest_date_for_full_payment` | 11/25 | 12/25 |
| `spending_changes_needed` | 22/25 | 22/25 |
| `decision_explanation` | 0/25 | 0/25 |

## Changed requests and trace evidence

`request_05` changes from `affordable_now` / `full_payment` to `not_affordable` / `not_recommended`. Its forecast no longer invents post-termination payroll. The amount safe today drops from `15488` to `7006.21`; it does not yet match the solved `737`, indicating a separate remaining forecast gap rather than a reason to broaden this rule.

## Regressions or risks

No core field regressed. The rule requires both a final/last term and a payroll/salary/pay term on a settled salary credit, so it does not infer employment termination from ordinary income variability.

## Completed lifecycle-conformance boundary

The milestone now also makes the full conservative cash-state boundary explicit:

- An unconfirmed pending credit is excluded.
- A pending credit is included only with an attributable `confirm_credit` fact,
  using that fact's effective cash date.
- A scheduled salary is included only when the supplied event explicitly says it
  is confirmed and includes its settlement date; other scheduled credits are
  excluded.
- Pending debits remain in the ledger as conservative liabilities.
- `investment_value` records are excluded before cash-flow construction,
  including when their status is `unrealized`.

`test_credit_lifecycle.py` covers each case. The full suite has 24 tests, the
sample metrics remain `4/25`, `19/25`, `21/25`, `16/25`, `12/25`, and `22/25`
for amount, status, method, plan, earliest date, and spending changes
respectively, and output validation remains at zero errors.

## Recommendation: accept

The rule is attributable, traceable, independently tested, and improves four core exact-match totals without regression. The next diagnosis should address missing essential variable spending rather than expand terminal-income matching.
