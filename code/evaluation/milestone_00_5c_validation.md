# Milestone 00.5c — Validator and Untrusted-Content Conformance

## Scope

This milestone changes no prediction logic. It verifies existing output-boundary
rules and the evidence boundary with synthetic invalid rows and an untrusted
message. Evidence extraction remains limited to typed `EvidenceFact` values;
message text is never an executable instruction.

## Verified constraints

- `affordable_now` requires an earliest full-payment date exactly equal to the
  request date.
- `spending_changes_needed` accepts one to three actions only.
- The same event cannot appear in two spending actions.
- Instructional text from an untrusted message resolves to `ignore`, not a
  decision command.

## Prediction-integrity check

The sample prediction artifact was hashed before and after the validation-only
work. Both hashes are identical:

```text
SHA256 40F271DD1CF3588A37A9FA6FF59E28387E971D273D34C86B1175EA0DEB55B4C4
```

## Validation

```text
python -m unittest discover -s code/tests -p "test*.py" -v
python code/main.py --evaluate-samples
git diff --check
```
