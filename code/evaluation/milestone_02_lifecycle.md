# Milestone 2 - Lifecycle and linked-event resolver

## Scope and hypothesis

Replace blanket parent suppression with an explicit resolver based only on
`linked_event_id`, lifecycle status, direction, and event type. No proximity,
category matching, sample request IDs, or solved output fields are used.

The conflict order is encoded conservatively: explicit terminal/settled state,
then an explicitly linked replacement, then a settled occurrence over an open
representation, and finally retain uncertain debits while unavailable credits
remain excluded by their individual cash state.

## Files and behaviour changed

- `code/main.py`
  - Validates that every supplied link exists, stays within one user, and is
    not self-referential.
  - Adds immutable `LifecycleDecision` and `LifecycleResolution` records.
  - Adds `resolve_event_lifecycles()` with traceable rule IDs.
  - Removes the old rule that suppressed every event which happened to be the
    parent of another event.
  - Keeps refunds and investment sales as separate cash legs.
  - Keeps pending refunds unavailable under the existing credit-state rule.
  - Makes a settled linked record supersede a pending/scheduled representation
    of the same-direction lifecycle.
  - Keeps ambiguous linked debits as liabilities.
  - Excludes linked unrealized valuations without suppressing their purchase.
  - Carries both event IDs and the lifecycle reason into forecast-ledger traces.
- `code/tests/test_linked_event_lifecycle.py`
  - Adds six synthetic relationship-chain checks.
- `code/evaluation/sample_request_20_lifecycle_trace.md`
  - Demonstrates a settled purchase plus unavailable pending refund.

## Participant-data inventory

The supplied participant-facing event file contains 58 linked pairs and seven
shapes:

| Linked shape | Pairs |
| --- | ---: |
| settled expense -> settled refund | 14 |
| investment purchase -> unrealized valuation | 10 |
| cancelled authorization -> settled expense | 8 |
| settled expense -> pending refund | 8 |
| failed debt debit -> scheduled retry | 7 |
| settled expense -> pending possible duplicate debit | 6 |
| investment purchase -> settled investment sale | 5 |

All 58 links exist and remain within the same user. The resolver emits 116
per-event decisions: 54 distinct-cash-leg retains, 20 non-cash-child decisions,
30 terminal-predecessor/replacement decisions, and 12 conservative ambiguous
debit retains.

## Commands run

```text
python -m unittest discover -s code/tests -p "test*.py" -v
python code/main.py --evaluate-samples --predictions-path code/evaluation/sample_baseline_predictions.csv
python code/main.py --trace request_20 --write-trace code/evaluation/sample_request_20_lifecycle_trace.md
Get-FileHash -Algorithm SHA256 code/evaluation/sample_baseline_predictions.csv
```

## Validation result

- 43/43 tests passed.
- New synthetic cases cover pending-to-settled, pending-to-reversal/refund,
  pending refund unavailable, ambiguous duplicate debit, failed-to-scheduled
  retry, and linked unrealized valuation.
- Output validation errors: 0.
- Before and after prediction SHA-256:
  `40F271DD1CF3588A37A9FA6FF59E28387E971D273D34C86B1175EA0DEB55B4C4`

## Sample metrics: before -> after

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

No public sample prediction changed. The linked rows for the five affected
sample users are historical, unavailable pending credits, or non-cash values,
so the corrected relationship semantics do not move their forecast balances.
The request 20 trace records both sides of the refund relationship and the
message-based exclusion of the still-pending credit.

## Regressions or risks

- No public output or validator regression.
- Ambiguous debits intentionally remain conservative, even if a later reversal
  may eventually remove them.
- No new message pattern was added; evidence extraction remains unchanged.
- Fixed-range recurrence remains unchanged.

## Recommendation: accept

The feature closes the blanket linked-parent suppression defect and satisfies
the lifecycle contract without changing public outputs. Milestone 3 dated FX
conversion is the next isolated accuracy candidate.
