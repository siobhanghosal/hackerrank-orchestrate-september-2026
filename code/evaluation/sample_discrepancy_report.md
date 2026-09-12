# Sample discrepancy report

This audit reads the supplied `sample_baseline_predictions.csv`; report generation does not run prediction. Solved rows are used only to compare public samples, never as prediction inputs.

## Before-fix metrics

- Structured failures: **21/25** (decision explanation excluded from this failure count).
- Exact explanation matches: **0/25**; baseline explanations are intentionally generic.

| Field | Exact matches |
| --- | ---: |
| `amount_safe_to_pay` | 4/25 |
| `affordability_status` | 16/25 |
| `recommended_payment_method` | 18/25 |
| `payment_plan` | 14/25 |
| `earliest_date_for_full_payment` | 9/25 |
| `spending_changes_needed` | 22/25 |
| `decision_explanation` | 0/25 |

## After latest fix metrics

- Structured failures: **21/25** (decision explanation excluded from this failure count).
- Exact explanation matches: **0/25**; baseline explanations are intentionally generic.

| Field | Exact matches |
| --- | ---: |
| `amount_safe_to_pay` | 4/25 |
| `affordability_status` | 17/25 |
| `recommended_payment_method` | 19/25 |
| `payment_plan` | 14/25 |
| `earliest_date_for_full_payment` | 11/25 |
| `spending_changes_needed` | 22/25 |
| `decision_explanation` | 0/25 |

## Reusable failure categories

| Category | Failures | Requests |
| --- | ---: | --- |
| cancellations or amendments from messages | 5 | `request_04`, `request_14`, `request_15`, `request_20`, `request_24` |
| dated currency conversion | 1 | `request_25` |
| duplicate / linked-event handling | 1 | `request_05` |
| earliest-date computation | 6 | `request_02`, `request_03`, `request_08`, `request_17`, `request_18`, `request_22` |
| flexible spending changes | 3 | `request_06`, `request_11`, `request_21` |
| partial-payment eligibility and timing | 1 | `request_19` |
| payment-option schedule or financing fee handling | 1 | `request_07` |
| pending debit or credit handling | 2 | `request_10`, `request_23` |
| recurrence detection / forecasting frequency | 1 | `request_13` |

## Per-request evidence

## request_02 — user_02

Primary category: **earliest-date computation**

Both results select installments; the discrepancy is capacity/earliest-full-payment timing rather than an option-selection failure.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 17229139.2 | 16237972.2 |
| `decision_explanation` | Use 3 installments of IDR 15,952,906.67, starting 8 August 2025. This leaves at least IDR 29,158,400 available. | Baseline selected supplied installment option payment_option_05. |

### Financial profile

- Home currency: `IDR`
- Current balance: `60383889.2`
- Minimum balance: `29158400`
- Protected: `education|housing|utilities`; reduce: `entertainment`; stop: `cloud_storage`.
- Payment methods: `installments|partial_payment`; max installment months: `7`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-08-06 | recurring:utilities | recurring | utilities | -2141849.94 | Inferred recurring Municipal utilities |
| 2025-08-07 | recurring:insurance | recurring | insurance | -1132400 | Inferred recurring Household insurance |
| 2025-08-08 | recurring:education | recurring | education | -3040000 | Inferred recurring Course tuition |
| 2025-08-08 | event_185 | explicit | shopping | -1651100 | Pending merchant debit |
| 2025-08-10 | recurring:healthcare | recurring | healthcare | -1641668.72 | Inferred recurring Clinic payment |
| 2025-08-12 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-08-12 | recurring:cloud_storage | recurring | cloud_storage | -369550 | Inferred recurring Shared storage plan |
| 2025-08-14 | recurring:groceries | recurring | groceries | -2218141.61 | Inferred recurring Local market purchase |
| 2025-08-14 | recurring:entertainment | recurring | entertainment | -1352563.79 | Inferred recurring Cinema and events |
| 2025-08-15 | recurring:salary | recurring | salary | 42750000 | Inferred recurring Payroll credit |
| 2025-08-26 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-09-03 | recurring:housing | recurring | housing | -3534000 | Inferred recurring Home repair reserve |
| 2025-09-05 | recurring:utilities | recurring | utilities | -2141849.94 | Inferred recurring Municipal utilities |
| 2025-09-06 | recurring:insurance | recurring | insurance | -1132400 | Inferred recurring Household insurance |
| 2025-09-07 | recurring:education | recurring | education | -3040000 | Inferred recurring Course tuition |
| 2025-09-09 | recurring:healthcare | recurring | healthcare | -1641668.72 | Inferred recurring Clinic payment |
| 2025-09-09 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-09-11 | recurring:cloud_storage | recurring | cloud_storage | -369550 | Inferred recurring Shared storage plan |
| 2025-09-13 | recurring:entertainment | recurring | entertainment | -1352563.79 | Inferred recurring Cinema and events |
| 2025-09-14 | recurring:salary | recurring | salary | 42750000 | Inferred recurring Payroll credit |
| 2025-09-18 | recurring:groceries | recurring | groceries | -2218141.61 | Inferred recurring Local market purchase |
| 2025-09-23 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-10-03 | recurring:housing | recurring | housing | -3534000 | Inferred recurring Home repair reserve |
| 2025-10-05 | recurring:utilities | recurring | utilities | -2141849.94 | Inferred recurring Municipal utilities |
| 2025-10-06 | recurring:insurance | recurring | insurance | -1132400 | Inferred recurring Household insurance |
| 2025-10-07 | recurring:education | recurring | education | -3040000 | Inferred recurring Course tuition |
| 2025-10-07 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-10-09 | recurring:healthcare | recurring | healthcare | -1641668.72 | Inferred recurring Clinic payment |
| 2025-10-11 | recurring:cloud_storage | recurring | cloud_storage | -369550 | Inferred recurring Shared storage plan |
| 2025-10-13 | recurring:entertainment | recurring | entertainment | -1352563.79 | Inferred recurring Cinema and events |
| 2025-10-14 | recurring:salary | recurring | salary | 42750000 | Inferred recurring Payroll credit |
| 2025-10-21 | recurring:transport | recurring | transport | -1440242.94 | Inferred recurring Ride-hailing trip |
| 2025-10-23 | recurring:groceries | recurring | groceries | -2218141.61 | Inferred recurring Local market purchase |
| 2025-11-02 | recurring:housing | recurring | housing | -3534000 | Inferred recurring Home repair reserve |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_145` | 2025-02-10 | settled | groceries | 2477697.53 | cash date 2025-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_163` | 2025-02-11 | settled | transport | 1373039.34 | cash date 2025-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_176` | 2025-02-12 | settled | dining | 1166644.88 | cash date 2025-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_146` | 2025-02-20 | settled | groceries | 1667911.86 | cash date 2025-02-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_164` | 2025-02-25 | settled | transport | 995704.83 | cash date 2025-02-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_147` | 2025-03-02 | settled | groceries | 1418745.34 | cash date 2025-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_105` | 2025-03-04 | settled | housing | 3534000 | cash date 2025-03-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_177` | 2025-03-05 | settled | dining | 1101709.76 | cash date 2025-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_106` | 2025-03-07 | settled | utilities | 2143659.02 | cash date 2025-03-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_107` | 2025-03-08 | settled | insurance | 1132400 | cash date 2025-03-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_108` | 2025-03-09 | settled | education | 3040000 | cash date 2025-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_109` | 2025-03-11 | settled | healthcare | 1594883.08 | cash date 2025-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_165` | 2025-03-11 | settled | transport | 1062246.98 | cash date 2025-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_148` | 2025-03-12 | settled | groceries | 1455258.76 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_111` | 2025-03-13 | settled | cloud_storage | 369550 | cash date 2025-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_104` | 2025-03-15 | settled | salary | 33345000 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_110` | 2025-03-15 | settled | entertainment | 1289187.4 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_149` | 2025-03-22 | settled | groceries | 1920485.7 | cash date 2025-03-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_166` | 2025-03-25 | settled | transport | 1053078.61 | cash date 2025-03-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_178` | 2025-03-26 | settled | dining | 935929.08 | cash date 2025-03-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_150` | 2025-04-01 | settled | groceries | 1630631.42 | cash date 2025-04-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_113` | 2025-04-04 | settled | housing | 3534000 | cash date 2025-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_114` | 2025-04-07 | settled | utilities | 2081730.85 | cash date 2025-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_115` | 2025-04-08 | settled | insurance | 1132400 | cash date 2025-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_167` | 2025-04-08 | settled | transport | 1294200.86 | cash date 2025-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_116` | 2025-04-09 | settled | education | 3040000 | cash date 2025-04-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_117` | 2025-04-11 | settled | healthcare | 1467514.81 | cash date 2025-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_151` | 2025-04-11 | settled | groceries | 1664708.05 | cash date 2025-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_119` | 2025-04-13 | settled | cloud_storage | 369550 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_112` | 2025-04-15 | settled | salary | 33345000 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_118` | 2025-04-15 | settled | entertainment | 1367779.89 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_179` | 2025-04-16 | settled | dining | 1271076.93 | cash date 2025-04-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_152` | 2025-04-21 | settled | groceries | 1478895.05 | cash date 2025-04-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_168` | 2025-04-22 | settled | transport | 1440242.94 | cash date 2025-04-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_153` | 2025-05-01 | settled | groceries | 2192475.45 | cash date 2025-05-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_121` | 2025-05-04 | settled | housing | 3534000 | cash date 2025-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_169` | 2025-05-06 | settled | transport | 1021628.43 | cash date 2025-05-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_122` | 2025-05-07 | settled | utilities | 1830311.06 | cash date 2025-05-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_180` | 2025-05-07 | settled | dining | 971169.92 | cash date 2025-05-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_123` | 2025-05-08 | settled | insurance | 1132400 | cash date 2025-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_124` | 2025-05-09 | settled | education | 3040000 | cash date 2025-05-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_125` | 2025-05-11 | settled | healthcare | 1452405.16 | cash date 2025-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_154` | 2025-05-11 | settled | groceries | 1852958.27 | cash date 2025-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_127` | 2025-05-13 | settled | cloud_storage | 369550 | cash date 2025-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_120` | 2025-05-15 | settled | salary | 33345000 | cash date 2025-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_126` | 2025-05-15 | settled | entertainment | 1287628.28 | cash date 2025-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_170` | 2025-05-20 | settled | transport | 1374936.26 | cash date 2025-05-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_155` | 2025-05-21 | settled | groceries | 2030400.43 | cash date 2025-05-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_181` | 2025-05-28 | settled | dining | 1111388.15 | cash date 2025-05-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_156` | 2025-05-31 | settled | groceries | 1611886.08 | cash date 2025-05-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_171` | 2025-06-03 | settled | transport | 1329347.44 | cash date 2025-06-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_129` | 2025-06-04 | settled | housing | 3534000 | cash date 2025-06-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_130` | 2025-06-07 | settled | utilities | 1981601.61 | cash date 2025-06-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_131` | 2025-06-08 | settled | insurance | 1132400 | cash date 2025-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_132` | 2025-06-09 | settled | education | 3040000 | cash date 2025-06-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_157` | 2025-06-10 | settled | groceries | 2158165.32 | cash date 2025-06-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_133` | 2025-06-11 | settled | healthcare | 1641668.72 | cash date 2025-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_135` | 2025-06-13 | settled | cloud_storage | 369550 | cash date 2025-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_128` | 2025-06-15 | settled | salary | 33345000 | cash date 2025-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_134` | 2025-06-15 | settled | entertainment | 1193699.1 | cash date 2025-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_172` | 2025-06-17 | settled | transport | 1309608.46 | cash date 2025-06-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_182` | 2025-06-18 | settled | dining | 947892.35 | cash date 2025-06-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_158` | 2025-06-20 | settled | groceries | 2222527.88 | cash date 2025-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_159` | 2025-06-30 | settled | groceries | 2079368.25 | cash date 2025-06-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_173` | 2025-07-01 | settled | transport | 1111352.32 | cash date 2025-07-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_137` | 2025-07-04 | settled | housing | 3534000 | cash date 2025-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_138` | 2025-07-07 | settled | utilities | 2141849.94 | cash date 2025-07-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_139` | 2025-07-08 | settled | insurance | 1132400 | cash date 2025-07-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_140` | 2025-07-09 | settled | education | 3040000 | cash date 2025-07-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_183` | 2025-07-09 | settled | dining | 1043758.65 | cash date 2025-07-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_160` | 2025-07-10 | settled | groceries | 2218141.61 | cash date 2025-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_141` | 2025-07-11 | settled | healthcare | 1538498.1 | cash date 2025-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_143` | 2025-07-13 | settled | cloud_storage | 369550 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_136` | 2025-07-15 | settled | salary | 33345000 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_142` | 2025-07-15 | settled | entertainment | 1352563.79 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_174` | 2025-07-15 | settled | transport | 1327886.54 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_161` | 2025-07-20 | settled | groceries | 2365919.6 | cash date 2025-07-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_175` | 2025-07-29 | settled | transport | 1062310.27 | cash date 2025-07-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_162` | 2025-07-30 | settled | groceries | 1913686.86 | cash date 2025-07-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_184` | 2025-07-30 | settled | dining | 1204805.34 | cash date 2025-07-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_144` | 2025-08-04 | settled | housing | 3534000 | cash date 2025-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_01` | 2025-07-29T09:30:00Z | `` | employer | Rincian penggajian Anda di Cobalt Systems telah berubah. Gaji bulanan Anda naik menjadi IDR 42750000. Perubahan ini berlaku mulai 2025-08-15. Jumlah yang diperbarui akan terlihat pada slip gaji berikutnya. Ref payroll EMP-0001. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_05` | installments | 2025-08-08:15952906.67\|2025-09-07:15952906.67\|2025-10-07:15952906.67 | 1840720.01 | 47858720.01 |
| `payment_option_06` | full_payment | 2025-08-05:46018000 | 0 | 46018000 |
| `payment_option_07` | installments | 2025-08-12:2914473.33\|2025-09-12:2914473.33\|2025-10-13:2914473.33\|2025-11-13:2914473.33\|2025-12-14:2914473.33\|2026-01-14:2914473.33\|2026-02-14:2914473.33\|2026-03-17:2914473.33\|2026-04-17:2914473.33\|2026-05-18:2914473.33\|2026-06-18:2914473.33\|2026-07-19:2914473.33\|2026-08-19:2914473.33\|2026-09-19:2914473.33\|2026-10-20:2914473.33\|2026-11-20:2914473.33\|2026-12-21:2914473.33\|2027-01-21:2914473.33 | 6442519.94 | 52460519.94 |

## request_03 — user_03

Primary category: **earliest-date computation**

The baseline finds a later date but represents wait with payment_plan=none instead of the solved future full-payment commitment, and its daily date is not conservative enough.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 873000 | 2190071.39 |
| `payment_plan` | 2019-11-15:5491000 | 2019-10-15:5491000 |
| `earliest_date_for_full_payment` | 2019-11-15 | 2019-10-15 |
| `decision_explanation` | Pay IDR 5,491,000 in full on 15 November 2019. Paying earlier would take the balance below the IDR 2,668,700 minimum. | Baseline forecast finds a later safe full-payment date. |

### Financial profile

- Home currency: `IDR`
- Current balance: `5810300`
- Minimum balance: `2668700`
- Protected: `groceries|rent|utilities`; reduce: `shopping|streaming`; stop: `cloud_storage|streaming`.
- Payment methods: `full_payment|installments|partial_payment`; max installment months: `2`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2019-09-07 | recurring:utilities | recurring | utilities | -303042.45 | Inferred recurring Water and power payment |
| 2019-09-07 | event_254 | explicit | healthcare | -95000 | Pending pharmacy card charge |
| 2019-09-08 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-09-10 | recurring:streaming | recurring | streaming | -117800 | Inferred recurring Video streaming plan |
| 2019-09-13 | recurring:shopping | recurring | shopping | -180395.29 | Inferred recurring Clothing and household items |
| 2019-09-13 | recurring:cloud_storage | recurring | cloud_storage | -20900 | Inferred recurring Shared storage plan |
| 2019-09-14 | recurring:salary | recurring | salary | 4365000 | Inferred recurring Payroll credit |
| 2019-09-18 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-09-28 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-10-03 | recurring:rent | recurring | rent | -1140000 | Inferred recurring Landlord standing order |
| 2019-10-07 | recurring:utilities | recurring | utilities | -303042.45 | Inferred recurring Water and power payment |
| 2019-10-08 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-10-10 | recurring:streaming | recurring | streaming | -117800 | Inferred recurring Video streaming plan |
| 2019-10-13 | recurring:shopping | recurring | shopping | -180395.29 | Inferred recurring Clothing and household items |
| 2019-10-13 | recurring:cloud_storage | recurring | cloud_storage | -20900 | Inferred recurring Shared storage plan |
| 2019-10-14 | recurring:salary | recurring | salary | 4365000 | Inferred recurring Payroll credit |
| 2019-10-18 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-10-28 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-11-02 | recurring:rent | recurring | rent | -1140000 | Inferred recurring Landlord standing order |
| 2019-11-06 | recurring:utilities | recurring | utilities | -303042.45 | Inferred recurring Water and power payment |
| 2019-11-07 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-11-09 | recurring:streaming | recurring | streaming | -117800 | Inferred recurring Video streaming plan |
| 2019-11-12 | recurring:shopping | recurring | shopping | -180395.29 | Inferred recurring Clothing and household items |
| 2019-11-12 | recurring:cloud_storage | recurring | cloud_storage | -20900 | Inferred recurring Shared storage plan |
| 2019-11-13 | recurring:salary | recurring | salary | 4365000 | Inferred recurring Payroll credit |
| 2019-11-17 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-11-27 | recurring:groceries | recurring | groceries | -234390.87 | Inferred recurring Bulk pantry shop |
| 2019-12-02 | recurring:rent | recurring | rent | -1140000 | Inferred recurring Landlord standing order |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_244` | 2019-03-09 | settled | dining | 117456.78 | cash date 2019-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_217` | 2019-03-12 | settled | groceries | 159576.52 | cash date 2019-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_235` | 2019-03-13 | settled | transport | 81510.25 | cash date 2019-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_218` | 2019-03-22 | settled | groceries | 234390.87 | cash date 2019-03-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_245` | 2019-03-30 | settled | dining | 141412.46 | cash date 2019-03-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_219` | 2019-04-01 | settled | groceries | 230312.98 | cash date 2019-04-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_236` | 2019-04-03 | settled | transport | 116319.21 | cash date 2019-04-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_187` | 2019-04-04 | settled | rent | 1140000 | cash date 2019-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_188` | 2019-04-08 | settled | utilities | 295330.29 | cash date 2019-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_190` | 2019-04-11 | settled | streaming | 117800 | cash date 2019-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_220` | 2019-04-11 | settled | groceries | 234602.65 | cash date 2019-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_189` | 2019-04-14 | settled | cloud_storage | 20900 | cash date 2019-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_191` | 2019-04-14 | settled | shopping | 151493.37 | cash date 2019-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_186` | 2019-04-15 | settled | salary | 4365000 | cash date 2019-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_246` | 2019-04-20 | settled | dining | 146236.28 | cash date 2019-04-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_221` | 2019-04-21 | settled | groceries | 209875.85 | cash date 2019-04-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_237` | 2019-04-24 | settled | transport | 71790.29 | cash date 2019-04-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_222` | 2019-05-01 | settled | groceries | 178469.49 | cash date 2019-05-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_193` | 2019-05-04 | settled | rent | 1140000 | cash date 2019-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_194` | 2019-05-08 | settled | utilities | 290684.15 | cash date 2019-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_196` | 2019-05-11 | settled | streaming | 117800 | cash date 2019-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_223` | 2019-05-11 | settled | groceries | 180577.99 | cash date 2019-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_247` | 2019-05-11 | settled | dining | 132247.64 | cash date 2019-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_195` | 2019-05-14 | settled | cloud_storage | 20900 | cash date 2019-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_197` | 2019-05-14 | settled | shopping | 184274.02 | cash date 2019-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_192` | 2019-05-15 | settled | salary | 4365000 | cash date 2019-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_238` | 2019-05-15 | settled | transport | 73531.06 | cash date 2019-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_224` | 2019-05-21 | settled | groceries | 155851.46 | cash date 2019-05-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_225` | 2019-05-31 | settled | groceries | 188355.72 | cash date 2019-05-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_248` | 2019-06-01 | settled | dining | 158476.5 | cash date 2019-06-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_199` | 2019-06-04 | settled | rent | 1140000 | cash date 2019-06-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_239` | 2019-06-05 | settled | transport | 106806.88 | cash date 2019-06-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_200` | 2019-06-08 | settled | utilities | 270537.63 | cash date 2019-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_226` | 2019-06-10 | settled | groceries | 166710.61 | cash date 2019-06-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_202` | 2019-06-11 | settled | streaming | 117800 | cash date 2019-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_201` | 2019-06-14 | settled | cloud_storage | 20900 | cash date 2019-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_203` | 2019-06-14 | settled | shopping | 153395.26 | cash date 2019-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_198` | 2019-06-15 | settled | salary | 4365000 | cash date 2019-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_227` | 2019-06-20 | settled | groceries | 171495.67 | cash date 2019-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_249` | 2019-06-22 | settled | dining | 175170.67 | cash date 2019-06-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_240` | 2019-06-26 | settled | transport | 79693.97 | cash date 2019-06-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_228` | 2019-06-30 | settled | groceries | 145691.38 | cash date 2019-06-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_205` | 2019-07-04 | settled | rent | 1140000 | cash date 2019-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_206` | 2019-07-08 | settled | utilities | 303042.45 | cash date 2019-07-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_229` | 2019-07-10 | settled | groceries | 171259.18 | cash date 2019-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_208` | 2019-07-11 | settled | streaming | 117800 | cash date 2019-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_250` | 2019-07-13 | settled | dining | 171303.21 | cash date 2019-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_207` | 2019-07-14 | settled | cloud_storage | 20900 | cash date 2019-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_209` | 2019-07-14 | settled | shopping | 173930.81 | cash date 2019-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_204` | 2019-07-15 | settled | salary | 4365000 | cash date 2019-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_241` | 2019-07-17 | settled | transport | 83523.33 | cash date 2019-07-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_230` | 2019-07-20 | settled | groceries | 173004.74 | cash date 2019-07-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_231` | 2019-07-30 | settled | groceries | 214266.98 | cash date 2019-07-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_251` | 2019-08-03 | settled | dining | 171191.99 | cash date 2019-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_212` | 2019-08-04 | settled | rent | 1140000 | cash date 2019-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_242` | 2019-08-07 | settled | transport | 99961.13 | cash date 2019-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_213` | 2019-08-08 | settled | utilities | 262344.55 | cash date 2019-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_232` | 2019-08-09 | settled | groceries | 221578.88 | cash date 2019-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_215` | 2019-08-11 | settled | streaming | 117800 | cash date 2019-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_214` | 2019-08-14 | settled | cloud_storage | 20900 | cash date 2019-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_216` | 2019-08-14 | settled | shopping | 180395.29 | cash date 2019-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_210` | 2019-08-15 | settled | salary | 4365000 | cash date 2019-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_233` | 2019-08-19 | settled | groceries | 240706.45 | cash date 2019-08-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_211` | 2019-08-20 | settled | salary | 1964250 | cash date 2019-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_252` | 2019-08-24 | settled | dining | 135718.35 | cash date 2019-08-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_243` | 2019-08-28 | settled | transport | 106233.46 | cash date 2019-08-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_234` | 2019-08-29 | settled | groceries | 200238.72 | cash date 2019-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_253` | 2019-08-31 | settled | salary |  | amount requires linked image review |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_02` | 2019-08-31T09:30:00Z | `` | employer | Tim payroll BrightPath Media telah mengirim pembaruan. Gaji rutin untuk penggajian berikutnya sudah dikonfirmasi. Slip gaji berikutnya akan menampilkan gaji rutin dan penyesuaian satu kali secara terpisah. Ref payroll EMP-0002. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| `image_01` | `event_253` | request_03 |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_08` | full_payment | 2019-09-03:5491000 | 0 | 5491000 |
| `payment_option_09` | installments | 2019-09-17:308541.9\|2019-10-15:308541.9\|2019-11-12:308541.9\|2019-12-10:308541.9\|2020-01-07:308541.9\|2020-02-04:308541.9\|2020-03-03:308541.9\|2020-03-31:308541.9\|2020-04-28:308541.9\|2020-05-26:308541.9\|2020-06-23:308541.9\|2020-07-21:308541.9\|2020-08-18:308541.9\|2020-09-15:308541.9\|2020-10-13:308541.9\|2020-11-10:308541.9\|2020-12-08:308541.9\|2021-01-05:308541.9\|2021-02-02:308541.9\|2021-03-02:308541.9\|2021-03-30:308541.9 | 988379.9 | 6479379.9 |
| `payment_option_10` | installments | 2019-09-06:279125.83\|2019-10-07:279125.83\|2019-11-07:279125.83\|2019-12-08:279125.83\|2020-01-08:279125.83\|2020-02-08:279125.83\|2020-03-10:279125.83\|2020-04-10:279125.83\|2020-05-11:279125.83\|2020-06-11:279125.83\|2020-07-12:279125.83\|2020-08-12:279125.83\|2020-09-12:279125.83\|2020-10-13:279125.83\|2020-11-13:279125.83\|2020-12-14:279125.83\|2021-01-14:279125.83\|2021-02-14:279125.83\|2021-03-17:279125.83\|2021-04-17:279125.83\|2021-05-18:279125.83\|2021-06-18:279125.83\|2021-07-19:279125.83\|2021-08-19:279125.83 | 1208019.92 | 6699019.92 |

## request_04 — user_04

Primary category: **cancellations or amendments from messages**

Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 8401800 | 12693000 |
| `affordability_status` | affordable_later | affordable_now |
| `recommended_payment_method` | wait | full_payment |
| `payment_plan` | 2024-06-15:12693000 | 2024-06-04:12693000 |
| `earliest_date_for_full_payment` | 2024-06-15 | 2024-06-04 |
| `decision_explanation` | Wait until 15 June 2024, then pay IDR 12,693,000 in full. Paying sooner would put the IDR 30,686,600 minimum at risk. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `IDR`
- Current balance: `52206950`
- Minimum balance: `30686600`
- Protected: `groceries|rent|transport`; reduce: `entertainment`; stop: `music_subscription`.
- Payment methods: `full_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-06-08 | recurring:gym | recurring | gym | -1027900 | Inferred recurring Gym membership |
| 2024-06-09 | recurring:music_subscription | recurring | music_subscription | -332500 | Inferred recurring Music service subscription |
| 2024-06-11 | event_357 | explicit | education | -1704300 | Scheduled school fee |
| 2024-06-11 | recurring:delivery_membership | recurring | delivery_membership | -377150 | Inferred recurring Food delivery membership |
| 2024-06-12 | recurring:entertainment | recurring | entertainment | -1542620 | Inferred recurring Local event tickets |
| 2024-06-14 | recurring:salary | recurring | salary | 38190000 | Inferred recurring Payroll credit |
| 2024-07-01 | recurring:rent | recurring | rent | -12293000 | Inferred recurring Residential rent payment |
| 2024-07-04 | recurring:utilities | recurring | utilities | -2033868.83 | Inferred recurring Municipal utilities |
| 2024-07-08 | recurring:dining | recurring | dining | -2102251.18 | Inferred recurring Family dinner |
| 2024-07-08 | recurring:gym | recurring | gym | -1027900 | Inferred recurring Gym membership |
| 2024-07-09 | recurring:music_subscription | recurring | music_subscription | -332500 | Inferred recurring Music service subscription |
| 2024-07-11 | recurring:delivery_membership | recurring | delivery_membership | -377150 | Inferred recurring Food delivery membership |
| 2024-07-12 | recurring:entertainment | recurring | entertainment | -1542620 | Inferred recurring Local event tickets |
| 2024-07-14 | recurring:salary | recurring | salary | 38190000 | Inferred recurring Payroll credit |
| 2024-07-31 | recurring:rent | recurring | rent | -12293000 | Inferred recurring Residential rent payment |
| 2024-08-03 | recurring:utilities | recurring | utilities | -2033868.83 | Inferred recurring Municipal utilities |
| 2024-08-07 | recurring:gym | recurring | gym | -1027900 | Inferred recurring Gym membership |
| 2024-08-08 | recurring:music_subscription | recurring | music_subscription | -332500 | Inferred recurring Music service subscription |
| 2024-08-10 | recurring:delivery_membership | recurring | delivery_membership | -377150 | Inferred recurring Food delivery membership |
| 2024-08-11 | recurring:entertainment | recurring | entertainment | -1542620 | Inferred recurring Local event tickets |
| 2024-08-12 | recurring:dining | recurring | dining | -2102251.18 | Inferred recurring Family dinner |
| 2024-08-13 | recurring:salary | recurring | salary | 38190000 | Inferred recurring Payroll credit |
| 2024-08-30 | recurring:rent | recurring | rent | -12293000 | Inferred recurring Residential rent payment |
| 2024-09-02 | recurring:utilities | recurring | utilities | -2033868.83 | Inferred recurring Municipal utilities |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_292` | 2023-12-09 | settled | groceries | 1685953.79 | cash date 2023-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_318` | 2023-12-10 | settled | transport | 649231.24 | cash date 2023-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_344` | 2023-12-11 | settled | dining | 2111827.25 | cash date 2023-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_293` | 2023-12-16 | settled | groceries | 1749986.6 | cash date 2023-12-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_319` | 2023-12-17 | settled | transport | 876705.51 | cash date 2023-12-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_294` | 2023-12-23 | settled | groceries | 1383275.31 | cash date 2023-12-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_320` | 2023-12-24 | settled | transport | 825832.49 | cash date 2023-12-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_345` | 2023-12-25 | settled | dining | 1839656.04 | cash date 2023-12-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_295` | 2023-12-30 | settled | groceries | 1482897.31 | cash date 2023-12-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_321` | 2023-12-31 | settled | transport | 769694.2 | cash date 2023-12-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_256` | 2024-01-01 | settled | rent | 12293000 | cash date 2024-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_257` | 2024-01-05 | settled | utilities | 2017103.37 | cash date 2024-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_296` | 2024-01-06 | settled | groceries | 1818044.76 | cash date 2024-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_322` | 2024-01-07 | settled | transport | 841811.01 | cash date 2024-01-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_346` | 2024-01-08 | settled | dining | 1279029.86 | cash date 2024-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_260` | 2024-01-09 | settled | gym | 1027900 | cash date 2024-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_258` | 2024-01-10 | settled | music_subscription | 332500 | cash date 2024-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_259` | 2024-01-12 | settled | delivery_membership | 377150 | cash date 2024-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_261` | 2024-01-13 | settled | entertainment | 1484369.68 | cash date 2024-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_297` | 2024-01-13 | settled | groceries | 1413898.4 | cash date 2024-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_323` | 2024-01-14 | settled | transport | 820888.17 | cash date 2024-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_255` | 2024-01-15 | settled | salary | 38190000 | cash date 2024-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_298` | 2024-01-20 | settled | groceries | 1351288.83 | cash date 2024-01-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_324` | 2024-01-21 | settled | transport | 870102.58 | cash date 2024-01-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_347` | 2024-01-22 | settled | dining | 2067659.14 | cash date 2024-01-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_299` | 2024-01-27 | settled | groceries | 1178544.55 | cash date 2024-01-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_325` | 2024-01-28 | settled | transport | 1011616.29 | cash date 2024-01-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_263` | 2024-02-01 | settled | rent | 12293000 | cash date 2024-02-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_300` | 2024-02-03 | settled | groceries | 1697006.55 | cash date 2024-02-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_326` | 2024-02-04 | settled | transport | 596927.82 | cash date 2024-02-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_264` | 2024-02-05 | settled | utilities | 1981052.47 | cash date 2024-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_348` | 2024-02-05 | settled | dining | 1650545.96 | cash date 2024-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_267` | 2024-02-09 | settled | gym | 1027900 | cash date 2024-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_265` | 2024-02-10 | settled | music_subscription | 332500 | cash date 2024-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_301` | 2024-02-10 | settled | groceries | 1087788.82 | cash date 2024-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_327` | 2024-02-11 | settled | transport | 595968.94 | cash date 2024-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_266` | 2024-02-12 | settled | delivery_membership | 377150 | cash date 2024-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_268` | 2024-02-13 | settled | entertainment | 1375854.05 | cash date 2024-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_262` | 2024-02-15 | settled | salary | 38190000 | cash date 2024-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_302` | 2024-02-17 | settled | groceries | 1753801.95 | cash date 2024-02-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_328` | 2024-02-18 | settled | transport | 954666.65 | cash date 2024-02-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_349` | 2024-02-19 | settled | dining | 1931412.81 | cash date 2024-02-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_303` | 2024-02-24 | settled | groceries | 1203621.92 | cash date 2024-02-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_329` | 2024-02-25 | settled | transport | 843406.32 | cash date 2024-02-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_271` | 2024-03-01 | settled | rent | 12293000 | cash date 2024-03-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_304` | 2024-03-02 | settled | groceries | 1674003.66 | cash date 2024-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_330` | 2024-03-03 | settled | transport | 589707.32 | cash date 2024-03-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_350` | 2024-03-04 | settled | dining | 1551598.07 | cash date 2024-03-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_272` | 2024-03-05 | settled | utilities | 2033868.83 | cash date 2024-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_275` | 2024-03-09 | settled | gym | 1027900 | cash date 2024-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_305` | 2024-03-09 | settled | groceries | 1347842.61 | cash date 2024-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_273` | 2024-03-10 | settled | music_subscription | 332500 | cash date 2024-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_331` | 2024-03-10 | settled | transport | 997182.25 | cash date 2024-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_274` | 2024-03-12 | settled | delivery_membership | 377150 | cash date 2024-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_276` | 2024-03-13 | settled | entertainment | 1542620 | cash date 2024-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_269` | 2024-03-15 | settled | salary | 38190000 | cash date 2024-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_306` | 2024-03-16 | settled | groceries | 1453711.32 | cash date 2024-03-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_332` | 2024-03-17 | settled | transport | 677221.86 | cash date 2024-03-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_351` | 2024-03-18 | settled | dining | 2102251.18 | cash date 2024-03-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_270` | 2024-03-22 | settled | salary | 10498464.28 | cash date 2024-03-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_307` | 2024-03-23 | settled | groceries | 1447770.09 | cash date 2024-03-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_333` | 2024-03-24 | settled | transport | 889762.96 | cash date 2024-03-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_308` | 2024-03-30 | settled | groceries | 1261462.72 | cash date 2024-03-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_334` | 2024-03-31 | settled | transport | 842011.07 | cash date 2024-03-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_278` | 2024-04-01 | settled | rent | 12293000 | cash date 2024-04-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_352` | 2024-04-01 | settled | dining | 1282286.6 | cash date 2024-04-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_279` | 2024-04-05 | settled | utilities | 1980834.82 | cash date 2024-04-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_309` | 2024-04-06 | settled | groceries | 1825667.28 | cash date 2024-04-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_335` | 2024-04-07 | settled | transport | 1000668.29 | cash date 2024-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_282` | 2024-04-09 | settled | gym | 1027900 | cash date 2024-04-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_280` | 2024-04-10 | settled | music_subscription | 332500 | cash date 2024-04-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_281` | 2024-04-12 | settled | delivery_membership | 377150 | cash date 2024-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_283` | 2024-04-13 | settled | entertainment | 1291303.65 | cash date 2024-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_310` | 2024-04-13 | settled | groceries | 1184189.4 | cash date 2024-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_336` | 2024-04-14 | settled | transport | 935850.82 | cash date 2024-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_277` | 2024-04-15 | settled | salary | 38190000 | cash date 2024-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_353` | 2024-04-15 | settled | dining | 1259307.64 | cash date 2024-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_311` | 2024-04-20 | settled | groceries | 1617937.79 | cash date 2024-04-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_337` | 2024-04-21 | settled | transport | 874634.88 | cash date 2024-04-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_312` | 2024-04-27 | settled | groceries | 1519414.73 | cash date 2024-04-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_338` | 2024-04-28 | settled | transport | 766019.04 | cash date 2024-04-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_354` | 2024-04-29 | settled | dining | 1661337.11 | cash date 2024-04-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_285` | 2024-05-01 | settled | rent | 12293000 | cash date 2024-05-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_313` | 2024-05-04 | settled | groceries | 1831437.58 | cash date 2024-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_286` | 2024-05-05 | settled | utilities | 2004118.6 | cash date 2024-05-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_339` | 2024-05-05 | settled | transport | 1030376.9 | cash date 2024-05-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_289` | 2024-05-09 | settled | gym | 1027900 | cash date 2024-05-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_287` | 2024-05-10 | settled | music_subscription | 332500 | cash date 2024-05-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_314` | 2024-05-11 | settled | groceries | 1698278.31 | cash date 2024-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_288` | 2024-05-12 | settled | delivery_membership | 377150 | cash date 2024-05-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_340` | 2024-05-12 | settled | transport | 912938.95 | cash date 2024-05-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_290` | 2024-05-13 | settled | entertainment | 1231859.39 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_355` | 2024-05-13 | settled | dining | 1886856.1 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_284` | 2024-05-15 | settled | salary | 38190000 | cash date 2024-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_315` | 2024-05-18 | settled | groceries | 1075064.04 | cash date 2024-05-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_341` | 2024-05-19 | settled | transport | 853091.62 | cash date 2024-05-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_316` | 2024-05-25 | settled | groceries | 1809752.54 | cash date 2024-05-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_342` | 2024-05-26 | settled | transport | 602450.01 | cash date 2024-05-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_356` | 2024-05-27 | settled | dining | 2108488.15 | cash date 2024-05-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_291` | 2024-06-01 | settled | rent | 12293000 | cash date 2024-06-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_317` | 2024-06-01 | settled | groceries | 1433695.5 | cash date 2024-06-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_343` | 2024-06-02 | settled | transport | 1016425.58 | cash date 2024-06-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_03` | 2024-06-01T09:30:00Z | `` | employer | Rincian penggajian Anda di Greenfield Foods telah berubah. Bonus kuartalan Anda masih menunggu hasil akhir penilaian kinerja. Jumlah akhir dan tanggal pembayaran belum disetujui. Kami akan mengirim pembaruan setelah tim payroll mengonfirmasi jumlah dan tanggalnya. Ref payroll EMP-0003. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_11` | full_payment | 2024-06-04:12693000 | 0 | 12693000 |
| `payment_option_12` | installments | 2024-06-04:875817\|2024-07-04:875817\|2024-08-03:875817\|2024-09-02:875817\|2024-10-02:875817\|2024-11-01:875817\|2024-12-01:875817\|2024-12-31:875817\|2025-01-30:875817\|2025-03-01:875817\|2025-03-31:875817\|2025-04-30:875817\|2025-05-30:875817\|2025-06-29:875817\|2025-07-29:875817 | 444255 | 13137255 |

