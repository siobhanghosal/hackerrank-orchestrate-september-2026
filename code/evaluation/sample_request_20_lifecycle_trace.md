# Trace: request_20

As of `2026-02-07`, current balance is `102609.05` INR.

## Supplied post-request events counted

- `event_1787` — 2026-02-08: -4470 (Pending online order charge; explicit).

## Inferred recurring commitments counted

- `Payroll credit` (`salary`): credit 108000 every 30 days, starting 2026-02-14; evidence: event_1717, event_1725, event_1733.
- `Home association fee` (`housing`): debit 7950 every 31 days, starting 2026-03-05; evidence: event_1726, event_1734, event_1741.
- `Municipal utilities` (`utilities`): debit 7769.87 every 31 days, starting 2026-03-08; evidence: event_1727, event_1735, event_1742.
- `Household insurance` (`insurance`): debit 3290 every 31 days, starting 2026-03-09; evidence: event_1728, event_1736, event_1743.
- `School fee payment` (`education`): debit 8740 every 30 days, starting 2026-03-08; evidence: event_1721, event_1729, event_1737.
- `Family healthcare expense` (`healthcare`): debit 6654.33 every 30 days, starting 2026-02-08; evidence: event_1722, event_1730, event_1738.
- `Cinema and events` (`entertainment`): debit 2115.92 every 30 days, starting 2026-02-12; evidence: event_1723, event_1731, event_1739.
- `Shared storage plan` (`cloud_storage`): debit 365 every 30 days, starting 2026-02-10; evidence: event_1724, event_1732, event_1740.

## Evidence resolutions

- `message_14`: `exclude_credit` effective 2026-02-06; explicit statement that the related credit is not yet available.
- `event_1785`: excluded by `message_14` under explicit statement that the related credit is not yet available; evidence message_14.

## Linked-event lifecycle resolution

- `event_1784` -> `event_1785`: `retain` under `lifecycle_distinct_cash_leg`; original transaction and linked refund/sale are distinct cash movements.
- `event_1785` -> `event_1784`: `retain` under `lifecycle_distinct_cash_leg`; linked refund/sale follows its own cash status and effective date.

## Safe no-change payment candidates

- None; no safe permitted no-change payment candidate completes by the desired date.

## Authorized spending-change search

- Baseline full_payment ending 2026-02-07 shortfall: 279196.2.
- Candidate reduce_to:event_1739:1085 / full_payment: 90-day savings 3092.76, minimum -213665.28; insufficient or too late.
- Candidate stop:event_1740 / full_payment: 90-day savings 1095, minimum -214331.2; insufficient or too late.
- Candidate reduce_to:event_1739:1085|stop:event_1740 / full_payment: 90-day savings 4187.76, minimum -213300.28; insufficient or too late.
- No safe authorized candidate found; preserved existing output.
- Candidate/guard simulations: 4.

## Baseline 90-day result

- Minimum projected balance before this request: 89003.8 on 2026-02-12.
- First minimum-balance breach: none.

## Ordered ledger for the recommended output

