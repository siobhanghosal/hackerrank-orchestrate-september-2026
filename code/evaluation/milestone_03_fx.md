# Milestone 3 — dated FX conversion

## Scope

This milestone establishes one deterministic conversion path for every
foreign-currency cash event before it enters the 90-day ledger.  It changes no
decision-selection rules, recurrence rules, payment-option rules, or public
sample labels.

## Conversion contract

`resolve_dated_fx_rate` takes the event cash date, original currency, and the
profile's home currency.  It uses the following ordered rules:

1. A same-currency event uses the Decimal identity rate of `1`.
2. An exact-date direct `from_currency → to_currency` row is authoritative.
3. Otherwise, an exact-date reverse row is inverted using `Decimal("1") / rate`.
4. When neither exact-date pair exists, the event is excluded conservatively;
   no nearest-date or live rate is invented.

An exact duplicate date/direction rate row is rejected by the data loader.
That is the only ambiguous source-pair case.  A direct and reverse row on the
same date are not treated as ambiguous: the direct row is authoritative,
because dataset rates may be independently rounded and therefore not exact
reciprocals.

Every included converted `ForecastFlow` retains its original amount/currency,
rate, and FX rule.  Missing-rate exclusions retain the `fx_missing_pair` rule.
The trace ledger renders these values, so conversion provenance is visible
without changing the financial calculation.

## Participant-data audit

The supplied participant files contain 139 foreign-currency cash events.  Each
has a direct exact-date rate.  Thus the public samples exercise the direct
path; inverse, identity, missing-date, and rounded-pair precedence are covered
by synthetic tests.

Request 25 is the public cross-currency example.  Its confirmed salary is
converted on its cash date, 2024-03-15:

```text
1,800 USD × 15,833.33 USD→IDR = 28,499,994 IDR
```

The provenance and ordered ledger are in
[sample_request_25_fx_trace.md](sample_request_25_fx_trace.md).

## Regression checks

```text
python -m unittest discover -s code/tests -p "test*.py"
python code/main.py --evaluate-samples --predictions-path code/evaluation/sample_baseline_predictions.csv
python code/main.py --check-evidence-regressions
```

| Check | Before | After | Result |
| --- | ---: | ---: | --- |
| Unit tests | 43 | 49 | pass |
| Structured public-sample matches | 94 / 175 | 94 / 175 | no regression |
| Amount-safe matches | 4 / 25 | 4 / 25 | unchanged |
| Status matches | 19 / 25 | 19 / 25 | unchanged |
| Method matches | 21 / 25 | 21 / 25 | unchanged |
| Payment-plan matches | 16 / 25 | 16 / 25 | unchanged |
| Earliest-date matches | 12 / 25 | 12 / 25 | unchanged |
| Spending-change matches | 22 / 25 | 22 / 25 | unchanged |

The stable result is expected: the supplied foreign flows were already direct
exact-date conversions.  Milestone 3 adds deterministic inverse handling,
strict data validation, and auditable provenance for evaluation cases that use
the other valid FX configurations.