## request_05 — user_05

Primary category: **duplicate / linked-event handling**

The request has pending or linked lifecycle evidence; the baseline's child-ID suppression is not a complete lifecycle resolver and can omit or double reserve cash.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 737 | 15488 |
| `affordability_status` | not_affordable | affordable_now |
| `recommended_payment_method` | not_recommended | full_payment |
| `payment_plan` | none | 2025-11-06:15488 |
| `earliest_date_for_full_payment` |  | 2025-11-06 |
| `decision_explanation` | Do not make this payment by 12 January 2026. None of the available options keeps the ZAR 13,100 minimum protected. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `ZAR`
- Current balance: `46475.1`
- Minimum balance: `13100`
- Protected: `family_support|groceries|healthcare|rent`; reduce: `shopping`; stop: `cloud_storage`.
- Payment methods: `full_payment|installments|partial_payment`; max installment months: `4`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-11-09 | recurring:healthcare | recurring | healthcare | -722.37 | Inferred recurring Therapy appointment |
| 2025-11-10 | recurring:debt_repayment | recurring | debt_repayment | -968 | Inferred recurring Vehicle loan payment |
| 2025-11-11 | recurring:shopping | recurring | shopping | -422.67 | Inferred recurring Personal shopping |
| 2025-11-11 | recurring:cloud_storage | recurring | cloud_storage | -113.3 | Inferred recurring Cloud storage plan |
| 2025-11-12 | recurring:family_support | recurring | family_support | -840.4 | Inferred recurring Dependent care payment |
| 2025-11-16 | recurring:salary | recurring | salary | 14740 | Inferred recurring Payroll credit |
| 2025-12-03 | recurring:rent | recurring | rent | -4972 | Inferred recurring Apartment rent transfer |
| 2025-12-05 | recurring:utilities | recurring | utilities | -750.89 | Inferred recurring Municipal utilities |
| 2025-12-09 | recurring:healthcare | recurring | healthcare | -722.37 | Inferred recurring Therapy appointment |
| 2025-12-10 | recurring:debt_repayment | recurring | debt_repayment | -968 | Inferred recurring Vehicle loan payment |
| 2025-12-11 | recurring:shopping | recurring | shopping | -422.67 | Inferred recurring Personal shopping |
| 2025-12-11 | recurring:cloud_storage | recurring | cloud_storage | -113.3 | Inferred recurring Cloud storage plan |
| 2025-12-12 | recurring:family_support | recurring | family_support | -840.4 | Inferred recurring Dependent care payment |
| 2025-12-17 | recurring:salary | recurring | salary | 14740 | Inferred recurring Payroll credit |
| 2026-01-03 | recurring:rent | recurring | rent | -4972 | Inferred recurring Apartment rent transfer |
| 2026-01-04 | recurring:utilities | recurring | utilities | -750.89 | Inferred recurring Municipal utilities |
| 2026-01-08 | recurring:healthcare | recurring | healthcare | -722.37 | Inferred recurring Therapy appointment |
| 2026-01-09 | recurring:debt_repayment | recurring | debt_repayment | -968 | Inferred recurring Vehicle loan payment |
| 2026-01-10 | recurring:shopping | recurring | shopping | -422.67 | Inferred recurring Personal shopping |
| 2026-01-10 | recurring:cloud_storage | recurring | cloud_storage | -113.3 | Inferred recurring Cloud storage plan |
| 2026-01-11 | recurring:family_support | recurring | family_support | -840.4 | Inferred recurring Dependent care payment |
| 2026-01-17 | recurring:salary | recurring | salary | 14740 | Inferred recurring Payroll credit |
| 2026-02-03 | recurring:rent | recurring | rent | -4972 | Inferred recurring Apartment rent transfer |
| 2026-02-03 | recurring:utilities | recurring | utilities | -750.89 | Inferred recurring Municipal utilities |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_399` | 2025-05-13 | settled | groceries | 784.81 | cash date 2025-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_425` | 2025-05-14 | settled | transport | 489.31 | cash date 2025-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_400` | 2025-05-20 | settled | groceries | 818.16 | cash date 2025-05-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_401` | 2025-05-27 | settled | groceries | 680.15 | cash date 2025-05-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_426` | 2025-05-28 | settled | transport | 424.26 | cash date 2025-05-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_359` | 2025-06-02 | settled | rent | 4972 | cash date 2025-06-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_402` | 2025-06-03 | settled | groceries | 530.44 | cash date 2025-06-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_360` | 2025-06-06 | settled | utilities | 604.15 | cash date 2025-06-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_362` | 2025-06-10 | settled | healthcare | 777.27 | cash date 2025-06-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_403` | 2025-06-10 | settled | groceries | 695.96 | cash date 2025-06-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_361` | 2025-06-11 | settled | debt_repayment | 968 | cash date 2025-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_427` | 2025-06-11 | settled | transport | 504.23 | cash date 2025-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_364` | 2025-06-12 | settled | cloud_storage | 113.3 | cash date 2025-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_365` | 2025-06-12 | settled | shopping | 379.94 | cash date 2025-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_363` | 2025-06-13 | settled | family_support | 840.4 | cash date 2025-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_358` | 2025-06-15 | settled | salary | 14740 | cash date 2025-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_404` | 2025-06-17 | settled | groceries | 835 | cash date 2025-06-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_405` | 2025-06-24 | settled | groceries | 635.23 | cash date 2025-06-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_428` | 2025-06-25 | settled | transport | 492.86 | cash date 2025-06-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_406` | 2025-07-01 | settled | groceries | 661.93 | cash date 2025-07-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_367` | 2025-07-02 | settled | rent | 4972 | cash date 2025-07-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_368` | 2025-07-06 | settled | utilities | 658.41 | cash date 2025-07-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_407` | 2025-07-08 | settled | groceries | 567.19 | cash date 2025-07-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_429` | 2025-07-09 | settled | transport | 363.28 | cash date 2025-07-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_370` | 2025-07-10 | settled | healthcare | 641.37 | cash date 2025-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_369` | 2025-07-11 | settled | debt_repayment | 968 | cash date 2025-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_372` | 2025-07-12 | settled | cloud_storage | 113.3 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_373` | 2025-07-12 | settled | shopping | 404.24 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_371` | 2025-07-13 | settled | family_support | 840.4 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_366` | 2025-07-15 | settled | salary | 14740 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_408` | 2025-07-15 | settled | groceries | 767.92 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_409` | 2025-07-22 | settled | groceries | 807.31 | cash date 2025-07-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_430` | 2025-07-23 | settled | transport | 311 | cash date 2025-07-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_410` | 2025-07-29 | settled | groceries | 800.63 | cash date 2025-07-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_375` | 2025-08-02 | settled | rent | 4972 | cash date 2025-08-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_411` | 2025-08-05 | settled | groceries | 813.64 | cash date 2025-08-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_376` | 2025-08-06 | settled | utilities | 750.89 | cash date 2025-08-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_431` | 2025-08-06 | settled | transport | 431.81 | cash date 2025-08-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_378` | 2025-08-10 | settled | healthcare | 632.59 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_377` | 2025-08-11 | settled | debt_repayment | 968 | cash date 2025-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_380` | 2025-08-12 | settled | cloud_storage | 113.3 | cash date 2025-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_381` | 2025-08-12 | settled | shopping | 422.67 | cash date 2025-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_412` | 2025-08-12 | settled | groceries | 853.42 | cash date 2025-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_379` | 2025-08-13 | settled | family_support | 840.4 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_374` | 2025-08-15 | settled | salary | 14740 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_413` | 2025-08-19 | settled | groceries | 773.83 | cash date 2025-08-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_432` | 2025-08-20 | settled | transport | 354.2 | cash date 2025-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_414` | 2025-08-26 | settled | groceries | 845.02 | cash date 2025-08-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_383` | 2025-09-02 | settled | rent | 4972 | cash date 2025-09-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_415` | 2025-09-02 | settled | groceries | 762.65 | cash date 2025-09-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_433` | 2025-09-03 | settled | transport | 485.59 | cash date 2025-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_384` | 2025-09-06 | settled | utilities | 706.37 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_416` | 2025-09-09 | settled | groceries | 515.4 | cash date 2025-09-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_386` | 2025-09-10 | settled | healthcare | 721.44 | cash date 2025-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_385` | 2025-09-11 | settled | debt_repayment | 968 | cash date 2025-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_388` | 2025-09-12 | settled | cloud_storage | 113.3 | cash date 2025-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_389` | 2025-09-12 | settled | shopping | 420.31 | cash date 2025-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_387` | 2025-09-13 | settled | family_support | 840.4 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_382` | 2025-09-15 | settled | salary | 14740 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_417` | 2025-09-16 | settled | groceries | 682.39 | cash date 2025-09-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_434` | 2025-09-17 | settled | transport | 411.47 | cash date 2025-09-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_418` | 2025-09-23 | settled | groceries | 675.81 | cash date 2025-09-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_419` | 2025-09-30 | settled | groceries | 547.6 | cash date 2025-09-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_435` | 2025-10-01 | settled | transport | 377.26 | cash date 2025-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_391` | 2025-10-02 | settled | rent | 4972 | cash date 2025-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_392` | 2025-10-06 | settled | utilities | 713.71 | cash date 2025-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_420` | 2025-10-07 | settled | groceries | 826.66 | cash date 2025-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_394` | 2025-10-10 | settled | healthcare | 722.37 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_393` | 2025-10-11 | settled | debt_repayment | 968 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_396` | 2025-10-12 | settled | cloud_storage | 113.3 | cash date 2025-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_397` | 2025-10-12 | settled | shopping | 362.09 | cash date 2025-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_395` | 2025-10-13 | settled | family_support | 840.4 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_421` | 2025-10-14 | settled | groceries | 768.64 | cash date 2025-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_390` | 2025-10-15 | settled | salary | 14740 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_436` | 2025-10-15 | settled | transport | 352.46 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_422` | 2025-10-21 | settled | groceries | 709.62 | cash date 2025-10-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_423` | 2025-10-28 | settled | groceries | 684.39 | cash date 2025-10-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_437` | 2025-10-29 | settled | transport | 388.74 | cash date 2025-10-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_398` | 2025-11-02 | settled | rent | 4972 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_424` | 2025-11-04 | settled | groceries | 720.51 | cash date 2025-11-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_438` | 2025-11-04 | failed | utilities |  | failed event |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_13` | full_payment | 2025-11-06:15488 | 0 | 15488 |
| `payment_option_14` | installments | 2025-11-09:980.91\|2025-12-10:980.91\|2026-01-10:980.91\|2026-02-10:980.91\|2026-03-13:980.91\|2026-04-13:980.91\|2026-05-14:980.91\|2026-06-14:980.91\|2026-07-15:980.91\|2026-08-15:980.91\|2026-09-15:980.91\|2026-10-16:980.91\|2026-11-16:980.91\|2026-12-17:980.91\|2027-01-17:980.91\|2027-02-17:980.91\|2027-03-20:980.91\|2027-04-20:980.91 | 2168.38 | 17656.38 |
| `payment_option_15` | installments | 2025-11-20:787.31\|2025-12-20:787.31\|2026-01-19:787.31\|2026-02-18:787.31\|2026-03-20:787.31\|2026-04-19:787.31\|2026-05-19:787.31\|2026-06-18:787.31\|2026-07-18:787.31\|2026-08-17:787.31\|2026-09-16:787.31\|2026-10-16:787.31\|2026-11-15:787.31\|2026-12-15:787.31\|2027-01-14:787.31\|2027-02-13:787.31\|2027-03-15:787.31\|2027-04-14:787.31\|2027-05-14:787.31\|2027-06-13:787.31\|2027-07-13:787.31\|2027-08-12:787.31\|2027-09-11:787.31\|2027-10-11:787.31 | 3407.44 | 18895.44 |

## request_06 — user_06

Primary category: **flexible spending changes**

The solved plan changes flexible recurring spending, while the baseline never models authorized stop/reduce actions or their resulting forecast cash flows.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 603.3 | 620.4 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `payment_plan` | 2026-01-03:620.40 | 2026-01-03:620.4 |
| `earliest_date_for_full_payment` | 2026-01-15 | 2026-01-03 |
| `spending_changes_needed` | stop:event_476 | none |
| `decision_explanation` | Stop the family streaming plan, then pay EUR 620.40 today. This leaves at least EUR 800 available. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `EUR`
- Current balance: `1942.4`
- Minimum balance: `800`
- Protected: `insurance|rent|transport`; reduce: ``; stop: `streaming`.
- Payment methods: `full_payment|partial_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-01-06 | recurring:utilities | recurring | utilities | -58.98 | Inferred recurring Water and power payment |
| 2026-01-07 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-01-07 | recurring:insurance | recurring | insurance | -26 | Inferred recurring Vehicle insurance premium |
| 2026-01-09 | recurring:streaming | recurring | streaming | -19 | Inferred recurring Family streaming plan |
| 2026-01-12 | recurring:shopping | recurring | shopping | -39.88 | Inferred recurring Household shopping |
| 2026-01-12 | recurring:cloud_storage | recurring | cloud_storage | -5 | Inferred recurring Shared storage plan |
| 2026-01-14 | recurring:entertainment | recurring | entertainment | -38.33 | Inferred recurring Monthly entertainment spend |
| 2026-01-14 | recurring:salary | recurring | salary | 1037.52 | Inferred recurring Payroll credit |
| 2026-01-17 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-01-27 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-02-01 | recurring:rent | recurring | rent | -254.1 | Inferred recurring Monthly rent |
| 2026-02-05 | recurring:utilities | recurring | utilities | -58.98 | Inferred recurring Water and power payment |
| 2026-02-06 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-02-06 | recurring:insurance | recurring | insurance | -26 | Inferred recurring Vehicle insurance premium |
| 2026-02-08 | recurring:streaming | recurring | streaming | -19 | Inferred recurring Family streaming plan |
| 2026-02-11 | recurring:shopping | recurring | shopping | -39.88 | Inferred recurring Household shopping |
| 2026-02-11 | recurring:cloud_storage | recurring | cloud_storage | -5 | Inferred recurring Shared storage plan |
| 2026-02-13 | recurring:entertainment | recurring | entertainment | -38.33 | Inferred recurring Monthly entertainment spend |
| 2026-02-13 | recurring:salary | recurring | salary | 1037.52 | Inferred recurring Payroll credit |
| 2026-02-16 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-02-26 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-03-03 | recurring:rent | recurring | rent | -254.1 | Inferred recurring Monthly rent |
| 2026-03-07 | recurring:utilities | recurring | utilities | -58.98 | Inferred recurring Water and power payment |
| 2026-03-08 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-03-08 | recurring:insurance | recurring | insurance | -26 | Inferred recurring Vehicle insurance premium |
| 2026-03-10 | recurring:streaming | recurring | streaming | -19 | Inferred recurring Family streaming plan |
| 2026-03-13 | recurring:shopping | recurring | shopping | -39.88 | Inferred recurring Household shopping |
| 2026-03-13 | recurring:cloud_storage | recurring | cloud_storage | -5 | Inferred recurring Shared storage plan |
| 2026-03-15 | recurring:entertainment | recurring | entertainment | -38.33 | Inferred recurring Monthly entertainment spend |
| 2026-03-15 | recurring:salary | recurring | salary | 1037.52 | Inferred recurring Payroll credit |
| 2026-03-18 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-03-28 | recurring:groceries | recurring | groceries | -51.55 | Inferred recurring Fresh food shop |
| 2026-04-02 | recurring:rent | recurring | rent | -254.1 | Inferred recurring Monthly rent |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_479` | 2025-07-11 | settled | groceries | 43.16 | cash date 2025-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_497` | 2025-07-12 | settled | transport | 23.68 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_532` | 2025-07-13 | settled | dining | 53.26 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_498` | 2025-07-17 | settled | transport | 23.83 | cash date 2025-07-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_533` | 2025-07-20 | settled | dining | 50.79 | cash date 2025-07-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_480` | 2025-07-21 | settled | groceries | 53.56 | cash date 2025-07-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_499` | 2025-07-22 | settled | transport | 24.21 | cash date 2025-07-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_500` | 2025-07-27 | settled | transport | 19.73 | cash date 2025-07-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_534` | 2025-07-27 | settled | dining | 34.99 | cash date 2025-07-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_481` | 2025-07-31 | settled | groceries | 49.49 | cash date 2025-07-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_501` | 2025-08-01 | settled | transport | 32.17 | cash date 2025-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_440` | 2025-08-03 | settled | rent | 254.1 | cash date 2025-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_535` | 2025-08-03 | settled | dining | 42.1 | cash date 2025-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_502` | 2025-08-06 | settled | transport | 27.8 | cash date 2025-08-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_441` | 2025-08-07 | settled | utilities | 58.34 | cash date 2025-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_442` | 2025-08-08 | settled | insurance | 26 | cash date 2025-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_444` | 2025-08-10 | settled | streaming | 19 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_482` | 2025-08-10 | settled | groceries | 43.57 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_536` | 2025-08-10 | settled | dining | 48.98 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_503` | 2025-08-11 | settled | transport | 28.03 | cash date 2025-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_443` | 2025-08-13 | settled | cloud_storage | 5 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_445` | 2025-08-13 | settled | shopping | 41.44 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_439` | 2025-08-15 | settled | salary | 1441 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_446` | 2025-08-15 | settled | entertainment | 32.1 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_504` | 2025-08-16 | settled | transport | 26.82 | cash date 2025-08-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_537` | 2025-08-17 | settled | dining | 46.84 | cash date 2025-08-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_483` | 2025-08-20 | settled | groceries | 31.69 | cash date 2025-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_505` | 2025-08-21 | settled | transport | 27.29 | cash date 2025-08-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_538` | 2025-08-24 | settled | dining | 38.44 | cash date 2025-08-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_506` | 2025-08-26 | settled | transport | 31.89 | cash date 2025-08-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_484` | 2025-08-30 | settled | groceries | 50.53 | cash date 2025-08-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_507` | 2025-08-31 | settled | transport | 27.65 | cash date 2025-08-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_539` | 2025-08-31 | settled | dining | 37.25 | cash date 2025-08-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_448` | 2025-09-03 | settled | rent | 254.1 | cash date 2025-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_508` | 2025-09-05 | settled | transport | 29.46 | cash date 2025-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_449` | 2025-09-07 | settled | utilities | 52.62 | cash date 2025-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_540` | 2025-09-07 | settled | dining | 40.23 | cash date 2025-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_450` | 2025-09-08 | settled | insurance | 26 | cash date 2025-09-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_485` | 2025-09-09 | settled | groceries | 51.97 | cash date 2025-09-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_452` | 2025-09-10 | settled | streaming | 19 | cash date 2025-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_509` | 2025-09-10 | settled | transport | 21.32 | cash date 2025-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_451` | 2025-09-13 | settled | cloud_storage | 5 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_453` | 2025-09-13 | settled | shopping | 46.25 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_541` | 2025-09-14 | settled | dining | 43.95 | cash date 2025-09-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_447` | 2025-09-15 | settled | salary | 1441 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_454` | 2025-09-15 | settled | entertainment | 35.1 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_510` | 2025-09-15 | settled | transport | 29.47 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_486` | 2025-09-19 | settled | groceries | 48.32 | cash date 2025-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_511` | 2025-09-20 | settled | transport | 28.08 | cash date 2025-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_542` | 2025-09-21 | settled | dining | 56.6 | cash date 2025-09-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_512` | 2025-09-25 | settled | transport | 31.87 | cash date 2025-09-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_543` | 2025-09-28 | settled | dining | 48.14 | cash date 2025-09-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_487` | 2025-09-29 | settled | groceries | 51.55 | cash date 2025-09-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_513` | 2025-09-30 | settled | transport | 21.1 | cash date 2025-09-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_456` | 2025-10-03 | settled | rent | 254.1 | cash date 2025-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_514` | 2025-10-05 | settled | transport | 28.87 | cash date 2025-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_544` | 2025-10-05 | settled | dining | 37.02 | cash date 2025-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_457` | 2025-10-07 | settled | utilities | 58.98 | cash date 2025-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_458` | 2025-10-08 | settled | insurance | 26 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_488` | 2025-10-09 | settled | groceries | 46.22 | cash date 2025-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_460` | 2025-10-10 | settled | streaming | 19 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_515` | 2025-10-10 | settled | transport | 28.61 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_545` | 2025-10-12 | settled | dining | 47.33 | cash date 2025-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_459` | 2025-10-13 | settled | cloud_storage | 5 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_461` | 2025-10-13 | settled | shopping | 39.46 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_455` | 2025-10-15 | settled | salary | 1441 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_462` | 2025-10-15 | settled | entertainment | 32.18 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_516` | 2025-10-15 | settled | transport | 22.14 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_489` | 2025-10-19 | settled | groceries | 32.96 | cash date 2025-10-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_546` | 2025-10-19 | settled | dining | 54.09 | cash date 2025-10-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_517` | 2025-10-20 | settled | transport | 28.65 | cash date 2025-10-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_518` | 2025-10-25 | settled | transport | 23.31 | cash date 2025-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_547` | 2025-10-26 | settled | dining | 53.71 | cash date 2025-10-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_490` | 2025-10-29 | settled | groceries | 51.4 | cash date 2025-10-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_519` | 2025-10-30 | settled | transport | 29.32 | cash date 2025-10-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_548` | 2025-11-02 | settled | dining | 32.9 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_464` | 2025-11-03 | settled | rent | 254.1 | cash date 2025-11-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_520` | 2025-11-04 | settled | transport | 24.5 | cash date 2025-11-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_465` | 2025-11-07 | settled | utilities | 56.71 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_466` | 2025-11-08 | settled | insurance | 26 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_491` | 2025-11-08 | settled | groceries | 34 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_521` | 2025-11-09 | settled | transport | 31.69 | cash date 2025-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_549` | 2025-11-09 | settled | dining | 43.17 | cash date 2025-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_468` | 2025-11-10 | settled | streaming | 19 | cash date 2025-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_467` | 2025-11-13 | settled | cloud_storage | 5 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_469` | 2025-11-13 | settled | shopping | 37.96 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_522` | 2025-11-14 | settled | transport | 30.82 | cash date 2025-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_463` | 2025-11-15 | settled | salary | 1037.52 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_470` | 2025-11-15 | settled | entertainment | 37.36 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_550` | 2025-11-16 | settled | dining | 37.42 | cash date 2025-11-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_492` | 2025-11-18 | settled | groceries | 45.4 | cash date 2025-11-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_523` | 2025-11-19 | settled | transport | 27.59 | cash date 2025-11-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_551` | 2025-11-23 | settled | dining | 55.16 | cash date 2025-11-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_524` | 2025-11-24 | settled | transport | 32.36 | cash date 2025-11-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_493` | 2025-11-28 | settled | groceries | 51.23 | cash date 2025-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_525` | 2025-11-29 | settled | transport | 27.97 | cash date 2025-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_552` | 2025-11-30 | settled | dining | 57.57 | cash date 2025-11-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_472` | 2025-12-03 | settled | rent | 254.1 | cash date 2025-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_526` | 2025-12-04 | settled | transport | 29.57 | cash date 2025-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_473` | 2025-12-07 | settled | utilities | 51.86 | cash date 2025-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_553` | 2025-12-07 | settled | dining | 45.39 | cash date 2025-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_474` | 2025-12-08 | settled | insurance | 26 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_494` | 2025-12-08 | settled | groceries | 40.91 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_527` | 2025-12-09 | settled | transport | 19.18 | cash date 2025-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_476` | 2025-12-10 | settled | streaming | 19 | cash date 2025-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_475` | 2025-12-13 | settled | cloud_storage | 5 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_477` | 2025-12-13 | settled | shopping | 39.88 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_528` | 2025-12-14 | settled | transport | 25.9 | cash date 2025-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_554` | 2025-12-14 | settled | dining | 36 | cash date 2025-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_471` | 2025-12-15 | settled | salary | 1037.52 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_478` | 2025-12-15 | settled | entertainment | 38.33 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_495` | 2025-12-18 | settled | groceries | 52.76 | cash date 2025-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_529` | 2025-12-19 | settled | transport | 24.92 | cash date 2025-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_555` | 2025-12-21 | settled | dining | 57.28 | cash date 2025-12-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_530` | 2025-12-24 | settled | transport | 21.46 | cash date 2025-12-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_496` | 2025-12-28 | settled | groceries | 32.69 | cash date 2025-12-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_556` | 2025-12-28 | settled | dining | 48.36 | cash date 2025-12-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_531` | 2025-12-29 | settled | transport | 32.9 | cash date 2025-12-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_557` | 2025-12-31 | cancelled | shopping |  | cancelled event |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_04` | 2025-12-28T09:30:00Z | `` | employer | Here’s the latest payroll information from Northstar Labs. Your temporary monthly pay is EUR 1037.52. The reduced amount continues for the next payroll. This is the amount currently scheduled for the affected pay cycle. Payroll ref EMP-0004. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_16` | full_payment | 2026-01-03:620.4 | 0 | 620.4 |
| `payment_option_17` | installments | 2026-01-10:34.86\|2026-02-07:34.86\|2026-03-07:34.86\|2026-04-04:34.86\|2026-05-02:34.86\|2026-05-30:34.86\|2026-06-27:34.86\|2026-07-25:34.86\|2026-08-22:34.86\|2026-09-19:34.86\|2026-10-17:34.86\|2026-11-14:34.86\|2026-12-12:34.86\|2027-01-09:34.86\|2027-02-06:34.86\|2027-03-06:34.86\|2027-04-03:34.86\|2027-05-01:34.86\|2027-05-29:34.86\|2027-06-26:34.86\|2027-07-24:34.86 | 111.66 | 732.06 |
| `payment_option_18` | installments | 2026-01-17:111.67\|2026-02-16:111.67\|2026-03-18:111.67\|2026-04-17:111.67\|2026-05-17:111.67\|2026-06-16:111.67 | 49.62 | 670.02 |

## request_07 — user_07

Primary category: **payment-option schedule or financing fee handling**

