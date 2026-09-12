# Evidence fact audit — public sample contexts

Scope: the 17 messages and five images associated with `sample_requests.csv` users or request IDs. `effective date` is the explicit date where present, otherwise the document/message date. Message actions below reflect the conservative resolver; image text was visually inspected for this audit but is not injected into the pipeline because no deterministic local OCR engine is available.

## Messages

| Source | Date / effective date | Action | Affected item | Extracted amount | Confidence | Exact reason |
| --- | --- | --- | --- | --- | --- | --- |
| `messages.csv:message_01` | 2025-07-29 / 2025-08-15 | amend | recurring salary | IDR 42,750,000 | high | Employer explicitly states the monthly salary and the effective date. |
| `messages.csv:message_02` | 2019-08-31 / 2019-08-31 | ignore | none | — | low | Confirms a payroll generally but supplies no amount, payment date, or identifiable event amendment. |
| `messages.csv:message_03` | 2024-06-01 / 2024-06-01 | ignore | unapproved quarterly bonus | — | high availability fact, no target | The bonus amount and payment date are explicitly unapproved; no matching supplied future credit is identifiable to override. |
| `messages.csv:message_04` | 2025-12-28 / 2025-12-28 | amend | next recurring salary | EUR 1,037.52 | high | Employer states the temporary monthly pay and that it applies to the affected next payroll. |
| `messages.csv:message_05` | 2024-08-29 / 2024-09-23 | amend | next recurring salary date | — | high | Employer explicitly replaces the earlier payroll date. |
| `messages.csv:message_06` | 2025-02-06 / 2025-02-06 | amend | next recurring salary | EUR 1,422.85 | high | Employer explicitly states the reduced next-salary amount. |
| `messages.csv:message_07` | 2024-11-25 / 2024-11-25 | ignore | QuickCrew payout | — | high availability fact, no target | The credit is explicitly not withdrawable, but the notice has no related event and no uniquely identifiable supplied payout event. |
| `messages.csv:message_08` | 2025-04-22 / 2025-04-22 | amend | recurring base salary | IDR 38,760,000 | high | Employer confirms a base salary; the unapproved commission is not counted. |
| `messages.csv:message_09` | 2026-03-25 / 2026-03-25 | cancel | future recurring salary | — | high | Employer explicitly says the seasonal contract ended and no off-season income or renewal is confirmed. |
| `messages.csv:message_10` | 2025-07-27 / 2025-08-15 | amend | recurring salary | EUR 2,717 | high | Employer explicitly states the regular salary and date it resumes. The childcare deduction has no stated amount, so it is not invented. |
| `messages.csv:message_11` | 2026-01-03 / 2026-01-15 | confirm | first salary | EUR 1,661 | high | Employer states both a first-salary amount and a confirmed credit date. |
| `messages.csv:message_12` | 2023-08-01 / 2023-08-01 | ignore | rent recurrence | +12% (no base amount) | low | The notice lacks an identifiable next rent event and a resulting payment amount; no amount is inferred. |
| `messages.csv:message_13` | 2026-07-01 / 2026-07-01 | ignore | matching own-account transfer | — | low | No transaction IDs or amounts are supplied; the message alone cannot safely eliminate either entry. |
| `messages.csv:message_14` | 2026-02-06 / 2026-02-06 | delay / exclude | `event_1785` refund | INR 8,640 (event record) | high | The linked merchant notice explicitly says the refund has not reached the account. |
| `messages.csv:message_15` | 2024-12-02 / 2024-12-02 | ignore | `event_1960` portfolio valuation | EUR 369.60 (event record) | high | It explicitly confirms no sale or cash proceeds; the already-unrealized non-cash event remains excluded. |
| `messages.csv:message_16` | 2025-04-26 / 2025-04-26 | ignore | prize claim | — | high availability fact, no target | The prize is explicitly not credited, but no related supplied credit event is identified. |
| `messages.csv:message_17` | 2025-12-29 / 2025-12-29 | confirm | `event_2165` prize proceeds | INR 33,550 (event record) | high | The linked notice says proceeds reached the account and the claim is closed; it confirms that one settled credit and does not create future income. |

## Linked images

| Source | Date / effective date | Action | Affected event | Extracted amount | Confidence | Exact reason |
| --- | --- | --- | --- | --- | --- | --- |
| `images.csv:image_01` / `media/images/image_01.png` | 2019-08-31 / 2019-08-31 | confirm historical amount | `event_253` | IDR 4,365,000 net pay | high visual | Payslip explicitly shows August 2019 net pay; it is historical at the request date. |
| `images.csv:image_02` / `media/images/image_02.png` | 2023-08-11 / 2023-08-16 | amend amount | `event_1442` | INR 1,000,000 balance due | high visual | Rent receipt explicitly labels the balance due; the event supplies the scheduled settlement date. |
| `images.csv:image_03` / `media/images/image_03.png` | 2026-02-27 / 2026-02-27 | confirm historical amount | `event_1545` | INR 41,772 | high visual | Receipt shows net amount and cash paid; this is historical before the request. |
| `images.csv:image_04` / `media/images/image_04.png` | 2024-09-03 / 2024-09-03 | confirm historical amount | `event_1700` | INR 2,854 | high visual | Delivered grocery-order item bill displays INR 2,854; it is historical before the request. |
| `images.csv:image_05` / `media/images/image_05.png` | 2026-02-06 / 2026-02-09 | amend amount | `event_1786` | INR 822.05 | high visual | Telecom statement explicitly shows amount due after 06-Feb-2026; event supplies pending settlement date. |

## Resolver boundaries

- Only text facts matching an explicit high-confidence pattern are applied automatically.
- Resolver rules never create an expense, income, date, or amount that is absent from the evidence.
- Image amounts remain auditable but excluded from automatic use until a deterministic, packaged OCR/extraction path is available.
