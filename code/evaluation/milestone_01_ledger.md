# Milestone 1 - Forecast ledger contract

## Scope and hypothesis

This milestone is a diagnostic refactor only. It replaces the thin cash-flow
record with one canonical immutable `ForecastFlow`, makes same-day ordering an
explicit reusable rule, and retains enough provenance to explain every applied
flow. It does not change recurrence, lifecycle, evidence, FX, or plan-selection
policy.

## Files and behaviour changed

- `code/main.py`
  - Added immutable `ForecastFlow` with finite-`Decimal` validation, source
    event IDs, evidence IDs, and inclusion reason.
  - Added immutable `LedgerStep` with sequence, opening balance, and closing
    balance.
  - Centralized ordering in `forecast_flow_order_key`: date, debits before
    credits, then source ID, kind, category, and exact amount.
  - Added `SimulationResult.first_breach()` and a shared output-plan
    re-simulation path.
  - Extended `--trace` with the ordered ledger and first minimum-balance breach.
  - Added `--write-ledger-delta-report` for all mismatched public samples.
- `code/tests/test_forecast_ledger.py`
  - Added five synthetic ledger contract checks.
- `code/evaluation/sample_ledger_delta_report.md`
  - Records expected/actual differences, balances, included/excluded events,
    safe candidates, and immediate-full first breach for all 21 failures.
- `code/evaluation/sample_request_01_trace.md`
  - Refreshed with canonical ordered-ledger provenance.

## Commands run

```text
python -m unittest discover -s code/tests -p "test*.py" -v
python code/main.py --write-ledger-delta-report code/evaluation/sample_ledger_delta_report.md
python code/main.py --trace request_01 --write-trace code/evaluation/sample_request_01_trace.md
python code/main.py --evaluate-samples --predictions-path code/evaluation/sample_baseline_predictions.csv
Get-FileHash -Algorithm SHA256 code/evaluation/sample_baseline_predictions.csv
```

## Validation result

- 37/37 unit tests passed.
- Five new synthetic checks cover flow immutability, finite `Decimal` values,
  exact decimal arithmetic, deterministic same-day ordering, exclusion of an
  already-settled occurrence, and inclusion of a future pending debit.
- Output validation errors: 0.
- Prediction artifact before SHA-256:
  `40F271DD1CF3588A37A9FA6FF59E28387E971D273D34C86B1175EA0DEB55B4C4`
- Prediction artifact after SHA-256:
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

No prediction row changed. `sample_request_01_trace.md` demonstrates the new
ordering contract and provenance while retaining its previous decision. The
new delta report covers all 21 mismatched requests without feeding solved
fields into prediction.

## Regressions or risks

- None observed in outputs or tests.
- The ledger exposes missing lifecycle/FX/payment semantics but deliberately
  does not correct them in this milestone.
- The accepted fixed-day recurrence policy is unchanged.

## Recommendation: accept

The pass criteria are satisfied. The next isolated feature should use this
ledger to implement explicit linked-event lifecycle resolution.