The baseline does not rank all safe supplied offers against the solved plan's completion date, total payable amount, and financing fee semantics.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 87170.56 | 0 |
| `affordability_status` | affordable_with_plan | not_affordable |
| `recommended_payment_method` | installments | not_recommended |
| `payment_plan` | 2024-09-12:68432\|2024-10-10:68432\|2024-11-07:68432 | none |
| `earliest_date_for_full_payment` | 2024-10-23 |  |
| `decision_explanation` | Use 3 installments of INR 68,432, starting 12 September 2024. This leaves at least INR 93,000 available. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `INR`
- Current balance: `218945.56`
- Minimum balance: `93000`
- Protected: `debt_repayment|rent|utilities`; reduce: `dining`; stop: `music_subscription`.
- Payment methods: `installments`; max installment months: `12`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-09-07 | recurring:utilities | recurring | utilities | -7387.41 | Inferred recurring Electricity bill |
| 2024-09-12 | recurring:debt_repayment | recurring | debt_repayment | -15650 | Inferred recurring Personal loan payment |
| 2024-09-12 | recurring:music_subscription | recurring | music_subscription | -1005 | Inferred recurring Music subscription |
| 2024-09-20 | recurring:transport | recurring | transport | -3822.62 | Inferred recurring Rail pass |
| 2024-10-05 | recurring:rent | recurring | rent | -34200 | Inferred recurring Monthly rent |
| 2024-10-07 | recurring:utilities | recurring | utilities | -7387.41 | Inferred recurring Electricity bill |
| 2024-10-11 | recurring:transport | recurring | transport | -3822.62 | Inferred recurring Rail pass |
| 2024-10-12 | recurring:debt_repayment | recurring | debt_repayment | -15650 | Inferred recurring Personal loan payment |
| 2024-10-12 | recurring:music_subscription | recurring | music_subscription | -1005 | Inferred recurring Music subscription |
| 2024-11-01 | recurring:transport | recurring | transport | -3822.62 | Inferred recurring Rail pass |
| 2024-11-05 | recurring:rent | recurring | rent | -34200 | Inferred recurring Monthly rent |
| 2024-11-06 | recurring:utilities | recurring | utilities | -7387.41 | Inferred recurring Electricity bill |
| 2024-11-11 | recurring:debt_repayment | recurring | debt_repayment | -15650 | Inferred recurring Personal loan payment |
| 2024-11-11 | recurring:music_subscription | recurring | music_subscription | -1005 | Inferred recurring Music subscription |
| 2024-11-22 | recurring:transport | recurring | transport | -3822.62 | Inferred recurring Rail pass |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_606` | 2024-03-11 | settled | dining | 7246.72 | cash date 2024-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_584` | 2024-03-14 | settled | groceries | 8380.73 | cash date 2024-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_597` | 2024-03-15 | settled | transport | 3690.82 | cash date 2024-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_585` | 2024-03-28 | settled | groceries | 6433.29 | cash date 2024-03-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_607` | 2024-04-01 | settled | dining | 4111.12 | cash date 2024-04-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_559` | 2024-04-04 | settled | rent | 34200 | cash date 2024-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_598` | 2024-04-05 | settled | transport | 3465.99 | cash date 2024-04-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_560` | 2024-04-08 | settled | utilities | 7219.31 | cash date 2024-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_586` | 2024-04-11 | settled | groceries | 6022.17 | cash date 2024-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_561` | 2024-04-13 | settled | debt_repayment | 15650 | cash date 2024-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_562` | 2024-04-13 | settled | music_subscription | 1005 | cash date 2024-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_558` | 2024-04-15 | settled | salary | 149000 | cash date 2024-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_608` | 2024-04-22 | settled | dining | 6371.55 | cash date 2024-04-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_587` | 2024-04-25 | settled | groceries | 6789.05 | cash date 2024-04-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_599` | 2024-04-26 | settled | transport | 2786.58 | cash date 2024-04-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_564` | 2024-05-04 | settled | rent | 34200 | cash date 2024-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_565` | 2024-05-08 | settled | utilities | 7049.68 | cash date 2024-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_588` | 2024-05-09 | settled | groceries | 8280.58 | cash date 2024-05-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_566` | 2024-05-13 | settled | debt_repayment | 15650 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_567` | 2024-05-13 | settled | music_subscription | 1005 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_609` | 2024-05-13 | settled | dining | 6313.91 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_563` | 2024-05-15 | settled | salary | 149000 | cash date 2024-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_600` | 2024-05-17 | settled | transport | 3104.36 | cash date 2024-05-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_589` | 2024-05-23 | settled | groceries | 7329.91 | cash date 2024-05-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_610` | 2024-06-03 | settled | dining | 5802.49 | cash date 2024-06-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_569` | 2024-06-04 | settled | rent | 34200 | cash date 2024-06-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_590` | 2024-06-06 | settled | groceries | 7849.54 | cash date 2024-06-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_601` | 2024-06-07 | settled | transport | 2439.43 | cash date 2024-06-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_570` | 2024-06-08 | settled | utilities | 7387.41 | cash date 2024-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_571` | 2024-06-13 | settled | debt_repayment | 15650 | cash date 2024-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_572` | 2024-06-13 | settled | music_subscription | 1005 | cash date 2024-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_568` | 2024-06-15 | settled | salary | 149000 | cash date 2024-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_591` | 2024-06-20 | settled | groceries | 7968.39 | cash date 2024-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_611` | 2024-06-24 | settled | dining | 4541.62 | cash date 2024-06-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_602` | 2024-06-28 | settled | transport | 3822.62 | cash date 2024-06-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_574` | 2024-07-04 | settled | rent | 34200 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_592` | 2024-07-04 | settled | groceries | 6889.87 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_575` | 2024-07-08 | settled | utilities | 6081.25 | cash date 2024-07-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_576` | 2024-07-13 | settled | debt_repayment | 15650 | cash date 2024-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_577` | 2024-07-13 | settled | music_subscription | 1005 | cash date 2024-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_573` | 2024-07-15 | settled | salary | 149000 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_612` | 2024-07-15 | settled | dining | 6664.9 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_593` | 2024-07-18 | settled | groceries | 5665.77 | cash date 2024-07-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_603` | 2024-07-19 | settled | transport | 2751.86 | cash date 2024-07-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_594` | 2024-08-01 | settled | groceries | 7913.81 | cash date 2024-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_579` | 2024-08-04 | settled | rent | 34200 | cash date 2024-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_613` | 2024-08-05 | settled | dining | 5799.66 | cash date 2024-08-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_580` | 2024-08-08 | settled | utilities | 6209.57 | cash date 2024-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_604` | 2024-08-09 | settled | transport | 3773.92 | cash date 2024-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_581` | 2024-08-13 | settled | debt_repayment | 15650 | cash date 2024-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_582` | 2024-08-13 | settled | music_subscription | 1005 | cash date 2024-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_595` | 2024-08-15 | settled | groceries | 7280.22 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_578` | 2024-08-23 | settled | salary | 149000 | cash date 2024-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_614` | 2024-08-26 | settled | dining | 6493.86 | cash date 2024-08-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_596` | 2024-08-29 | settled | groceries | 5710.65 | cash date 2024-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_605` | 2024-08-30 | settled | transport | 3145.62 | cash date 2024-08-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_583` | 2024-09-04 | settled | rent | 34200 | cash date 2024-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_05` | 2024-08-29T09:30:00Z | `` | employer | BrightPath Media has updated your payroll record. Your confirmed salary is now expected on 2024-09-23. This replaces the payroll date shown in the earlier update. Please use the revised date for anything you normally pay around payday. Payroll ref EMP-0005. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_19` | installments | 2024-09-12:68432\|2024-10-10:68432\|2024-11-07:68432 | 7896 | 205296 |
| `payment_option_20` | full_payment | 2024-09-05:197400 | 0 | 197400 |
| `payment_option_21` | installments | 2024-09-19:14476\|2024-10-19:14476\|2024-11-18:14476\|2024-12-18:14476\|2025-01-17:14476\|2025-02-16:14476\|2025-03-18:14476\|2025-04-17:14476\|2025-05-17:14476\|2025-06-16:14476\|2025-07-16:14476\|2025-08-15:14476\|2025-09-14:14476\|2025-10-14:14476\|2025-11-13:14476 | 19740 | 217140 |

## request_08 — user_08

Primary category: **earliest-date computation**

The baseline finds a later date but represents wait with payment_plan=none instead of the solved future full-payment commitment, and its daily date is not conservative enough.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 284.57 | 521.57 |
| `payment_plan` | 2025-04-15:996.60 | 2025-02-15:996.6 |
| `earliest_date_for_full_payment` | 2025-04-15 | 2025-02-15 |
| `decision_explanation` | Pay EUR 996.60 in full on 15 April 2025. Paying earlier would take the balance below the EUR 800 minimum. | Baseline forecast finds a later safe full-payment date. |

### Financial profile

- Home currency: `EUR`
- Current balance: `1536.57`
- Minimum balance: `800`
- Protected: `debt_repayment|education|groceries|rent`; reduce: `dining`; stop: `delivery_membership|music_subscription`.
- Payment methods: `full_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-02-09 | recurring:debt_repayment | recurring | debt_repayment | -177 | Inferred recurring Personal loan payment |
| 2025-02-09 | recurring:music_subscription | recurring | music_subscription | -14 | Inferred recurring Music subscription |
| 2025-02-11 | recurring:delivery_membership | recurring | delivery_membership | -24 | Inferred recurring Grocery delivery membership |
| 2025-02-14 | recurring:salary | recurring | salary | 1422.85 | Inferred recurring Payroll credit |
| 2025-03-04 | recurring:rent | recurring | rent | -467.5 | Inferred recurring Apartment rent transfer |
| 2025-03-08 | recurring:education | recurring | education | -89 | Inferred recurring School fee payment |
| 2025-03-08 | recurring:utilities | recurring | utilities | -82.61 | Inferred recurring Municipal utilities |
| 2025-03-11 | recurring:debt_repayment | recurring | debt_repayment | -177 | Inferred recurring Personal loan payment |
| 2025-03-11 | recurring:music_subscription | recurring | music_subscription | -14 | Inferred recurring Music subscription |
| 2025-03-13 | recurring:delivery_membership | recurring | delivery_membership | -24 | Inferred recurring Grocery delivery membership |
| 2025-03-16 | recurring:salary | recurring | salary | 1422.85 | Inferred recurring Payroll credit |
| 2025-04-04 | recurring:rent | recurring | rent | -467.5 | Inferred recurring Apartment rent transfer |
| 2025-04-07 | recurring:education | recurring | education | -89 | Inferred recurring School fee payment |
| 2025-04-08 | recurring:utilities | recurring | utilities | -82.61 | Inferred recurring Municipal utilities |
| 2025-04-10 | recurring:debt_repayment | recurring | debt_repayment | -177 | Inferred recurring Personal loan payment |
| 2025-04-10 | recurring:music_subscription | recurring | music_subscription | -14 | Inferred recurring Music subscription |
| 2025-04-12 | recurring:delivery_membership | recurring | delivery_membership | -24 | Inferred recurring Grocery delivery membership |
| 2025-04-15 | recurring:salary | recurring | salary | 1422.85 | Inferred recurring Payroll credit |
| 2025-05-05 | recurring:rent | recurring | rent | -467.5 | Inferred recurring Apartment rent transfer |
| 2025-05-07 | recurring:education | recurring | education | -89 | Inferred recurring School fee payment |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_652` | 2024-08-13 | settled | groceries | 78.42 | cash date 2024-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_678` | 2024-08-14 | settled | transport | 34.09 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_704` | 2024-08-15 | settled | dining | 51.75 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_653` | 2024-08-20 | settled | groceries | 77.07 | cash date 2024-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_679` | 2024-08-21 | settled | transport | 36.65 | cash date 2024-08-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_654` | 2024-08-27 | settled | groceries | 51.01 | cash date 2024-08-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_680` | 2024-08-28 | settled | transport | 41.53 | cash date 2024-08-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_705` | 2024-08-29 | settled | dining | 59.94 | cash date 2024-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_616` | 2024-09-01 | settled | rent | 467.5 | cash date 2024-09-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_655` | 2024-09-03 | settled | groceries | 52.28 | cash date 2024-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_681` | 2024-09-04 | settled | transport | 40.21 | cash date 2024-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_617` | 2024-09-05 | settled | utilities | 79.19 | cash date 2024-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_618` | 2024-09-07 | settled | education | 89 | cash date 2024-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_619` | 2024-09-10 | settled | debt_repayment | 177 | cash date 2024-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_620` | 2024-09-10 | settled | music_subscription | 14 | cash date 2024-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_656` | 2024-09-10 | settled | groceries | 68 | cash date 2024-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_682` | 2024-09-11 | settled | transport | 37.62 | cash date 2024-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_621` | 2024-09-12 | settled | delivery_membership | 24 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_706` | 2024-09-12 | settled | dining | 46.25 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_615` | 2024-09-15 | settled | salary | 1422.85 | cash date 2024-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_657` | 2024-09-17 | settled | groceries | 54.35 | cash date 2024-09-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_683` | 2024-09-18 | settled | transport | 43.53 | cash date 2024-09-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_658` | 2024-09-24 | settled | groceries | 46.71 | cash date 2024-09-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_684` | 2024-09-25 | settled | transport | 30.47 | cash date 2024-09-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_707` | 2024-09-26 | settled | dining | 60.66 | cash date 2024-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_623` | 2024-10-01 | settled | rent | 467.5 | cash date 2024-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_659` | 2024-10-01 | settled | groceries | 74.35 | cash date 2024-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_685` | 2024-10-02 | settled | transport | 36.94 | cash date 2024-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_624` | 2024-10-05 | settled | utilities | 80.9 | cash date 2024-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_625` | 2024-10-07 | settled | education | 89 | cash date 2024-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_660` | 2024-10-08 | settled | groceries | 48.16 | cash date 2024-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_686` | 2024-10-09 | settled | transport | 38.07 | cash date 2024-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_626` | 2024-10-10 | settled | debt_repayment | 177 | cash date 2024-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_627` | 2024-10-10 | settled | music_subscription | 14 | cash date 2024-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_708` | 2024-10-10 | settled | dining | 48.98 | cash date 2024-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_628` | 2024-10-12 | settled | delivery_membership | 24 | cash date 2024-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_622` | 2024-10-15 | settled | salary | 1422.85 | cash date 2024-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_661` | 2024-10-15 | settled | groceries | 68.99 | cash date 2024-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_687` | 2024-10-16 | settled | transport | 26.69 | cash date 2024-10-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_662` | 2024-10-22 | settled | groceries | 57.01 | cash date 2024-10-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_688` | 2024-10-23 | settled | transport | 46.08 | cash date 2024-10-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_709` | 2024-10-24 | settled | dining | 41.5 | cash date 2024-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_663` | 2024-10-29 | settled | groceries | 47.78 | cash date 2024-10-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_689` | 2024-10-30 | settled | transport | 45.56 | cash date 2024-10-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_630` | 2024-11-01 | settled | rent | 467.5 | cash date 2024-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_631` | 2024-11-05 | settled | utilities | 68.44 | cash date 2024-11-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_664` | 2024-11-05 | settled | groceries | 51.6 | cash date 2024-11-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_690` | 2024-11-06 | settled | transport | 39.38 | cash date 2024-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_632` | 2024-11-07 | settled | education | 89 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_710` | 2024-11-07 | settled | dining | 58.15 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_633` | 2024-11-10 | settled | debt_repayment | 177 | cash date 2024-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_634` | 2024-11-10 | settled | music_subscription | 14 | cash date 2024-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_635` | 2024-11-12 | settled | delivery_membership | 24 | cash date 2024-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_665` | 2024-11-12 | settled | groceries | 76.07 | cash date 2024-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_691` | 2024-11-13 | settled | transport | 37 | cash date 2024-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_629` | 2024-11-15 | settled | salary | 1422.85 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_666` | 2024-11-19 | settled | groceries | 69.32 | cash date 2024-11-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_692` | 2024-11-20 | settled | transport | 40.22 | cash date 2024-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_711` | 2024-11-21 | settled | dining | 45.5 | cash date 2024-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_667` | 2024-11-26 | settled | groceries | 60.11 | cash date 2024-11-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_693` | 2024-11-27 | settled | transport | 35.69 | cash date 2024-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_637` | 2024-12-01 | settled | rent | 467.5 | cash date 2024-12-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_668` | 2024-12-03 | settled | groceries | 51 | cash date 2024-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_694` | 2024-12-04 | settled | transport | 29.03 | cash date 2024-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_638` | 2024-12-05 | settled | utilities | 82.61 | cash date 2024-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_712` | 2024-12-05 | settled | dining | 46.75 | cash date 2024-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_639` | 2024-12-07 | settled | education | 89 | cash date 2024-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_640` | 2024-12-10 | settled | debt_repayment | 177 | cash date 2024-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_641` | 2024-12-10 | settled | music_subscription | 14 | cash date 2024-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_669` | 2024-12-10 | settled | groceries | 56.62 | cash date 2024-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_695` | 2024-12-11 | settled | transport | 35.98 | cash date 2024-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_642` | 2024-12-12 | settled | delivery_membership | 24 | cash date 2024-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_636` | 2024-12-15 | settled | salary | 1422.85 | cash date 2024-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_670` | 2024-12-17 | settled | groceries | 55.02 | cash date 2024-12-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_696` | 2024-12-18 | settled | transport | 43.51 | cash date 2024-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_713` | 2024-12-19 | settled | dining | 49.45 | cash date 2024-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_671` | 2024-12-24 | settled | groceries | 53.11 | cash date 2024-12-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_697` | 2024-12-25 | settled | transport | 43.2 | cash date 2024-12-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_672` | 2024-12-31 | settled | groceries | 51.85 | cash date 2024-12-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_644` | 2025-01-01 | settled | rent | 467.5 | cash date 2025-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_698` | 2025-01-01 | settled | transport | 31.5 | cash date 2025-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_714` | 2025-01-02 | settled | dining | 56.05 | cash date 2025-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_645` | 2025-01-05 | settled | utilities | 69.28 | cash date 2025-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_646` | 2025-01-07 | settled | education | 89 | cash date 2025-01-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_673` | 2025-01-07 | settled | groceries | 48 | cash date 2025-01-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_699` | 2025-01-08 | settled | transport | 41.57 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_647` | 2025-01-10 | settled | debt_repayment | 177 | cash date 2025-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_648` | 2025-01-10 | settled | music_subscription | 14 | cash date 2025-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_649` | 2025-01-12 | settled | delivery_membership | 24 | cash date 2025-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_674` | 2025-01-14 | settled | groceries | 45.99 | cash date 2025-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_643` | 2025-01-15 | settled | salary | 782.57 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_700` | 2025-01-15 | settled | transport | 32.95 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_715` | 2025-01-16 | settled | dining | 53.65 | cash date 2025-01-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_675` | 2025-01-21 | settled | groceries | 53.96 | cash date 2025-01-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_701` | 2025-01-22 | settled | transport | 31.67 | cash date 2025-01-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_676` | 2025-01-28 | settled | groceries | 65.92 | cash date 2025-01-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_702` | 2025-01-29 | settled | transport | 28.33 | cash date 2025-01-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_716` | 2025-01-30 | settled | dining | 42.33 | cash date 2025-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_650` | 2025-02-01 | settled | rent | 467.5 | cash date 2025-02-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_677` | 2025-02-04 | settled | groceries | 72.38 | cash date 2025-02-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_651` | 2025-02-05 | settled | utilities | 80.55 | cash date 2025-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_703` | 2025-02-05 | settled | transport | 47.21 | cash date 2025-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_06` | 2025-02-06T09:30:00Z | `` | employer | Hi, Greenfield Foods payroll here. Your next salary is reduced to EUR 1422.85. The adjustment is due to approved unpaid leave. The adjustment will be visible on your next payslip. Payroll ref EMP-0006. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_22` | full_payment | 2025-02-07:996.6 | 0 | 996.6 |
| `payment_option_23` | installments | 2025-02-07:63.12\|2025-03-10:63.12\|2025-04-10:63.12\|2025-05-11:63.12\|2025-06-11:63.12\|2025-07-12:63.12\|2025-08-12:63.12\|2025-09-12:63.12\|2025-10-13:63.12\|2025-11-13:63.12\|2025-12-14:63.12\|2026-01-14:63.12\|2026-02-14:63.12\|2026-03-17:63.12\|2026-04-17:63.12\|2026-05-18:63.12\|2026-06-18:63.12\|2026-07-19:63.12 | 139.56 | 1136.16 |

## request_10 — user_10

Primary category: **pending debit or credit handling**

The supporting message says a bonus, commission, refund, prize, or payout is not yet cash. The forecast must reserve its absence until an explicit settlement/credit record exists.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 12700 | 266700 |
| `decision_explanation` | Do not make this payment by 10 February 2025. None of the available options keeps the INR 225,400 minimum protected. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `INR`
- Current balance: `750155`
- Minimum balance: `225400`
- Protected: `groceries|rent|transport`; reduce: `dining|entertainment|gym`; stop: `delivery_membership|music_subscription`.
- Payment methods: `installments|partial_payment`; max installment months: `6`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-12-08 | recurring:utilities | recurring | utilities | -17771.13 | Inferred recurring Electricity and water bill |
| 2024-12-12 | recurring:gym | recurring | gym | -4860 | Inferred recurring Community fitness plan |
| 2024-12-13 | recurring:music_subscription | recurring | music_subscription | -2800 | Inferred recurring Music subscription |
| 2024-12-15 | recurring:delivery_membership | recurring | delivery_membership | -1895 | Inferred recurring Delivery service plan |
| 2024-12-16 | recurring:entertainment | recurring | entertainment | -4883.78 | Inferred recurring Cinema and events |
| 2024-12-20 | recurring:salary | recurring | salary | 47802.51 | Inferred recurring Driver platform payout |
| 2025-01-01 | recurring:transport | recurring | transport | -7568.88 | Inferred recurring Parking and tolls |
| 2025-01-02 | recurring:rent | recurring | rent | -69100 | Inferred recurring Monthly rent |
| 2025-01-05 | recurring:salary | recurring | salary | 47802.51 | Inferred recurring Driver platform payout |
| 2025-01-08 | recurring:utilities | recurring | utilities | -17771.13 | Inferred recurring Electricity and water bill |
| 2025-01-12 | recurring:gym | recurring | gym | -4860 | Inferred recurring Community fitness plan |
| 2025-01-13 | recurring:music_subscription | recurring | music_subscription | -2800 | Inferred recurring Music subscription |
| 2025-01-15 | recurring:delivery_membership | recurring | delivery_membership | -1895 | Inferred recurring Delivery service plan |
| 2025-01-16 | recurring:entertainment | recurring | entertainment | -4883.78 | Inferred recurring Cinema and events |
| 2025-01-21 | recurring:salary | recurring | salary | 47802.51 | Inferred recurring Driver platform payout |
| 2025-02-01 | recurring:rent | recurring | rent | -69100 | Inferred recurring Monthly rent |
| 2025-02-02 | recurring:transport | recurring | transport | -7568.88 | Inferred recurring Parking and tolls |
| 2025-02-06 | recurring:salary | recurring | salary | 47802.51 | Inferred recurring Driver platform payout |
| 2025-02-08 | recurring:utilities | recurring | utilities | -17771.13 | Inferred recurring Electricity and water bill |
| 2025-02-12 | recurring:gym | recurring | gym | -4860 | Inferred recurring Community fitness plan |
| 2025-02-13 | recurring:music_subscription | recurring | music_subscription | -2800 | Inferred recurring Music subscription |
| 2025-02-15 | recurring:delivery_membership | recurring | delivery_membership | -1895 | Inferred recurring Delivery service plan |
| 2025-02-16 | recurring:entertainment | recurring | entertainment | -4883.78 | Inferred recurring Cinema and events |
| 2025-02-22 | recurring:salary | recurring | salary | 47802.51 | Inferred recurring Driver platform payout |
| 2025-03-03 | recurring:rent | recurring | rent | -69100 | Inferred recurring Monthly rent |
| 2025-03-06 | recurring:transport | recurring | transport | -7568.88 | Inferred recurring Parking and tolls |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_841` | 2024-06-13 | settled | groceries | 10089.49 | cash date 2024-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_867` | 2024-06-14 | settled | transport | 6859.81 | cash date 2024-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_892` | 2024-06-15 | settled | dining | 8813.96 | cash date 2024-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_842` | 2024-06-20 | settled | groceries | 12216.63 | cash date 2024-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_868` | 2024-06-21 | settled | transport | 7100.47 | cash date 2024-06-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_843` | 2024-06-27 | settled | groceries | 10431.63 | cash date 2024-06-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_869` | 2024-06-28 | settled | transport | 4830.13 | cash date 2024-06-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_893` | 2024-06-29 | settled | dining | 9260.11 | cash date 2024-06-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_793` | 2024-07-03 | settled | rent | 69100 | cash date 2024-07-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_789` | 2024-07-04 | settled | salary | 74420.35 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_844` | 2024-07-04 | settled | groceries | 12027.49 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_870` | 2024-07-05 | settled | transport | 4956.67 | cash date 2024-07-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_794` | 2024-07-07 | settled | utilities | 19224.83 | cash date 2024-07-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_790` | 2024-07-11 | settled | salary | 74852.29 | cash date 2024-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_797` | 2024-07-11 | settled | gym | 4860 | cash date 2024-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_845` | 2024-07-11 | settled | groceries | 9512.16 | cash date 2024-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_795` | 2024-07-12 | settled | music_subscription | 2800 | cash date 2024-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_871` | 2024-07-12 | settled | transport | 5489.62 | cash date 2024-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_894` | 2024-07-13 | settled | dining | 8274.24 | cash date 2024-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_796` | 2024-07-14 | settled | delivery_membership | 1895 | cash date 2024-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_798` | 2024-07-15 | settled | entertainment | 4770.41 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_791` | 2024-07-18 | settled | salary | 54774.8 | cash date 2024-07-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_846` | 2024-07-18 | settled | groceries | 10839.89 | cash date 2024-07-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_872` | 2024-07-19 | settled | transport | 7530.3 | cash date 2024-07-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_792` | 2024-07-25 | settled | salary | 82410.47 | cash date 2024-07-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_847` | 2024-07-25 | settled | groceries | 11898.24 | cash date 2024-07-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_873` | 2024-07-26 | settled | transport | 7568.88 | cash date 2024-07-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_895` | 2024-07-27 | settled | dining | 6897.95 | cash date 2024-07-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_848` | 2024-08-01 | settled | groceries | 12020.19 | cash date 2024-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_874` | 2024-08-02 | settled | transport | 6683.23 | cash date 2024-08-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_803` | 2024-08-03 | settled | rent | 69100 | cash date 2024-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_799` | 2024-08-04 | settled | salary | 72641.37 | cash date 2024-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_804` | 2024-08-07 | settled | utilities | 17538.11 | cash date 2024-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_849` | 2024-08-08 | settled | groceries | 11986 | cash date 2024-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_875` | 2024-08-09 | settled | transport | 6632.3 | cash date 2024-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_896` | 2024-08-10 | settled | dining | 9399.4 | cash date 2024-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_800` | 2024-08-11 | settled | salary | 59553.07 | cash date 2024-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_807` | 2024-08-11 | settled | gym | 4860 | cash date 2024-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_805` | 2024-08-12 | settled | music_subscription | 2800 | cash date 2024-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_806` | 2024-08-14 | settled | delivery_membership | 1895 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_808` | 2024-08-15 | settled | entertainment | 4504.6 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_850` | 2024-08-15 | settled | groceries | 11074.05 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_876` | 2024-08-16 | settled | transport | 5641.87 | cash date 2024-08-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_801` | 2024-08-18 | settled | salary | 65056.43 | cash date 2024-08-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_851` | 2024-08-22 | settled | groceries | 9929.21 | cash date 2024-08-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_877` | 2024-08-23 | settled | transport | 5747.77 | cash date 2024-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_897` | 2024-08-24 | settled | dining | 9621.2 | cash date 2024-08-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_802` | 2024-08-25 | settled | salary | 47245.98 | cash date 2024-08-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_852` | 2024-08-29 | settled | groceries | 8855.55 | cash date 2024-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_878` | 2024-08-30 | settled | transport | 5753.54 | cash date 2024-08-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_813` | 2024-09-03 | settled | rent | 69100 | cash date 2024-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_809` | 2024-09-04 | settled | salary | 81755.75 | cash date 2024-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_853` | 2024-09-05 | settled | groceries | 12641.36 | cash date 2024-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_879` | 2024-09-06 | settled | transport | 7448.62 | cash date 2024-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_814` | 2024-09-07 | settled | utilities | 15748.74 | cash date 2024-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_898` | 2024-09-07 | settled | dining | 6375.03 | cash date 2024-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_810` | 2024-09-11 | settled | salary | 67741.04 | cash date 2024-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_817` | 2024-09-11 | settled | gym | 4860 | cash date 2024-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_815` | 2024-09-12 | settled | music_subscription | 2800 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_854` | 2024-09-12 | settled | groceries | 10087.39 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_880` | 2024-09-13 | settled | transport | 5018.36 | cash date 2024-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_816` | 2024-09-14 | settled | delivery_membership | 1895 | cash date 2024-09-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_818` | 2024-09-15 | settled | entertainment | 4700.56 | cash date 2024-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_811` | 2024-09-18 | settled | salary | 79168.24 | cash date 2024-09-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_855` | 2024-09-19 | settled | groceries | 11596.13 | cash date 2024-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_881` | 2024-09-20 | settled | transport | 6582.39 | cash date 2024-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_899` | 2024-09-21 | settled | dining | 10079.99 | cash date 2024-09-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_812` | 2024-09-25 | settled | salary | 69351.86 | cash date 2024-09-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_856` | 2024-09-26 | settled | groceries | 8809.04 | cash date 2024-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_882` | 2024-09-27 | settled | transport | 6785.52 | cash date 2024-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_823` | 2024-10-03 | settled | rent | 69100 | cash date 2024-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_857` | 2024-10-03 | settled | groceries | 9807.08 | cash date 2024-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_819` | 2024-10-04 | settled | salary | 78226.16 | cash date 2024-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_883` | 2024-10-04 | settled | transport | 4472.6 | cash date 2024-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_900` | 2024-10-05 | settled | dining | 10525.43 | cash date 2024-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_824` | 2024-10-07 | settled | utilities | 15236.94 | cash date 2024-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_858` | 2024-10-10 | settled | groceries | 12589.2 | cash date 2024-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_820` | 2024-10-11 | settled | salary | 65488.36 | cash date 2024-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_827` | 2024-10-11 | settled | gym | 4860 | cash date 2024-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_884` | 2024-10-11 | settled | transport | 4570.28 | cash date 2024-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_825` | 2024-10-12 | settled | music_subscription | 2800 | cash date 2024-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_826` | 2024-10-14 | settled | delivery_membership | 1895 | cash date 2024-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_828` | 2024-10-15 | settled | entertainment | 4366.61 | cash date 2024-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_859` | 2024-10-17 | settled | groceries | 13621.53 | cash date 2024-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_821` | 2024-10-18 | settled | salary | 60517.87 | cash date 2024-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_885` | 2024-10-18 | settled | transport | 5776.08 | cash date 2024-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_901` | 2024-10-19 | settled | dining | 8538.83 | cash date 2024-10-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_860` | 2024-10-24 | settled | groceries | 12767.81 | cash date 2024-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_822` | 2024-10-25 | settled | salary | 40977.52 | cash date 2024-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_886` | 2024-10-25 | settled | transport | 6245.32 | cash date 2024-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_861` | 2024-10-31 | settled | groceries | 9968.28 | cash date 2024-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_887` | 2024-11-01 | settled | transport | 6819.66 | cash date 2024-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_902` | 2024-11-02 | settled | dining | 8480.31 | cash date 2024-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_833` | 2024-11-03 | settled | rent | 69100 | cash date 2024-11-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_829` | 2024-11-04 | settled | salary | 60877.41 | cash date 2024-11-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_834` | 2024-11-07 | settled | utilities | 17771.13 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_862` | 2024-11-07 | settled | groceries | 10392.47 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_888` | 2024-11-08 | settled | transport | 5350.7 | cash date 2024-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_830` | 2024-11-11 | settled | salary | 44415.5 | cash date 2024-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_837` | 2024-11-11 | settled | gym | 4860 | cash date 2024-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_835` | 2024-11-12 | settled | music_subscription | 2800 | cash date 2024-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_836` | 2024-11-14 | settled | delivery_membership | 1895 | cash date 2024-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_863` | 2024-11-14 | settled | groceries | 12092.24 | cash date 2024-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_838` | 2024-11-15 | settled | entertainment | 4883.78 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_889` | 2024-11-15 | settled | transport | 4990.01 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_903` | 2024-11-16 | settled | dining | 8253.71 | cash date 2024-11-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_831` | 2024-11-18 | settled | salary | 47802.51 | cash date 2024-11-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_864` | 2024-11-21 | settled | groceries | 8157.98 | cash date 2024-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_890` | 2024-11-22 | settled | transport | 4356.14 | cash date 2024-11-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_832` | 2024-11-25 | settled | salary | 82667.27 | cash date 2024-11-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_865` | 2024-11-28 | settled | groceries | 8755.75 | cash date 2024-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_891` | 2024-11-29 | settled | transport | 6359.49 | cash date 2024-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_904` | 2024-11-30 | settled | dining | 10370.83 | cash date 2024-11-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_840` | 2024-12-03 | settled | rent | 69100 | cash date 2024-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_839` | 2024-12-04 | settled | salary | 52239.8 | cash date 2024-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_866` | 2024-12-05 | settled | groceries | 8011.08 | cash date 2024-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_07` | 2024-11-25T09:30:00Z | `` | service_provider | Here’s the latest service update from QuickCrew. The next QuickCrew payout is still pending. The weekly earnings shown in the QuickCrew app can change until the payout is closed. The balance isn’t withdrawable until the payout shows as completed. Case ref SER-0007. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_27` | full_payment | 2024-12-06:266700 | 0 | 266700 |
| `payment_option_28` | installments | 2024-12-13:19558\|2025-01-12:19558\|2025-02-11:19558\|2025-03-13:19558\|2025-04-12:19558\|2025-05-12:19558\|2025-06-11:19558\|2025-07-11:19558\|2025-08-10:19558\|2025-09-09:19558\|2025-10-09:19558\|2025-11-08:19558\|2025-12-08:19558\|2026-01-07:19558\|2026-02-06:19558 | 26670 | 293370 |

