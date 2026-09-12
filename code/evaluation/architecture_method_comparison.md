# Forecast Architecture Comparison — Public Samples Only

## Test scope

Each run predicts the 25 rows in `dataset/sample_requests.csv` and compares its output with that file's supplied solved columns. The financial profiles, events, payment options, exchange rates, and evidence files remain contextual inputs; no `dataset/requests.csv` predictions are generated for this comparison.

The metrics below count exact matches by output field. They are evaluation-only and are not consulted by forecasting logic.

## Method 1 — Fixed-range recurring payments (current control)

This is the current active architecture. It adds all explicit post-request events and, for every well-supported historical recurring stream, generates 90-day future occurrences by its inferred fixed day interval.

| Measure | Result |
| --- | ---: |
| Sample rows | 25 |
| Rows with a structured-field discrepancy | 21 |
| `amount_safe_to_pay` | 4/25 |
| `affordability_status` | 17/25 |
| `recommended_payment_method` | 19/25 |
| `payment_plan` | 14/25 |
| `earliest_date_for_full_payment` | 11/25 |
| `spending_changes_needed` | 22/25 |
| `decision_explanation` | 0/25 |
| Validation errors | 0 |

## Method 2 — Event-by-event calculation

Pending experiment. This will use only supplied, dated, post-request cash events in the 90-day ledger and will not infer recurring occurrences.

## Method 3 — Event-first hybrid

Pending experiment. This will retain explicit dated events as authoritative and infer a recurring occurrence only for a supported stream's uncovered gap, suppressing a generated occurrence that matches an explicit future event.

## Final comparison and recommendation

Pending completion of Methods 2 and 3.
