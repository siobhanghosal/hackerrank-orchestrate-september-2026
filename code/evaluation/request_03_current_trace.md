# Trace: request_03

As of `2019-09-03`, current balance is `5810300` IDR.

## Supplied post-request events counted

- `event_254` — 2019-09-07: -95000 (Pending pharmacy card charge; explicit).

## Inferred recurring commitments counted

- `Payroll credit` (`salary`): credit 4365000 every 30 days, starting 2019-09-14; evidence: event_198, event_204, event_210.
- `Landlord standing order` (`rent`): debit 1140000 every 30 days, starting 2019-10-03; evidence: event_199, event_205, event_212.
- `Water and power payment` (`utilities`): debit 303042.45 every 30 days, starting 2019-09-07; evidence: event_200, event_206, event_213.
- `Shared storage plan` (`cloud_storage`): debit 20900 every 30 days, starting 2019-09-13; evidence: event_201, event_207, event_214.
- `Video streaming plan` (`streaming`): debit 117800 every 30 days, starting 2019-09-10; evidence: event_202, event_208, event_215.
- `Clothing and household items` (`shopping`): debit 180395.29 every 30 days, starting 2019-09-13; evidence: event_203, event_209, event_216.
- `Bulk pantry shop` (`groceries`): debit 234390.87 every 10 days, starting 2019-09-08; evidence: event_217, event_218, event_219.

## Payment-option evaluation

- `payment_option_08`: rejected; not an installment option.
- `payment_option_09`: rejected; option exceeds max_installment_months.
- `payment_option_10`: rejected; option exceeds max_installment_months.

## Wait and partial-payment search

- Earliest safe one-payment date: 2019-10-15.
- Safe second payment after request-date amount 2190071.39: 2019-10-15.

## Safe no-change payment candidates

- `wait`: completes 2019-10-15, starts 2019-10-15, total 5491000, payments 1, option no supplied option; selector rank (False, False, Decimal('5491000'), datetime.date(2019, 10, 15), 1, '') — selected.

## Authorized spending-change search

- Existing no-change plan shortfall: 0 IDR.
- Preserved existing safe no-change output; spending changes are unnecessary.
- Candidate/guard simulations: 1.

## Baseline 90-day result

- Minimum projected balance before this request: 4858771.39 on 2019-09-13.
- First minimum-balance breach: none.

## Ordered ledger for the recommended output

Same-day rule: debits first, then credits; ties use source ID, kind, category, and exact Decimal amount.

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason | Original | FX rate rule |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2019-09-07 | debit | -95000 | 5810300 | 5715300 | `event_254` | explicit | `event_254` | - | pending debit retained as a conservative liability | - | - |
| 2 | 2019-09-07 | debit | -303042.45 | 5715300 | 5412257.55 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence | - | - |
| 3 | 2019-09-08 | debit | -234390.87 | 5412257.55 | 5177866.68 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 4 | 2019-09-10 | debit | -117800 | 5177866.68 | 5060066.68 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence | - | - |
| 5 | 2019-09-13 | debit | -20900 | 5060066.68 | 5039166.68 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence | - | - |
| 6 | 2019-09-13 | debit | -180395.29 | 5039166.68 | 4858771.39 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence | - | - |
| 7 | 2019-09-14 | credit | 4365000 | 4858771.39 | 9223771.39 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence | - | - |
| 8 | 2019-09-18 | debit | -234390.87 | 9223771.39 | 8989380.52 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 9 | 2019-09-28 | debit | -234390.87 | 8989380.52 | 8754989.65 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 10 | 2019-10-03 | debit | -1140000 | 8754989.65 | 7614989.65 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence | - | - |
| 11 | 2019-10-07 | debit | -303042.45 | 7614989.65 | 7311947.2 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence | - | - |
| 12 | 2019-10-08 | debit | -234390.87 | 7311947.2 | 7077556.33 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 13 | 2019-10-10 | debit | -117800 | 7077556.33 | 6959756.33 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence | - | - |
| 14 | 2019-10-13 | debit | -20900 | 6959756.33 | 6938856.33 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence | - | - |
| 15 | 2019-10-13 | debit | -180395.29 | 6938856.33 | 6758461.04 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence | - | - |
| 16 | 2019-10-14 | credit | 4365000 | 6758461.04 | 11123461.04 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence | - | - |
| 17 | 2019-10-15 | debit | -5491000 | 11123461.04 | 5632461.04 | `request_payment` | requested_payment | - | - | candidate payment from the selected request plan | - | - |
| 18 | 2019-10-18 | debit | -234390.87 | 5632461.04 | 5398070.17 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 19 | 2019-10-28 | debit | -234390.87 | 5398070.17 | 5163679.3 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 20 | 2019-11-02 | debit | -1140000 | 5163679.3 | 4023679.3 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence | - | - |
| 21 | 2019-11-06 | debit | -303042.45 | 4023679.3 | 3720636.85 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence | - | - |
| 22 | 2019-11-07 | debit | -234390.87 | 3720636.85 | 3486245.98 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 23 | 2019-11-09 | debit | -117800 | 3486245.98 | 3368445.98 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence | - | - |
| 24 | 2019-11-12 | debit | -20900 | 3368445.98 | 3347545.98 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence | - | - |
| 25 | 2019-11-12 | debit | -180395.29 | 3347545.98 | 3167150.69 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence | - | - |
| 26 | 2019-11-13 | credit | 4365000 | 3167150.69 | 7532150.69 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence | - | - |
| 27 | 2019-11-17 | debit | -234390.87 | 7532150.69 | 7297759.82 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 28 | 2019-11-27 | debit | -234390.87 | 7297759.82 | 7063368.95 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence | - | - |
| 29 | 2019-12-02 | debit | -1140000 | 7063368.95 | 5923368.95 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence | - | - |

First recommended-plan breach: none.