## request_11 — user_11

Primary category: **flexible spending changes**

The solved plan changes flexible recurring spending, while the baseline never models authorized stop/reduce actions or their resulting forecast cash flows.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 12510645 | 13110000 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `earliest_date_for_full_payment` | 2025-07-15 | 2025-05-03 |
| `spending_changes_needed` | reduce_to:event_989:665950 | none |
| `decision_explanation` | Reduce the weekend food delivery to IDR 665,950, then pay IDR 13,110,000 today. This leaves at least IDR 34,140,600 available. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `IDR`
- Current balance: `63531795`
- Minimum balance: `34140600`
- Protected: `education|housing|utilities`; reduce: `dining|entertainment`; stop: `cloud_storage`.
- Payment methods: `full_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-05-06 | recurring:housing | recurring | housing | -2954500 | Inferred recurring Home association fee |
| 2025-05-09 | recurring:utilities | recurring | utilities | -2796165.18 | Inferred recurring Municipal utilities |
| 2025-05-10 | recurring:insurance | recurring | insurance | -1881000 | Inferred recurring Vehicle insurance premium |
| 2025-05-11 | recurring:education | recurring | education | -2544100 | Inferred recurring Child education fee |
| 2025-05-13 | recurring:healthcare | recurring | healthcare | -3165638.3 | Inferred recurring Regular medicine purchase |
| 2025-05-15 | recurring:cloud_storage | recurring | cloud_storage | -168150 | Inferred recurring Cloud storage plan |
| 2025-05-16 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Base salary |
| 2025-05-17 | recurring:entertainment | recurring | entertainment | -1674887.61 | Inferred recurring Games and recreation |
| 2025-05-28 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Performance commission |
| 2025-06-06 | recurring:housing | recurring | housing | -2954500 | Inferred recurring Home association fee |
| 2025-06-09 | recurring:utilities | recurring | utilities | -2796165.18 | Inferred recurring Municipal utilities |
| 2025-06-10 | recurring:insurance | recurring | insurance | -1881000 | Inferred recurring Vehicle insurance premium |
| 2025-06-11 | recurring:education | recurring | education | -2544100 | Inferred recurring Child education fee |
| 2025-06-13 | recurring:healthcare | recurring | healthcare | -3165638.3 | Inferred recurring Regular medicine purchase |
| 2025-06-15 | recurring:cloud_storage | recurring | cloud_storage | -168150 | Inferred recurring Cloud storage plan |
| 2025-06-16 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Base salary |
| 2025-06-17 | recurring:entertainment | recurring | entertainment | -1674887.61 | Inferred recurring Games and recreation |
| 2025-06-28 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Performance commission |
| 2025-07-07 | recurring:housing | recurring | housing | -2954500 | Inferred recurring Home association fee |
| 2025-07-10 | recurring:utilities | recurring | utilities | -2796165.18 | Inferred recurring Municipal utilities |
| 2025-07-11 | recurring:insurance | recurring | insurance | -1881000 | Inferred recurring Vehicle insurance premium |
| 2025-07-12 | recurring:education | recurring | education | -2544100 | Inferred recurring Child education fee |
| 2025-07-14 | recurring:healthcare | recurring | healthcare | -3165638.3 | Inferred recurring Regular medicine purchase |
| 2025-07-16 | recurring:cloud_storage | recurring | cloud_storage | -168150 | Inferred recurring Cloud storage plan |
| 2025-07-17 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Base salary |
| 2025-07-18 | recurring:entertainment | recurring | entertainment | -1674887.61 | Inferred recurring Games and recreation |
| 2025-07-29 | recurring:salary | recurring | salary | 38760000 | Inferred recurring Performance commission |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_981` | 2024-11-06 | settled | dining | 1018758.07 | cash date 2024-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_950` | 2024-11-09 | settled | groceries | 1053064.17 | cash date 2024-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_968` | 2024-11-10 | settled | transport | 1230316.5 | cash date 2024-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_951` | 2024-11-19 | settled | groceries | 1565130.98 | cash date 2024-11-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_969` | 2024-11-24 | settled | transport | 825660.54 | cash date 2024-11-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_982` | 2024-11-27 | settled | dining | 1485097.86 | cash date 2024-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_952` | 2024-11-29 | settled | groceries | 1714643.08 | cash date 2024-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_907` | 2024-12-05 | settled | housing | 2954500 | cash date 2024-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_908` | 2024-12-08 | settled | utilities | 2916312.61 | cash date 2024-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_970` | 2024-12-08 | settled | transport | 788053.2 | cash date 2024-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_909` | 2024-12-09 | settled | insurance | 1881000 | cash date 2024-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_953` | 2024-12-09 | settled | groceries | 1644304.53 | cash date 2024-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_910` | 2024-12-10 | settled | education | 2544100 | cash date 2024-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_911` | 2024-12-12 | settled | healthcare | 2635764.61 | cash date 2024-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_913` | 2024-12-14 | settled | cloud_storage | 168150 | cash date 2024-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_905` | 2024-12-15 | settled | salary | 23256000 | cash date 2024-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_912` | 2024-12-16 | settled | entertainment | 1404572.9 | cash date 2024-12-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_983` | 2024-12-18 | settled | dining | 1528058.96 | cash date 2024-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_954` | 2024-12-19 | settled | groceries | 1406401.86 | cash date 2024-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_971` | 2024-12-22 | settled | transport | 893623.46 | cash date 2024-12-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_906` | 2024-12-24 | settled | salary | 16715584.16 | cash date 2024-12-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_955` | 2024-12-29 | settled | groceries | 1063530.58 | cash date 2024-12-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_916` | 2025-01-05 | settled | housing | 2954500 | cash date 2025-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_972` | 2025-01-05 | settled | transport | 1212904.33 | cash date 2025-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_917` | 2025-01-08 | settled | utilities | 2891149.67 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_956` | 2025-01-08 | settled | groceries | 1395524.8 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_984` | 2025-01-08 | settled | dining | 1697463.1 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_918` | 2025-01-09 | settled | insurance | 1881000 | cash date 2025-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_919` | 2025-01-10 | settled | education | 2544100 | cash date 2025-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_920` | 2025-01-12 | settled | healthcare | 3118089.32 | cash date 2025-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_922` | 2025-01-14 | settled | cloud_storage | 168150 | cash date 2025-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_914` | 2025-01-15 | settled | salary | 23256000 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_921` | 2025-01-16 | settled | entertainment | 1688239.04 | cash date 2025-01-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_957` | 2025-01-18 | settled | groceries | 1578114.18 | cash date 2025-01-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_973` | 2025-01-19 | settled | transport | 1307205.52 | cash date 2025-01-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_915` | 2025-01-24 | settled | salary | 8908379.93 | cash date 2025-01-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_958` | 2025-01-28 | settled | groceries | 1763208.29 | cash date 2025-01-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_985` | 2025-01-29 | settled | dining | 1052748.56 | cash date 2025-01-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_974` | 2025-02-02 | settled | transport | 785218.72 | cash date 2025-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_925` | 2025-02-05 | settled | housing | 2954500 | cash date 2025-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_959` | 2025-02-07 | settled | groceries | 1241008.74 | cash date 2025-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_926` | 2025-02-08 | settled | utilities | 2508782.45 | cash date 2025-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_927` | 2025-02-09 | settled | insurance | 1881000 | cash date 2025-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_928` | 2025-02-10 | settled | education | 2544100 | cash date 2025-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_929` | 2025-02-12 | settled | healthcare | 2973572.96 | cash date 2025-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_931` | 2025-02-14 | settled | cloud_storage | 168150 | cash date 2025-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_923` | 2025-02-15 | settled | salary | 23256000 | cash date 2025-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_930` | 2025-02-16 | settled | entertainment | 1587027.72 | cash date 2025-02-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_975` | 2025-02-16 | settled | transport | 1185524.72 | cash date 2025-02-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_960` | 2025-02-17 | settled | groceries | 1222447.75 | cash date 2025-02-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_986` | 2025-02-19 | settled | dining | 1365643.7 | cash date 2025-02-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_924` | 2025-02-24 | settled | salary | 15989420 | cash date 2025-02-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_961` | 2025-02-27 | settled | groceries | 1614291.7 | cash date 2025-02-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_976` | 2025-03-02 | settled | transport | 1200020.76 | cash date 2025-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_934` | 2025-03-05 | settled | housing | 2954500 | cash date 2025-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_935` | 2025-03-08 | settled | utilities | 2488665.63 | cash date 2025-03-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_936` | 2025-03-09 | settled | insurance | 1881000 | cash date 2025-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_962` | 2025-03-09 | settled | groceries | 1655671.41 | cash date 2025-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_937` | 2025-03-10 | settled | education | 2544100 | cash date 2025-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_938` | 2025-03-12 | settled | healthcare | 3165638.3 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_987` | 2025-03-12 | settled | dining | 1335266.7 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_940` | 2025-03-14 | settled | cloud_storage | 168150 | cash date 2025-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_932` | 2025-03-15 | settled | salary | 23256000 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_939` | 2025-03-16 | settled | entertainment | 1649906.5 | cash date 2025-03-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_977` | 2025-03-16 | settled | transport | 1244032.33 | cash date 2025-03-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_963` | 2025-03-19 | settled | groceries | 1311350.07 | cash date 2025-03-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_933` | 2025-03-24 | settled | salary | 20012106.46 | cash date 2025-03-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_964` | 2025-03-29 | settled | groceries | 1292005.65 | cash date 2025-03-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_978` | 2025-03-30 | settled | transport | 1122838.73 | cash date 2025-03-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_988` | 2025-04-02 | settled | dining | 1503635.49 | cash date 2025-04-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_943` | 2025-04-05 | settled | housing | 2954500 | cash date 2025-04-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_944` | 2025-04-08 | settled | utilities | 2796165.18 | cash date 2025-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_965` | 2025-04-08 | settled | groceries | 1590529.64 | cash date 2025-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_945` | 2025-04-09 | settled | insurance | 1881000 | cash date 2025-04-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_946` | 2025-04-10 | settled | education | 2544100 | cash date 2025-04-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_947` | 2025-04-12 | settled | healthcare | 2826901.92 | cash date 2025-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_979` | 2025-04-13 | settled | transport | 1103949.29 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_949` | 2025-04-14 | settled | cloud_storage | 168150 | cash date 2025-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_941` | 2025-04-15 | settled | salary | 23256000 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_948` | 2025-04-16 | settled | entertainment | 1674887.61 | cash date 2025-04-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_966` | 2025-04-18 | settled | groceries | 1131582.3 | cash date 2025-04-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_989` | 2025-04-23 | settled | dining | 1163530.49 | cash date 2025-04-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_942` | 2025-04-24 | settled | salary | 8502888.2 | cash date 2025-04-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_980` | 2025-04-27 | settled | transport | 1244835.69 | cash date 2025-04-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_967` | 2025-04-28 | settled | groceries | 1341187.18 | cash date 2025-04-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_08` | 2025-04-22T09:30:00Z | `` | employer | Berikut informasi penggajian terbaru dari Greenfield Foods. Gaji pokok yang dikonfirmasi adalah IDR 38760000. Komisi dari transaksi yang masih berjalan belum disetujui. Transaksi yang masih berjalan tidak masuk pembayaran sampai komisinya dinyatakan diperoleh. Ref payroll EMP-0008. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_29` | full_payment | 2025-05-03:13110000 | 0 | 13110000 |
| `payment_option_30` | installments | 2025-05-17:830300\|2025-06-17:830300\|2025-07-18:830300\|2025-08-18:830300\|2025-09-18:830300\|2025-10-19:830300\|2025-11-19:830300\|2025-12-20:830300\|2026-01-20:830300\|2026-02-20:830300\|2026-03-23:830300\|2026-04-23:830300\|2026-05-24:830300\|2026-06-24:830300\|2026-07-25:830300\|2026-08-25:830300\|2026-09-25:830300\|2026-10-26:830300 | 1835400 | 14945400 |
| `payment_option_31` | installments | 2025-05-03:2359800\|2025-05-31:2359800\|2025-06-28:2359800\|2025-07-26:2359800\|2025-08-23:2359800\|2025-09-20:2359800 | 1048800 | 14158800 |
| `payment_option_32` | installments | 2025-05-06:666425\|2025-06-05:666425\|2025-07-05:666425\|2025-08-04:666425\|2025-09-03:666425\|2025-10-03:666425\|2025-11-02:666425\|2025-12-02:666425\|2026-01-01:666425\|2026-01-31:666425\|2026-03-02:666425\|2026-04-01:666425\|2026-05-01:666425\|2026-05-31:666425\|2026-06-30:666425\|2026-07-30:666425\|2026-08-29:666425\|2026-09-28:666425\|2026-10-28:666425\|2026-11-27:666425\|2026-12-27:666425\|2027-01-26:666425\|2027-02-25:666425\|2027-03-27:666425 | 2884200 | 15994200 |

## request_13 — user_13

Primary category: **recurrence detection / forecasting frequency**

The solved result is later-safe while the baseline is now-safe or uses a different date, indicating that recurring essential commitments or their cadence are under-forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 433.4 | 941.6 |
| `affordability_status` | affordable_later | affordable_now |
| `recommended_payment_method` | wait | full_payment |
| `payment_plan` | 2024-05-15:941.60 | 2024-03-07:941.6 |
| `earliest_date_for_full_payment` | 2024-05-15 | 2024-03-07 |
| `decision_explanation` | Pay EUR 941.60 in full on 15 May 2024. Paying earlier would take the balance below the EUR 1,300 minimum. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `EUR`
- Current balance: `2789.52`
- Minimum balance: `1300`
- Protected: `groceries|rent|transport`; reduce: `gym`; stop: `delivery_membership|music_subscription`.
- Payment methods: `full_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-03-12 | recurring:gym | recurring | gym | -61 | Inferred recurring Community fitness plan |
| 2024-03-13 | recurring:music_subscription | recurring | music_subscription | -29 | Inferred recurring Music subscription |
| 2024-03-15 | recurring:delivery_membership | recurring | delivery_membership | -21 | Inferred recurring Delivery service plan |
| 2024-03-15 | event_1161 | explicit | salary | 1343.54 | Next confirmed salary |
| 2024-03-16 | recurring:entertainment | recurring | entertainment | -37.9 | Inferred recurring Local event tickets |
| 2024-03-17 | recurring:salary | recurring | salary | 1343.54 | Inferred recurring Primary household salary |
| 2024-03-22 | recurring:salary | recurring | salary | 771.17 | Inferred recurring Second household income |
| 2024-04-01 | recurring:rent | recurring | rent | -622.6 | Inferred recurring Shared housing rent |
| 2024-04-03 | recurring:transport | recurring | transport | -50.46 | Inferred recurring Ride-hailing trip |
| 2024-04-05 | recurring:utilities | recurring | utilities | -143.7 | Inferred recurring Water and power payment |
| 2024-04-12 | recurring:gym | recurring | gym | -61 | Inferred recurring Community fitness plan |
| 2024-04-13 | recurring:music_subscription | recurring | music_subscription | -29 | Inferred recurring Music subscription |
| 2024-04-15 | recurring:delivery_membership | recurring | delivery_membership | -21 | Inferred recurring Delivery service plan |
| 2024-04-16 | recurring:entertainment | recurring | entertainment | -37.9 | Inferred recurring Local event tickets |
| 2024-04-17 | recurring:salary | recurring | salary | 1343.54 | Inferred recurring Primary household salary |
| 2024-04-22 | recurring:salary | recurring | salary | 771.17 | Inferred recurring Second household income |
| 2024-05-01 | recurring:rent | recurring | rent | -622.6 | Inferred recurring Shared housing rent |
| 2024-05-05 | recurring:utilities | recurring | utilities | -143.7 | Inferred recurring Water and power payment |
| 2024-05-08 | recurring:transport | recurring | transport | -50.46 | Inferred recurring Ride-hailing trip |
| 2024-05-13 | recurring:gym | recurring | gym | -61 | Inferred recurring Community fitness plan |
| 2024-05-14 | recurring:music_subscription | recurring | music_subscription | -29 | Inferred recurring Music subscription |
| 2024-05-16 | recurring:delivery_membership | recurring | delivery_membership | -21 | Inferred recurring Delivery service plan |
| 2024-05-17 | recurring:entertainment | recurring | entertainment | -37.9 | Inferred recurring Local event tickets |
| 2024-05-18 | recurring:salary | recurring | salary | 1343.54 | Inferred recurring Primary household salary |
| 2024-05-23 | recurring:salary | recurring | salary | 771.17 | Inferred recurring Second household income |
| 2024-05-31 | recurring:rent | recurring | rent | -622.6 | Inferred recurring Shared housing rent |
| 2024-06-04 | recurring:utilities | recurring | utilities | -143.7 | Inferred recurring Water and power payment |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1096` | 2023-09-12 | settled | groceries | 91.05 | cash date 2023-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1122` | 2023-09-13 | settled | transport | 44.85 | cash date 2023-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1148` | 2023-09-14 | settled | dining | 75.47 | cash date 2023-09-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1097` | 2023-09-19 | settled | groceries | 114.9 | cash date 2023-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1123` | 2023-09-20 | settled | transport | 35.12 | cash date 2023-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1098` | 2023-09-26 | settled | groceries | 120.16 | cash date 2023-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1124` | 2023-09-27 | settled | transport | 34.47 | cash date 2023-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1149` | 2023-09-28 | settled | dining | 68.7 | cash date 2023-09-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1057` | 2023-10-02 | settled | rent | 622.6 | cash date 2023-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1099` | 2023-10-03 | settled | groceries | 82.38 | cash date 2023-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1125` | 2023-10-04 | settled | transport | 34.28 | cash date 2023-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1058` | 2023-10-06 | settled | utilities | 162.77 | cash date 2023-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1061` | 2023-10-10 | settled | gym | 61 | cash date 2023-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1100` | 2023-10-10 | settled | groceries | 115.37 | cash date 2023-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1059` | 2023-10-11 | settled | music_subscription | 29 | cash date 2023-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1126` | 2023-10-11 | settled | transport | 50.6 | cash date 2023-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1150` | 2023-10-12 | settled | dining | 80.09 | cash date 2023-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1060` | 2023-10-13 | settled | delivery_membership | 21 | cash date 2023-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1062` | 2023-10-14 | settled | entertainment | 33.83 | cash date 2023-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1055` | 2023-10-15 | settled | salary | 1343.54 | cash date 2023-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1101` | 2023-10-17 | settled | groceries | 89.89 | cash date 2023-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1127` | 2023-10-18 | settled | transport | 55.33 | cash date 2023-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1056` | 2023-10-20 | settled | salary | 993.88 | cash date 2023-10-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1102` | 2023-10-24 | settled | groceries | 91.28 | cash date 2023-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1128` | 2023-10-25 | settled | transport | 34.09 | cash date 2023-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1151` | 2023-10-26 | settled | dining | 62.71 | cash date 2023-10-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1103` | 2023-10-31 | settled | groceries | 108.75 | cash date 2023-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1129` | 2023-11-01 | settled | transport | 54.58 | cash date 2023-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1065` | 2023-11-02 | settled | rent | 622.6 | cash date 2023-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1066` | 2023-11-06 | settled | utilities | 143.39 | cash date 2023-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1104` | 2023-11-07 | settled | groceries | 101.74 | cash date 2023-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1130` | 2023-11-08 | settled | transport | 33.97 | cash date 2023-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1152` | 2023-11-09 | settled | dining | 53.91 | cash date 2023-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1069` | 2023-11-10 | settled | gym | 61 | cash date 2023-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1067` | 2023-11-11 | settled | music_subscription | 29 | cash date 2023-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1068` | 2023-11-13 | settled | delivery_membership | 21 | cash date 2023-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1070` | 2023-11-14 | settled | entertainment | 30.88 | cash date 2023-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1105` | 2023-11-14 | settled | groceries | 102.05 | cash date 2023-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1063` | 2023-11-15 | settled | salary | 1343.54 | cash date 2023-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1131` | 2023-11-15 | settled | transport | 48.13 | cash date 2023-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1064` | 2023-11-20 | settled | salary | 771.17 | cash date 2023-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1106` | 2023-11-21 | settled | groceries | 119.05 | cash date 2023-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1132` | 2023-11-22 | settled | transport | 54.4 | cash date 2023-11-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1153` | 2023-11-23 | settled | dining | 80.35 | cash date 2023-11-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1107` | 2023-11-28 | settled | groceries | 101.87 | cash date 2023-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1133` | 2023-11-29 | settled | transport | 38.31 | cash date 2023-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1073` | 2023-12-02 | settled | rent | 622.6 | cash date 2023-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1108` | 2023-12-05 | settled | groceries | 106.05 | cash date 2023-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1074` | 2023-12-06 | settled | utilities | 146.33 | cash date 2023-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1134` | 2023-12-06 | settled | transport | 44.07 | cash date 2023-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1154` | 2023-12-07 | settled | dining | 64.45 | cash date 2023-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1077` | 2023-12-10 | settled | gym | 61 | cash date 2023-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1075` | 2023-12-11 | settled | music_subscription | 29 | cash date 2023-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1109` | 2023-12-12 | settled | groceries | 102.25 | cash date 2023-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1076` | 2023-12-13 | settled | delivery_membership | 21 | cash date 2023-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1135` | 2023-12-13 | settled | transport | 50.38 | cash date 2023-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1078` | 2023-12-14 | settled | entertainment | 37.9 | cash date 2023-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1071` | 2023-12-15 | settled | salary | 1343.54 | cash date 2023-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1110` | 2023-12-19 | settled | groceries | 93.15 | cash date 2023-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1072` | 2023-12-20 | settled | salary | 948.46 | cash date 2023-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1136` | 2023-12-20 | settled | transport | 49.29 | cash date 2023-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1155` | 2023-12-21 | settled | dining | 70.45 | cash date 2023-12-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1111` | 2023-12-26 | settled | groceries | 81.24 | cash date 2023-12-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1137` | 2023-12-27 | settled | transport | 46.73 | cash date 2023-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1081` | 2024-01-02 | settled | rent | 622.6 | cash date 2024-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1112` | 2024-01-02 | settled | groceries | 86.23 | cash date 2024-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1138` | 2024-01-03 | settled | transport | 43.41 | cash date 2024-01-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1156` | 2024-01-04 | settled | dining | 61.59 | cash date 2024-01-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1082` | 2024-01-06 | settled | utilities | 143.7 | cash date 2024-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1113` | 2024-01-09 | settled | groceries | 94.28 | cash date 2024-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1085` | 2024-01-10 | settled | gym | 61 | cash date 2024-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1139` | 2024-01-10 | settled | transport | 58.44 | cash date 2024-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1083` | 2024-01-11 | settled | music_subscription | 29 | cash date 2024-01-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1084` | 2024-01-13 | settled | delivery_membership | 21 | cash date 2024-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1086` | 2024-01-14 | settled | entertainment | 31.8 | cash date 2024-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1079` | 2024-01-15 | settled | salary | 1343.54 | cash date 2024-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1114` | 2024-01-16 | settled | groceries | 84.23 | cash date 2024-01-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1140` | 2024-01-17 | settled | transport | 33.5 | cash date 2024-01-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1157` | 2024-01-18 | settled | dining | 48.2 | cash date 2024-01-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1080` | 2024-01-20 | settled | salary | 881.45 | cash date 2024-01-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1115` | 2024-01-23 | settled | groceries | 120.89 | cash date 2024-01-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1141` | 2024-01-24 | settled | transport | 56.63 | cash date 2024-01-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1116` | 2024-01-30 | settled | groceries | 114.53 | cash date 2024-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1142` | 2024-01-31 | settled | transport | 46.98 | cash date 2024-01-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1158` | 2024-02-01 | settled | dining | 60.34 | cash date 2024-02-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1088` | 2024-02-02 | settled | rent | 622.6 | cash date 2024-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1089` | 2024-02-06 | settled | utilities | 131.53 | cash date 2024-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1117` | 2024-02-06 | settled | groceries | 73.74 | cash date 2024-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1143` | 2024-02-07 | settled | transport | 45.29 | cash date 2024-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1092` | 2024-02-10 | settled | gym | 61 | cash date 2024-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1090` | 2024-02-11 | settled | music_subscription | 29 | cash date 2024-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1091` | 2024-02-13 | settled | delivery_membership | 21 | cash date 2024-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1118` | 2024-02-13 | settled | groceries | 98.36 | cash date 2024-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1093` | 2024-02-14 | settled | entertainment | 30.39 | cash date 2024-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1144` | 2024-02-14 | settled | transport | 45.37 | cash date 2024-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1087` | 2024-02-15 | settled | salary | 1343.54 | cash date 2024-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1159` | 2024-02-15 | settled | dining | 48.02 | cash date 2024-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1119` | 2024-02-20 | settled | groceries | 118.36 | cash date 2024-02-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1145` | 2024-02-21 | settled | transport | 39.48 | cash date 2024-02-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1120` | 2024-02-27 | settled | groceries | 85.71 | cash date 2024-02-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1146` | 2024-02-28 | settled | transport | 50.46 | cash date 2024-02-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1160` | 2024-02-29 | settled | dining | 61.28 | cash date 2024-02-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1094` | 2024-03-02 | settled | rent | 622.6 | cash date 2024-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1121` | 2024-03-05 | settled | groceries | 93.66 | cash date 2024-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1095` | 2024-03-06 | settled | utilities | 134.25 | cash date 2024-03-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1147` | 2024-03-06 | settled | transport | 37.29 | cash date 2024-03-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_36` | full_payment | 2024-03-07:941.6 | 0 | 941.6 |
| `payment_option_37` | installments | 2024-03-10:69.05\|2024-04-09:69.05\|2024-05-09:69.05\|2024-06-08:69.05\|2024-07-08:69.05\|2024-08-07:69.05\|2024-09-06:69.05\|2024-10-06:69.05\|2024-11-05:69.05\|2024-12-05:69.05\|2025-01-04:69.05\|2025-02-03:69.05\|2025-03-05:69.05\|2025-04-04:69.05\|2025-05-04:69.05 | 94.15 | 1035.75 |
| `payment_option_38` | installments | 2024-03-21:47.86\|2024-04-18:47.86\|2024-05-16:47.86\|2024-06-13:47.86\|2024-07-11:47.86\|2024-08-08:47.86\|2024-09-05:47.86\|2024-10-03:47.86\|2024-10-31:47.86\|2024-11-28:47.86\|2024-12-26:47.86\|2025-01-23:47.86\|2025-02-20:47.86\|2025-03-20:47.86\|2025-04-17:47.86\|2025-05-15:47.86\|2025-06-12:47.86\|2025-07-10:47.86\|2025-08-07:47.86\|2025-09-04:47.86\|2025-10-02:47.86\|2025-10-30:47.86\|2025-11-27:47.86\|2025-12-25:47.86 | 207.04 | 1148.64 |

## request_14 — user_14

