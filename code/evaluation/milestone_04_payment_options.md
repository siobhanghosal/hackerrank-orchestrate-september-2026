# Milestone 4 — payment-option semantics

## Scope and hypothesis

Evaluate every supplied installment option as its complete dated schedule and
fee-bearing total, rather than treating a first installment as sufficient
evidence that an option is usable.  This is a plan-required prerequisite for
the safe wait/partial planner in Milestone 5.

## Files and behaviour changed

- `code/main.py`
  - Validates payment-option request linkage, finite positive payment values,
    dates/frequencies, schedule total, financing fee, and total payable at load
    time.
  - Validates `total_payable_amount == requested_amount + financing_fee` and
    `sum(schedule) == total_payable_amount` using `Decimal`.
  - Adds `PaymentOptionEvaluation`, which records each offer's complete
    schedule, eligibility, safety result, and deterministic rejection reason.
  - Uses those evaluations to construct installment candidates.
  - Adds option acceptance/rejection output to `--trace`.
- `code/tests/test_payment_options.py`
  - Covers a fee-bearing valid/invalid total, unsafe intermediate installment,
    safe later installment, deadline violation, and term-limit rejection.
- `code/evaluation/sample_request_19_payment_options_trace.md`
  - Shows all three supplied offers and why the two-payment option is the only
    currently eligible installment candidate.

## Commands run

```text
python -m unittest discover -s code/tests -p "test*.py"
python code/main.py --evaluate-samples --predictions-path code/evaluation/sample_baseline_predictions.csv
python code/main.py --trace request_19 --write-trace code/evaluation/sample_request_19_payment_options_trace.md
```

## Validation result

- 53/53 unit tests pass.
- Dataset payment options load with complete schedule and fee validation.
- Output validation errors: 0.

## Sample metrics: before → after

| Field | Before | After |
| --- | ---: | ---: |
| `amount_safe_to_pay` | 4/25 | 4/25 |
| `affordability_status` | 19/25 | 19/25 |
| `recommended_payment_method` | 21/25 | 21/25 |
| `payment_plan` | 16/25 | 16/25 |
| `earliest_date_for_full_payment` | 12/25 | 12/25 |
| `spending_changes_needed` | 22/25 | 22/25 |
| Structured total | 94/175 | 94/175 |

## Changed requests and trace evidence

No public prediction changes.  This is expected: the currently selected public
installment schedules were already internally valid and safe.  The new trace
now makes the decision checkable.  For request 19, the full-payment option is
not an installment, the three-payment offer exceeds the user's two-month
limit, and the two-payment option is safe.  The remaining discrepancy is a
Milestone 5 issue: no eligible partial-payment candidate is constructed with a
second-payment feasibility search.

## Regressions or risks

- No output or validator regression.
- The option contract rejects malformed source data early rather than silently
  selecting it.
- This milestone does not change recurrence or cash-flow availability.

## Recommendation: accept

Milestone 4 meets the implementation-plan contract.  Its completed option
evaluation is now the shared input for Milestone 5, where safe future-payment
and partial-payment candidates can produce decision changes.
