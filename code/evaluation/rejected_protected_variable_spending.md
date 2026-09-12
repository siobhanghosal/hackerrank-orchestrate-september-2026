# Rejected Experiment — Protected Variable Spending Forecast

## Hypothesis

Forecast stable weekly protected grocery and transport debits when their merchant descriptions vary and therefore do not form a named fixed recurrence.

## Result

The candidate correctly exposed missing grocery/transport flows in traces, but it was too broad and conservative for the public contexts.

| Field | Accepted baseline | Candidate |
| --- | ---: | ---: |
| `amount_safe_to_pay` | 4/25 | 2/25 |
| `affordability_status` | 18/25 | 15/25 |
| `recommended_payment_method` | 20/25 | 17/25 |
| `payment_plan` | 15/25 | 13/25 |
| `earliest_date_for_full_payment` | 12/25 | 10/25 |
| `spending_changes_needed` | 22/25 | 22/25 |

Validation remained clean, but four protected core metrics regressed. The implementation was reverted and is not active.

## Lesson

The traces establish a real coverage gap for variable essential spending, but category-level extrapolation needs a narrower evidence threshold and must be re-tested as a separate candidate.
