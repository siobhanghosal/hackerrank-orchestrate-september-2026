# Milestone 00 — Accepted baseline

## Scope and hypothesis

This milestone freezes and verifies the active deterministic baseline. It makes no financial-policy, recurrence, evidence, selector, validator, or ledger change.

The rejected recurrence-reconciliation candidate remains inactive. The active forecast continues to use the previously accepted recurrence and explicit-event behaviour.

## Repository state

- Branch: `main`
- Commit: `255c52e8f430967bacb83674f9815e2339b292de` (`Initial Commit`)
- `code/main.py` SHA-256: `162C3A22FE49A4BC606EE9C12BBEEA1F29DA80D17D21A323CD428CA153A22F84`
- `code/evaluation/sample_baseline_predictions.csv` SHA-256: `339C5EEE0B2BE937A3D51B4119034DC20D62D988B10A9DBE4D6B307BB11FF9AB`
- Working-tree checks at verification time: no staged or unstaged implementation diff; `git diff --check` emitted no whitespace errors.

## Commands run

```text
python code/main.py --evaluate-samples
python code/main.py --check-evidence-regressions
python -m unittest discover -s code -p "test*.py" -v
python -c "... predict all 250 requests in memory and call validate_output_rows(...) ..."
git diff --check
```

## Validation result

- Full request set: 250 predicted rows; 0 validation errors.
- Public sample predictions: 25 rows; 0 validation errors.
- Evidence regression checks: passed, covering 9 high-confidence facts across 25 sample contexts.
- Regression suite: 12 tests passed.

## Sample metrics: accepted baseline

| Field | Exact matches |
| --- | ---: |
| `amount_safe_to_pay` | 4/25 |
| `affordability_status` | 17/25 |
| `recommended_payment_method` | 19/25 |
| `payment_plan` | 14/25 |
| `earliest_date_for_full_payment` | 11/25 |
| `spending_changes_needed` | 22/25 |
| `decision_explanation` | 0/25 |

Requests with one or more structured-field discrepancies: 21/25.

## Regressions or risks

No accepted baseline metric regressed in this verification. The known recurrence-reconciliation experiment is documented separately as rejected; it is not part of the active baseline.

## Recommendation: accept

Milestone 0 is complete. Use this report and its hashes as the comparison point for the isolated Milestone 0.5a selector-tie-break candidate.
