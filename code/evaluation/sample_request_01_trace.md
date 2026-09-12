# Trace: request_01

As of `2024-03-03`, current balance is `58481.1` ZAR.

## Supplied post-request events counted

- `event_102` — 2024-03-05: -567.6 (Pending fuel authorization; explicit).
- `event_103` — 2024-03-15: 23320 (Next confirmed salary; explicit).

## Inferred recurring commitments counted

- `Apartment rent transfer` (`rent`): debit 5148 every 30 days, starting 2024-04-01; evidence: event_19, event_26, event_32.
- `Household utility payment` (`utilities`): debit 1651.81 every 31 days, starting 2024-03-08; evidence: event_14, event_20, event_27.
- `Professional training fee` (`education`): debit 1821.6 every 31 days, starting 2024-03-10; evidence: event_15, event_21, event_28.
- `Education loan instalment` (`debt_repayment`): debit 3487 every 31 days, starting 2024-03-13; evidence: event_16, event_22, event_29.
- `Music service subscription` (`music_subscription`): debit 235.4 every 31 days, starting 2024-03-13; evidence: event_17, event_23, event_30.
- `Delivery service plan` (`delivery_membership`): debit 306.9 every 31 days, starting 2024-03-15; evidence: event_18, event_24, event_31.

## Lifecycle records excluded

- `event_100` — cancelled event.

## Safe no-change payment candidates

- `full_payment`: completes 2024-03-03, starts 2024-03-03, total 25256, payments 1, option payment_option_01; selector rank (False, False, Decimal('25256'), datetime.date(2024, 3, 3), 1, 'payment_option_01') — selected.

## Authorized spending-change search

- Existing no-change plan shortfall: 0 ZAR.
- Preserved existing safe no-change output; spending changes are unnecessary.
- Candidate/guard simulations: 1.

## Baseline 90-day result

- Minimum projected balance before this request: 43281.37 on 2024-05-31.
- First minimum-balance breach: none.

## Ordered ledger for the recommended output

Same-day rule: debits first, then credits; ties use source ID, kind, category, and exact Decimal amount.

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-03-03 | debit | -25256 | 58481.1 | 33225.1 | `request_payment` | requested_payment | - | - | candidate payment from the selected request plan |
| 2 | 2024-03-05 | debit | -567.6 | 33225.1 | 32657.5 | `event_102` | explicit | `event_102` | - | pending debit retained as a conservative liability |
| 3 | 2024-03-08 | debit | -1651.81 | 32657.5 | 31005.69 | `recurring:utilities` | recurring | `event_14`, `event_20`, `event_27` | - | history supports a fixed 31-day recurrence |
| 4 | 2024-03-10 | debit | -1821.6 | 31005.69 | 29184.09 | `recurring:education` | recurring | `event_15`, `event_21`, `event_28` | - | history supports a fixed 31-day recurrence |
| 5 | 2024-03-13 | debit | -3487 | 29184.09 | 25697.09 | `recurring:debt_repayment` | recurring | `event_16`, `event_22`, `event_29` | - | history supports a fixed 31-day recurrence |
| 6 | 2024-03-13 | debit | -235.4 | 25697.09 | 25461.69 | `recurring:music_subscription` | recurring | `event_17`, `event_23`, `event_30` | - | history supports a fixed 31-day recurrence |
| 7 | 2024-03-15 | debit | -306.9 | 25461.69 | 25154.79 | `recurring:delivery_membership` | recurring | `event_18`, `event_24`, `event_31` | - | history supports a fixed 31-day recurrence |
| 8 | 2024-03-15 | credit | 23320 | 25154.79 | 48474.79 | `event_103` | explicit | `event_103` | - | cash event |
| 9 | 2024-04-01 | debit | -5148 | 48474.79 | 43326.79 | `recurring:rent` | recurring | `event_19`, `event_26`, `event_32` | - | history supports a fixed 30-day recurrence |
| 10 | 2024-04-08 | debit | -1651.81 | 43326.79 | 41674.98 | `recurring:utilities` | recurring | `event_14`, `event_20`, `event_27` | - | history supports a fixed 31-day recurrence |
| 11 | 2024-04-10 | debit | -1821.6 | 41674.98 | 39853.38 | `recurring:education` | recurring | `event_15`, `event_21`, `event_28` | - | history supports a fixed 31-day recurrence |
| 12 | 2024-04-13 | debit | -3487 | 39853.38 | 36366.38 | `recurring:debt_repayment` | recurring | `event_16`, `event_22`, `event_29` | - | history supports a fixed 31-day recurrence |
| 13 | 2024-04-13 | debit | -235.4 | 36366.38 | 36130.98 | `recurring:music_subscription` | recurring | `event_17`, `event_23`, `event_30` | - | history supports a fixed 31-day recurrence |
| 14 | 2024-04-15 | debit | -306.9 | 36130.98 | 35824.08 | `recurring:delivery_membership` | recurring | `event_18`, `event_24`, `event_31` | - | history supports a fixed 31-day recurrence |
| 15 | 2024-05-01 | debit | -5148 | 35824.08 | 30676.08 | `recurring:rent` | recurring | `event_19`, `event_26`, `event_32` | - | history supports a fixed 30-day recurrence |
| 16 | 2024-05-09 | debit | -1651.81 | 30676.08 | 29024.27 | `recurring:utilities` | recurring | `event_14`, `event_20`, `event_27` | - | history supports a fixed 31-day recurrence |
| 17 | 2024-05-11 | debit | -1821.6 | 29024.27 | 27202.67 | `recurring:education` | recurring | `event_15`, `event_21`, `event_28` | - | history supports a fixed 31-day recurrence |
| 18 | 2024-05-14 | debit | -3487 | 27202.67 | 23715.67 | `recurring:debt_repayment` | recurring | `event_16`, `event_22`, `event_29` | - | history supports a fixed 31-day recurrence |
| 19 | 2024-05-14 | debit | -235.4 | 23715.67 | 23480.27 | `recurring:music_subscription` | recurring | `event_17`, `event_23`, `event_30` | - | history supports a fixed 31-day recurrence |
| 20 | 2024-05-16 | debit | -306.9 | 23480.27 | 23173.37 | `recurring:delivery_membership` | recurring | `event_18`, `event_24`, `event_31` | - | history supports a fixed 31-day recurrence |
| 21 | 2024-05-31 | debit | -5148 | 23173.37 | 18025.37 | `recurring:rent` | recurring | `event_19`, `event_26`, `event_32` | - | history supports a fixed 30-day recurrence |

First recommended-plan breach: none.