Primary category: **cancellations or amendments from messages**

Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 597.74 | 0 |
| `decision_explanation` | Do not proceed with the EUR 5,414.20 request. Although EUR 597.74 is available today, the full amount cannot be completed safely within 90 days. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `EUR`
- Current balance: `3931.74`
- Minimum balance: `2200`
- Protected: `family_support|groceries|healthcare|rent`; reduce: `shopping`; stop: `cloud_storage`.
- Payment methods: `partial_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-08-06 | recurring:utilities | recurring | utilities | -153.69 | Inferred recurring Energy provider bill |
| 2025-08-10 | recurring:healthcare | recurring | healthcare | -95.17 | Inferred recurring Family healthcare expense |
| 2025-08-11 | recurring:debt_repayment | recurring | debt_repayment | -350 | Inferred recurring Credit card repayment |
| 2025-08-12 | recurring:shopping | recurring | shopping | -140.39 | Inferred recurring Online retail purchases |
| 2025-08-12 | recurring:cloud_storage | recurring | cloud_storage | -14 | Inferred recurring Cloud storage plan |
| 2025-08-13 | recurring:family_support | recurring | family_support | -226 | Inferred recurring Family support payment |
| 2025-09-02 | recurring:rent | recurring | rent | -688.6 | Inferred recurring Monthly rent |
| 2025-09-05 | recurring:utilities | recurring | utilities | -153.69 | Inferred recurring Energy provider bill |
| 2025-09-09 | recurring:healthcare | recurring | healthcare | -95.17 | Inferred recurring Family healthcare expense |
| 2025-09-10 | recurring:debt_repayment | recurring | debt_repayment | -350 | Inferred recurring Credit card repayment |
| 2025-09-11 | recurring:shopping | recurring | shopping | -140.39 | Inferred recurring Online retail purchases |
| 2025-09-11 | recurring:cloud_storage | recurring | cloud_storage | -14 | Inferred recurring Cloud storage plan |
| 2025-09-12 | recurring:family_support | recurring | family_support | -226 | Inferred recurring Family support payment |
| 2025-10-02 | recurring:rent | recurring | rent | -688.6 | Inferred recurring Monthly rent |
| 2025-10-05 | recurring:utilities | recurring | utilities | -153.69 | Inferred recurring Energy provider bill |
| 2025-10-09 | recurring:healthcare | recurring | healthcare | -95.17 | Inferred recurring Family healthcare expense |
| 2025-10-10 | recurring:debt_repayment | recurring | debt_repayment | -350 | Inferred recurring Credit card repayment |
| 2025-10-11 | recurring:shopping | recurring | shopping | -140.39 | Inferred recurring Online retail purchases |
| 2025-10-11 | recurring:cloud_storage | recurring | cloud_storage | -14 | Inferred recurring Cloud storage plan |
| 2025-10-12 | recurring:family_support | recurring | family_support | -226 | Inferred recurring Family support payment |
| 2025-11-01 | recurring:rent | recurring | rent | -688.6 | Inferred recurring Monthly rent |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1201` | 2025-02-09 | settled | groceries | 103.53 | cash date 2025-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1227` | 2025-02-10 | settled | transport | 46.75 | cash date 2025-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1202` | 2025-02-16 | settled | groceries | 95.35 | cash date 2025-02-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1203` | 2025-02-23 | settled | groceries | 104.91 | cash date 2025-02-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1228` | 2025-02-24 | settled | transport | 58.52 | cash date 2025-02-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1204` | 2025-03-02 | settled | groceries | 81.22 | cash date 2025-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1163` | 2025-03-03 | settled | rent | 688.6 | cash date 2025-03-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1164` | 2025-03-07 | settled | utilities | 141.46 | cash date 2025-03-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1205` | 2025-03-09 | settled | groceries | 92.09 | cash date 2025-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1229` | 2025-03-10 | settled | transport | 37.65 | cash date 2025-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1166` | 2025-03-11 | settled | healthcare | 92.08 | cash date 2025-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1165` | 2025-03-12 | settled | debt_repayment | 350 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1168` | 2025-03-13 | settled | cloud_storage | 14 | cash date 2025-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1169` | 2025-03-13 | settled | shopping | 137.03 | cash date 2025-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1167` | 2025-03-14 | settled | family_support | 226 | cash date 2025-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1162` | 2025-03-15 | settled | salary | 2717 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1206` | 2025-03-16 | settled | groceries | 121.61 | cash date 2025-03-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1207` | 2025-03-23 | settled | groceries | 87.64 | cash date 2025-03-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1230` | 2025-03-24 | settled | transport | 47.73 | cash date 2025-03-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1208` | 2025-03-30 | settled | groceries | 140.51 | cash date 2025-03-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1171` | 2025-04-03 | settled | rent | 688.6 | cash date 2025-04-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1209` | 2025-04-06 | settled | groceries | 131.02 | cash date 2025-04-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1172` | 2025-04-07 | settled | utilities | 156.08 | cash date 2025-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1231` | 2025-04-07 | settled | transport | 53.15 | cash date 2025-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1174` | 2025-04-11 | settled | healthcare | 92.65 | cash date 2025-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1173` | 2025-04-12 | settled | debt_repayment | 350 | cash date 2025-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1176` | 2025-04-13 | settled | cloud_storage | 14 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1177` | 2025-04-13 | settled | shopping | 123.04 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1210` | 2025-04-13 | settled | groceries | 83.71 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1175` | 2025-04-14 | settled | family_support | 226 | cash date 2025-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1170` | 2025-04-15 | settled | salary | 2717 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1211` | 2025-04-20 | settled | groceries | 93.46 | cash date 2025-04-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1232` | 2025-04-21 | settled | transport | 56.49 | cash date 2025-04-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1212` | 2025-04-27 | settled | groceries | 90.76 | cash date 2025-04-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1178` | 2025-05-03 | settled | rent | 688.6 | cash date 2025-05-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1213` | 2025-05-04 | settled | groceries | 106.55 | cash date 2025-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1233` | 2025-05-05 | settled | transport | 55.52 | cash date 2025-05-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1179` | 2025-05-07 | settled | utilities | 143.45 | cash date 2025-05-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1181` | 2025-05-11 | settled | healthcare | 95.17 | cash date 2025-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1214` | 2025-05-11 | settled | groceries | 93.65 | cash date 2025-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1180` | 2025-05-12 | settled | debt_repayment | 350 | cash date 2025-05-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1183` | 2025-05-13 | settled | cloud_storage | 14 | cash date 2025-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1184` | 2025-05-13 | settled | shopping | 123.12 | cash date 2025-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1182` | 2025-05-14 | settled | family_support | 226 | cash date 2025-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1215` | 2025-05-18 | settled | groceries | 96.42 | cash date 2025-05-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1234` | 2025-05-19 | settled | transport | 52.26 | cash date 2025-05-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1216` | 2025-05-25 | settled | groceries | 101.15 | cash date 2025-05-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1217` | 2025-06-01 | settled | groceries | 129.68 | cash date 2025-06-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1235` | 2025-06-02 | settled | transport | 50.48 | cash date 2025-06-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1185` | 2025-06-03 | settled | rent | 688.6 | cash date 2025-06-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1186` | 2025-06-07 | settled | utilities | 146.41 | cash date 2025-06-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1218` | 2025-06-08 | settled | groceries | 123.41 | cash date 2025-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1188` | 2025-06-11 | settled | healthcare | 91.77 | cash date 2025-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1187` | 2025-06-12 | settled | debt_repayment | 350 | cash date 2025-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1190` | 2025-06-13 | settled | cloud_storage | 14 | cash date 2025-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1191` | 2025-06-13 | settled | shopping | 123.77 | cash date 2025-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1189` | 2025-06-14 | settled | family_support | 226 | cash date 2025-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1219` | 2025-06-15 | settled | groceries | 94.21 | cash date 2025-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1236` | 2025-06-16 | settled | transport | 55.96 | cash date 2025-06-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1220` | 2025-06-22 | settled | groceries | 86.49 | cash date 2025-06-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1221` | 2025-06-29 | settled | groceries | 138.85 | cash date 2025-06-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1237` | 2025-06-30 | settled | transport | 62.3 | cash date 2025-06-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1193` | 2025-07-03 | settled | rent | 688.6 | cash date 2025-07-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1222` | 2025-07-06 | settled | groceries | 102.54 | cash date 2025-07-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1194` | 2025-07-07 | settled | utilities | 153.69 | cash date 2025-07-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1196` | 2025-07-11 | settled | healthcare | 87.84 | cash date 2025-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1195` | 2025-07-12 | settled | debt_repayment | 350 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1198` | 2025-07-13 | settled | cloud_storage | 14 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1199` | 2025-07-13 | settled | shopping | 140.39 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1223` | 2025-07-13 | settled | groceries | 112.72 | cash date 2025-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1197` | 2025-07-14 | settled | family_support | 226 | cash date 2025-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1238` | 2025-07-14 | settled | transport | 43.12 | cash date 2025-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1192` | 2025-07-15 | settled | salary | 2717 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1224` | 2025-07-20 | settled | groceries | 96.86 | cash date 2025-07-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1225` | 2025-07-27 | settled | groceries | 86.83 | cash date 2025-07-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1239` | 2025-07-28 | settled | transport | 43.88 | cash date 2025-07-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1200` | 2025-08-03 | settled | rent | 688.6 | cash date 2025-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1226` | 2025-08-03 | settled | groceries | 129.56 | cash date 2025-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_10` | 2025-07-27T09:30:00Z | `` | employer | Here’s the latest payroll information from HarborWorks. Regular salary of EUR 2717 resumes on 2025-08-15. A new recurring childcare payment begins in the same month. The updated pay and deductions will appear from the next cycle. Payroll ref EMP-0010. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_39` | full_payment | 2025-08-04:5414.2 | 0 | 5414.2 |
| `payment_option_40` | installments | 2025-08-11:342.9\|2025-09-11:342.9\|2025-10-12:342.9\|2025-11-12:342.9\|2025-12-13:342.9\|2026-01-13:342.9\|2026-02-13:342.9\|2026-03-16:342.9\|2026-04-16:342.9\|2026-05-17:342.9\|2026-06-17:342.9\|2026-07-18:342.9\|2026-08-18:342.9\|2026-09-18:342.9\|2026-10-19:342.9\|2026-11-19:342.9\|2026-12-20:342.9\|2027-01-20:342.9 | 758 | 6172.2 |

## request_15 — user_15

Primary category: **cancellations or amendments from messages**

Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 83.05 | 0 |
| `decision_explanation` | Do not make this payment by 1 February 2026. None of the available options keeps the EUR 1,200 minimum protected. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `EUR`
- Current balance: `1770.05`
- Minimum balance: `1200`
- Protected: `debt_repayment|education|groceries|rent`; reduce: `dining`; stop: ``.
- Payment methods: `partial_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-01-07 | recurring:utilities | recurring | utilities | -90.39 | Inferred recurring Energy provider bill |
| 2026-01-09 | recurring:education | recurring | education | -159 | Inferred recurring School fee payment |
| 2026-01-12 | recurring:debt_repayment | recurring | debt_repayment | -84 | Inferred recurring Credit card repayment |
| 2026-01-12 | recurring:music_subscription | recurring | music_subscription | -11 | Inferred recurring Music subscription |
| 2026-01-14 | recurring:delivery_membership | recurring | delivery_membership | -27 | Inferred recurring Food delivery membership |
| 2026-01-21 | recurring:transport | recurring | transport | -41.35 | Inferred recurring Ride-hailing trip |
| 2026-02-03 | recurring:rent | recurring | rent | -435.6 | Inferred recurring Landlord standing order |
| 2026-02-06 | recurring:utilities | recurring | utilities | -90.39 | Inferred recurring Energy provider bill |
| 2026-02-08 | recurring:education | recurring | education | -159 | Inferred recurring School fee payment |
| 2026-02-11 | recurring:debt_repayment | recurring | debt_repayment | -84 | Inferred recurring Credit card repayment |
| 2026-02-11 | recurring:transport | recurring | transport | -41.35 | Inferred recurring Ride-hailing trip |
| 2026-02-11 | recurring:music_subscription | recurring | music_subscription | -11 | Inferred recurring Music subscription |
| 2026-02-13 | recurring:delivery_membership | recurring | delivery_membership | -27 | Inferred recurring Food delivery membership |
| 2026-03-04 | recurring:transport | recurring | transport | -41.35 | Inferred recurring Ride-hailing trip |
| 2026-03-05 | recurring:rent | recurring | rent | -435.6 | Inferred recurring Landlord standing order |
| 2026-03-08 | recurring:utilities | recurring | utilities | -90.39 | Inferred recurring Energy provider bill |
| 2026-03-10 | recurring:education | recurring | education | -159 | Inferred recurring School fee payment |
| 2026-03-13 | recurring:debt_repayment | recurring | debt_repayment | -84 | Inferred recurring Credit card repayment |
| 2026-03-13 | recurring:music_subscription | recurring | music_subscription | -11 | Inferred recurring Music subscription |
| 2026-03-15 | recurring:delivery_membership | recurring | delivery_membership | -27 | Inferred recurring Food delivery membership |
| 2026-03-25 | recurring:transport | recurring | transport | -41.35 | Inferred recurring Ride-hailing trip |
| 2026-04-04 | recurring:rent | recurring | rent | -435.6 | Inferred recurring Landlord standing order |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1323` | 2025-07-12 | settled | dining | 33.39 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1273` | 2025-07-15 | settled | groceries | 51.57 | cash date 2025-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1298` | 2025-07-16 | settled | transport | 29.41 | cash date 2025-07-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1274` | 2025-07-22 | settled | groceries | 63.15 | cash date 2025-07-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1299` | 2025-07-23 | settled | transport | 39.06 | cash date 2025-07-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1324` | 2025-07-26 | settled | dining | 41.42 | cash date 2025-07-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1275` | 2025-07-29 | settled | groceries | 64.39 | cash date 2025-07-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1300` | 2025-07-30 | settled | transport | 42.66 | cash date 2025-07-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1240` | 2025-08-04 | settled | rent | 435.6 | cash date 2025-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1276` | 2025-08-05 | settled | groceries | 55.63 | cash date 2025-08-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1301` | 2025-08-06 | settled | transport | 29.38 | cash date 2025-08-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1241` | 2025-08-08 | settled | utilities | 84.12 | cash date 2025-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1325` | 2025-08-09 | settled | dining | 45.13 | cash date 2025-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1242` | 2025-08-10 | settled | education | 159 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1277` | 2025-08-12 | settled | groceries | 68.03 | cash date 2025-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1243` | 2025-08-13 | settled | debt_repayment | 84 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1244` | 2025-08-13 | settled | music_subscription | 11 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1302` | 2025-08-13 | settled | transport | 26.48 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1245` | 2025-08-15 | settled | delivery_membership | 27 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1278` | 2025-08-19 | settled | groceries | 46.76 | cash date 2025-08-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1303` | 2025-08-20 | settled | transport | 26.5 | cash date 2025-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1326` | 2025-08-23 | settled | dining | 44.75 | cash date 2025-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1279` | 2025-08-26 | settled | groceries | 71.92 | cash date 2025-08-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1304` | 2025-08-27 | settled | transport | 25.11 | cash date 2025-08-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1280` | 2025-09-02 | settled | groceries | 49.38 | cash date 2025-09-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1305` | 2025-09-03 | settled | transport | 37.01 | cash date 2025-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1246` | 2025-09-04 | settled | rent | 435.6 | cash date 2025-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1327` | 2025-09-06 | settled | dining | 53.58 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1247` | 2025-09-08 | settled | utilities | 85.91 | cash date 2025-09-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1281` | 2025-09-09 | settled | groceries | 73.5 | cash date 2025-09-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1248` | 2025-09-10 | settled | education | 159 | cash date 2025-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1306` | 2025-09-10 | settled | transport | 29.73 | cash date 2025-09-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1249` | 2025-09-13 | settled | debt_repayment | 84 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1250` | 2025-09-13 | settled | music_subscription | 11 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1251` | 2025-09-15 | settled | delivery_membership | 27 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1282` | 2025-09-16 | settled | groceries | 71.16 | cash date 2025-09-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1307` | 2025-09-17 | settled | transport | 35.61 | cash date 2025-09-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1328` | 2025-09-20 | settled | dining | 36.23 | cash date 2025-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1283` | 2025-09-23 | settled | groceries | 72.3 | cash date 2025-09-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1308` | 2025-09-24 | settled | transport | 31.28 | cash date 2025-09-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1284` | 2025-09-30 | settled | groceries | 59.88 | cash date 2025-09-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1309` | 2025-10-01 | settled | transport | 29.3 | cash date 2025-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1252` | 2025-10-04 | settled | rent | 435.6 | cash date 2025-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1329` | 2025-10-04 | settled | dining | 32.17 | cash date 2025-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1285` | 2025-10-07 | settled | groceries | 48.88 | cash date 2025-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1253` | 2025-10-08 | settled | utilities | 90.39 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1310` | 2025-10-08 | settled | transport | 26 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1254` | 2025-10-10 | settled | education | 159 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1255` | 2025-10-13 | settled | debt_repayment | 84 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1256` | 2025-10-13 | settled | music_subscription | 11 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1286` | 2025-10-14 | settled | groceries | 69.83 | cash date 2025-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1257` | 2025-10-15 | settled | delivery_membership | 27 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1311` | 2025-10-15 | settled | transport | 25.57 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1330` | 2025-10-18 | settled | dining | 34.51 | cash date 2025-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1287` | 2025-10-21 | settled | groceries | 62.21 | cash date 2025-10-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1312` | 2025-10-22 | settled | transport | 25.35 | cash date 2025-10-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1288` | 2025-10-28 | settled | groceries | 68.35 | cash date 2025-10-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1313` | 2025-10-29 | settled | transport | 34.86 | cash date 2025-10-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1331` | 2025-11-01 | settled | dining | 38.56 | cash date 2025-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1259` | 2025-11-04 | settled | rent | 435.6 | cash date 2025-11-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1289` | 2025-11-04 | settled | groceries | 56.7 | cash date 2025-11-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1314` | 2025-11-05 | settled | transport | 31.09 | cash date 2025-11-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1260` | 2025-11-08 | settled | utilities | 87.14 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1261` | 2025-11-10 | settled | education | 159 | cash date 2025-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1290` | 2025-11-11 | settled | groceries | 52.65 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1315` | 2025-11-12 | settled | transport | 32.48 | cash date 2025-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1262` | 2025-11-13 | settled | debt_repayment | 84 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1263` | 2025-11-13 | settled | music_subscription | 11 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1258` | 2025-11-15 | settled | salary | 1661 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1264` | 2025-11-15 | settled | delivery_membership | 27 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1332` | 2025-11-15 | settled | dining | 51.08 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1291` | 2025-11-18 | settled | groceries | 53.42 | cash date 2025-11-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1316` | 2025-11-19 | settled | transport | 36.7 | cash date 2025-11-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1292` | 2025-11-25 | settled | groceries | 47.26 | cash date 2025-11-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1317` | 2025-11-26 | settled | transport | 38.53 | cash date 2025-11-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1333` | 2025-11-29 | settled | dining | 32.62 | cash date 2025-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1293` | 2025-12-02 | settled | groceries | 64.51 | cash date 2025-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1318` | 2025-12-03 | settled | transport | 25.63 | cash date 2025-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1266` | 2025-12-04 | settled | rent | 435.6 | cash date 2025-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1267` | 2025-12-08 | settled | utilities | 84.41 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1294` | 2025-12-09 | settled | groceries | 64.22 | cash date 2025-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1268` | 2025-12-10 | settled | education | 159 | cash date 2025-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1319` | 2025-12-10 | settled | transport | 41.35 | cash date 2025-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1269` | 2025-12-13 | settled | debt_repayment | 84 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1270` | 2025-12-13 | settled | music_subscription | 11 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1334` | 2025-12-13 | settled | dining | 38.07 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1265` | 2025-12-15 | settled | salary | 1661 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1271` | 2025-12-15 | settled | delivery_membership | 27 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1295` | 2025-12-16 | settled | groceries | 52.69 | cash date 2025-12-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1320` | 2025-12-17 | settled | transport | 36.86 | cash date 2025-12-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1296` | 2025-12-23 | settled | groceries | 49.9 | cash date 2025-12-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1321` | 2025-12-24 | settled | transport | 27.67 | cash date 2025-12-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1335` | 2025-12-27 | settled | dining | 49.35 | cash date 2025-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1297` | 2025-12-30 | settled | groceries | 64.42 | cash date 2025-12-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1322` | 2025-12-31 | settled | transport | 30.31 | cash date 2025-12-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1272` | 2026-01-04 | settled | rent | 435.6 | cash date 2026-01-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_11` | 2026-01-03T09:30:00Z | `` | employer | A quick update from the payroll team at Riverline Retail. Your first salary will be EUR 1661. The confirmed credit date is 2026-01-15. The money will appear after the bank posts the credit. Payroll ref EMP-0011. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_41` | full_payment | 2026-01-06:3685 | 0 | 3685 |
| `payment_option_42` | installments | 2026-01-20:207.06\|2026-02-17:207.06\|2026-03-17:207.06\|2026-04-14:207.06\|2026-05-12:207.06\|2026-06-09:207.06\|2026-07-07:207.06\|2026-08-04:207.06\|2026-09-01:207.06\|2026-09-29:207.06\|2026-10-27:207.06\|2026-11-24:207.06\|2026-12-22:207.06\|2027-01-19:207.06\|2027-02-16:207.06\|2027-03-16:207.06\|2027-04-13:207.06\|2027-05-11:207.06\|2027-06-08:207.06\|2027-07-06:207.06\|2027-08-03:207.06 | 663.26 | 4348.26 |
| `payment_option_43` | installments | 2026-01-09:187.32\|2026-02-09:187.32\|2026-03-12:187.32\|2026-04-12:187.32\|2026-05-13:187.32\|2026-06-13:187.32\|2026-07-14:187.32\|2026-08-14:187.32\|2026-09-14:187.32\|2026-10-15:187.32\|2026-11-15:187.32\|2026-12-16:187.32\|2027-01-16:187.32\|2027-02-16:187.32\|2027-03-19:187.32\|2027-04-19:187.32\|2027-05-20:187.32\|2027-06-20:187.32\|2027-07-21:187.32\|2027-08-21:187.32\|2027-09-21:187.32\|2027-10-22:187.32\|2027-11-22:187.32\|2027-12-23:187.32 | 810.68 | 4495.68 |

## request_17 — user_17

Primary category: **earliest-date computation**

Both results select installments; the discrepancy is capacity/earliest-full-payment timing rather than an option-selection failure.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 243849.58 | 274600 |
| `earliest_date_for_full_payment` | 2026-03-15 | 2026-03-01 |
| `decision_explanation` | Use 3 installments of INR 95,194.67, starting 1 March 2026. This leaves at least INR 166,100 available. | Baseline selected supplied installment option payment_option_47. |

### Financial profile

- Home currency: `INR`
- Current balance: `550379.58`
- Minimum balance: `166100`
- Protected: `debt_repayment|education|groceries|rent`; reduce: `dining`; stop: `delivery_membership|music_subscription`.
- Payment methods: `installments`; max installment months: `3`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-03-05 | recurring:rent | recurring | rent | -49600 | Inferred recurring Apartment rent transfer |
| 2026-03-09 | recurring:utilities | recurring | utilities | -10246.53 | Inferred recurring Municipal utilities |
| 2026-03-11 | recurring:education | recurring | education | -13660 | Inferred recurring Course tuition |
| 2026-03-14 | recurring:debt_repayment | recurring | debt_repayment | -30200 | Inferred recurring Credit card repayment |
| 2026-03-14 | recurring:music_subscription | recurring | music_subscription | -2055 | Inferred recurring Music subscription |
| 2026-03-15 | event_1546 | explicit | salary | 206000 | Next confirmed salary |
| 2026-03-16 | recurring:delivery_membership | recurring | delivery_membership | -1675 | Inferred recurring Food delivery membership |
| 2026-03-18 | recurring:salary | recurring | salary | 206000 | Inferred recurring Payroll credit |
| 2026-04-05 | recurring:rent | recurring | rent | -49600 | Inferred recurring Apartment rent transfer |
| 2026-04-09 | recurring:utilities | recurring | utilities | -10246.53 | Inferred recurring Municipal utilities |
| 2026-04-11 | recurring:education | recurring | education | -13660 | Inferred recurring Course tuition |
| 2026-04-14 | recurring:debt_repayment | recurring | debt_repayment | -30200 | Inferred recurring Credit card repayment |
| 2026-04-14 | recurring:music_subscription | recurring | music_subscription | -2055 | Inferred recurring Music subscription |
| 2026-04-16 | recurring:delivery_membership | recurring | delivery_membership | -1675 | Inferred recurring Food delivery membership |
| 2026-04-18 | recurring:salary | recurring | salary | 206000 | Inferred recurring Payroll credit |
| 2026-05-06 | recurring:rent | recurring | rent | -49600 | Inferred recurring Apartment rent transfer |
| 2026-05-10 | recurring:utilities | recurring | utilities | -10246.53 | Inferred recurring Municipal utilities |
| 2026-05-12 | recurring:education | recurring | education | -13660 | Inferred recurring Course tuition |
| 2026-05-15 | recurring:debt_repayment | recurring | debt_repayment | -30200 | Inferred recurring Credit card repayment |
| 2026-05-15 | recurring:music_subscription | recurring | music_subscription | -2055 | Inferred recurring Music subscription |
| 2026-05-17 | recurring:delivery_membership | recurring | delivery_membership | -1675 | Inferred recurring Food delivery membership |
| 2026-05-19 | recurring:salary | recurring | salary | 206000 | Inferred recurring Payroll credit |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1478` | 2025-09-05 | settled | groceries | 9392.54 | cash date 2025-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1504` | 2025-09-06 | settled | transport | 3913.59 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1530` | 2025-09-07 | settled | dining | 5641.06 | cash date 2025-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1479` | 2025-09-12 | settled | groceries | 7679.25 | cash date 2025-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1505` | 2025-09-13 | settled | transport | 6046.8 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1480` | 2025-09-19 | settled | groceries | 10039.54 | cash date 2025-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1506` | 2025-09-20 | settled | transport | 3972.38 | cash date 2025-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1531` | 2025-09-21 | settled | dining | 4425.44 | cash date 2025-09-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1481` | 2025-09-26 | settled | groceries | 9785.51 | cash date 2025-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1507` | 2025-09-27 | settled | transport | 5639.47 | cash date 2025-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1444` | 2025-10-02 | settled | rent | 49600 | cash date 2025-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1482` | 2025-10-03 | settled | groceries | 7187.32 | cash date 2025-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1508` | 2025-10-04 | settled | transport | 4445.42 | cash date 2025-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1532` | 2025-10-05 | settled | dining | 4695.55 | cash date 2025-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1445` | 2025-10-06 | settled | utilities | 9481.13 | cash date 2025-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1446` | 2025-10-08 | settled | education | 13660 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1483` | 2025-10-10 | settled | groceries | 8574.98 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1447` | 2025-10-11 | settled | debt_repayment | 30200 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1448` | 2025-10-11 | settled | music_subscription | 2055 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1509` | 2025-10-11 | settled | transport | 6225.69 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1449` | 2025-10-13 | settled | delivery_membership | 1675 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1443` | 2025-10-15 | settled | salary | 206000 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1484` | 2025-10-17 | settled | groceries | 11380.46 | cash date 2025-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1510` | 2025-10-18 | settled | transport | 5386.34 | cash date 2025-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1533` | 2025-10-19 | settled | dining | 5554.91 | cash date 2025-10-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1485` | 2025-10-24 | settled | groceries | 6706.54 | cash date 2025-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1511` | 2025-10-25 | settled | transport | 5421.55 | cash date 2025-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1486` | 2025-10-31 | settled | groceries | 7585.37 | cash date 2025-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1512` | 2025-11-01 | settled | transport | 5936.87 | cash date 2025-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1451` | 2025-11-02 | settled | rent | 49600 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1534` | 2025-11-02 | settled | dining | 6027.54 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1452` | 2025-11-06 | settled | utilities | 9530.77 | cash date 2025-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1487` | 2025-11-07 | settled | groceries | 7446.25 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1453` | 2025-11-08 | settled | education | 13660 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1513` | 2025-11-08 | settled | transport | 6420.35 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1454` | 2025-11-11 | settled | debt_repayment | 30200 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1455` | 2025-11-11 | settled | music_subscription | 2055 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1456` | 2025-11-13 | settled | delivery_membership | 1675 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1488` | 2025-11-14 | settled | groceries | 10300.07 | cash date 2025-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1450` | 2025-11-15 | settled | salary | 206000 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1514` | 2025-11-15 | settled | transport | 4008.13 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1535` | 2025-11-16 | settled | dining | 5593.53 | cash date 2025-11-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1489` | 2025-11-21 | settled | groceries | 8500.09 | cash date 2025-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1515` | 2025-11-22 | settled | transport | 5126.25 | cash date 2025-11-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1490` | 2025-11-28 | settled | groceries | 7237.45 | cash date 2025-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1516` | 2025-11-29 | settled | transport | 5036.82 | cash date 2025-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1536` | 2025-11-30 | settled | dining | 6839.37 | cash date 2025-11-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1458` | 2025-12-02 | settled | rent | 49600 | cash date 2025-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1491` | 2025-12-05 | settled | groceries | 8836.99 | cash date 2025-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1459` | 2025-12-06 | settled | utilities | 10246.53 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1517` | 2025-12-06 | settled | transport | 6170.7 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1460` | 2025-12-08 | settled | education | 13660 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1461` | 2025-12-11 | settled | debt_repayment | 30200 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1462` | 2025-12-11 | settled | music_subscription | 2055 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1492` | 2025-12-12 | settled | groceries | 10690 | cash date 2025-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1463` | 2025-12-13 | settled | delivery_membership | 1675 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1518` | 2025-12-13 | settled | transport | 5790.36 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1537` | 2025-12-14 | settled | dining | 6048.91 | cash date 2025-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1457` | 2025-12-15 | settled | salary | 206000 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1493` | 2025-12-19 | settled | groceries | 10432.03 | cash date 2025-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1519` | 2025-12-20 | settled | transport | 4328.91 | cash date 2025-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1494` | 2025-12-26 | settled | groceries | 11392.07 | cash date 2025-12-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1520` | 2025-12-27 | settled | transport | 5080.56 | cash date 2025-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1538` | 2025-12-28 | settled | dining | 6795.26 | cash date 2025-12-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1465` | 2026-01-02 | settled | rent | 49600 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1495` | 2026-01-02 | settled | groceries | 8124.44 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1521` | 2026-01-03 | settled | transport | 4844.94 | cash date 2026-01-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1466` | 2026-01-06 | settled | utilities | 9948.15 | cash date 2026-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1467` | 2026-01-08 | settled | education | 13660 | cash date 2026-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1496` | 2026-01-09 | settled | groceries | 11433.33 | cash date 2026-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1522` | 2026-01-10 | settled | transport | 5940.36 | cash date 2026-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1468` | 2026-01-11 | settled | debt_repayment | 30200 | cash date 2026-01-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1469` | 2026-01-11 | settled | music_subscription | 2055 | cash date 2026-01-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1539` | 2026-01-11 | settled | dining | 6797.26 | cash date 2026-01-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1470` | 2026-01-13 | settled | delivery_membership | 1675 | cash date 2026-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1464` | 2026-01-15 | settled | salary | 206000 | cash date 2026-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1497` | 2026-01-16 | settled | groceries | 7093.83 | cash date 2026-01-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1523` | 2026-01-17 | settled | transport | 6406.38 | cash date 2026-01-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1498` | 2026-01-23 | settled | groceries | 8638.54 | cash date 2026-01-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1524` | 2026-01-24 | settled | transport | 5758.89 | cash date 2026-01-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1540` | 2026-01-25 | settled | dining | 5254.41 | cash date 2026-01-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1543` | 2026-01-26 | settled | work_expense | 12360 | superseded transaction lifecycle record |
| `event_1499` | 2026-01-30 | settled | groceries | 8581.99 | cash date 2026-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1525` | 2026-01-31 | settled | transport | 4661.7 | cash date 2026-01-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1472` | 2026-02-02 | settled | rent | 49600 | cash date 2026-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1473` | 2026-02-06 | settled | utilities | 8487.15 | cash date 2026-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1500` | 2026-02-06 | settled | groceries | 11342.57 | cash date 2026-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1526` | 2026-02-07 | settled | transport | 5650.43 | cash date 2026-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1474` | 2026-02-08 | settled | education | 13660 | cash date 2026-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1541` | 2026-02-08 | settled | dining | 6688.81 | cash date 2026-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1475` | 2026-02-11 | settled | debt_repayment | 30200 | cash date 2026-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1476` | 2026-02-11 | settled | music_subscription | 2055 | cash date 2026-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1477` | 2026-02-13 | settled | delivery_membership | 1675 | cash date 2026-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1501` | 2026-02-13 | settled | groceries | 10873.47 | cash date 2026-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1527` | 2026-02-14 | settled | transport | 3902.91 | cash date 2026-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1471` | 2026-02-15 | settled | salary | 206000 | cash date 2026-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1502` | 2026-02-20 | settled | groceries | 8543.01 | cash date 2026-02-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1528` | 2026-02-21 | settled | transport | 5741.08 | cash date 2026-02-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1542` | 2026-02-22 | settled | dining | 4747.76 | cash date 2026-02-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1544` | 2026-02-26 | settled | work_expense | 12360 | cash date 2026-02-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1503` | 2026-02-27 | settled | groceries | 8716.51 | cash date 2026-02-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1545` | 2026-02-27 | settled | groceries |  | amount requires linked image review |
| `event_1529` | 2026-02-28 | settled | transport | 5372.15 | cash date 2026-02-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| `image_03` | `event_1545` | request_17 |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| `event_1544` | `event_1543` | settled | refund |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_47` | installments | 2026-03-01:95194.67\|2026-03-31:95194.67\|2026-04-30:95194.67 | 10984.01 | 285584.01 |
| `payment_option_48` | full_payment | 2026-03-01:274600 | 0 | 274600 |
| `payment_option_49` | installments | 2026-03-04:17391.33\|2026-04-04:17391.33\|2026-05-05:17391.33\|2026-06-05:17391.33\|2026-07-06:17391.33\|2026-08-06:17391.33\|2026-09-06:17391.33\|2026-10-07:17391.33\|2026-11-07:17391.33\|2026-12-08:17391.33\|2027-01-08:17391.33\|2027-02-08:17391.33\|2027-03-11:17391.33\|2027-04-11:17391.33\|2027-05-12:17391.33\|2027-06-12:17391.33\|2027-07-13:17391.33\|2027-08-13:17391.33 | 38443.94 | 313043.94 |

## request_18 — user_18

Primary category: **earliest-date computation**

The baseline finds a later date but represents wait with payment_plan=none instead of the solved future full-payment commitment, and its daily date is not conservative enough.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 462 | 787.59 |
| `payment_plan` | 2026-09-15:3246.10 | 2026-08-15:3246.1 |
| `earliest_date_for_full_payment` | 2026-09-15 | 2026-08-15 |
| `decision_explanation` | Pay EUR 3,246.10 in full on 15 September 2026. Paying earlier would take the balance below the EUR 1,400 minimum. | Baseline forecast finds a later safe full-payment date. |

### Financial profile

