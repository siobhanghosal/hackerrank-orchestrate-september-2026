# Milestone 00.5a — Selector Tie-Break Conformance

## Scope and hypothesis

Replace the previous early-return payment selection with one construction-and-selection pass over all safe, permitted, no-change payment candidates. The selector must follow the literal ordering in `problem_statement.md`:

1. Complete by `desired_completion_date`.
2. Require no spending changes.
3. Minimize total paid.
4. Start earlier.
5. Use fewer payments.
6. Use the lowest `payment_option_id` as the final tie-breaker.

This milestone does not change cash-flow construction, evidence resolution, lifecycle handling, recurrence, FX, candidate safety simulation, or validation rules.

## Files/behaviour changed

- `code/main.py`
  - Adds a typed `PaymentCandidate` representation.
  - Builds all safe, permitted full-payment, installment, partial-payment, and later-wait candidates before selection.
  - Applies the literal selector tuple in one location, `candidate_rank`.
  - Makes `wait` eligible only if full payment becomes safe strictly after `request_date`.
  - Adds the safe candidates, rank tuple, and selected candidate to `--trace`.
- `code/test_selector_tiebreak.py`
  - Covers deadline, cost, start date, payment count, and option-ID precedence with synthetic candidates.

## Commands run

```text
python -m unittest discover -s code -p "test*.py" -v
python code/main.py --evaluate-samples
python code/main.py --trace request_01
git diff --check
```

## Validation result

- 15 synthetic and regression tests passed.
- Sample-output validation errors: 0.
- Trace confirms the selector rank for `request_01` and selects its full-payment candidate.

## Sample metrics: before → after

| Field | Before | After |
| --- | ---: | ---: |
| `amount_safe_to_pay` | 4/25 | 4/25 |
| `affordability_status` | 17/25 | 17/25 |
| `recommended_payment_method` | 19/25 | 19/25 |
| `payment_plan` | 14/25 | 14/25 |
| `earliest_date_for_full_payment` | 11/25 | 11/25 |
| `spending_changes_needed` | 22/25 | 22/25 |
| `decision_explanation` | 0/25 | 0/25 |

## Changed requests and trace evidence

No structured sample output changed from the fixed-range control. The no-change candidate and its selected rank are now visible in `--trace`; for `request_01`, the selected full-payment candidate has rank:

```text
(False, False, Decimal('25256'), 2024-03-03, 1, 'payment_option_01')
```

The first candidate implementation briefly treated a same-day `wait` as distinct from a safe full payment. That is not a valid `wait` recommendation under the specification, so it was excluded. The final candidate produces no public-output regression.

## Regressions or risks

No metric or validation regression remains. The selector order is independently tested; however, this public sample set contains no case where the new order changes the final output, so hidden cases are the primary expected benefit.

## Recommendation: accept after manual review

The candidate is isolated, conforms to the specified ranking order, passes its tests, and preserves the accepted baseline metrics.
