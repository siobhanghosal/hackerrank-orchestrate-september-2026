# Authorized spending-change audit

This audit was prepared before modifying decisions. Calculations use the existing
event normalization, recurrence generation and 90-day simulator. No solved output
fields authorize an action.

## Authorization and scope

Both tables must authorize a change: `financial_profiles.csv` supplies
`expense_categories_user_is_willing_to_stop` or
`expense_categories_user_is_willing_to_reduce`, while `financial_events.csv`
supplies `flexibility` (`stoppable`, `reducible`, `reducible_or_stoppable`).
`expense_categories_to_protect` always vetoes a change. Reductions respect
`minimum_allowed_amount`; a missing lower bound is not invented. Payments must
also respect `payment_methods_user_will_consider`, installment limits and request
partial-payment permissions.

An action names the latest historical source event of a supported recurring
stream. It changes only that stream's **already-generated occurrences strictly
after request_date**, within the original 90-day horizon. It does not refund the
historical source event or change a pending/scheduled explicit debit. Matching
uses the existing rule's description, category, source ID, amount and generated
dates, not category alone. Ambiguous stream matches are ineligible. Foreign-currency
streams are deferred to avoid applying an input-currency reduction to converted
cash without a defined future conversion. History, cadence and explicit events
remain unchanged.

## request_06 / user_06

Request 2026-01-03: EUR 620.40 due 2026-01-14. Balance EUR 1,942.40;
minimum EUR 800. Protected: rent, transport, insurance. Stop permission: streaming;
no reduce permission. Full/partial methods accepted; request disallows partial.

| Source event / stream | Authorization | Future dates | Maximum saving per occurrence / horizon |
| --- | --- | --- | --- |
| event_476 / Family streaming plan | `flexibility=stoppable`; streaming in stop list; unprotected | Jan 9, Feb 8, Mar 10, 2026 | EUR 19 / 57 |

Other recurring expenses are fixed or not authorized. Full payment already has a
projected minimum of EUR 1,083.26: shortfall **0**, headroom EUR 283.26. Thus no
change is necessary and the existing decision must be preserved. Savings can
cover at most EUR 19 of a shortfall after Jan 9, 38 after Feb 8, 57 after Mar 10;
none is available before Jan 9.

## request_11 / user_11

Request 2025-05-03: IDR 13,110,000 due 2025-06-12. Balance IDR 63,531,795;
minimum IDR 34,140,600. Protected: housing, utilities, education. Reduce permission:
dining, entertainment. Stop permission: cloud_storage. Only full payment accepted.

| Source event / stream | Authorization | Future dates | Maximum saving per occurrence / horizon |
| --- | --- | --- | --- |
| event_948 / Games and recreation | `flexibility=reducible`; entertainment in reduce list; minimum_allowed_amount=755250 | May 17, Jun 17, Jul 18, 2025 | IDR 919,637.61 / 2,758,912.83 (forecast 1,674,887.61 reduced to 755,250) |
| event_949 / Cloud storage plan | `flexibility=stoppable`; cloud_storage in stop list | May 15, Jun 15, Jul 16, 2025 | IDR 168,150 / 504,450 |

Dining records (including event_989, reducible with minimum 665950) have profile
permission but **no supported generated recurrence**. They cannot produce savings
in this task. Full payment already has a projected minimum of IDR 36,912,241.52:
shortfall **0**, headroom IDR 2,771,641.52. Preserve the decision. Maximum savings
are cumulative only after each listed date; none are available before May 15.

## request_21 / user_21

Request 2026-04-03: USD 1,574.40 due 2026-04-14. Balance USD 3,911.35;
minimum USD 1,800. Protected: groceries, utilities, rent. Reduce permission:
dining, streaming, shopping. Stop permission: cloud_storage, streaming.
Only full payment accepted.

| Source event / stream | Authorization | Future dates | Maximum saving per occurrence / horizon |
| --- | --- | --- | --- |
| event_1815 / Online backup subscription | `flexibility=stoppable`; cloud_storage in stop list | Apr 11, May 11, Jun 10, 2026 | USD 11 / 33 |
| event_1816 / Streaming subscription | `flexibility=reducible_or_stoppable`; streaming in both lists; minimum_allowed_amount=23.5 | Apr 8, May 8, Jun 7, 2026 | Reduce: USD 23.50 / 70.50; stop: USD 47 / 141 (mutually exclusive) |
| event_1817 / Monthly shopping spend | `flexibility=reducible`; shopping in reduce list; minimum_allowed_amount=49.6 | Apr 11, May 11, Jun 10, 2026 | USD 76.78 / 230.34 (forecast 126.38 reduced to 49.60) |

Dining permission alone cannot create a recurrence. Full payment already has a
projected minimum of USD 1,975.49: shortfall **0**, headroom USD 175.49. Preserve
the decision. Before Apr 8 none of these changes can cover a shortfall; later
coverage equals cumulative savings on the corresponding dates.

## Before feature: exact matches out of 25

Amount 4; status 17; method 19; payment plan 14; earliest date 11; spending changes
22; explanation 0. There are 21 requests with structured differences and zero
existing validator errors. These counts are for verification only.