- Home currency: `EUR`
- Current balance: `2486`
- Minimum balance: `1400`
- Protected: `healthcare|housing|utilities`; reduce: `dining|streaming`; stop: `streaming`.
- Payment methods: `full_payment|partial_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-07-08 | recurring:insurance | recurring | insurance | -68 | Inferred recurring Household insurance |
| 2026-07-10 | recurring:streaming | recurring | streaming | -68 | Inferred recurring Family streaming plan |
| 2026-07-11 | recurring:healthcare | recurring | healthcare | -162.41 | Inferred recurring Clinic payment |
| 2026-07-15 | recurring:salary | recurring | salary | 2310 | Inferred recurring Payroll credit |
| 2026-08-03 | recurring:housing | recurring | housing | -167 | Inferred recurring Building maintenance payment |
| 2026-08-06 | recurring:utilities | recurring | utilities | -125.4 | Inferred recurring Energy provider bill |
| 2026-08-07 | recurring:insurance | recurring | insurance | -68 | Inferred recurring Household insurance |
| 2026-08-09 | recurring:streaming | recurring | streaming | -68 | Inferred recurring Family streaming plan |
| 2026-08-10 | recurring:healthcare | recurring | healthcare | -162.41 | Inferred recurring Clinic payment |
| 2026-08-14 | recurring:salary | recurring | salary | 2310 | Inferred recurring Payroll credit |
| 2026-09-02 | recurring:housing | recurring | housing | -167 | Inferred recurring Building maintenance payment |
| 2026-09-05 | recurring:utilities | recurring | utilities | -125.4 | Inferred recurring Energy provider bill |
| 2026-09-06 | recurring:insurance | recurring | insurance | -68 | Inferred recurring Household insurance |
| 2026-09-08 | recurring:streaming | recurring | streaming | -68 | Inferred recurring Family streaming plan |
| 2026-09-09 | recurring:healthcare | recurring | healthcare | -162.41 | Inferred recurring Clinic payment |
| 2026-09-13 | recurring:salary | recurring | salary | 2310 | Inferred recurring Payroll credit |
| 2026-10-02 | recurring:housing | recurring | housing | -167 | Inferred recurring Building maintenance payment |
| 2026-10-05 | recurring:utilities | recurring | utilities | -125.4 | Inferred recurring Energy provider bill |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1578` | 2026-01-12 | settled | groceries | 64.84 | cash date 2026-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1596` | 2026-01-13 | settled | transport | 36.86 | cash date 2026-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1609` | 2026-01-14 | settled | dining | 66.7 | cash date 2026-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1579` | 2026-01-22 | settled | groceries | 101.66 | cash date 2026-01-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1597` | 2026-01-27 | settled | transport | 35.48 | cash date 2026-01-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1610` | 2026-01-28 | settled | dining | 69.84 | cash date 2026-01-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1580` | 2026-02-01 | settled | groceries | 96.63 | cash date 2026-02-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1548` | 2026-02-04 | settled | housing | 167 | cash date 2026-02-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1549` | 2026-02-07 | settled | utilities | 100.59 | cash date 2026-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1550` | 2026-02-08 | settled | insurance | 68 | cash date 2026-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1552` | 2026-02-10 | settled | streaming | 68 | cash date 2026-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1598` | 2026-02-10 | settled | transport | 54.53 | cash date 2026-02-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1551` | 2026-02-11 | settled | healthcare | 164.1 | cash date 2026-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1581` | 2026-02-11 | settled | groceries | 101.08 | cash date 2026-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1611` | 2026-02-11 | settled | dining | 92.92 | cash date 2026-02-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1547` | 2026-02-15 | settled | salary | 2310 | cash date 2026-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1582` | 2026-02-21 | settled | groceries | 87.39 | cash date 2026-02-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1599` | 2026-02-24 | settled | transport | 53.15 | cash date 2026-02-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1612` | 2026-02-25 | settled | dining | 98.51 | cash date 2026-02-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1583` | 2026-03-03 | settled | groceries | 106.43 | cash date 2026-03-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1554` | 2026-03-04 | settled | housing | 167 | cash date 2026-03-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1555` | 2026-03-07 | settled | utilities | 101.24 | cash date 2026-03-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1556` | 2026-03-08 | settled | insurance | 68 | cash date 2026-03-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1558` | 2026-03-10 | settled | streaming | 68 | cash date 2026-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1600` | 2026-03-10 | settled | transport | 38.59 | cash date 2026-03-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1557` | 2026-03-11 | settled | healthcare | 150.18 | cash date 2026-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1613` | 2026-03-11 | settled | dining | 108.96 | cash date 2026-03-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1584` | 2026-03-13 | settled | groceries | 66.3 | cash date 2026-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1553` | 2026-03-15 | settled | salary | 2310 | cash date 2026-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1585` | 2026-03-23 | settled | groceries | 108.09 | cash date 2026-03-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1601` | 2026-03-24 | settled | transport | 52.9 | cash date 2026-03-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1614` | 2026-03-25 | settled | dining | 75.46 | cash date 2026-03-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1586` | 2026-04-02 | settled | groceries | 110.8 | cash date 2026-04-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1560` | 2026-04-04 | settled | housing | 167 | cash date 2026-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1561` | 2026-04-07 | settled | utilities | 125.4 | cash date 2026-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1602` | 2026-04-07 | settled | transport | 36.49 | cash date 2026-04-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1562` | 2026-04-08 | settled | insurance | 68 | cash date 2026-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1615` | 2026-04-08 | settled | dining | 66.71 | cash date 2026-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1564` | 2026-04-10 | settled | streaming | 68 | cash date 2026-04-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1563` | 2026-04-11 | settled | healthcare | 152.41 | cash date 2026-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1587` | 2026-04-12 | settled | groceries | 82.18 | cash date 2026-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1559` | 2026-04-15 | settled | salary | 2310 | cash date 2026-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1603` | 2026-04-21 | settled | transport | 47.5 | cash date 2026-04-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1588` | 2026-04-22 | settled | groceries | 94.02 | cash date 2026-04-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1616` | 2026-04-22 | settled | dining | 103.86 | cash date 2026-04-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1589` | 2026-05-02 | settled | groceries | 115 | cash date 2026-05-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1566` | 2026-05-04 | settled | housing | 167 | cash date 2026-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1604` | 2026-05-05 | settled | transport | 50.57 | cash date 2026-05-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1617` | 2026-05-06 | settled | dining | 81.05 | cash date 2026-05-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1567` | 2026-05-07 | settled | utilities | 121.67 | cash date 2026-05-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1568` | 2026-05-08 | settled | insurance | 68 | cash date 2026-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1570` | 2026-05-10 | settled | streaming | 68 | cash date 2026-05-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1569` | 2026-05-11 | settled | healthcare | 162.41 | cash date 2026-05-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1590` | 2026-05-12 | settled | groceries | 83.94 | cash date 2026-05-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1565` | 2026-05-15 | settled | salary | 2310 | cash date 2026-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1605` | 2026-05-19 | settled | transport | 34.87 | cash date 2026-05-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1618` | 2026-05-20 | settled | dining | 101.82 | cash date 2026-05-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1591` | 2026-05-22 | settled | groceries | 87.91 | cash date 2026-05-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1592` | 2026-06-01 | settled | groceries | 71.92 | cash date 2026-06-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1606` | 2026-06-02 | settled | transport | 36.29 | cash date 2026-06-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1619` | 2026-06-03 | settled | dining | 62.87 | cash date 2026-06-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1572` | 2026-06-04 | settled | housing | 167 | cash date 2026-06-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1573` | 2026-06-07 | settled | utilities | 107.43 | cash date 2026-06-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1574` | 2026-06-08 | settled | insurance | 68 | cash date 2026-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1576` | 2026-06-10 | settled | streaming | 68 | cash date 2026-06-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1575` | 2026-06-11 | settled | healthcare | 147.96 | cash date 2026-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1593` | 2026-06-11 | settled | groceries | 101.9 | cash date 2026-06-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1571` | 2026-06-15 | settled | salary | 2310 | cash date 2026-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1607` | 2026-06-16 | settled | transport | 49.04 | cash date 2026-06-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1620` | 2026-06-17 | settled | dining | 82.67 | cash date 2026-06-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1594` | 2026-06-21 | settled | groceries | 90.08 | cash date 2026-06-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1608` | 2026-06-30 | settled | transport | 43.81 | cash date 2026-06-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1595` | 2026-07-01 | settled | groceries | 111.41 | cash date 2026-07-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1621` | 2026-07-01 | settled | dining | 101.88 | cash date 2026-07-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1577` | 2026-07-04 | settled | housing | 167 | cash date 2026-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_13` | 2026-07-01T09:30:00Z | `` | bank | There’s an update from Summit Bank on your recent account activity. The matching debit and credit came from a transfer between your two accounts. Both accounts are registered under the same account holder. Both entries will remain visible in your transaction history. Txn ref BAN-0013. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_50` | full_payment | 2026-07-07:3246.1 | 0 | 3246.1 |
| `payment_option_51` | installments | 2026-07-14:182.4\|2026-08-11:182.4\|2026-09-08:182.4\|2026-10-06:182.4\|2026-11-03:182.4\|2026-12-01:182.4\|2026-12-29:182.4\|2027-01-26:182.4\|2027-02-23:182.4\|2027-03-23:182.4\|2027-04-20:182.4\|2027-05-18:182.4\|2027-06-15:182.4\|2027-07-13:182.4\|2027-08-10:182.4\|2027-09-07:182.4\|2027-10-05:182.4\|2027-11-02:182.4\|2027-11-30:182.4\|2027-12-28:182.4\|2028-01-25:182.4 | 584.3 | 3830.4 |

## request_19 — user_19

Primary category: **partial-payment eligibility and timing**

The solved plan uses a two-payment schedule; the baseline needs a payment-date-specific capacity calculation for both the first amount and the remaining amount.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 28820 | 39660 |
| `recommended_payment_method` | partial_payment | installments |
| `payment_plan` | 2024-09-04:28820\|2024-09-15:10840 | 2024-09-04:20623.2\|2024-10-02:20623.2 |
| `earliest_date_for_full_payment` | 2024-09-15 | 2024-09-04 |
| `decision_explanation` | Pay INR 28,820 today and the remaining INR 10,840 on 15 September 2024. This completes the full request and keeps the INR 92,800 minimum protected. | Baseline selected supplied installment option payment_option_53. |

### Financial profile

- Home currency: `INR`
- Current balance: `199545`
- Minimum balance: `92800`
- Protected: `family_support|groceries|healthcare|rent`; reduce: `shopping`; stop: `cloud_storage`.
- Payment methods: `installments|partial_payment`; max installment months: `2`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-09-07 | recurring:utilities | recurring | utilities | -6129.19 | Inferred recurring Municipal utilities |
| 2024-09-11 | recurring:healthcare | recurring | healthcare | -8645.36 | Inferred recurring Clinic payment |
| 2024-09-12 | recurring:debt_repayment | recurring | debt_repayment | -11850 | Inferred recurring Loan repayment |
| 2024-09-12 | recurring:groceries | recurring | groceries | -6070.85 | Inferred recurring Fresh food shop |
| 2024-09-13 | recurring:shopping | recurring | shopping | -6069.58 | Inferred recurring Clothing and household items |
| 2024-09-13 | recurring:cloud_storage | recurring | cloud_storage | -395 | Inferred recurring Online backup subscription |
| 2024-09-14 | recurring:family_support | recurring | family_support | -12650 | Inferred recurring Childcare contribution |
| 2024-09-14 | recurring:salary | recurring | salary | 131000 | Inferred recurring Payroll credit |
| 2024-10-03 | recurring:rent | recurring | rent | -36100 | Inferred recurring Residential rent payment |
| 2024-10-06 | recurring:groceries | recurring | groceries | -6070.85 | Inferred recurring Fresh food shop |
| 2024-10-07 | recurring:utilities | recurring | utilities | -6129.19 | Inferred recurring Municipal utilities |
| 2024-10-11 | recurring:healthcare | recurring | healthcare | -8645.36 | Inferred recurring Clinic payment |
| 2024-10-12 | recurring:debt_repayment | recurring | debt_repayment | -11850 | Inferred recurring Loan repayment |
| 2024-10-13 | recurring:shopping | recurring | shopping | -6069.58 | Inferred recurring Clothing and household items |
| 2024-10-13 | recurring:cloud_storage | recurring | cloud_storage | -395 | Inferred recurring Online backup subscription |
| 2024-10-14 | recurring:family_support | recurring | family_support | -12650 | Inferred recurring Childcare contribution |
| 2024-10-14 | recurring:salary | recurring | salary | 131000 | Inferred recurring Payroll credit |
| 2024-10-30 | recurring:groceries | recurring | groceries | -6070.85 | Inferred recurring Fresh food shop |
| 2024-11-02 | recurring:rent | recurring | rent | -36100 | Inferred recurring Residential rent payment |
| 2024-11-06 | recurring:utilities | recurring | utilities | -6129.19 | Inferred recurring Municipal utilities |
| 2024-11-10 | recurring:healthcare | recurring | healthcare | -8645.36 | Inferred recurring Clinic payment |
| 2024-11-11 | recurring:debt_repayment | recurring | debt_repayment | -11850 | Inferred recurring Loan repayment |
| 2024-11-12 | recurring:shopping | recurring | shopping | -6069.58 | Inferred recurring Clothing and household items |
| 2024-11-12 | recurring:cloud_storage | recurring | cloud_storage | -395 | Inferred recurring Online backup subscription |
| 2024-11-13 | recurring:family_support | recurring | family_support | -12650 | Inferred recurring Childcare contribution |
| 2024-11-13 | recurring:salary | recurring | salary | 131000 | Inferred recurring Payroll credit |
| 2024-11-23 | recurring:groceries | recurring | groceries | -6070.85 | Inferred recurring Fresh food shop |
| 2024-12-02 | recurring:rent | recurring | rent | -36100 | Inferred recurring Residential rent payment |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1662` | 2024-03-13 | settled | groceries | 4418.91 | cash date 2024-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1687` | 2024-03-14 | settled | transport | 3054.24 | cash date 2024-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1663` | 2024-03-20 | settled | groceries | 4871.72 | cash date 2024-03-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1664` | 2024-03-27 | settled | groceries | 6070.85 | cash date 2024-03-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1688` | 2024-03-28 | settled | transport | 3298.25 | cash date 2024-03-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1665` | 2024-04-03 | settled | groceries | 5452.26 | cash date 2024-04-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1623` | 2024-04-04 | settled | rent | 36100 | cash date 2024-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1624` | 2024-04-08 | settled | utilities | 6141.28 | cash date 2024-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1666` | 2024-04-10 | settled | groceries | 5912.83 | cash date 2024-04-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1689` | 2024-04-11 | settled | transport | 3476.92 | cash date 2024-04-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1626` | 2024-04-12 | settled | healthcare | 8946.09 | cash date 2024-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1625` | 2024-04-13 | settled | debt_repayment | 11850 | cash date 2024-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1628` | 2024-04-14 | settled | cloud_storage | 395 | cash date 2024-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1629` | 2024-04-14 | settled | shopping | 6302.66 | cash date 2024-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1622` | 2024-04-15 | settled | salary | 131000 | cash date 2024-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1627` | 2024-04-15 | settled | family_support | 12650 | cash date 2024-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1667` | 2024-04-17 | settled | groceries | 3877.79 | cash date 2024-04-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1668` | 2024-04-24 | settled | groceries | 4056.71 | cash date 2024-04-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1690` | 2024-04-25 | settled | transport | 3849.5 | cash date 2024-04-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1669` | 2024-05-01 | settled | groceries | 4744.13 | cash date 2024-05-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1631` | 2024-05-04 | settled | rent | 36100 | cash date 2024-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1632` | 2024-05-08 | settled | utilities | 5525.82 | cash date 2024-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1670` | 2024-05-08 | settled | groceries | 3593.25 | cash date 2024-05-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1691` | 2024-05-09 | settled | transport | 2640.96 | cash date 2024-05-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1634` | 2024-05-12 | settled | healthcare | 9619.88 | cash date 2024-05-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1633` | 2024-05-13 | settled | debt_repayment | 11850 | cash date 2024-05-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1636` | 2024-05-14 | settled | cloud_storage | 395 | cash date 2024-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1637` | 2024-05-14 | settled | shopping | 5593.2 | cash date 2024-05-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1630` | 2024-05-15 | settled | salary | 131000 | cash date 2024-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1635` | 2024-05-15 | settled | family_support | 12650 | cash date 2024-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1671` | 2024-05-15 | settled | groceries | 3852.58 | cash date 2024-05-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1672` | 2024-05-22 | settled | groceries | 5406.2 | cash date 2024-05-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1692` | 2024-05-23 | settled | transport | 3432.81 | cash date 2024-05-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1673` | 2024-05-29 | settled | groceries | 5542.84 | cash date 2024-05-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1639` | 2024-06-04 | settled | rent | 36100 | cash date 2024-06-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1674` | 2024-06-05 | settled | groceries | 4738.95 | cash date 2024-06-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1693` | 2024-06-06 | settled | transport | 2610.24 | cash date 2024-06-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1640` | 2024-06-08 | settled | utilities | 6029.9 | cash date 2024-06-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1642` | 2024-06-12 | settled | healthcare | 8335.2 | cash date 2024-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1675` | 2024-06-12 | settled | groceries | 3575.19 | cash date 2024-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1641` | 2024-06-13 | settled | debt_repayment | 11850 | cash date 2024-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1644` | 2024-06-14 | settled | cloud_storage | 395 | cash date 2024-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1645` | 2024-06-14 | settled | shopping | 6069.58 | cash date 2024-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1638` | 2024-06-15 | settled | salary | 131000 | cash date 2024-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1643` | 2024-06-15 | settled | family_support | 12650 | cash date 2024-06-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1676` | 2024-06-19 | settled | groceries | 5146.94 | cash date 2024-06-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1694` | 2024-06-20 | settled | transport | 2788.22 | cash date 2024-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1677` | 2024-06-26 | settled | groceries | 5908.15 | cash date 2024-06-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1678` | 2024-07-03 | settled | groceries | 4444.74 | cash date 2024-07-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1647` | 2024-07-04 | settled | rent | 36100 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1695` | 2024-07-04 | settled | transport | 3242.46 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1648` | 2024-07-08 | settled | utilities | 5951.99 | cash date 2024-07-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1679` | 2024-07-10 | settled | groceries | 4667.68 | cash date 2024-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1650` | 2024-07-12 | settled | healthcare | 8496.34 | cash date 2024-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1649` | 2024-07-13 | settled | debt_repayment | 11850 | cash date 2024-07-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1652` | 2024-07-14 | settled | cloud_storage | 395 | cash date 2024-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1653` | 2024-07-14 | settled | shopping | 5772.78 | cash date 2024-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1646` | 2024-07-15 | settled | salary | 131000 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1651` | 2024-07-15 | settled | family_support | 12650 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1680` | 2024-07-17 | settled | groceries | 4493.39 | cash date 2024-07-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1696` | 2024-07-18 | settled | transport | 3659.94 | cash date 2024-07-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1681` | 2024-07-24 | settled | groceries | 5184.21 | cash date 2024-07-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1682` | 2024-07-31 | settled | groceries | 3460.53 | cash date 2024-07-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1697` | 2024-08-01 | settled | transport | 2759.93 | cash date 2024-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1655` | 2024-08-04 | settled | rent | 36100 | cash date 2024-08-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1683` | 2024-08-07 | settled | groceries | 6005.09 | cash date 2024-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1656` | 2024-08-08 | settled | utilities | 6129.19 | cash date 2024-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1658` | 2024-08-12 | settled | healthcare | 8645.36 | cash date 2024-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1657` | 2024-08-13 | settled | debt_repayment | 11850 | cash date 2024-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1660` | 2024-08-14 | settled | cloud_storage | 395 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1661` | 2024-08-14 | settled | shopping | 5431.12 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1684` | 2024-08-14 | settled | groceries | 4963.39 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1654` | 2024-08-15 | settled | salary | 131000 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1659` | 2024-08-15 | settled | family_support | 12650 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1698` | 2024-08-15 | settled | transport | 2462.29 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1685` | 2024-08-21 | settled | groceries | 4864.04 | cash date 2024-08-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1686` | 2024-08-28 | settled | groceries | 4068.18 | cash date 2024-08-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1699` | 2024-08-29 | settled | transport | 2765.93 | cash date 2024-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1700` | 2024-09-03 | settled | groceries |  | amount requires linked image review |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| `image_04` | `event_1700` | request_19 |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_52` | full_payment | 2024-09-04:39660 | 0 | 39660 |
| `payment_option_53` | installments | 2024-09-04:20623.2\|2024-10-02:20623.2 | 1586.4 | 41246.4 |
| `payment_option_54` | installments | 2024-09-10:14013.2\|2024-10-11:14013.2\|2024-11-11:14013.2 | 2379.6 | 42039.6 |

## request_20 — user_20

Primary category: **cancellations or amendments from messages**

Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 5400 | 24503.8 |
| `decision_explanation` | Do not make this payment by 22 February 2026. None of the available options keeps the INR 64,500 minimum protected. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `INR`
- Current balance: `102609.05`
- Minimum balance: `64500`
- Protected: `education|housing|utilities`; reduce: `dining|entertainment`; stop: `cloud_storage`.
- Payment methods: `full_payment|installments|partial_payment`; max installment months: `11`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-02-08 | recurring:healthcare | recurring | healthcare | -6654.33 | Inferred recurring Family healthcare expense |
| 2026-02-08 | event_1787 | explicit | shopping | -4470 | Pending online order charge |
| 2026-02-10 | recurring:cloud_storage | recurring | cloud_storage | -365 | Inferred recurring Shared storage plan |
| 2026-02-12 | recurring:entertainment | recurring | entertainment | -2115.92 | Inferred recurring Cinema and events |
| 2026-02-14 | recurring:salary | recurring | salary | 108000 | Inferred recurring Payroll credit |
| 2026-03-05 | recurring:housing | recurring | housing | -7950 | Inferred recurring Home association fee |
| 2026-03-08 | recurring:education | recurring | education | -8740 | Inferred recurring School fee payment |
| 2026-03-08 | recurring:utilities | recurring | utilities | -7769.87 | Inferred recurring Municipal utilities |
| 2026-03-09 | recurring:insurance | recurring | insurance | -3290 | Inferred recurring Household insurance |
| 2026-03-10 | recurring:healthcare | recurring | healthcare | -6654.33 | Inferred recurring Family healthcare expense |
| 2026-03-12 | recurring:cloud_storage | recurring | cloud_storage | -365 | Inferred recurring Shared storage plan |
| 2026-03-14 | recurring:entertainment | recurring | entertainment | -2115.92 | Inferred recurring Cinema and events |
| 2026-03-16 | recurring:salary | recurring | salary | 108000 | Inferred recurring Payroll credit |
| 2026-04-05 | recurring:housing | recurring | housing | -7950 | Inferred recurring Home association fee |
| 2026-04-07 | recurring:education | recurring | education | -8740 | Inferred recurring School fee payment |
| 2026-04-08 | recurring:utilities | recurring | utilities | -7769.87 | Inferred recurring Municipal utilities |
| 2026-04-09 | recurring:healthcare | recurring | healthcare | -6654.33 | Inferred recurring Family healthcare expense |
| 2026-04-09 | recurring:insurance | recurring | insurance | -3290 | Inferred recurring Household insurance |
| 2026-04-11 | recurring:cloud_storage | recurring | cloud_storage | -365 | Inferred recurring Shared storage plan |
| 2026-04-13 | recurring:entertainment | recurring | entertainment | -2115.92 | Inferred recurring Cinema and events |
| 2026-04-15 | recurring:salary | recurring | salary | 108000 | Inferred recurring Payroll credit |
| 2026-05-06 | recurring:housing | recurring | housing | -7950 | Inferred recurring Home association fee |
| 2026-05-07 | recurring:education | recurring | education | -8740 | Inferred recurring School fee payment |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1744` | 2025-08-13 | settled | groceries | 3866.5 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1762` | 2025-08-14 | settled | transport | 2046.25 | cash date 2025-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1775` | 2025-08-15 | settled | dining | 3150.77 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1745` | 2025-08-23 | settled | groceries | 3724.49 | cash date 2025-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1763` | 2025-08-28 | settled | transport | 2060.7 | cash date 2025-08-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1702` | 2025-09-02 | settled | housing | 7950 | cash date 2025-09-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1746` | 2025-09-02 | settled | groceries | 3127.16 | cash date 2025-09-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1703` | 2025-09-05 | settled | utilities | 7784.29 | cash date 2025-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1776` | 2025-09-05 | settled | dining | 3075.11 | cash date 2025-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1704` | 2025-09-06 | settled | insurance | 3290 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1705` | 2025-09-07 | settled | education | 8740 | cash date 2025-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1706` | 2025-09-09 | settled | healthcare | 5968.18 | cash date 2025-09-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1708` | 2025-09-11 | settled | cloud_storage | 365 | cash date 2025-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1764` | 2025-09-11 | settled | transport | 2195.41 | cash date 2025-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1747` | 2025-09-12 | settled | groceries | 4104.17 | cash date 2025-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1707` | 2025-09-13 | settled | entertainment | 2298.76 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1701` | 2025-09-15 | settled | salary | 108000 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1748` | 2025-09-22 | settled | groceries | 2968.61 | cash date 2025-09-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1765` | 2025-09-25 | settled | transport | 2632 | cash date 2025-09-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1777` | 2025-09-26 | settled | dining | 3365.58 | cash date 2025-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1710` | 2025-10-02 | settled | housing | 7950 | cash date 2025-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1749` | 2025-10-02 | settled | groceries | 4660.33 | cash date 2025-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1711` | 2025-10-05 | settled | utilities | 7977.68 | cash date 2025-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1712` | 2025-10-06 | settled | insurance | 3290 | cash date 2025-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1713` | 2025-10-07 | settled | education | 8740 | cash date 2025-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1714` | 2025-10-09 | settled | healthcare | 6648.5 | cash date 2025-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1766` | 2025-10-09 | settled | transport | 3063.34 | cash date 2025-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1716` | 2025-10-11 | settled | cloud_storage | 365 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1750` | 2025-10-12 | settled | groceries | 4109.13 | cash date 2025-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1715` | 2025-10-13 | settled | entertainment | 2279.67 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1709` | 2025-10-15 | settled | salary | 108000 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1778` | 2025-10-17 | settled | dining | 4270.04 | cash date 2025-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1751` | 2025-10-22 | settled | groceries | 2812.26 | cash date 2025-10-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1767` | 2025-10-23 | settled | transport | 2359.03 | cash date 2025-10-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1752` | 2025-11-01 | settled | groceries | 3525.04 | cash date 2025-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1718` | 2025-11-02 | settled | housing | 7950 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1719` | 2025-11-05 | settled | utilities | 8058.75 | cash date 2025-11-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1720` | 2025-11-06 | settled | insurance | 3290 | cash date 2025-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1768` | 2025-11-06 | settled | transport | 2628.75 | cash date 2025-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1721` | 2025-11-07 | settled | education | 8740 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1779` | 2025-11-07 | settled | dining | 2857.78 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1722` | 2025-11-09 | settled | healthcare | 5907.73 | cash date 2025-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1724` | 2025-11-11 | settled | cloud_storage | 365 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1753` | 2025-11-11 | settled | groceries | 3386.09 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1723` | 2025-11-13 | settled | entertainment | 2115.92 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1717` | 2025-11-15 | settled | salary | 108000 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1769` | 2025-11-20 | settled | transport | 2836.95 | cash date 2025-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1754` | 2025-11-21 | settled | groceries | 3796.24 | cash date 2025-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1780` | 2025-11-28 | settled | dining | 4308.23 | cash date 2025-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1755` | 2025-12-01 | settled | groceries | 3016.03 | cash date 2025-12-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1726` | 2025-12-02 | settled | housing | 7950 | cash date 2025-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1770` | 2025-12-04 | settled | transport | 2570.15 | cash date 2025-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1727` | 2025-12-05 | settled | utilities | 6848.62 | cash date 2025-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1728` | 2025-12-06 | settled | insurance | 3290 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1729` | 2025-12-07 | settled | education | 8740 | cash date 2025-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1730` | 2025-12-09 | settled | healthcare | 6505.49 | cash date 2025-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1732` | 2025-12-11 | settled | cloud_storage | 365 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1756` | 2025-12-11 | settled | groceries | 4683.37 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1731` | 2025-12-13 | settled | entertainment | 1949.86 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1725` | 2025-12-15 | settled | salary | 108000 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1771` | 2025-12-18 | settled | transport | 3145.95 | cash date 2025-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1781` | 2025-12-19 | settled | dining | 2629.91 | cash date 2025-12-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1757` | 2025-12-21 | settled | groceries | 3067.82 | cash date 2025-12-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1758` | 2025-12-31 | settled | groceries | 3588.1 | cash date 2025-12-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1772` | 2026-01-01 | settled | transport | 2838.14 | cash date 2026-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1734` | 2026-01-02 | settled | housing | 7950 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1735` | 2026-01-05 | settled | utilities | 7551.74 | cash date 2026-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1736` | 2026-01-06 | settled | insurance | 3290 | cash date 2026-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1737` | 2026-01-07 | settled | education | 8740 | cash date 2026-01-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1738` | 2026-01-09 | settled | healthcare | 6654.33 | cash date 2026-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1782` | 2026-01-09 | settled | dining | 3352.75 | cash date 2026-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1759` | 2026-01-10 | settled | groceries | 3752.77 | cash date 2026-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1740` | 2026-01-11 | settled | cloud_storage | 365 | cash date 2026-01-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1739` | 2026-01-13 | settled | entertainment | 2097.15 | cash date 2026-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1733` | 2026-01-15 | settled | salary | 108000 | cash date 2026-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1773` | 2026-01-15 | settled | transport | 3150.25 | cash date 2026-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1784` | 2026-01-15 | settled | shopping | 8640 | superseded transaction lifecycle record |
| `event_1760` | 2026-01-20 | settled | groceries | 3702.16 | cash date 2026-01-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1774` | 2026-01-29 | settled | transport | 3243.84 | cash date 2026-01-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1761` | 2026-01-30 | settled | groceries | 4719.22 | cash date 2026-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1783` | 2026-01-30 | settled | dining | 3803.95 | cash date 2026-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1741` | 2026-02-02 | settled | housing | 7950 | cash date 2026-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1742` | 2026-02-05 | settled | utilities | 7769.87 | cash date 2026-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1743` | 2026-02-06 | settled | insurance | 3290 | cash date 2026-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1786` | 2026-02-09 | pending | utilities |  | amount requires linked image review |
| `event_1785` | 2026-02-14 | pending | shopping |  | explicit statement that the related credit is not yet available; evidence message_14 |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_14` | 2026-02-06T09:30:00Z | `event_1785` | merchant | CartLane has new information about your payment or refund. Your refund has been initiated but has not reached your account yet. We’ll send another update when the credit is completed. Order ref MER-0014. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| `image_05` | `event_1786` | request_20 |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| `event_1785` | `event_1784` | pending | refund |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_55` | full_payment | 2026-02-07:303700 | 0 | 303700 |
| `payment_option_56` | installments | 2026-02-07:19234.33\|2026-03-10:19234.33\|2026-04-10:19234.33\|2026-05-11:19234.33\|2026-06-11:19234.33\|2026-07-12:19234.33\|2026-08-12:19234.33\|2026-09-12:19234.33\|2026-10-13:19234.33\|2026-11-13:19234.33\|2026-12-14:19234.33\|2027-01-14:19234.33\|2027-02-14:19234.33\|2027-03-17:19234.33\|2027-04-17:19234.33\|2027-05-18:19234.33\|2027-06-18:19234.33\|2027-07-19:19234.33 | 42517.94 | 346217.94 |

## request_21 — user_21

Primary category: **flexible spending changes**

The solved plan changes flexible recurring spending, while the baseline never models authorized stop/reduce actions or their resulting forecast cash flows.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 1543.35 | 1574.4 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `payment_plan` | 2026-04-03:1574.40 | 2026-04-03:1574.4 |
| `earliest_date_for_full_payment` | 2026-04-15 | 2026-04-03 |
| `spending_changes_needed` | stop:event_1815\|reduce_to:event_1816:23.50 | none |
| `decision_explanation` | Stop the online backup subscription and reduce the streaming subscription to USD 23.50, then pay USD 1,574.40 today. This leaves at least USD 1,800 available. | Baseline forecast keeps the balance above the minimum after full payment. |

### Financial profile