Same-day rule: debits first, then credits; ties use source ID, kind, category, and exact Decimal amount.

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-02-08 | debit | -4470 | 102609.05 | 98139.05 | `event_1787` | explicit | `event_1787` | - | pending debit retained as a conservative liability |
| 2 | 2026-02-08 | debit | -6654.33 | 98139.05 | 91484.72 | `recurring:healthcare` | recurring | `event_1722`, `event_1730`, `event_1738` | - | history supports a fixed 30-day recurrence |
| 3 | 2026-02-10 | debit | -365 | 91484.72 | 91119.72 | `recurring:cloud_storage` | recurring | `event_1724`, `event_1732`, `event_1740` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-02-12 | debit | -2115.92 | 91119.72 | 89003.8 | `recurring:entertainment` | recurring | `event_1723`, `event_1731`, `event_1739` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-02-14 | credit | 108000 | 89003.8 | 197003.8 | `recurring:salary` | recurring | `event_1717`, `event_1725`, `event_1733` | - | history supports a fixed 30-day recurrence |
| 6 | 2026-03-05 | debit | -7950 | 197003.8 | 189053.8 | `recurring:housing` | recurring | `event_1726`, `event_1734`, `event_1741` | - | history supports a fixed 31-day recurrence |
| 7 | 2026-03-08 | debit | -8740 | 189053.8 | 180313.8 | `recurring:education` | recurring | `event_1721`, `event_1729`, `event_1737` | - | history supports a fixed 30-day recurrence |
| 8 | 2026-03-08 | debit | -7769.87 | 180313.8 | 172543.93 | `recurring:utilities` | recurring | `event_1727`, `event_1735`, `event_1742` | - | history supports a fixed 31-day recurrence |
| 9 | 2026-03-09 | debit | -3290 | 172543.93 | 169253.93 | `recurring:insurance` | recurring | `event_1728`, `event_1736`, `event_1743` | - | history supports a fixed 31-day recurrence |
| 10 | 2026-03-10 | debit | -6654.33 | 169253.93 | 162599.6 | `recurring:healthcare` | recurring | `event_1722`, `event_1730`, `event_1738` | - | history supports a fixed 30-day recurrence |
| 11 | 2026-03-12 | debit | -365 | 162599.6 | 162234.6 | `recurring:cloud_storage` | recurring | `event_1724`, `event_1732`, `event_1740` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-03-14 | debit | -2115.92 | 162234.6 | 160118.68 | `recurring:entertainment` | recurring | `event_1723`, `event_1731`, `event_1739` | - | history supports a fixed 30-day recurrence |
| 13 | 2026-03-16 | credit | 108000 | 160118.68 | 268118.68 | `recurring:salary` | recurring | `event_1717`, `event_1725`, `event_1733` | - | history supports a fixed 30-day recurrence |
| 14 | 2026-04-05 | debit | -7950 | 268118.68 | 260168.68 | `recurring:housing` | recurring | `event_1726`, `event_1734`, `event_1741` | - | history supports a fixed 31-day recurrence |
| 15 | 2026-04-07 | debit | -8740 | 260168.68 | 251428.68 | `recurring:education` | recurring | `event_1721`, `event_1729`, `event_1737` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-04-08 | debit | -7769.87 | 251428.68 | 243658.81 | `recurring:utilities` | recurring | `event_1727`, `event_1735`, `event_1742` | - | history supports a fixed 31-day recurrence |
| 17 | 2026-04-09 | debit | -6654.33 | 243658.81 | 237004.48 | `recurring:healthcare` | recurring | `event_1722`, `event_1730`, `event_1738` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-04-09 | debit | -3290 | 237004.48 | 233714.48 | `recurring:insurance` | recurring | `event_1728`, `event_1736`, `event_1743` | - | history supports a fixed 31-day recurrence |
| 19 | 2026-04-11 | debit | -365 | 233714.48 | 233349.48 | `recurring:cloud_storage` | recurring | `event_1724`, `event_1732`, `event_1740` | - | history supports a fixed 30-day recurrence |
| 20 | 2026-04-13 | debit | -2115.92 | 233349.48 | 231233.56 | `recurring:entertainment` | recurring | `event_1723`, `event_1731`, `event_1739` | - | history supports a fixed 30-day recurrence |
| 21 | 2026-04-15 | credit | 108000 | 231233.56 | 339233.56 | `recurring:salary` | recurring | `event_1717`, `event_1725`, `event_1733` | - | history supports a fixed 30-day recurrence |
| 22 | 2026-05-06 | debit | -7950 | 339233.56 | 331283.56 | `recurring:housing` | recurring | `event_1726`, `event_1734`, `event_1741` | - | history supports a fixed 31-day recurrence |
| 23 | 2026-05-07 | debit | -8740 | 331283.56 | 322543.56 | `recurring:education` | recurring | `event_1721`, `event_1729`, `event_1737` | - | history supports a fixed 30-day recurrence |

First recommended-plan breach: none.
