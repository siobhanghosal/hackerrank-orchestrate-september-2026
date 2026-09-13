# Milestone 5 — safe wait and partial-payment planner

## Scope and hypothesis

Make future full-payment and two-payment plans independent, fully simulated
candidates.  A partial plan may not borrow the safe date of a hypothetical
single full payment: its specific second payment must be safe after the
request-date payment has already occurred.

## Files and behaviour changed

- `code/main.py`
  - Adds `earliest_safe_partial_remainder`, which searches each date after the
    request date through the earlier of the deadline and 90-day horizon.
  - Simulates both partial-payment legs together for every candidate date.
  - Creates a partial candidate only for an allowed method, a strictly partial
    positive first payment, and a safe timely second payment.
  - Adds wait/partial search results to `--trace`.
- `code/tests/test_wait_partial.py`
  - Covers unsafe-now/safe-later full payment, safe first payment with a safe
    later remainder, safe first payment with unsafe remainder, and a disallowed
    partial-payment method.
- `code/evaluation/sample_request_19_wait_partial_trace.md`
  - Shows the full and partial search inputs for the current request 19
    forecast.

## Commands run

```text
python -m unittest discover -s code/tests -p "test*.py"
python code/main.py --evaluate-samples --predictions-path code/evaluation/sample_baseline_predictions.csv
python code/main.py --trace request_19 --write-trace code/evaluation/sample_request_19_wait_partial_trace.md
```

## Validation result

- 57/57 unit tests pass.
- Output validation errors: 0.
- Same-day debit-before-credit ordering is preserved in both full and partial
  simulations.

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

No public prediction changes.  In request 19, the current forecast's
request-date capacity is already the full request amount, so the contract
correctly forbids a partial candidate.  The solved public row's smaller first
payment therefore points upstream: its cash forecast/capacity differs, rather
than its partial-plan validation rule.

## Regressions or risks

- No output or validator regression.
- A future plan cannot be accepted merely because its first payment is safe;
  the remainder must survive its own dated simulation.
- The feature deliberately does not change the approved fixed-range recurrence
  policy.

## Recommendation: accept

Milestone 5 meets the plan's functional requirements but does not increase the
public metric.  The next work must target an upstream forecast discrepancy or
explicit evidence resolution that demonstrably changes affected sample rows;
no additional diagnostic-only milestone should be started first.