- Home currency: `USD`
- Current balance: `3911.35`
- Minimum balance: `1800`
- Protected: `groceries|rent|utilities`; reduce: `dining|shopping|streaming`; stop: `cloud_storage|streaming`.
- Payment methods: `full_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-04-05 | recurring:utilities | recurring | utilities | -124.08 | Inferred recurring Municipal utilities |
| 2026-04-05 | event_1857 | explicit | transport | -53 | Pending fuel authorization |
| 2026-04-08 | recurring:streaming | recurring | streaming | -47 | Inferred recurring Streaming subscription |
| 2026-04-11 | recurring:shopping | recurring | shopping | -126.38 | Inferred recurring Monthly shopping spend |
| 2026-04-11 | recurring:cloud_storage | recurring | cloud_storage | -11 | Inferred recurring Online backup subscription |
| 2026-04-14 | recurring:salary | recurring | salary | 2256 | Inferred recurring Payroll credit |
| 2026-04-15 | event_1858 | explicit | salary | 2256 | Next confirmed salary |
| 2026-05-03 | recurring:rent | recurring | rent | -718.8 | Inferred recurring Residential rent payment |
| 2026-05-05 | recurring:utilities | recurring | utilities | -124.08 | Inferred recurring Municipal utilities |
| 2026-05-08 | recurring:streaming | recurring | streaming | -47 | Inferred recurring Streaming subscription |
| 2026-05-11 | recurring:shopping | recurring | shopping | -126.38 | Inferred recurring Monthly shopping spend |
| 2026-05-11 | recurring:cloud_storage | recurring | cloud_storage | -11 | Inferred recurring Online backup subscription |
| 2026-05-14 | recurring:salary | recurring | salary | 2256 | Inferred recurring Payroll credit |
| 2026-06-03 | recurring:rent | recurring | rent | -718.8 | Inferred recurring Residential rent payment |
| 2026-06-04 | recurring:utilities | recurring | utilities | -124.08 | Inferred recurring Municipal utilities |
| 2026-06-07 | recurring:streaming | recurring | streaming | -47 | Inferred recurring Streaming subscription |
| 2026-06-10 | recurring:shopping | recurring | shopping | -126.38 | Inferred recurring Monthly shopping spend |
| 2026-06-10 | recurring:cloud_storage | recurring | cloud_storage | -11 | Inferred recurring Online backup subscription |
| 2026-06-13 | recurring:salary | recurring | salary | 2256 | Inferred recurring Payroll credit |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1819` | 2025-10-08 | settled | groceries | 65.93 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1837` | 2025-10-09 | settled | transport | 38.96 | cash date 2025-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1846` | 2025-10-10 | settled | dining | 82.43 | cash date 2025-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1820` | 2025-10-18 | settled | groceries | 104.23 | cash date 2025-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1821` | 2025-10-28 | settled | groceries | 92.12 | cash date 2025-10-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1838` | 2025-10-30 | settled | transport | 37.19 | cash date 2025-10-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1847` | 2025-10-31 | settled | dining | 68.28 | cash date 2025-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1789` | 2025-11-02 | settled | rent | 718.8 | cash date 2025-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1790` | 2025-11-06 | settled | utilities | 115.31 | cash date 2025-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1822` | 2025-11-07 | settled | groceries | 68.82 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1792` | 2025-11-09 | settled | streaming | 47 | cash date 2025-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1791` | 2025-11-12 | settled | cloud_storage | 11 | cash date 2025-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1793` | 2025-11-12 | settled | shopping | 133.38 | cash date 2025-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1788` | 2025-11-15 | settled | salary | 2256 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1823` | 2025-11-17 | settled | groceries | 95.62 | cash date 2025-11-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1839` | 2025-11-20 | settled | transport | 34.52 | cash date 2025-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1848` | 2025-11-21 | settled | dining | 85.96 | cash date 2025-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1824` | 2025-11-27 | settled | groceries | 104.19 | cash date 2025-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1795` | 2025-12-02 | settled | rent | 718.8 | cash date 2025-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1796` | 2025-12-06 | settled | utilities | 123.72 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1825` | 2025-12-07 | settled | groceries | 72.06 | cash date 2025-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1798` | 2025-12-09 | settled | streaming | 47 | cash date 2025-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1840` | 2025-12-11 | settled | transport | 50 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1797` | 2025-12-12 | settled | cloud_storage | 11 | cash date 2025-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1799` | 2025-12-12 | settled | shopping | 115.86 | cash date 2025-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1849` | 2025-12-12 | settled | dining | 60.18 | cash date 2025-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1794` | 2025-12-15 | settled | salary | 2256 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1826` | 2025-12-17 | settled | groceries | 101.34 | cash date 2025-12-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1827` | 2025-12-27 | settled | groceries | 84.7 | cash date 2025-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1855` | 2025-12-29 | settled | investment | 676.8 | superseded transaction lifecycle record |
| `event_1841` | 2026-01-01 | settled | transport | 40.66 | cash date 2026-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1801` | 2026-01-02 | settled | rent | 718.8 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1850` | 2026-01-02 | settled | dining | 88.07 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1802` | 2026-01-06 | settled | utilities | 120.59 | cash date 2026-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1828` | 2026-01-06 | settled | groceries | 77.2 | cash date 2026-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1804` | 2026-01-09 | settled | streaming | 47 | cash date 2026-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1803` | 2026-01-12 | settled | cloud_storage | 11 | cash date 2026-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1805` | 2026-01-12 | settled | shopping | 120.74 | cash date 2026-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1800` | 2026-01-15 | settled | salary | 2256 | cash date 2026-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1829` | 2026-01-16 | settled | groceries | 79 | cash date 2026-01-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1842` | 2026-01-22 | settled | transport | 33.38 | cash date 2026-01-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1851` | 2026-01-23 | settled | dining | 100.63 | cash date 2026-01-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1830` | 2026-01-26 | settled | groceries | 66.13 | cash date 2026-01-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1807` | 2026-02-02 | settled | rent | 718.8 | cash date 2026-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1831` | 2026-02-05 | settled | groceries | 85.9 | cash date 2026-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1808` | 2026-02-06 | settled | utilities | 122.18 | cash date 2026-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1810` | 2026-02-09 | settled | streaming | 47 | cash date 2026-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1809` | 2026-02-12 | settled | cloud_storage | 11 | cash date 2026-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1811` | 2026-02-12 | settled | shopping | 115.71 | cash date 2026-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1843` | 2026-02-12 | settled | transport | 51.42 | cash date 2026-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1852` | 2026-02-13 | settled | dining | 97.67 | cash date 2026-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1806` | 2026-02-15 | settled | salary | 2256 | cash date 2026-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1832` | 2026-02-15 | settled | groceries | 90.57 | cash date 2026-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1833` | 2026-02-25 | settled | groceries | 71.22 | cash date 2026-02-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1813` | 2026-03-02 | settled | rent | 718.8 | cash date 2026-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1844` | 2026-03-05 | settled | transport | 47.84 | cash date 2026-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1814` | 2026-03-06 | settled | utilities | 124.08 | cash date 2026-03-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1853` | 2026-03-06 | settled | dining | 98.39 | cash date 2026-03-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1834` | 2026-03-07 | settled | groceries | 70.98 | cash date 2026-03-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1816` | 2026-03-09 | settled | streaming | 47 | cash date 2026-03-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1815` | 2026-03-12 | settled | cloud_storage | 11 | cash date 2026-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1817` | 2026-03-12 | settled | shopping | 126.38 | cash date 2026-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1812` | 2026-03-15 | settled | salary | 2256 | cash date 2026-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1835` | 2026-03-17 | settled | groceries | 77.75 | cash date 2026-03-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1845` | 2026-03-26 | settled | transport | 36.86 | cash date 2026-03-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1836` | 2026-03-27 | settled | groceries | 97.55 | cash date 2026-03-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1854` | 2026-03-27 | settled | dining | 69.31 | cash date 2026-03-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1856` | 2026-04-01 | unrealized | investment |  | unrealized event |
| `event_1818` | 2026-04-02 | settled | rent | 718.8 | cash date 2026-04-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| `event_1856` | `event_1855` | unrealized | investment_valuation |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_57` | full_payment | 2026-04-03:1574.4 | 0 | 1574.4 |
| `payment_option_58` | installments | 2026-04-06:88.47\|2026-05-04:88.47\|2026-06-01:88.47\|2026-06-29:88.47\|2026-07-27:88.47\|2026-08-24:88.47\|2026-09-21:88.47\|2026-10-19:88.47\|2026-11-16:88.47\|2026-12-14:88.47\|2027-01-11:88.47\|2027-02-08:88.47\|2027-03-08:88.47\|2027-04-05:88.47\|2027-05-03:88.47\|2027-05-31:88.47\|2027-06-28:88.47\|2027-07-26:88.47\|2027-08-23:88.47\|2027-09-20:88.47\|2027-10-18:88.47 | 283.47 | 1857.87 |
| `payment_option_59` | installments | 2026-04-10:283.39\|2026-05-10:283.39\|2026-06-09:283.39\|2026-07-09:283.39\|2026-08-08:283.39\|2026-09-07:283.39 | 125.94 | 1700.34 |
| `payment_option_60` | installments | 2026-04-17:80.03\|2026-05-18:80.03\|2026-06-18:80.03\|2026-07-19:80.03\|2026-08-19:80.03\|2026-09-19:80.03\|2026-10-20:80.03\|2026-11-20:80.03\|2026-12-21:80.03\|2027-01-21:80.03\|2027-02-21:80.03\|2027-03-24:80.03\|2027-04-24:80.03\|2027-05-25:80.03\|2027-06-25:80.03\|2027-07-26:80.03\|2027-08-26:80.03\|2027-09-26:80.03\|2027-10-27:80.03\|2027-11-27:80.03\|2027-12-28:80.03\|2028-01-28:80.03\|2028-02-28:80.03\|2028-03-30:80.03 | 346.32 | 1920.72 |

## request_22 — user_22

Primary category: **earliest-date computation**

Both results select installments; the discrepancy is capacity/earliest-full-payment timing rather than an option-selection failure.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 475.46 | 506.65 |
| `earliest_date_for_full_payment` | 2025-01-15 | 2024-12-17 |
| `decision_explanation` | Use 3 installments of EUR 253.59, starting 8 December 2024. This leaves at least EUR 500 available. | Baseline selected supplied installment option payment_option_61. |

### Financial profile

- Home currency: `EUR`
- Current balance: `1132.46`
- Minimum balance: `500`
- Protected: `groceries|rent|transport`; reduce: ``; stop: `gym|music_subscription`.
- Payment methods: `installments`; max installment months: `6`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-12-08 | event_1961 | explicit | shopping | -43 | Pending merchant debit |
| 2024-12-08 | recurring:utilities | recurring | utilities | -31.52 | Inferred recurring Electricity and water bill |
| 2024-12-12 | recurring:gym | recurring | gym | -17 | Inferred recurring Gym membership |
| 2024-12-13 | recurring:music_subscription | recurring | music_subscription | -6 | Inferred recurring Music service subscription |
| 2024-12-15 | recurring:delivery_membership | recurring | delivery_membership | -5 | Inferred recurring Food delivery membership |
| 2024-12-16 | recurring:entertainment | recurring | entertainment | -23.29 | Inferred recurring Weekend entertainment |
| 2024-12-16 | recurring:salary | recurring | salary | 616 | Inferred recurring Payroll credit |
| 2024-12-28 | recurring:transport | recurring | transport | -12.7 | Inferred recurring Commuter pass |
| 2025-01-02 | recurring:rent | recurring | rent | -178.2 | Inferred recurring Apartment rent transfer |
| 2025-01-08 | recurring:utilities | recurring | utilities | -31.52 | Inferred recurring Electricity and water bill |
| 2025-01-12 | recurring:gym | recurring | gym | -17 | Inferred recurring Gym membership |
| 2025-01-13 | recurring:music_subscription | recurring | music_subscription | -6 | Inferred recurring Music service subscription |
| 2025-01-15 | recurring:delivery_membership | recurring | delivery_membership | -5 | Inferred recurring Food delivery membership |
| 2025-01-16 | recurring:entertainment | recurring | entertainment | -23.29 | Inferred recurring Weekend entertainment |
| 2025-01-16 | recurring:salary | recurring | salary | 616 | Inferred recurring Payroll credit |
| 2025-01-29 | recurring:transport | recurring | transport | -12.7 | Inferred recurring Commuter pass |
| 2025-02-01 | recurring:rent | recurring | rent | -178.2 | Inferred recurring Apartment rent transfer |
| 2025-02-08 | recurring:utilities | recurring | utilities | -31.52 | Inferred recurring Electricity and water bill |
| 2025-02-12 | recurring:gym | recurring | gym | -17 | Inferred recurring Gym membership |
| 2025-02-13 | recurring:music_subscription | recurring | music_subscription | -6 | Inferred recurring Music service subscription |
| 2025-02-15 | recurring:delivery_membership | recurring | delivery_membership | -5 | Inferred recurring Food delivery membership |
| 2025-02-16 | recurring:entertainment | recurring | entertainment | -23.29 | Inferred recurring Weekend entertainment |
| 2025-02-16 | recurring:salary | recurring | salary | 616 | Inferred recurring Payroll credit |
| 2025-03-02 | recurring:transport | recurring | transport | -12.7 | Inferred recurring Commuter pass |
| 2025-03-03 | recurring:rent | recurring | rent | -178.2 | Inferred recurring Apartment rent transfer |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_1895` | 2024-06-12 | settled | groceries | 23.95 | cash date 2024-06-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1921` | 2024-06-13 | settled | transport | 16.09 | cash date 2024-06-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1946` | 2024-06-14 | settled | dining | 12.25 | cash date 2024-06-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1896` | 2024-06-19 | settled | groceries | 29.03 | cash date 2024-06-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1922` | 2024-06-20 | settled | transport | 11.63 | cash date 2024-06-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1897` | 2024-06-26 | settled | groceries | 22.38 | cash date 2024-06-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1923` | 2024-06-27 | settled | transport | 16.34 | cash date 2024-06-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1947` | 2024-06-28 | settled | dining | 18.82 | cash date 2024-06-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1860` | 2024-07-03 | settled | rent | 178.2 | cash date 2024-07-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1898` | 2024-07-03 | settled | groceries | 20.6 | cash date 2024-07-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1924` | 2024-07-04 | settled | transport | 10.38 | cash date 2024-07-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1861` | 2024-07-07 | settled | utilities | 32.53 | cash date 2024-07-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1899` | 2024-07-10 | settled | groceries | 26.47 | cash date 2024-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1864` | 2024-07-11 | settled | gym | 17 | cash date 2024-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1925` | 2024-07-11 | settled | transport | 12.33 | cash date 2024-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1862` | 2024-07-12 | settled | music_subscription | 6 | cash date 2024-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1948` | 2024-07-12 | settled | dining | 13.59 | cash date 2024-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1863` | 2024-07-14 | settled | delivery_membership | 5 | cash date 2024-07-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1859` | 2024-07-15 | settled | salary | 616 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1865` | 2024-07-15 | settled | entertainment | 19.64 | cash date 2024-07-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1900` | 2024-07-17 | settled | groceries | 28.31 | cash date 2024-07-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1926` | 2024-07-18 | settled | transport | 12.7 | cash date 2024-07-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1901` | 2024-07-24 | settled | groceries | 22.88 | cash date 2024-07-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1927` | 2024-07-25 | settled | transport | 12.95 | cash date 2024-07-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1949` | 2024-07-26 | settled | dining | 14.46 | cash date 2024-07-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1902` | 2024-07-31 | settled | groceries | 25.75 | cash date 2024-07-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1928` | 2024-08-01 | settled | transport | 12.59 | cash date 2024-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1867` | 2024-08-03 | settled | rent | 178.2 | cash date 2024-08-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1868` | 2024-08-07 | settled | utilities | 33.73 | cash date 2024-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1903` | 2024-08-07 | settled | groceries | 20.5 | cash date 2024-08-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1929` | 2024-08-08 | settled | transport | 9.7 | cash date 2024-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1950` | 2024-08-09 | settled | dining | 20.85 | cash date 2024-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1871` | 2024-08-11 | settled | gym | 17 | cash date 2024-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1869` | 2024-08-12 | settled | music_subscription | 6 | cash date 2024-08-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1870` | 2024-08-14 | settled | delivery_membership | 5 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1904` | 2024-08-14 | settled | groceries | 22.19 | cash date 2024-08-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1866` | 2024-08-15 | settled | salary | 616 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1872` | 2024-08-15 | settled | entertainment | 18.94 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1930` | 2024-08-15 | settled | transport | 10.41 | cash date 2024-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1905` | 2024-08-21 | settled | groceries | 21.76 | cash date 2024-08-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1931` | 2024-08-22 | settled | transport | 10.72 | cash date 2024-08-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1951` | 2024-08-23 | settled | dining | 15.63 | cash date 2024-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1906` | 2024-08-28 | settled | groceries | 23.84 | cash date 2024-08-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1932` | 2024-08-29 | settled | transport | 11.85 | cash date 2024-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1959` | 2024-09-01 | settled | investment | 184.8 | superseded transaction lifecycle record |
| `event_1874` | 2024-09-03 | settled | rent | 178.2 | cash date 2024-09-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1907` | 2024-09-04 | settled | groceries | 23.02 | cash date 2024-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1933` | 2024-09-05 | settled | transport | 12.65 | cash date 2024-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1952` | 2024-09-06 | settled | dining | 17.66 | cash date 2024-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1875` | 2024-09-07 | settled | utilities | 31.52 | cash date 2024-09-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1878` | 2024-09-11 | settled | gym | 17 | cash date 2024-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1908` | 2024-09-11 | settled | groceries | 28.46 | cash date 2024-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1876` | 2024-09-12 | settled | music_subscription | 6 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1934` | 2024-09-12 | settled | transport | 15.34 | cash date 2024-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1877` | 2024-09-14 | settled | delivery_membership | 5 | cash date 2024-09-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1873` | 2024-09-15 | settled | salary | 616 | cash date 2024-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1879` | 2024-09-15 | settled | entertainment | 23.29 | cash date 2024-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1909` | 2024-09-18 | settled | groceries | 22.14 | cash date 2024-09-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1935` | 2024-09-19 | settled | transport | 10.09 | cash date 2024-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1953` | 2024-09-20 | settled | dining | 16.03 | cash date 2024-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1910` | 2024-09-25 | settled | groceries | 19.54 | cash date 2024-09-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1936` | 2024-09-26 | settled | transport | 15.68 | cash date 2024-09-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1911` | 2024-10-02 | settled | groceries | 29.25 | cash date 2024-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1881` | 2024-10-03 | settled | rent | 178.2 | cash date 2024-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1937` | 2024-10-03 | settled | transport | 13.05 | cash date 2024-10-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1954` | 2024-10-04 | settled | dining | 14.22 | cash date 2024-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1882` | 2024-10-07 | settled | utilities | 27.68 | cash date 2024-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1912` | 2024-10-09 | settled | groceries | 27.59 | cash date 2024-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1938` | 2024-10-10 | settled | transport | 9.9 | cash date 2024-10-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1885` | 2024-10-11 | settled | gym | 17 | cash date 2024-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1883` | 2024-10-12 | settled | music_subscription | 6 | cash date 2024-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1884` | 2024-10-14 | settled | delivery_membership | 5 | cash date 2024-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1880` | 2024-10-15 | settled | salary | 616 | cash date 2024-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1886` | 2024-10-15 | settled | entertainment | 22.03 | cash date 2024-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1913` | 2024-10-16 | settled | groceries | 23.94 | cash date 2024-10-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1939` | 2024-10-17 | settled | transport | 15.93 | cash date 2024-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1955` | 2024-10-18 | settled | dining | 18.53 | cash date 2024-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1914` | 2024-10-23 | settled | groceries | 21.58 | cash date 2024-10-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1940` | 2024-10-24 | settled | transport | 15.08 | cash date 2024-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1915` | 2024-10-30 | settled | groceries | 29.81 | cash date 2024-10-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1941` | 2024-10-31 | settled | transport | 15.65 | cash date 2024-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1956` | 2024-11-01 | settled | dining | 12.65 | cash date 2024-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1888` | 2024-11-03 | settled | rent | 178.2 | cash date 2024-11-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1916` | 2024-11-06 | settled | groceries | 27.33 | cash date 2024-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1889` | 2024-11-07 | settled | utilities | 27.34 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1942` | 2024-11-07 | settled | transport | 14.93 | cash date 2024-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1892` | 2024-11-11 | settled | gym | 17 | cash date 2024-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1890` | 2024-11-12 | settled | music_subscription | 6 | cash date 2024-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1917` | 2024-11-13 | settled | groceries | 18.71 | cash date 2024-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1891` | 2024-11-14 | settled | delivery_membership | 5 | cash date 2024-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1943` | 2024-11-14 | settled | transport | 11.44 | cash date 2024-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1887` | 2024-11-15 | settled | salary | 616 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1893` | 2024-11-15 | settled | entertainment | 20.43 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1957` | 2024-11-15 | settled | dining | 15.84 | cash date 2024-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1918` | 2024-11-20 | settled | groceries | 18.6 | cash date 2024-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1944` | 2024-11-21 | settled | transport | 15.87 | cash date 2024-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1919` | 2024-11-27 | settled | groceries | 18.35 | cash date 2024-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1945` | 2024-11-28 | settled | transport | 15.02 | cash date 2024-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1958` | 2024-11-29 | settled | dining | 18.41 | cash date 2024-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1894` | 2024-12-03 | settled | rent | 178.2 | cash date 2024-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1960` | 2024-12-03 | unrealized | investment |  | unrealized event |
| `event_1920` | 2024-12-04 | settled | groceries | 26.82 | cash date 2024-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_15` | 2024-12-02T09:30:00Z | `event_1960` | financial_service | Here’s the latest account information from ClearFund. Your portfolio’s displayed market value has increased substantially. No units have been sold and no cash proceeds have been generated. The displayed value will continue to move with market prices. Account ref FIN-0015. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| `event_1960` | `event_1959` | unrealized | investment_valuation |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_61` | installments | 2024-12-08:253.59\|2025-01-05:253.59\|2025-02-02:253.59 | 29.27 | 760.77 |
| `payment_option_62` | full_payment | 2024-12-05:731.5 | 0 | 731.5 |
| `payment_option_63` | installments | 2024-12-12:53.64\|2025-01-11:53.64\|2025-02-10:53.64\|2025-03-12:53.64\|2025-04-11:53.64\|2025-05-11:53.64\|2025-06-10:53.64\|2025-07-10:53.64\|2025-08-09:53.64\|2025-09-08:53.64\|2025-10-08:53.64\|2025-11-07:53.64\|2025-12-07:53.64\|2026-01-06:53.64\|2026-02-05:53.64 | 73.1 | 804.6 |

## request_23 — user_23

Primary category: **pending debit or credit handling**

The supporting message says a bonus, commission, refund, prize, or payout is not yet cash. The forecast must reserve its absence until an explicit settlement/credit record exists.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 9152 | 7241.63 |
| `affordability_status` | affordable_later | not_affordable |
| `recommended_payment_method` | wait | not_recommended |
| `payment_plan` | 2025-07-15:38016 | none |
| `earliest_date_for_full_payment` | 2025-07-15 |  |
| `decision_explanation` | Pay ZAR 38,016 in full on 15 July 2025. Paying earlier would take the balance below the ZAR 27,000 minimum. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `ZAR`
- Current balance: `51957.9`
- Minimum balance: `27000`
- Protected: `family_support|groceries|healthcare|rent`; reduce: `shopping`; stop: `cloud_storage`.
- Payment methods: `full_payment|installments|partial_payment`; max installment months: `12`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2025-05-09 | recurring:utilities | recurring | utilities | -2915.67 | Inferred recurring Electricity bill |
| 2025-05-11 | event_2042 | explicit | healthcare | -1553.2 | Pending pharmacy card charge |
| 2025-05-13 | recurring:healthcare | recurring | healthcare | -1439.91 | Inferred recurring Clinic payment |
| 2025-05-14 | recurring:debt_repayment | recurring | debt_repayment | -5852 | Inferred recurring Education loan instalment |
| 2025-05-15 | recurring:shopping | recurring | shopping | -1389.39 | Inferred recurring Personal shopping |
| 2025-05-15 | recurring:cloud_storage | recurring | cloud_storage | -295.9 | Inferred recurring Cloud storage plan |
| 2025-05-16 | recurring:family_support | recurring | family_support | -4270.2 | Inferred recurring Childcare contribution |
| 2025-05-16 | recurring:salary | recurring | salary | 45760 | Inferred recurring Payroll credit |
| 2025-06-03 | recurring:rent | recurring | rent | -15312 | Inferred recurring Shared housing rent |
| 2025-06-09 | recurring:utilities | recurring | utilities | -2915.67 | Inferred recurring Electricity bill |
| 2025-06-13 | recurring:healthcare | recurring | healthcare | -1439.91 | Inferred recurring Clinic payment |
| 2025-06-14 | recurring:debt_repayment | recurring | debt_repayment | -5852 | Inferred recurring Education loan instalment |
| 2025-06-15 | recurring:shopping | recurring | shopping | -1389.39 | Inferred recurring Personal shopping |
| 2025-06-15 | recurring:cloud_storage | recurring | cloud_storage | -295.9 | Inferred recurring Cloud storage plan |
| 2025-06-16 | recurring:family_support | recurring | family_support | -4270.2 | Inferred recurring Childcare contribution |
| 2025-06-16 | recurring:salary | recurring | salary | 45760 | Inferred recurring Payroll credit |
| 2025-07-03 | recurring:rent | recurring | rent | -15312 | Inferred recurring Shared housing rent |
| 2025-07-10 | recurring:utilities | recurring | utilities | -2915.67 | Inferred recurring Electricity bill |
| 2025-07-14 | recurring:healthcare | recurring | healthcare | -1439.91 | Inferred recurring Clinic payment |
| 2025-07-15 | recurring:debt_repayment | recurring | debt_repayment | -5852 | Inferred recurring Education loan instalment |
| 2025-07-16 | recurring:shopping | recurring | shopping | -1389.39 | Inferred recurring Personal shopping |
| 2025-07-16 | recurring:cloud_storage | recurring | cloud_storage | -295.9 | Inferred recurring Cloud storage plan |
| 2025-07-17 | recurring:family_support | recurring | family_support | -4270.2 | Inferred recurring Childcare contribution |
| 2025-07-17 | recurring:salary | recurring | salary | 45760 | Inferred recurring Payroll credit |
| 2025-08-02 | recurring:rent | recurring | rent | -15312 | Inferred recurring Shared housing rent |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_2003` | 2024-11-13 | settled | groceries | 1401.85 | cash date 2024-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2028` | 2024-11-14 | settled | transport | 682.68 | cash date 2024-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2004` | 2024-11-20 | settled | groceries | 1332.28 | cash date 2024-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2005` | 2024-11-27 | settled | groceries | 1586.85 | cash date 2024-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2029` | 2024-11-28 | settled | transport | 1121.5 | cash date 2024-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1963` | 2024-12-04 | settled | rent | 15312 | cash date 2024-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2006` | 2024-12-04 | settled | groceries | 1372.64 | cash date 2024-12-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1964` | 2024-12-08 | settled | utilities | 2877.85 | cash date 2024-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2007` | 2024-12-11 | settled | groceries | 1821.15 | cash date 2024-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1966` | 2024-12-12 | settled | healthcare | 1341.05 | cash date 2024-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2030` | 2024-12-12 | settled | transport | 747.69 | cash date 2024-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1965` | 2024-12-13 | settled | debt_repayment | 5852 | cash date 2024-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1968` | 2024-12-14 | settled | cloud_storage | 295.9 | cash date 2024-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1969` | 2024-12-14 | settled | shopping | 1279.39 | cash date 2024-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1962` | 2024-12-15 | settled | salary | 45760 | cash date 2024-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1967` | 2024-12-15 | settled | family_support | 4270.2 | cash date 2024-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2008` | 2024-12-18 | settled | groceries | 2207.92 | cash date 2024-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2009` | 2024-12-25 | settled | groceries | 1981.14 | cash date 2024-12-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2031` | 2024-12-26 | settled | transport | 777.57 | cash date 2024-12-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2010` | 2025-01-01 | settled | groceries | 2178.52 | cash date 2025-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1971` | 2025-01-04 | settled | rent | 15312 | cash date 2025-01-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1972` | 2025-01-08 | settled | utilities | 2484.32 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2011` | 2025-01-08 | settled | groceries | 1927.69 | cash date 2025-01-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2032` | 2025-01-09 | settled | transport | 896.02 | cash date 2025-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1974` | 2025-01-12 | settled | healthcare | 1331.22 | cash date 2025-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1973` | 2025-01-13 | settled | debt_repayment | 5852 | cash date 2025-01-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1976` | 2025-01-14 | settled | cloud_storage | 295.9 | cash date 2025-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1977` | 2025-01-14 | settled | shopping | 1396.33 | cash date 2025-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1970` | 2025-01-15 | settled | salary | 45760 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1975` | 2025-01-15 | settled | family_support | 4270.2 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2012` | 2025-01-15 | settled | groceries | 2125.65 | cash date 2025-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2013` | 2025-01-22 | settled | groceries | 1544.99 | cash date 2025-01-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2033` | 2025-01-23 | settled | transport | 904.55 | cash date 2025-01-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2014` | 2025-01-29 | settled | groceries | 1914.51 | cash date 2025-01-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2041` | 2025-02-01 | settled | investment | 13728 | cash date 2025-02-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1979` | 2025-02-04 | settled | rent | 15312 | cash date 2025-02-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2015` | 2025-02-05 | settled | groceries | 1421.88 | cash date 2025-02-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2034` | 2025-02-06 | settled | transport | 968.71 | cash date 2025-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1980` | 2025-02-08 | settled | utilities | 2915.67 | cash date 2025-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1982` | 2025-02-12 | settled | healthcare | 1439.91 | cash date 2025-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2016` | 2025-02-12 | settled | groceries | 1556.59 | cash date 2025-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1981` | 2025-02-13 | settled | debt_repayment | 5852 | cash date 2025-02-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1984` | 2025-02-14 | settled | cloud_storage | 295.9 | cash date 2025-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1985` | 2025-02-14 | settled | shopping | 1389.39 | cash date 2025-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1978` | 2025-02-15 | settled | salary | 45760 | cash date 2025-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1983` | 2025-02-15 | settled | family_support | 4270.2 | cash date 2025-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2017` | 2025-02-19 | settled | groceries | 2186.26 | cash date 2025-02-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2035` | 2025-02-20 | settled | transport | 1046.56 | cash date 2025-02-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2018` | 2025-02-26 | settled | groceries | 2146.88 | cash date 2025-02-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1987` | 2025-03-04 | settled | rent | 15312 | cash date 2025-03-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2019` | 2025-03-05 | settled | groceries | 1717.87 | cash date 2025-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2036` | 2025-03-06 | settled | transport | 738.21 | cash date 2025-03-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1988` | 2025-03-08 | settled | utilities | 2813.94 | cash date 2025-03-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1990` | 2025-03-12 | settled | healthcare | 1317.68 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2020` | 2025-03-12 | settled | groceries | 2074.73 | cash date 2025-03-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1989` | 2025-03-13 | settled | debt_repayment | 5852 | cash date 2025-03-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1992` | 2025-03-14 | settled | cloud_storage | 295.9 | cash date 2025-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1993` | 2025-03-14 | settled | shopping | 1232.23 | cash date 2025-03-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1986` | 2025-03-15 | settled | salary | 45760 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1991` | 2025-03-15 | settled | family_support | 4270.2 | cash date 2025-03-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2021` | 2025-03-19 | settled | groceries | 1372.44 | cash date 2025-03-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2037` | 2025-03-20 | settled | transport | 956.01 | cash date 2025-03-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2022` | 2025-03-26 | settled | groceries | 1706.85 | cash date 2025-03-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2023` | 2025-04-02 | settled | groceries | 1487.69 | cash date 2025-04-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2038` | 2025-04-03 | settled | transport | 1092.98 | cash date 2025-04-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1995` | 2025-04-04 | settled | rent | 15312 | cash date 2025-04-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1996` | 2025-04-08 | settled | utilities | 2680.15 | cash date 2025-04-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2024` | 2025-04-09 | settled | groceries | 1794.76 | cash date 2025-04-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1998` | 2025-04-12 | settled | healthcare | 1377.89 | cash date 2025-04-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1997` | 2025-04-13 | settled | debt_repayment | 5852 | cash date 2025-04-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2000` | 2025-04-14 | settled | cloud_storage | 295.9 | cash date 2025-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2001` | 2025-04-14 | settled | shopping | 1281.33 | cash date 2025-04-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1994` | 2025-04-15 | settled | salary | 45760 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_1999` | 2025-04-15 | settled | family_support | 4270.2 | cash date 2025-04-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2025` | 2025-04-16 | settled | groceries | 1678.37 | cash date 2025-04-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2039` | 2025-04-17 | settled | transport | 834 | cash date 2025-04-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2026` | 2025-04-23 | settled | groceries | 1514.83 | cash date 2025-04-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2027` | 2025-04-30 | settled | groceries | 1257.56 | cash date 2025-04-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2040` | 2025-05-01 | settled | transport | 783.18 | cash date 2025-05-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2002` | 2025-05-04 | settled | rent | 15312 | cash date 2025-05-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_16` | 2025-04-26T09:30:00Z | `` | financial_service | Here’s the latest account information from DrawPay. Your prize claim has been verified and is still in payment processing. The payment has not been credited to your account yet. We’ll confirm again if and when the money is actually credited. Account ref FIN-0016. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_64` | full_payment | 2025-05-07:38016 | 0 | 38016 |
| `payment_option_65` | installments | 2025-05-21:2407.68\|2025-06-21:2407.68\|2025-07-22:2407.68\|2025-08-22:2407.68\|2025-09-22:2407.68\|2025-10-23:2407.68\|2025-11-23:2407.68\|2025-12-24:2407.68\|2026-01-24:2407.68\|2026-02-24:2407.68\|2026-03-27:2407.68\|2026-04-27:2407.68\|2026-05-28:2407.68\|2026-06-28:2407.68\|2026-07-29:2407.68\|2026-08-29:2407.68\|2026-09-29:2407.68\|2026-10-30:2407.68 | 5322.24 | 43338.24 |
| `payment_option_66` | installments | 2025-05-10:1932.48\|2025-06-09:1932.48\|2025-07-09:1932.48\|2025-08-08:1932.48\|2025-09-07:1932.48\|2025-10-07:1932.48\|2025-11-06:1932.48\|2025-12-06:1932.48\|2026-01-05:1932.48\|2026-02-04:1932.48\|2026-03-06:1932.48\|2026-04-05:1932.48\|2026-05-05:1932.48\|2026-06-04:1932.48\|2026-07-04:1932.48\|2026-08-03:1932.48\|2026-09-02:1932.48\|2026-10-02:1932.48\|2026-11-01:1932.48\|2026-12-01:1932.48\|2026-12-31:1932.48\|2027-01-30:1932.48\|2027-03-01:1932.48\|2027-03-31:1932.48 | 8363.52 | 46379.52 |

## request_24 — user_24

Primary category: **cancellations or amendments from messages**

Relevant message/image evidence is loaded but not interpreted, so confirmed amendments, cancellations, and image-only amounts cannot affect the forecast.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 13420 | 23553.06 |
| `decision_explanation` | Do not proceed with the INR 109,600 request. Although INR 13,420 is available today, the full amount cannot be completed safely within 90 days. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `INR`
- Current balance: `85045`
- Minimum balance: `51000`
- Protected: `insurance|rent|transport`; reduce: `dining|streaming`; stop: `cloud_storage|streaming`.
- Payment methods: `partial_payment`; max installment months: ``.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2026-01-05 | recurring:insurance | recurring | insurance | -2510 | Inferred recurring Insurance policy payment |
| 2026-01-07 | recurring:streaming | recurring | streaming | -1200 | Inferred recurring Family streaming plan |
| 2026-01-10 | recurring:shopping | recurring | shopping | -2680.78 | Inferred recurring Monthly shopping spend |
| 2026-01-10 | recurring:cloud_storage | recurring | cloud_storage | -355 | Inferred recurring Online backup subscription |
| 2026-01-11 | event_2166 | explicit | insurance | -1830 | Scheduled insurance payment |
| 2026-01-12 | recurring:entertainment | recurring | entertainment | -1916.16 | Inferred recurring Local event tickets |
| 2026-01-14 | recurring:salary | recurring | salary | 61000 | Inferred recurring Payroll credit |
| 2026-01-28 | recurring:dining | recurring | dining | -2151.71 | Inferred recurring Family dinner |
| 2026-01-31 | recurring:rent | recurring | rent | -18600 | Inferred recurring Landlord standing order |
| 2026-02-03 | recurring:utilities | recurring | utilities | -3490.5 | Inferred recurring Household utility payment |
| 2026-02-04 | recurring:insurance | recurring | insurance | -2510 | Inferred recurring Insurance policy payment |
| 2026-02-05 | recurring:dining | recurring | dining | -2137.71 | Inferred recurring Lunch with colleagues |
| 2026-02-06 | recurring:streaming | recurring | streaming | -1200 | Inferred recurring Family streaming plan |
| 2026-02-09 | recurring:shopping | recurring | shopping | -2680.78 | Inferred recurring Monthly shopping spend |
| 2026-02-09 | recurring:cloud_storage | recurring | cloud_storage | -355 | Inferred recurring Online backup subscription |
| 2026-02-11 | recurring:entertainment | recurring | entertainment | -1916.16 | Inferred recurring Local event tickets |
| 2026-02-13 | recurring:salary | recurring | salary | 61000 | Inferred recurring Payroll credit |
| 2026-03-01 | recurring:dining | recurring | dining | -2151.71 | Inferred recurring Family dinner |
| 2026-03-02 | recurring:rent | recurring | rent | -18600 | Inferred recurring Landlord standing order |
| 2026-03-05 | recurring:utilities | recurring | utilities | -3490.5 | Inferred recurring Household utility payment |
| 2026-03-06 | recurring:insurance | recurring | insurance | -2510 | Inferred recurring Insurance policy payment |
| 2026-03-08 | recurring:streaming | recurring | streaming | -1200 | Inferred recurring Family streaming plan |
| 2026-03-09 | recurring:dining | recurring | dining | -2137.71 | Inferred recurring Lunch with colleagues |
| 2026-03-11 | recurring:shopping | recurring | shopping | -2680.78 | Inferred recurring Monthly shopping spend |
| 2026-03-11 | recurring:cloud_storage | recurring | cloud_storage | -355 | Inferred recurring Online backup subscription |
| 2026-03-13 | recurring:entertainment | recurring | entertainment | -1916.16 | Inferred recurring Local event tickets |
| 2026-03-15 | recurring:salary | recurring | salary | 61000 | Inferred recurring Payroll credit |
| 2026-04-01 | recurring:rent | recurring | rent | -18600 | Inferred recurring Landlord standing order |
| 2026-04-02 | recurring:dining | recurring | dining | -2151.71 | Inferred recurring Family dinner |
| 2026-04-04 | recurring:utilities | recurring | utilities | -3490.5 | Inferred recurring Household utility payment |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_2084` | 2025-07-10 | settled | groceries | 2886.9 | cash date 2025-07-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2102` | 2025-07-11 | settled | transport | 1663.51 | cash date 2025-07-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2138` | 2025-07-12 | settled | dining | 1757.23 | cash date 2025-07-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2103` | 2025-07-16 | settled | transport | 1021.64 | cash date 2025-07-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2139` | 2025-07-19 | settled | dining | 1886.97 | cash date 2025-07-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2085` | 2025-07-20 | settled | groceries | 2024.93 | cash date 2025-07-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2104` | 2025-07-21 | settled | transport | 1760.99 | cash date 2025-07-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2105` | 2025-07-26 | settled | transport | 1208.87 | cash date 2025-07-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2140` | 2025-07-26 | settled | dining | 2149.97 | cash date 2025-07-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2086` | 2025-07-30 | settled | groceries | 2236.73 | cash date 2025-07-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2106` | 2025-07-31 | settled | transport | 1232.11 | cash date 2025-07-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2044` | 2025-08-01 | settled | rent | 18600 | cash date 2025-08-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2141` | 2025-08-02 | settled | dining | 2239.04 | cash date 2025-08-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2045` | 2025-08-05 | settled | utilities | 3049.81 | cash date 2025-08-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2107` | 2025-08-05 | settled | transport | 1319.2 | cash date 2025-08-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2046` | 2025-08-06 | settled | insurance | 2510 | cash date 2025-08-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2048` | 2025-08-08 | settled | streaming | 1200 | cash date 2025-08-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2087` | 2025-08-09 | settled | groceries | 2439.18 | cash date 2025-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2142` | 2025-08-09 | settled | dining | 1328.72 | cash date 2025-08-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2108` | 2025-08-10 | settled | transport | 1536.25 | cash date 2025-08-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2047` | 2025-08-11 | settled | cloud_storage | 355 | cash date 2025-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2049` | 2025-08-11 | settled | shopping | 2409.82 | cash date 2025-08-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2050` | 2025-08-13 | settled | entertainment | 1870.6 | cash date 2025-08-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2043` | 2025-08-15 | settled | salary | 61000 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2109` | 2025-08-15 | settled | transport | 1122.2 | cash date 2025-08-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2143` | 2025-08-16 | settled | dining | 1291.44 | cash date 2025-08-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2088` | 2025-08-19 | settled | groceries | 2564.99 | cash date 2025-08-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2110` | 2025-08-20 | settled | transport | 1576.88 | cash date 2025-08-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2144` | 2025-08-23 | settled | dining | 2105.67 | cash date 2025-08-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2111` | 2025-08-25 | settled | transport | 1091.32 | cash date 2025-08-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2089` | 2025-08-29 | settled | groceries | 2201.87 | cash date 2025-08-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2112` | 2025-08-30 | settled | transport | 1119.08 | cash date 2025-08-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2145` | 2025-08-30 | settled | dining | 2046.83 | cash date 2025-08-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2052` | 2025-09-01 | settled | rent | 18600 | cash date 2025-09-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2113` | 2025-09-04 | settled | transport | 1370.25 | cash date 2025-09-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2053` | 2025-09-05 | settled | utilities | 3226.12 | cash date 2025-09-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2054` | 2025-09-06 | settled | insurance | 2510 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2146` | 2025-09-06 | settled | dining | 2288.09 | cash date 2025-09-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2056` | 2025-09-08 | settled | streaming | 1200 | cash date 2025-09-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2090` | 2025-09-08 | settled | groceries | 2601.43 | cash date 2025-09-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2114` | 2025-09-09 | settled | transport | 1401.3 | cash date 2025-09-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2055` | 2025-09-11 | settled | cloud_storage | 355 | cash date 2025-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2057` | 2025-09-11 | settled | shopping | 2514.9 | cash date 2025-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2058` | 2025-09-13 | settled | entertainment | 2124.72 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2147` | 2025-09-13 | settled | dining | 1893.38 | cash date 2025-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2115` | 2025-09-14 | settled | transport | 1393.89 | cash date 2025-09-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2051` | 2025-09-15 | settled | salary | 61000 | cash date 2025-09-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2091` | 2025-09-18 | settled | groceries | 2958.79 | cash date 2025-09-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2116` | 2025-09-19 | settled | transport | 1153.55 | cash date 2025-09-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2148` | 2025-09-20 | settled | dining | 1783.1 | cash date 2025-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2117` | 2025-09-24 | settled | transport | 1586.75 | cash date 2025-09-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2149` | 2025-09-27 | settled | dining | 2137.71 | cash date 2025-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2092` | 2025-09-28 | settled | groceries | 2042.7 | cash date 2025-09-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2118` | 2025-09-29 | settled | transport | 1218.23 | cash date 2025-09-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2060` | 2025-10-01 | settled | rent | 18600 | cash date 2025-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2164` | 2025-10-01 | settled | investment | 18300 | cash date 2025-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2119` | 2025-10-04 | settled | transport | 1750.91 | cash date 2025-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2150` | 2025-10-04 | settled | dining | 1985.64 | cash date 2025-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2061` | 2025-10-05 | settled | utilities | 3417.7 | cash date 2025-10-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2062` | 2025-10-06 | settled | insurance | 2510 | cash date 2025-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2064` | 2025-10-08 | settled | streaming | 1200 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2093` | 2025-10-08 | settled | groceries | 2145.69 | cash date 2025-10-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2120` | 2025-10-09 | settled | transport | 1585.39 | cash date 2025-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2063` | 2025-10-11 | settled | cloud_storage | 355 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2065` | 2025-10-11 | settled | shopping | 2680.78 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2151` | 2025-10-11 | settled | dining | 1496.44 | cash date 2025-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2066` | 2025-10-13 | settled | entertainment | 1916.16 | cash date 2025-10-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2121` | 2025-10-14 | settled | transport | 1069.31 | cash date 2025-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2059` | 2025-10-15 | settled | salary | 61000 | cash date 2025-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2094` | 2025-10-18 | settled | groceries | 1843.76 | cash date 2025-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2152` | 2025-10-18 | settled | dining | 1662.99 | cash date 2025-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2122` | 2025-10-19 | settled | transport | 1314.27 | cash date 2025-10-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2123` | 2025-10-24 | settled | transport | 1731.13 | cash date 2025-10-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2153` | 2025-10-25 | settled | dining | 1942.46 | cash date 2025-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2095` | 2025-10-28 | settled | groceries | 2358.78 | cash date 2025-10-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2124` | 2025-10-29 | settled | transport | 1110.11 | cash date 2025-10-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2068` | 2025-11-01 | settled | rent | 18600 | cash date 2025-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2154` | 2025-11-01 | settled | dining | 1818.76 | cash date 2025-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2125` | 2025-11-03 | settled | transport | 1256.01 | cash date 2025-11-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2069` | 2025-11-05 | settled | utilities | 3335.41 | cash date 2025-11-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2070` | 2025-11-06 | settled | insurance | 2510 | cash date 2025-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2096` | 2025-11-07 | settled | groceries | 2295.12 | cash date 2025-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2072` | 2025-11-08 | settled | streaming | 1200 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2126` | 2025-11-08 | settled | transport | 1514.06 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2155` | 2025-11-08 | settled | dining | 1423.26 | cash date 2025-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2071` | 2025-11-11 | settled | cloud_storage | 355 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2073` | 2025-11-11 | settled | shopping | 2398.76 | cash date 2025-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2074` | 2025-11-13 | settled | entertainment | 1845.75 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2127` | 2025-11-13 | settled | transport | 1600.18 | cash date 2025-11-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2067` | 2025-11-15 | settled | salary | 61000 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2156` | 2025-11-15 | settled | dining | 2198 | cash date 2025-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2097` | 2025-11-17 | settled | groceries | 1824.41 | cash date 2025-11-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2128` | 2025-11-18 | settled | transport | 1534.77 | cash date 2025-11-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2157` | 2025-11-22 | settled | dining | 1345.87 | cash date 2025-11-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2129` | 2025-11-23 | settled | transport | 1050.4 | cash date 2025-11-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2098` | 2025-11-27 | settled | groceries | 2113.95 | cash date 2025-11-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2130` | 2025-11-28 | settled | transport | 1187.92 | cash date 2025-11-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2158` | 2025-11-29 | settled | dining | 1415.29 | cash date 2025-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2076` | 2025-12-01 | settled | rent | 18600 | cash date 2025-12-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2131` | 2025-12-03 | settled | transport | 1270.09 | cash date 2025-12-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2077` | 2025-12-05 | settled | utilities | 3490.5 | cash date 2025-12-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2078` | 2025-12-06 | settled | insurance | 2510 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2159` | 2025-12-06 | settled | dining | 1842.2 | cash date 2025-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2099` | 2025-12-07 | settled | groceries | 2260.73 | cash date 2025-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2080` | 2025-12-08 | settled | streaming | 1200 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2132` | 2025-12-08 | settled | transport | 1485.42 | cash date 2025-12-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2079` | 2025-12-11 | settled | cloud_storage | 355 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2081` | 2025-12-11 | settled | shopping | 2564 | cash date 2025-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2082` | 2025-12-13 | settled | entertainment | 1896.25 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2133` | 2025-12-13 | settled | transport | 1341.45 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2160` | 2025-12-13 | settled | dining | 1911.68 | cash date 2025-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2075` | 2025-12-15 | settled | salary | 61000 | cash date 2025-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2100` | 2025-12-17 | settled | groceries | 2106.55 | cash date 2025-12-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2134` | 2025-12-18 | settled | transport | 1059.47 | cash date 2025-12-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2161` | 2025-12-20 | settled | dining | 2184.47 | cash date 2025-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2135` | 2025-12-23 | settled | transport | 1438 | cash date 2025-12-23 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2101` | 2025-12-27 | settled | groceries | 2321.31 | cash date 2025-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2162` | 2025-12-27 | settled | dining | 2151.71 | cash date 2025-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2136` | 2025-12-28 | settled | transport | 1255.38 | cash date 2025-12-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2165` | 2025-12-28 | settled | windfall | 33550 | cash date 2025-12-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2083` | 2026-01-01 | settled | rent | 18600 | cash date 2026-01-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2137` | 2026-01-02 | settled | transport | 1593.41 | cash date 2026-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2163` | 2026-01-03 | settled | dining | 1918.02 | cash date 2026-01-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| `message_17` | 2025-12-29T09:30:00Z | `event_2165` | financial_service | Here’s the latest account information from PrizeTrack. The prize proceeds have reached your account after withholding. The claim is now closed and there are no further scheduled payments. There won’t be another payment unless a separate prize is confirmed. Account ref FIN-0017. |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_67` | full_payment | 2026-01-04:109600 | 0 | 109600 |
| `payment_option_68` | installments | 2026-01-04:6158.48\|2026-02-01:6158.48\|2026-03-01:6158.48\|2026-03-29:6158.48\|2026-04-26:6158.48\|2026-05-24:6158.48\|2026-06-21:6158.48\|2026-07-19:6158.48\|2026-08-16:6158.48\|2026-09-13:6158.48\|2026-10-11:6158.48\|2026-11-08:6158.48\|2026-12-06:6158.48\|2027-01-03:6158.48\|2027-01-31:6158.48\|2027-02-28:6158.48\|2027-03-28:6158.48\|2027-04-25:6158.48\|2027-05-23:6158.48\|2027-06-20:6158.48\|2027-07-18:6158.48 | 19728.08 | 129328.08 |

## request_25 — user_25

Primary category: **dated currency conversion**

At least one relevant cash event needs a dated conversion; the baseline's direct-rate-only handling can exclude valid events when a supplied reverse pair is required.

### Expected vs actual

| Field | Solved sample | Existing baseline artifact |
| --- | --- | --- |
| `amount_safe_to_pay` | 1425000 | 4567587.32 |
| `decision_explanation` | Do not make this payment by 17 April 2024. None of the available options keeps the IDR 23,379,100 minimum protected. | Baseline found no eligible safe plan within 90 days. |

### Financial profile

- Home currency: `IDR`
- Current balance: `32063050`
- Minimum balance: `23379100`
- Protected: `insurance|rent|transport`; reduce: ``; stop: ``.
- Payment methods: `full_payment|installments`; max installment months: `3`.

### Included 90-day forecast cash flows

| Date | Source | Kind | Category | Home-currency amount | Detail |
| --- | --- | --- | --- | ---: | --- |
| 2024-03-08 | recurring:utilities | recurring | utilities | -1341541.39 | Inferred recurring Household utility payment |
| 2024-03-09 | recurring:insurance | recurring | insurance | -904400 | Inferred recurring Insurance policy payment |
| 2024-03-11 | recurring:streaming | recurring | streaming | -573800 | Inferred recurring Video streaming plan |
| 2024-03-14 | recurring:shopping | recurring | shopping | -1170271.29 | Inferred recurring Monthly shopping spend |
| 2024-03-14 | recurring:cloud_storage | recurring | cloud_storage | -126350 | Inferred recurring Cloud storage plan |
| 2024-03-15 | event_2288 | explicit | salary | 28499994 | Next confirmed salary |
| 2024-03-16 | recurring:entertainment | recurring | entertainment | -504697.37 | Inferred recurring Games and recreation |
| 2024-03-17 | recurring:salary | recurring | salary | 28499994 | Inferred recurring International employer payroll |
| 2024-04-01 | recurring:rent | recurring | rent | -6954000 | Inferred recurring Monthly rent |
| 2024-04-08 | recurring:utilities | recurring | utilities | -1341541.39 | Inferred recurring Household utility payment |
| 2024-04-09 | recurring:insurance | recurring | insurance | -904400 | Inferred recurring Insurance policy payment |
| 2024-04-11 | recurring:streaming | recurring | streaming | -573800 | Inferred recurring Video streaming plan |
| 2024-04-14 | recurring:shopping | recurring | shopping | -1170271.29 | Inferred recurring Monthly shopping spend |
| 2024-04-14 | recurring:cloud_storage | recurring | cloud_storage | -126350 | Inferred recurring Cloud storage plan |
| 2024-04-16 | recurring:entertainment | recurring | entertainment | -504697.37 | Inferred recurring Games and recreation |
| 2024-04-17 | recurring:salary | recurring | salary | 28499994 | Inferred recurring International employer payroll |
| 2024-05-01 | recurring:rent | recurring | rent | -6954000 | Inferred recurring Monthly rent |
| 2024-05-09 | recurring:utilities | recurring | utilities | -1341541.39 | Inferred recurring Household utility payment |
| 2024-05-10 | recurring:insurance | recurring | insurance | -904400 | Inferred recurring Insurance policy payment |
| 2024-05-12 | recurring:streaming | recurring | streaming | -573800 | Inferred recurring Video streaming plan |
| 2024-05-15 | recurring:shopping | recurring | shopping | -1170271.29 | Inferred recurring Monthly shopping spend |
| 2024-05-15 | recurring:cloud_storage | recurring | cloud_storage | -126350 | Inferred recurring Cloud storage plan |
| 2024-05-17 | recurring:entertainment | recurring | entertainment | -504697.37 | Inferred recurring Games and recreation |
| 2024-05-18 | recurring:salary | recurring | salary | 28499994 | Inferred recurring International employer payroll |
| 2024-05-31 | recurring:rent | recurring | rent | -6954000 | Inferred recurring Monthly rent |

### Excluded source events

| Event | Cash date | Status | Category | Home-currency amount | Reason |
| --- | --- | --- | --- | ---: | --- |
| `event_2208` | 2023-09-11 | settled | groceries | 1348940.42 | cash date 2023-09-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2226` | 2023-09-12 | settled | transport | 725793.85 | cash date 2023-09-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2262` | 2023-09-13 | settled | dining | 979886.38 | cash date 2023-09-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2227` | 2023-09-17 | settled | transport | 447746.71 | cash date 2023-09-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2263` | 2023-09-20 | settled | dining | 1028620.35 | cash date 2023-09-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2209` | 2023-09-21 | settled | groceries | 1510693.45 | cash date 2023-09-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2228` | 2023-09-22 | settled | transport | 579668.34 | cash date 2023-09-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2229` | 2023-09-27 | settled | transport | 636547.25 | cash date 2023-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2264` | 2023-09-27 | settled | dining | 1117067.23 | cash date 2023-09-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2210` | 2023-10-01 | settled | groceries | 1490390.69 | cash date 2023-10-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2168` | 2023-10-02 | settled | rent | 6954000 | cash date 2023-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2230` | 2023-10-02 | settled | transport | 724399.08 | cash date 2023-10-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2265` | 2023-10-04 | settled | dining | 756322.76 | cash date 2023-10-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2169` | 2023-10-06 | settled | utilities | 1338903.44 | cash date 2023-10-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2170` | 2023-10-07 | settled | insurance | 904400 | cash date 2023-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2231` | 2023-10-07 | settled | transport | 591314.74 | cash date 2023-10-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2172` | 2023-10-09 | settled | streaming | 573800 | cash date 2023-10-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2211` | 2023-10-11 | settled | groceries | 1211444.04 | cash date 2023-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2266` | 2023-10-11 | settled | dining | 1249486.33 | cash date 2023-10-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2171` | 2023-10-12 | settled | cloud_storage | 126350 | cash date 2023-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2173` | 2023-10-12 | settled | shopping | 966785.96 | cash date 2023-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2232` | 2023-10-12 | settled | transport | 458415.57 | cash date 2023-10-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2174` | 2023-10-14 | settled | entertainment | 451681.59 | cash date 2023-10-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2167` | 2023-10-15 | settled | salary | 28499994 | cash date 2023-10-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2233` | 2023-10-17 | settled | transport | 445484.16 | cash date 2023-10-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2267` | 2023-10-18 | settled | dining | 1232054.29 | cash date 2023-10-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2212` | 2023-10-21 | settled | groceries | 1048982.51 | cash date 2023-10-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2234` | 2023-10-22 | settled | transport | 617815.52 | cash date 2023-10-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2268` | 2023-10-25 | settled | dining | 1115260.36 | cash date 2023-10-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2235` | 2023-10-27 | settled | transport | 567772.41 | cash date 2023-10-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2213` | 2023-10-31 | settled | groceries | 1066197.78 | cash date 2023-10-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2236` | 2023-11-01 | settled | transport | 507090.88 | cash date 2023-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2269` | 2023-11-01 | settled | dining | 1261355.55 | cash date 2023-11-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2176` | 2023-11-02 | settled | rent | 6954000 | cash date 2023-11-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2177` | 2023-11-06 | settled | utilities | 1401205.21 | cash date 2023-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2237` | 2023-11-06 | settled | transport | 454432.04 | cash date 2023-11-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2178` | 2023-11-07 | settled | insurance | 904400 | cash date 2023-11-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2270` | 2023-11-08 | settled | dining | 921922.8 | cash date 2023-11-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2180` | 2023-11-09 | settled | streaming | 573800 | cash date 2023-11-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2214` | 2023-11-10 | settled | groceries | 893559.78 | cash date 2023-11-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2238` | 2023-11-11 | settled | transport | 617984.73 | cash date 2023-11-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2179` | 2023-11-12 | settled | cloud_storage | 126350 | cash date 2023-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2181` | 2023-11-12 | settled | shopping | 1054608.5 | cash date 2023-11-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2182` | 2023-11-14 | settled | entertainment | 415734.51 | cash date 2023-11-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2175` | 2023-11-15 | settled | salary | 28499994 | cash date 2023-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2271` | 2023-11-15 | settled | dining | 1142868.87 | cash date 2023-11-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2239` | 2023-11-16 | settled | transport | 557483.97 | cash date 2023-11-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2215` | 2023-11-20 | settled | groceries | 1252001.65 | cash date 2023-11-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2240` | 2023-11-21 | settled | transport | 627417.61 | cash date 2023-11-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2272` | 2023-11-22 | settled | dining | 897310.27 | cash date 2023-11-22 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2241` | 2023-11-26 | settled | transport | 547424.01 | cash date 2023-11-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2273` | 2023-11-29 | settled | dining | 740801.32 | cash date 2023-11-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2216` | 2023-11-30 | settled | groceries | 1101344.82 | cash date 2023-11-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2242` | 2023-12-01 | settled | transport | 522613.77 | cash date 2023-12-01 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2184` | 2023-12-02 | settled | rent | 6954000 | cash date 2023-12-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2185` | 2023-12-06 | settled | utilities | 1334719.89 | cash date 2023-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2243` | 2023-12-06 | settled | transport | 695049.46 | cash date 2023-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2274` | 2023-12-06 | settled | dining | 1022655.76 | cash date 2023-12-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2186` | 2023-12-07 | settled | insurance | 904400 | cash date 2023-12-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2188` | 2023-12-09 | settled | streaming | 573800 | cash date 2023-12-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2217` | 2023-12-10 | settled | groceries | 876032.86 | cash date 2023-12-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2244` | 2023-12-11 | settled | transport | 721981.78 | cash date 2023-12-11 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2187` | 2023-12-12 | settled | cloud_storage | 126350 | cash date 2023-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2189` | 2023-12-12 | settled | shopping | 1000693.22 | cash date 2023-12-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2275` | 2023-12-13 | settled | dining | 1128974.93 | cash date 2023-12-13 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2190` | 2023-12-14 | settled | entertainment | 499510.22 | cash date 2023-12-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2183` | 2023-12-15 | settled | salary | 28499994 | cash date 2023-12-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2245` | 2023-12-16 | settled | transport | 732740.37 | cash date 2023-12-16 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2218` | 2023-12-20 | settled | groceries | 917586.64 | cash date 2023-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2276` | 2023-12-20 | settled | dining | 956749.83 | cash date 2023-12-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2246` | 2023-12-21 | settled | transport | 593848.06 | cash date 2023-12-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2247` | 2023-12-26 | settled | transport | 639058 | cash date 2023-12-26 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2277` | 2023-12-27 | settled | dining | 1095978.2 | cash date 2023-12-27 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2219` | 2023-12-30 | settled | groceries | 1454933.56 | cash date 2023-12-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2248` | 2023-12-31 | settled | transport | 721837.88 | cash date 2023-12-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2192` | 2024-01-02 | settled | rent | 6954000 | cash date 2024-01-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2278` | 2024-01-03 | settled | dining | 868921.02 | cash date 2024-01-03 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2249` | 2024-01-05 | settled | transport | 637250.91 | cash date 2024-01-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2193` | 2024-01-06 | settled | utilities | 1341541.39 | cash date 2024-01-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2194` | 2024-01-07 | settled | insurance | 904400 | cash date 2024-01-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2196` | 2024-01-09 | settled | streaming | 573800 | cash date 2024-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2220` | 2024-01-09 | settled | groceries | 983053.43 | cash date 2024-01-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2250` | 2024-01-10 | settled | transport | 562442.16 | cash date 2024-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2279` | 2024-01-10 | settled | dining | 925855.11 | cash date 2024-01-10 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2195` | 2024-01-12 | settled | cloud_storage | 126350 | cash date 2024-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2197` | 2024-01-12 | settled | shopping | 1102784.74 | cash date 2024-01-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2198` | 2024-01-14 | settled | entertainment | 504697.37 | cash date 2024-01-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2191` | 2024-01-15 | settled | salary | 28499994 | cash date 2024-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2251` | 2024-01-15 | settled | transport | 542331.16 | cash date 2024-01-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2280` | 2024-01-17 | settled | dining | 1204804.45 | cash date 2024-01-17 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2221` | 2024-01-19 | settled | groceries | 1388569.11 | cash date 2024-01-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2252` | 2024-01-20 | settled | transport | 463292.75 | cash date 2024-01-20 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2281` | 2024-01-24 | settled | dining | 1057617.64 | cash date 2024-01-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2253` | 2024-01-25 | settled | transport | 745983.26 | cash date 2024-01-25 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2222` | 2024-01-29 | settled | groceries | 1335295.2 | cash date 2024-01-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2254` | 2024-01-30 | settled | transport | 549524.6 | cash date 2024-01-30 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2282` | 2024-01-31 | settled | dining | 1251981.8 | cash date 2024-01-31 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2200` | 2024-02-02 | settled | rent | 6954000 | cash date 2024-02-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2255` | 2024-02-04 | settled | transport | 664768.21 | cash date 2024-02-04 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2201` | 2024-02-06 | settled | utilities | 1201903.67 | cash date 2024-02-06 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2202` | 2024-02-07 | settled | insurance | 904400 | cash date 2024-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2283` | 2024-02-07 | settled | dining | 949118.03 | cash date 2024-02-07 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2223` | 2024-02-08 | settled | groceries | 1369082.68 | cash date 2024-02-08 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2204` | 2024-02-09 | settled | streaming | 573800 | cash date 2024-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2256` | 2024-02-09 | settled | transport | 448075.32 | cash date 2024-02-09 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2203` | 2024-02-12 | settled | cloud_storage | 126350 | cash date 2024-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2205` | 2024-02-12 | settled | shopping | 1170271.29 | cash date 2024-02-12 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2206` | 2024-02-14 | settled | entertainment | 426338.4 | cash date 2024-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2257` | 2024-02-14 | settled | transport | 560613.2 | cash date 2024-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2284` | 2024-02-14 | settled | dining | 1051249.87 | cash date 2024-02-14 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2199` | 2024-02-15 | settled | salary | 28499994 | cash date 2024-02-15 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2224` | 2024-02-18 | settled | groceries | 864688.59 | cash date 2024-02-18 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2258` | 2024-02-19 | settled | transport | 458596.67 | cash date 2024-02-19 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2285` | 2024-02-21 | settled | dining | 777034.83 | cash date 2024-02-21 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2259` | 2024-02-24 | settled | transport | 663001.49 | cash date 2024-02-24 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2225` | 2024-02-28 | settled | groceries | 1472349.1 | cash date 2024-02-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2286` | 2024-02-28 | settled | dining | 1133036.68 | cash date 2024-02-28 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2260` | 2024-02-29 | settled | transport | 729004.44 | cash date 2024-02-29 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2207` | 2024-03-02 | settled | rent | 6954000 | cash date 2024-03-02 is already reflected in the as-of balance; retained only as potential recurrence evidence |
| `event_2287` | 2024-03-04 | failed | utilities |  | failed event |
| `event_2261` | 2024-03-05 | settled | transport | 571596.93 | cash date 2024-03-05 is already reflected in the as-of balance; retained only as potential recurrence evidence |

### Relevant evidence

#### Messages

| Message | Sent | Related event | Source | Text |
| --- | --- | --- | --- | --- |
| — | — | — | — | None |

#### Images

| Image | Related event | Request |
| --- | --- | --- |
| — | — | None |

#### Linked events

| Event | Linked event | Status | Type |
| --- | --- | --- | --- |
| — | — | — | None |

#### Payment options

| Option | Method | Schedule | Fee | Total payable |
| --- | --- | --- | ---: | ---: |
| `payment_option_69` | full_payment | 2024-03-06:60496000 | 0 | 60496000 |
| `payment_option_70` | installments | 2024-03-09:4436373.33\|2024-04-08:4436373.33\|2024-05-08:4436373.33\|2024-06-07:4436373.33\|2024-07-07:4436373.33\|2024-08-06:4436373.33\|2024-09-05:4436373.33\|2024-10-05:4436373.33\|2024-11-04:4436373.33\|2024-12-04:4436373.33\|2025-01-03:4436373.33\|2025-02-02:4436373.33\|2025-03-04:4436373.33\|2025-04-03:4436373.33\|2025-05-03:4436373.33 | 6049599.95 | 66545599.95 |
| `payment_option_71` | installments | 2024-03-20:3075213.33\|2024-04-17:3075213.33\|2024-05-15:3075213.33\|2024-06-12:3075213.33\|2024-07-10:3075213.33\|2024-08-07:3075213.33\|2024-09-04:3075213.33\|2024-10-02:3075213.33\|2024-10-30:3075213.33\|2024-11-27:3075213.33\|2024-12-25:3075213.33\|2025-01-22:3075213.33\|2025-02-19:3075213.33\|2025-03-19:3075213.33\|2025-04-16:3075213.33\|2025-05-14:3075213.33\|2025-06-11:3075213.33\|2025-07-09:3075213.33\|2025-08-06:3075213.33\|2025-09-03:3075213.33\|2025-10-01:3075213.33\|2025-10-29:3075213.33\|2025-11-26:3075213.33\|2025-12-24:3075213.33 | 13309119.92 | 73805119.92 |

