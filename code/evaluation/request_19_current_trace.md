# Trace: request_19

As of `2024-09-04`, current balance is `199545` INR.

## Supplied post-request events counted

- None.

## Inferred recurring commitments counted

- `Payroll credit` (`salary`): credit 131000 every 30 days, starting 2024-09-14; evidence: event_1638, event_1646, event_1654.
- `Residential rent payment` (`rent`): debit 36100 every 30 days, starting 2024-10-03; evidence: event_1639, event_1647, event_1655.
- `Municipal utilities` (`utilities`): debit 6129.19 every 30 days, starting 2024-09-07; evidence: event_1640, event_1648, event_1656.
- `Loan repayment` (`debt_repayment`): debit 11850 every 30 days, starting 2024-09-12; evidence: event_1641, event_1649, event_1657.
- `Clinic payment` (`healthcare`): debit 8645.36 every 30 days, starting 2024-09-11; evidence: event_1642, event_1650, event_1658.
- `Childcare contribution` (`family_support`): debit 12650 every 30 days, starting 2024-09-14; evidence: event_1643, event_1651, event_1659.
- `Online backup subscription` (`cloud_storage`): debit 395 every 30 days, starting 2024-09-13; evidence: event_1644, event_1652, event_1660.
- `Clothing and household items` (`shopping`): debit 6069.58 every 30 days, starting 2024-09-13; evidence: event_1645, event_1653, event_1661.
- `Fresh food shop` (`groceries`): debit 6070.85 every 24 days, starting 2024-09-12; evidence: event_1664, event_1668, event_1671.

## Payment-option evaluation

- `payment_option_52`: rejected; not an installment option.
- `payment_option_53`: accepted; all dated payments are safe through completion.
- `payment_option_54`: rejected; option exceeds max_installment_months.

## Wait and partial-payment search

- Earliest safe one-payment date: 2024-09-04.
- No partial candidate: the request-date capacity is zero or already covers the full request.

## Safe no-change payment candidates

- `installments`: completes 2024-10-02, starts 2024-09-04, total 41246.4, payments 2, option payment_option_53; selector rank (False, False, Decimal('41246.4'), datetime.date(2024, 9, 4), 2, 'payment_option_53') — selected.

## Authorized spending-change search

- Existing no-change plan shortfall: 0 INR.
- Preserved existing safe no-change output; spending changes are unnecessary.
- Candidate/guard simulations: 1.

## Baseline 90-day result

- Minimum projected balance before this request: 147735.02 on 2024-09-14.
- First minimum-balance breach: none.

## Ordered ledger for the recommended output

Same-day rule: debits first, then credits; ties use source ID, kind, category, and exact Decimal amount.

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason | Original | FX rate rule |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2024-09-04 | debit | -20623.2 | 199545 | 178921.8 | `request_payment` | requested_payment | - | - | candidate payment from the selected request plan | - | - |
| 2 | 2024-09-07 | debit | -6129.19 | 178921.8 | 172792.61 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence | - | - |
| 3 | 2024-09-11 | debit | -8645.36 | 172792.61 | 164147.25 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence | - | - |
| 4 | 2024-09-12 | debit | -11850 | 164147.25 | 152297.25 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence | - | - |
| 5 | 2024-09-12 | debit | -6070.85 | 152297.25 | 146226.4 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence | - | - |
| 6 | 2024-09-13 | debit | -395 | 146226.4 | 145831.4 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence | - | - |
| 7 | 2024-09-13 | debit | -6069.58 | 145831.4 | 139761.82 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence | - | - |
| 8 | 2024-09-14 | debit | -12650 | 139761.82 | 127111.82 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence | - | - |
| 9 | 2024-09-14 | credit | 131000 | 127111.82 | 258111.82 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence | - | - |
| 10 | 2024-10-02 | debit | -20623.2 | 258111.82 | 237488.62 | `request_payment` | requested_payment | - | - | candidate payment from the selected request plan | - | - |
| 11 | 2024-10-03 | debit | -36100 | 237488.62 | 201388.62 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence | - | - |
| 12 | 2024-10-06 | debit | -6070.85 | 201388.62 | 195317.77 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence | - | - |
| 13 | 2024-10-07 | debit | -6129.19 | 195317.77 | 189188.58 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence | - | - |
| 14 | 2024-10-11 | debit | -8645.36 | 189188.58 | 180543.22 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence | - | - |
| 15 | 2024-10-12 | debit | -11850 | 180543.22 | 168693.22 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence | - | - |
| 16 | 2024-10-13 | debit | -395 | 168693.22 | 168298.22 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence | - | - |
| 17 | 2024-10-13 | debit | -6069.58 | 168298.22 | 162228.64 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence | - | - |
| 18 | 2024-10-14 | debit | -12650 | 162228.64 | 149578.64 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence | - | - |
| 19 | 2024-10-14 | credit | 131000 | 149578.64 | 280578.64 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence | - | - |
| 20 | 2024-10-30 | debit | -6070.85 | 280578.64 | 274507.79 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence | - | - |
| 21 | 2024-11-02 | debit | -36100 | 274507.79 | 238407.79 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence | - | - |
| 22 | 2024-11-06 | debit | -6129.19 | 238407.79 | 232278.6 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence | - | - |
| 23 | 2024-11-10 | debit | -8645.36 | 232278.6 | 223633.24 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence | - | - |
| 24 | 2024-11-11 | debit | -11850 | 223633.24 | 211783.24 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence | - | - |
| 25 | 2024-11-12 | debit | -395 | 211783.24 | 211388.24 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence | - | - |
| 26 | 2024-11-12 | debit | -6069.58 | 211388.24 | 205318.66 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence | - | - |
| 27 | 2024-11-13 | debit | -12650 | 205318.66 | 192668.66 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence | - | - |
| 28 | 2024-11-13 | credit | 131000 | 192668.66 | 323668.66 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence | - | - |
| 29 | 2024-11-23 | debit | -6070.85 | 323668.66 | 317597.81 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence | - | - |
| 30 | 2024-12-02 | debit | -36100 | 317597.81 | 281497.81 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence | - | - |

First recommended-plan breach: none.
