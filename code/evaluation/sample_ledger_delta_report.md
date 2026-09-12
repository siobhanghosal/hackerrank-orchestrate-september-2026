# Sample ledger delta report

This diagnostic uses solved sample fields only for expected/actual comparison. Prediction, ledger assembly, and candidate selection never read those labels.

- Structured failures: **21/25**
- Structured exact matches: **94/175**

| Field | Exact matches |
| --- | ---: |
| `amount_safe_to_pay` | 4/25 |
| `affordability_status` | 19/25 |
| `recommended_payment_method` | 21/25 |
| `payment_plan` | 16/25 |
| `earliest_date_for_full_payment` | 12/25 |
| `spending_changes_needed` | 22/25 |

## request_02 - user_02

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 17229139.2 | 16237972.2 |

### Balance diagnostics

- Current balance: `60383889.2` IDR
- Required minimum: `29158400` IDR
- Baseline minimum before request payment: `45396372.2` on `2025-08-14`
- Computed safe amount now: `16237972.2`
- Computed earliest safe full-payment date: `2025-09-15`
- Immediate-full first breach: `2025-08-05` after `request_payment`, closing at `14365889.2`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-08-06 | debit | -2141849.94 | 60383889.2 | 58242039.26 | `recurring:utilities` | recurring | `event_122`, `event_130`, `event_138` | - | history supports a fixed 30-day recurrence |
| 2 | 2025-08-07 | debit | -1132400 | 58242039.26 | 57109639.26 | `recurring:insurance` | recurring | `event_123`, `event_131`, `event_139` | - | history supports a fixed 30-day recurrence |
| 3 | 2025-08-08 | debit | -1651100 | 57109639.26 | 55458539.26 | `event_185` | explicit | `event_185` | - | pending debit retained as a conservative liability |
| 4 | 2025-08-08 | debit | -3040000 | 55458539.26 | 52418539.26 | `recurring:education` | recurring | `event_124`, `event_132`, `event_140` | - | history supports a fixed 30-day recurrence |
| 5 | 2025-08-10 | debit | -1641668.72 | 52418539.26 | 50776870.54 | `recurring:healthcare` | recurring | `event_125`, `event_133`, `event_141` | - | history supports a fixed 30-day recurrence |
| 6 | 2025-08-12 | debit | -369550 | 50776870.54 | 50407320.54 | `recurring:cloud_storage` | recurring | `event_127`, `event_135`, `event_143` | - | history supports a fixed 30-day recurrence |
| 7 | 2025-08-12 | debit | -1440242.94 | 50407320.54 | 48967077.6 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 8 | 2025-08-14 | debit | -1352563.79 | 48967077.6 | 47614513.81 | `recurring:entertainment` | recurring | `event_126`, `event_134`, `event_142` | - | history supports a fixed 30-day recurrence |
| 9 | 2025-08-14 | debit | -2218141.61 | 47614513.81 | 45396372.2 | `recurring:groceries` | recurring | `event_153`, `event_156`, `event_160` | - | history supports a fixed 35-day recurrence |
| 10 | 2025-08-15 | credit | 42750000 | 45396372.2 | 88146372.2 | `recurring:salary` | recurring | `event_120`, `event_128`, `event_136` | `message_01` | history supports a fixed 30-day recurrence |
| 11 | 2025-08-26 | debit | -1440242.94 | 88146372.2 | 86706129.26 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 12 | 2025-09-03 | debit | -3534000 | 86706129.26 | 83172129.26 | `recurring:housing` | recurring | `event_129`, `event_137`, `event_144` | - | history supports a fixed 30-day recurrence |
| 13 | 2025-09-05 | debit | -2141849.94 | 83172129.26 | 81030279.32 | `recurring:utilities` | recurring | `event_122`, `event_130`, `event_138` | - | history supports a fixed 30-day recurrence |
| 14 | 2025-09-06 | debit | -1132400 | 81030279.32 | 79897879.32 | `recurring:insurance` | recurring | `event_123`, `event_131`, `event_139` | - | history supports a fixed 30-day recurrence |
| 15 | 2025-09-07 | debit | -3040000 | 79897879.32 | 76857879.32 | `recurring:education` | recurring | `event_124`, `event_132`, `event_140` | - | history supports a fixed 30-day recurrence |
| 16 | 2025-09-09 | debit | -1641668.72 | 76857879.32 | 75216210.6 | `recurring:healthcare` | recurring | `event_125`, `event_133`, `event_141` | - | history supports a fixed 30-day recurrence |
| 17 | 2025-09-09 | debit | -1440242.94 | 75216210.6 | 73775967.66 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 18 | 2025-09-11 | debit | -369550 | 73775967.66 | 73406417.66 | `recurring:cloud_storage` | recurring | `event_127`, `event_135`, `event_143` | - | history supports a fixed 30-day recurrence |
| 19 | 2025-09-13 | debit | -1352563.79 | 73406417.66 | 72053853.87 | `recurring:entertainment` | recurring | `event_126`, `event_134`, `event_142` | - | history supports a fixed 30-day recurrence |
| 20 | 2025-09-14 | credit | 42750000 | 72053853.87 | 114803853.87 | `recurring:salary` | recurring | `event_120`, `event_128`, `event_136` | `message_01` | history supports a fixed 30-day recurrence |
| 21 | 2025-09-18 | debit | -2218141.61 | 114803853.87 | 112585712.26 | `recurring:groceries` | recurring | `event_153`, `event_156`, `event_160` | - | history supports a fixed 35-day recurrence |
| 22 | 2025-09-23 | debit | -1440242.94 | 112585712.26 | 111145469.32 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 23 | 2025-10-03 | debit | -3534000 | 111145469.32 | 107611469.32 | `recurring:housing` | recurring | `event_129`, `event_137`, `event_144` | - | history supports a fixed 30-day recurrence |
| 24 | 2025-10-05 | debit | -2141849.94 | 107611469.32 | 105469619.38 | `recurring:utilities` | recurring | `event_122`, `event_130`, `event_138` | - | history supports a fixed 30-day recurrence |
| 25 | 2025-10-06 | debit | -1132400 | 105469619.38 | 104337219.38 | `recurring:insurance` | recurring | `event_123`, `event_131`, `event_139` | - | history supports a fixed 30-day recurrence |
| 26 | 2025-10-07 | debit | -3040000 | 104337219.38 | 101297219.38 | `recurring:education` | recurring | `event_124`, `event_132`, `event_140` | - | history supports a fixed 30-day recurrence |
| 27 | 2025-10-07 | debit | -1440242.94 | 101297219.38 | 99856976.44 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 28 | 2025-10-09 | debit | -1641668.72 | 99856976.44 | 98215307.72 | `recurring:healthcare` | recurring | `event_125`, `event_133`, `event_141` | - | history supports a fixed 30-day recurrence |
| 29 | 2025-10-11 | debit | -369550 | 98215307.72 | 97845757.72 | `recurring:cloud_storage` | recurring | `event_127`, `event_135`, `event_143` | - | history supports a fixed 30-day recurrence |
| 30 | 2025-10-13 | debit | -1352563.79 | 97845757.72 | 96493193.93 | `recurring:entertainment` | recurring | `event_126`, `event_134`, `event_142` | - | history supports a fixed 30-day recurrence |
| 31 | 2025-10-14 | credit | 42750000 | 96493193.93 | 139243193.93 | `recurring:salary` | recurring | `event_120`, `event_128`, `event_136` | `message_01` | history supports a fixed 30-day recurrence |
| 32 | 2025-10-21 | debit | -1440242.94 | 139243193.93 | 137802950.99 | `recurring:transport` | recurring | `event_166`, `event_167`, `event_168` | - | history supports a fixed 14-day recurrence |
| 33 | 2025-10-23 | debit | -2218141.61 | 137802950.99 | 135584809.38 | `recurring:groceries` | recurring | `event_153`, `event_156`, `event_160` | - | history supports a fixed 35-day recurrence |
| 34 | 2025-11-02 | debit | -3534000 | 135584809.38 | 132050809.38 | `recurring:housing` | recurring | `event_129`, `event_137`, `event_144` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_104` | 2025-03-15 | credit | 33345000 | already reflected in the current balance; may remain recurrence evidence |
| `event_105` | 2025-03-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_106` | 2025-03-07 | debit | 2143659.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_107` | 2025-03-08 | debit | 1132400 | already reflected in the current balance; may remain recurrence evidence |
| `event_108` | 2025-03-09 | debit | 3040000 | already reflected in the current balance; may remain recurrence evidence |
| `event_109` | 2025-03-11 | debit | 1594883.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_110` | 2025-03-15 | debit | 1289187.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_111` | 2025-03-13 | debit | 369550 | already reflected in the current balance; may remain recurrence evidence |
| `event_112` | 2025-04-15 | credit | 33345000 | already reflected in the current balance; may remain recurrence evidence |
| `event_113` | 2025-04-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_114` | 2025-04-07 | debit | 2081730.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_115` | 2025-04-08 | debit | 1132400 | already reflected in the current balance; may remain recurrence evidence |
| `event_116` | 2025-04-09 | debit | 3040000 | already reflected in the current balance; may remain recurrence evidence |
| `event_117` | 2025-04-11 | debit | 1467514.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_118` | 2025-04-15 | debit | 1367779.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_119` | 2025-04-13 | debit | 369550 | already reflected in the current balance; may remain recurrence evidence |
| `event_120` | 2025-05-15 | credit | 33345000 | already reflected in the current balance; may remain recurrence evidence |
| `event_121` | 2025-05-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_122` | 2025-05-07 | debit | 1830311.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_123` | 2025-05-08 | debit | 1132400 | already reflected in the current balance; may remain recurrence evidence |
| `event_124` | 2025-05-09 | debit | 3040000 | already reflected in the current balance; may remain recurrence evidence |
| `event_125` | 2025-05-11 | debit | 1452405.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_126` | 2025-05-15 | debit | 1287628.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_127` | 2025-05-13 | debit | 369550 | already reflected in the current balance; may remain recurrence evidence |
| `event_128` | 2025-06-15 | credit | 33345000 | already reflected in the current balance; may remain recurrence evidence |
| `event_129` | 2025-06-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_130` | 2025-06-07 | debit | 1981601.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_131` | 2025-06-08 | debit | 1132400 | already reflected in the current balance; may remain recurrence evidence |
| `event_132` | 2025-06-09 | debit | 3040000 | already reflected in the current balance; may remain recurrence evidence |
| `event_133` | 2025-06-11 | debit | 1641668.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_134` | 2025-06-15 | debit | 1193699.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_135` | 2025-06-13 | debit | 369550 | already reflected in the current balance; may remain recurrence evidence |
| `event_136` | 2025-07-15 | credit | 33345000 | already reflected in the current balance; may remain recurrence evidence |
| `event_137` | 2025-07-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_138` | 2025-07-07 | debit | 2141849.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_139` | 2025-07-08 | debit | 1132400 | already reflected in the current balance; may remain recurrence evidence |
| `event_140` | 2025-07-09 | debit | 3040000 | already reflected in the current balance; may remain recurrence evidence |
| `event_141` | 2025-07-11 | debit | 1538498.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_142` | 2025-07-15 | debit | 1352563.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_143` | 2025-07-13 | debit | 369550 | already reflected in the current balance; may remain recurrence evidence |
| `event_144` | 2025-08-04 | debit | 3534000 | already reflected in the current balance; may remain recurrence evidence |
| `event_145` | 2025-02-10 | debit | 2477697.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_146` | 2025-02-20 | debit | 1667911.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_147` | 2025-03-02 | debit | 1418745.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_148` | 2025-03-12 | debit | 1455258.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_149` | 2025-03-22 | debit | 1920485.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_150` | 2025-04-01 | debit | 1630631.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_151` | 2025-04-11 | debit | 1664708.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_152` | 2025-04-21 | debit | 1478895.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_153` | 2025-05-01 | debit | 2192475.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_154` | 2025-05-11 | debit | 1852958.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_155` | 2025-05-21 | debit | 2030400.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_156` | 2025-05-31 | debit | 1611886.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_157` | 2025-06-10 | debit | 2158165.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_158` | 2025-06-20 | debit | 2222527.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_159` | 2025-06-30 | debit | 2079368.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_160` | 2025-07-10 | debit | 2218141.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_161` | 2025-07-20 | debit | 2365919.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_162` | 2025-07-30 | debit | 1913686.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_163` | 2025-02-11 | debit | 1373039.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_164` | 2025-02-25 | debit | 995704.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_165` | 2025-03-11 | debit | 1062246.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_166` | 2025-03-25 | debit | 1053078.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_167` | 2025-04-08 | debit | 1294200.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_168` | 2025-04-22 | debit | 1440242.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_169` | 2025-05-06 | debit | 1021628.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_170` | 2025-05-20 | debit | 1374936.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_171` | 2025-06-03 | debit | 1329347.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_172` | 2025-06-17 | debit | 1309608.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_173` | 2025-07-01 | debit | 1111352.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_174` | 2025-07-15 | debit | 1327886.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_175` | 2025-07-29 | debit | 1062310.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_176` | 2025-02-12 | debit | 1166644.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_177` | 2025-03-05 | debit | 1101709.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_178` | 2025-03-26 | debit | 935929.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_179` | 2025-04-16 | debit | 1271076.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_180` | 2025-05-07 | debit | 971169.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_181` | 2025-05-28 | debit | 1111388.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_182` | 2025-06-18 | debit | 947892.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_183` | 2025-07-09 | debit | 1043758.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_184` | 2025-07-30 | debit | 1204805.34 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| installments | 2025-08-08 | 2025-10-07 | 47858720.01 | 3 | `payment_option_05` | `(False, False, Decimal('47858720.01'), datetime.date(2025, 8, 8), 3, 'payment_option_05')` | selected |

## request_03 - user_03

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 873000 | 2190071.39 |
| `payment_plan` | 2019-11-15:5491000 | 2019-10-15:5491000 |
| `earliest_date_for_full_payment` | 2019-11-15 | 2019-10-15 |

### Balance diagnostics

- Current balance: `5810300` IDR
- Required minimum: `2668700` IDR
- Baseline minimum before request payment: `4858771.39` on `2019-09-13`
- Computed safe amount now: `2190071.39`
- Computed earliest safe full-payment date: `2019-10-15`
- Immediate-full first breach: `2019-09-03` after `request_payment`, closing at `319300`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2019-09-07 | debit | -95000 | 5810300 | 5715300 | `event_254` | explicit | `event_254` | - | pending debit retained as a conservative liability |
| 2 | 2019-09-07 | debit | -303042.45 | 5715300 | 5412257.55 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence |
| 3 | 2019-09-08 | debit | -234390.87 | 5412257.55 | 5177866.68 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 4 | 2019-09-10 | debit | -117800 | 5177866.68 | 5060066.68 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence |
| 5 | 2019-09-13 | debit | -20900 | 5060066.68 | 5039166.68 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence |
| 6 | 2019-09-13 | debit | -180395.29 | 5039166.68 | 4858771.39 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence |
| 7 | 2019-09-14 | credit | 4365000 | 4858771.39 | 9223771.39 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence |
| 8 | 2019-09-18 | debit | -234390.87 | 9223771.39 | 8989380.52 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 9 | 2019-09-28 | debit | -234390.87 | 8989380.52 | 8754989.65 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 10 | 2019-10-03 | debit | -1140000 | 8754989.65 | 7614989.65 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence |
| 11 | 2019-10-07 | debit | -303042.45 | 7614989.65 | 7311947.2 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence |
| 12 | 2019-10-08 | debit | -234390.87 | 7311947.2 | 7077556.33 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 13 | 2019-10-10 | debit | -117800 | 7077556.33 | 6959756.33 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence |
| 14 | 2019-10-13 | debit | -20900 | 6959756.33 | 6938856.33 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence |
| 15 | 2019-10-13 | debit | -180395.29 | 6938856.33 | 6758461.04 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence |
| 16 | 2019-10-14 | credit | 4365000 | 6758461.04 | 11123461.04 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence |
| 17 | 2019-10-18 | debit | -234390.87 | 11123461.04 | 10889070.17 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 18 | 2019-10-28 | debit | -234390.87 | 10889070.17 | 10654679.3 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 19 | 2019-11-02 | debit | -1140000 | 10654679.3 | 9514679.3 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence |
| 20 | 2019-11-06 | debit | -303042.45 | 9514679.3 | 9211636.85 | `recurring:utilities` | recurring | `event_200`, `event_206`, `event_213` | - | history supports a fixed 30-day recurrence |
| 21 | 2019-11-07 | debit | -234390.87 | 9211636.85 | 8977245.98 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 22 | 2019-11-09 | debit | -117800 | 8977245.98 | 8859445.98 | `recurring:streaming` | recurring | `event_202`, `event_208`, `event_215` | - | history supports a fixed 30-day recurrence |
| 23 | 2019-11-12 | debit | -20900 | 8859445.98 | 8838545.98 | `recurring:cloud_storage` | recurring | `event_201`, `event_207`, `event_214` | - | history supports a fixed 30-day recurrence |
| 24 | 2019-11-12 | debit | -180395.29 | 8838545.98 | 8658150.69 | `recurring:shopping` | recurring | `event_203`, `event_209`, `event_216` | - | history supports a fixed 30-day recurrence |
| 25 | 2019-11-13 | credit | 4365000 | 8658150.69 | 13023150.69 | `recurring:salary` | recurring | `event_198`, `event_204`, `event_210` | - | history supports a fixed 30-day recurrence |
| 26 | 2019-11-17 | debit | -234390.87 | 13023150.69 | 12788759.82 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 27 | 2019-11-27 | debit | -234390.87 | 12788759.82 | 12554368.95 | `recurring:groceries` | recurring | `event_217`, `event_218`, `event_219` | - | history supports a fixed 10-day recurrence |
| 28 | 2019-12-02 | debit | -1140000 | 12554368.95 | 11414368.95 | `recurring:rent` | recurring | `event_199`, `event_205`, `event_212` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_186` | 2019-04-15 | credit | 4365000 | already reflected in the current balance; may remain recurrence evidence |
| `event_187` | 2019-04-04 | debit | 1140000 | already reflected in the current balance; may remain recurrence evidence |
| `event_188` | 2019-04-08 | debit | 295330.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_189` | 2019-04-14 | debit | 20900 | already reflected in the current balance; may remain recurrence evidence |
| `event_190` | 2019-04-11 | debit | 117800 | already reflected in the current balance; may remain recurrence evidence |
| `event_191` | 2019-04-14 | debit | 151493.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_192` | 2019-05-15 | credit | 4365000 | already reflected in the current balance; may remain recurrence evidence |
| `event_193` | 2019-05-04 | debit | 1140000 | already reflected in the current balance; may remain recurrence evidence |
| `event_194` | 2019-05-08 | debit | 290684.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_195` | 2019-05-14 | debit | 20900 | already reflected in the current balance; may remain recurrence evidence |
| `event_196` | 2019-05-11 | debit | 117800 | already reflected in the current balance; may remain recurrence evidence |
| `event_197` | 2019-05-14 | debit | 184274.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_198` | 2019-06-15 | credit | 4365000 | already reflected in the current balance; may remain recurrence evidence |
| `event_199` | 2019-06-04 | debit | 1140000 | already reflected in the current balance; may remain recurrence evidence |
| `event_200` | 2019-06-08 | debit | 270537.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_201` | 2019-06-14 | debit | 20900 | already reflected in the current balance; may remain recurrence evidence |
| `event_202` | 2019-06-11 | debit | 117800 | already reflected in the current balance; may remain recurrence evidence |
| `event_203` | 2019-06-14 | debit | 153395.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_204` | 2019-07-15 | credit | 4365000 | already reflected in the current balance; may remain recurrence evidence |
| `event_205` | 2019-07-04 | debit | 1140000 | already reflected in the current balance; may remain recurrence evidence |
| `event_206` | 2019-07-08 | debit | 303042.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_207` | 2019-07-14 | debit | 20900 | already reflected in the current balance; may remain recurrence evidence |
| `event_208` | 2019-07-11 | debit | 117800 | already reflected in the current balance; may remain recurrence evidence |
| `event_209` | 2019-07-14 | debit | 173930.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_210` | 2019-08-15 | credit | 4365000 | already reflected in the current balance; may remain recurrence evidence |
| `event_211` | 2019-08-20 | credit | 1964250 | already reflected in the current balance; may remain recurrence evidence |
| `event_212` | 2019-08-04 | debit | 1140000 | already reflected in the current balance; may remain recurrence evidence |
| `event_213` | 2019-08-08 | debit | 262344.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_214` | 2019-08-14 | debit | 20900 | already reflected in the current balance; may remain recurrence evidence |
| `event_215` | 2019-08-11 | debit | 117800 | already reflected in the current balance; may remain recurrence evidence |
| `event_216` | 2019-08-14 | debit | 180395.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_217` | 2019-03-12 | debit | 159576.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_218` | 2019-03-22 | debit | 234390.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_219` | 2019-04-01 | debit | 230312.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_220` | 2019-04-11 | debit | 234602.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_221` | 2019-04-21 | debit | 209875.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_222` | 2019-05-01 | debit | 178469.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_223` | 2019-05-11 | debit | 180577.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_224` | 2019-05-21 | debit | 155851.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_225` | 2019-05-31 | debit | 188355.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_226` | 2019-06-10 | debit | 166710.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_227` | 2019-06-20 | debit | 171495.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_228` | 2019-06-30 | debit | 145691.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_229` | 2019-07-10 | debit | 171259.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_230` | 2019-07-20 | debit | 173004.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_231` | 2019-07-30 | debit | 214266.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_232` | 2019-08-09 | debit | 221578.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_233` | 2019-08-19 | debit | 240706.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_234` | 2019-08-29 | debit | 200238.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_235` | 2019-03-13 | debit | 81510.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_236` | 2019-04-03 | debit | 116319.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_237` | 2019-04-24 | debit | 71790.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_238` | 2019-05-15 | debit | 73531.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_239` | 2019-06-05 | debit | 106806.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_240` | 2019-06-26 | debit | 79693.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_241` | 2019-07-17 | debit | 83523.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_242` | 2019-08-07 | debit | 99961.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_243` | 2019-08-28 | debit | 106233.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_244` | 2019-03-09 | debit | 117456.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_245` | 2019-03-30 | debit | 141412.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_246` | 2019-04-20 | debit | 146236.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_247` | 2019-05-11 | debit | 132247.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_248` | 2019-06-01 | debit | 158476.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_249` | 2019-06-22 | debit | 175170.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_250` | 2019-07-13 | debit | 171303.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_251` | 2019-08-03 | debit | 171191.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_252` | 2019-08-24 | debit | 135718.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_253` | 2019-08-31 | credit | - | amount requires linked image review |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| wait | 2019-10-15 | 2019-10-15 | 5491000 | 1 | `-` | `(False, False, Decimal('5491000'), datetime.date(2019, 10, 15), 1, '')` | selected |

## request_04 - user_04

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 8401800 | 12693000 |
| `affordability_status` | affordable_later | affordable_now |
| `recommended_payment_method` | wait | full_payment |
| `payment_plan` | 2024-06-15:12693000 | 2024-06-04:12693000 |
| `earliest_date_for_full_payment` | 2024-06-15 | 2024-06-04 |

### Balance diagnostics

- Current balance: `52206950` IDR
- Required minimum: `30686600` IDR
- Baseline minimum before request payment: `47222480` on `2024-06-12`
- Computed safe amount now: `12693000`
- Computed earliest safe full-payment date: `2024-06-04`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-06-08 | debit | -1027900 | 52206950 | 51179050 | `recurring:gym` | recurring | `event_275`, `event_282`, `event_289` | - | history supports a fixed 30-day recurrence |
| 2 | 2024-06-09 | debit | -332500 | 51179050 | 50846550 | `recurring:music_subscription` | recurring | `event_273`, `event_280`, `event_287` | - | history supports a fixed 30-day recurrence |
| 3 | 2024-06-11 | debit | -1704300 | 50846550 | 49142250 | `event_357` | explicit | `event_357` | - | cash event |
| 4 | 2024-06-11 | debit | -377150 | 49142250 | 48765100 | `recurring:delivery_membership` | recurring | `event_274`, `event_281`, `event_288` | - | history supports a fixed 30-day recurrence |
| 5 | 2024-06-12 | debit | -1542620 | 48765100 | 47222480 | `recurring:entertainment` | recurring | `event_276`, `event_283`, `event_290` | - | history supports a fixed 30-day recurrence |
| 6 | 2024-06-14 | credit | 38190000 | 47222480 | 85412480 | `recurring:salary` | recurring | `event_269`, `event_277`, `event_284` | - | history supports a fixed 30-day recurrence |
| 7 | 2024-07-01 | debit | -12293000 | 85412480 | 73119480 | `recurring:rent` | recurring | `event_278`, `event_285`, `event_291` | - | history supports a fixed 30-day recurrence |
| 8 | 2024-07-04 | debit | -2033868.83 | 73119480 | 71085611.17 | `recurring:utilities` | recurring | `event_272`, `event_279`, `event_286` | - | history supports a fixed 30-day recurrence |
| 9 | 2024-07-08 | debit | -2102251.18 | 71085611.17 | 68983359.99 | `recurring:dining` | recurring | `event_349`, `event_351`, `event_354` | - | history supports a fixed 35-day recurrence |
| 10 | 2024-07-08 | debit | -1027900 | 68983359.99 | 67955459.99 | `recurring:gym` | recurring | `event_275`, `event_282`, `event_289` | - | history supports a fixed 30-day recurrence |
| 11 | 2024-07-09 | debit | -332500 | 67955459.99 | 67622959.99 | `recurring:music_subscription` | recurring | `event_273`, `event_280`, `event_287` | - | history supports a fixed 30-day recurrence |
| 12 | 2024-07-11 | debit | -377150 | 67622959.99 | 67245809.99 | `recurring:delivery_membership` | recurring | `event_274`, `event_281`, `event_288` | - | history supports a fixed 30-day recurrence |
| 13 | 2024-07-12 | debit | -1542620 | 67245809.99 | 65703189.99 | `recurring:entertainment` | recurring | `event_276`, `event_283`, `event_290` | - | history supports a fixed 30-day recurrence |
| 14 | 2024-07-14 | credit | 38190000 | 65703189.99 | 103893189.99 | `recurring:salary` | recurring | `event_269`, `event_277`, `event_284` | - | history supports a fixed 30-day recurrence |
| 15 | 2024-07-31 | debit | -12293000 | 103893189.99 | 91600189.99 | `recurring:rent` | recurring | `event_278`, `event_285`, `event_291` | - | history supports a fixed 30-day recurrence |
| 16 | 2024-08-03 | debit | -2033868.83 | 91600189.99 | 89566321.16 | `recurring:utilities` | recurring | `event_272`, `event_279`, `event_286` | - | history supports a fixed 30-day recurrence |
| 17 | 2024-08-07 | debit | -1027900 | 89566321.16 | 88538421.16 | `recurring:gym` | recurring | `event_275`, `event_282`, `event_289` | - | history supports a fixed 30-day recurrence |
| 18 | 2024-08-08 | debit | -332500 | 88538421.16 | 88205921.16 | `recurring:music_subscription` | recurring | `event_273`, `event_280`, `event_287` | - | history supports a fixed 30-day recurrence |
| 19 | 2024-08-10 | debit | -377150 | 88205921.16 | 87828771.16 | `recurring:delivery_membership` | recurring | `event_274`, `event_281`, `event_288` | - | history supports a fixed 30-day recurrence |
| 20 | 2024-08-11 | debit | -1542620 | 87828771.16 | 86286151.16 | `recurring:entertainment` | recurring | `event_276`, `event_283`, `event_290` | - | history supports a fixed 30-day recurrence |
| 21 | 2024-08-12 | debit | -2102251.18 | 86286151.16 | 84183899.98 | `recurring:dining` | recurring | `event_349`, `event_351`, `event_354` | - | history supports a fixed 35-day recurrence |
| 22 | 2024-08-13 | credit | 38190000 | 84183899.98 | 122373899.98 | `recurring:salary` | recurring | `event_269`, `event_277`, `event_284` | - | history supports a fixed 30-day recurrence |
| 23 | 2024-08-30 | debit | -12293000 | 122373899.98 | 110080899.98 | `recurring:rent` | recurring | `event_278`, `event_285`, `event_291` | - | history supports a fixed 30-day recurrence |
| 24 | 2024-09-02 | debit | -2033868.83 | 110080899.98 | 108047031.15 | `recurring:utilities` | recurring | `event_272`, `event_279`, `event_286` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_255` | 2024-01-15 | credit | 38190000 | already reflected in the current balance; may remain recurrence evidence |
| `event_256` | 2024-01-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_257` | 2024-01-05 | debit | 2017103.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_258` | 2024-01-10 | debit | 332500 | already reflected in the current balance; may remain recurrence evidence |
| `event_259` | 2024-01-12 | debit | 377150 | already reflected in the current balance; may remain recurrence evidence |
| `event_260` | 2024-01-09 | debit | 1027900 | already reflected in the current balance; may remain recurrence evidence |
| `event_261` | 2024-01-13 | debit | 1484369.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_262` | 2024-02-15 | credit | 38190000 | already reflected in the current balance; may remain recurrence evidence |
| `event_263` | 2024-02-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_264` | 2024-02-05 | debit | 1981052.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_265` | 2024-02-10 | debit | 332500 | already reflected in the current balance; may remain recurrence evidence |
| `event_266` | 2024-02-12 | debit | 377150 | already reflected in the current balance; may remain recurrence evidence |
| `event_267` | 2024-02-09 | debit | 1027900 | already reflected in the current balance; may remain recurrence evidence |
| `event_268` | 2024-02-13 | debit | 1375854.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_269` | 2024-03-15 | credit | 38190000 | already reflected in the current balance; may remain recurrence evidence |
| `event_270` | 2024-03-22 | credit | 10498464.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_271` | 2024-03-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_272` | 2024-03-05 | debit | 2033868.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_273` | 2024-03-10 | debit | 332500 | already reflected in the current balance; may remain recurrence evidence |
| `event_274` | 2024-03-12 | debit | 377150 | already reflected in the current balance; may remain recurrence evidence |
| `event_275` | 2024-03-09 | debit | 1027900 | already reflected in the current balance; may remain recurrence evidence |
| `event_276` | 2024-03-13 | debit | 1542620 | already reflected in the current balance; may remain recurrence evidence |
| `event_277` | 2024-04-15 | credit | 38190000 | already reflected in the current balance; may remain recurrence evidence |
| `event_278` | 2024-04-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_279` | 2024-04-05 | debit | 1980834.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_280` | 2024-04-10 | debit | 332500 | already reflected in the current balance; may remain recurrence evidence |
| `event_281` | 2024-04-12 | debit | 377150 | already reflected in the current balance; may remain recurrence evidence |
| `event_282` | 2024-04-09 | debit | 1027900 | already reflected in the current balance; may remain recurrence evidence |
| `event_283` | 2024-04-13 | debit | 1291303.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_284` | 2024-05-15 | credit | 38190000 | already reflected in the current balance; may remain recurrence evidence |
| `event_285` | 2024-05-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_286` | 2024-05-05 | debit | 2004118.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_287` | 2024-05-10 | debit | 332500 | already reflected in the current balance; may remain recurrence evidence |
| `event_288` | 2024-05-12 | debit | 377150 | already reflected in the current balance; may remain recurrence evidence |
| `event_289` | 2024-05-09 | debit | 1027900 | already reflected in the current balance; may remain recurrence evidence |
| `event_290` | 2024-05-13 | debit | 1231859.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_291` | 2024-06-01 | debit | 12293000 | already reflected in the current balance; may remain recurrence evidence |
| `event_292` | 2023-12-09 | debit | 1685953.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_293` | 2023-12-16 | debit | 1749986.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_294` | 2023-12-23 | debit | 1383275.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_295` | 2023-12-30 | debit | 1482897.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_296` | 2024-01-06 | debit | 1818044.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_297` | 2024-01-13 | debit | 1413898.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_298` | 2024-01-20 | debit | 1351288.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_299` | 2024-01-27 | debit | 1178544.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_300` | 2024-02-03 | debit | 1697006.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_301` | 2024-02-10 | debit | 1087788.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_302` | 2024-02-17 | debit | 1753801.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_303` | 2024-02-24 | debit | 1203621.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_304` | 2024-03-02 | debit | 1674003.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_305` | 2024-03-09 | debit | 1347842.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_306` | 2024-03-16 | debit | 1453711.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_307` | 2024-03-23 | debit | 1447770.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_308` | 2024-03-30 | debit | 1261462.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_309` | 2024-04-06 | debit | 1825667.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_310` | 2024-04-13 | debit | 1184189.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_311` | 2024-04-20 | debit | 1617937.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_312` | 2024-04-27 | debit | 1519414.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_313` | 2024-05-04 | debit | 1831437.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_314` | 2024-05-11 | debit | 1698278.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_315` | 2024-05-18 | debit | 1075064.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_316` | 2024-05-25 | debit | 1809752.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_317` | 2024-06-01 | debit | 1433695.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_318` | 2023-12-10 | debit | 649231.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_319` | 2023-12-17 | debit | 876705.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_320` | 2023-12-24 | debit | 825832.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_321` | 2023-12-31 | debit | 769694.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_322` | 2024-01-07 | debit | 841811.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_323` | 2024-01-14 | debit | 820888.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_324` | 2024-01-21 | debit | 870102.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_325` | 2024-01-28 | debit | 1011616.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_326` | 2024-02-04 | debit | 596927.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_327` | 2024-02-11 | debit | 595968.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_328` | 2024-02-18 | debit | 954666.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_329` | 2024-02-25 | debit | 843406.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_330` | 2024-03-03 | debit | 589707.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_331` | 2024-03-10 | debit | 997182.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_332` | 2024-03-17 | debit | 677221.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_333` | 2024-03-24 | debit | 889762.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_334` | 2024-03-31 | debit | 842011.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_335` | 2024-04-07 | debit | 1000668.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_336` | 2024-04-14 | debit | 935850.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_337` | 2024-04-21 | debit | 874634.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_338` | 2024-04-28 | debit | 766019.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_339` | 2024-05-05 | debit | 1030376.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_340` | 2024-05-12 | debit | 912938.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_341` | 2024-05-19 | debit | 853091.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_342` | 2024-05-26 | debit | 602450.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_343` | 2024-06-02 | debit | 1016425.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_344` | 2023-12-11 | debit | 2111827.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_345` | 2023-12-25 | debit | 1839656.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_346` | 2024-01-08 | debit | 1279029.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_347` | 2024-01-22 | debit | 2067659.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_348` | 2024-02-05 | debit | 1650545.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_349` | 2024-02-19 | debit | 1931412.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_350` | 2024-03-04 | debit | 1551598.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_351` | 2024-03-18 | debit | 2102251.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_352` | 2024-04-01 | debit | 1282286.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_353` | 2024-04-15 | debit | 1259307.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_354` | 2024-04-29 | debit | 1661337.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_355` | 2024-05-13 | debit | 1886856.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_356` | 2024-05-27 | debit | 2108488.15 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| full_payment | 2024-06-04 | 2024-06-04 | 12693000 | 1 | `payment_option_11` | `(False, False, Decimal('12693000'), datetime.date(2024, 6, 4), 1, 'payment_option_11')` | selected |

## request_05 - user_05

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 737 | 7006.21 |

### Balance diagnostics

- Current balance: `46475.1` ZAR
- Required minimum: `13100` ZAR
- Baseline minimum before request payment: `20106.21` on `2026-02-03`
- Computed safe amount now: `7006.21`
- Computed earliest safe full-payment date: ``
- Immediate-full first breach: `2026-01-08` after `recurring:healthcare`, closing at `12685.47`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-11-09 | debit | -722.37 | 46475.1 | 45752.73 | `recurring:healthcare` | recurring | `event_378`, `event_386`, `event_394` | - | history supports a fixed 30-day recurrence |
| 2 | 2025-11-10 | debit | -968 | 45752.73 | 44784.73 | `recurring:debt_repayment` | recurring | `event_377`, `event_385`, `event_393` | - | history supports a fixed 30-day recurrence |
| 3 | 2025-11-11 | debit | -113.3 | 44784.73 | 44671.43 | `recurring:cloud_storage` | recurring | `event_380`, `event_388`, `event_396` | - | history supports a fixed 30-day recurrence |
| 4 | 2025-11-11 | debit | -422.67 | 44671.43 | 44248.76 | `recurring:shopping` | recurring | `event_381`, `event_389`, `event_397` | - | history supports a fixed 30-day recurrence |
| 5 | 2025-11-12 | debit | -840.4 | 44248.76 | 43408.36 | `recurring:family_support` | recurring | `event_379`, `event_387`, `event_395` | - | history supports a fixed 30-day recurrence |
| 6 | 2025-12-03 | debit | -4972 | 43408.36 | 38436.36 | `recurring:rent` | recurring | `event_383`, `event_391`, `event_398` | - | history supports a fixed 31-day recurrence |
| 7 | 2025-12-05 | debit | -750.89 | 38436.36 | 37685.47 | `recurring:utilities` | recurring | `event_376`, `event_384`, `event_392` | - | history supports a fixed 30-day recurrence |
| 8 | 2025-12-09 | debit | -722.37 | 37685.47 | 36963.1 | `recurring:healthcare` | recurring | `event_378`, `event_386`, `event_394` | - | history supports a fixed 30-day recurrence |
| 9 | 2025-12-10 | debit | -968 | 36963.1 | 35995.1 | `recurring:debt_repayment` | recurring | `event_377`, `event_385`, `event_393` | - | history supports a fixed 30-day recurrence |
| 10 | 2025-12-11 | debit | -113.3 | 35995.1 | 35881.8 | `recurring:cloud_storage` | recurring | `event_380`, `event_388`, `event_396` | - | history supports a fixed 30-day recurrence |
| 11 | 2025-12-11 | debit | -422.67 | 35881.8 | 35459.13 | `recurring:shopping` | recurring | `event_381`, `event_389`, `event_397` | - | history supports a fixed 30-day recurrence |
| 12 | 2025-12-12 | debit | -840.4 | 35459.13 | 34618.73 | `recurring:family_support` | recurring | `event_379`, `event_387`, `event_395` | - | history supports a fixed 30-day recurrence |
| 13 | 2026-01-03 | debit | -4972 | 34618.73 | 29646.73 | `recurring:rent` | recurring | `event_383`, `event_391`, `event_398` | - | history supports a fixed 31-day recurrence |
| 14 | 2026-01-04 | debit | -750.89 | 29646.73 | 28895.84 | `recurring:utilities` | recurring | `event_376`, `event_384`, `event_392` | - | history supports a fixed 30-day recurrence |
| 15 | 2026-01-08 | debit | -722.37 | 28895.84 | 28173.47 | `recurring:healthcare` | recurring | `event_378`, `event_386`, `event_394` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-01-09 | debit | -968 | 28173.47 | 27205.47 | `recurring:debt_repayment` | recurring | `event_377`, `event_385`, `event_393` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-01-10 | debit | -113.3 | 27205.47 | 27092.17 | `recurring:cloud_storage` | recurring | `event_380`, `event_388`, `event_396` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-01-10 | debit | -422.67 | 27092.17 | 26669.5 | `recurring:shopping` | recurring | `event_381`, `event_389`, `event_397` | - | history supports a fixed 30-day recurrence |
| 19 | 2026-01-11 | debit | -840.4 | 26669.5 | 25829.1 | `recurring:family_support` | recurring | `event_379`, `event_387`, `event_395` | - | history supports a fixed 30-day recurrence |
| 20 | 2026-02-03 | debit | -4972 | 25829.1 | 20857.1 | `recurring:rent` | recurring | `event_383`, `event_391`, `event_398` | - | history supports a fixed 31-day recurrence |
| 21 | 2026-02-03 | debit | -750.89 | 20857.1 | 20106.21 | `recurring:utilities` | recurring | `event_376`, `event_384`, `event_392` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_358` | 2025-06-15 | credit | 14740 | already reflected in the current balance; may remain recurrence evidence |
| `event_359` | 2025-06-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_360` | 2025-06-06 | debit | 604.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_361` | 2025-06-11 | debit | 968 | already reflected in the current balance; may remain recurrence evidence |
| `event_362` | 2025-06-10 | debit | 777.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_363` | 2025-06-13 | debit | 840.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_364` | 2025-06-12 | debit | 113.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_365` | 2025-06-12 | debit | 379.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_366` | 2025-07-15 | credit | 14740 | already reflected in the current balance; may remain recurrence evidence |
| `event_367` | 2025-07-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_368` | 2025-07-06 | debit | 658.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_369` | 2025-07-11 | debit | 968 | already reflected in the current balance; may remain recurrence evidence |
| `event_370` | 2025-07-10 | debit | 641.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_371` | 2025-07-13 | debit | 840.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_372` | 2025-07-12 | debit | 113.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_373` | 2025-07-12 | debit | 404.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_374` | 2025-08-15 | credit | 14740 | already reflected in the current balance; may remain recurrence evidence |
| `event_375` | 2025-08-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_376` | 2025-08-06 | debit | 750.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_377` | 2025-08-11 | debit | 968 | already reflected in the current balance; may remain recurrence evidence |
| `event_378` | 2025-08-10 | debit | 632.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_379` | 2025-08-13 | debit | 840.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_380` | 2025-08-12 | debit | 113.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_381` | 2025-08-12 | debit | 422.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_382` | 2025-09-15 | credit | 14740 | already reflected in the current balance; may remain recurrence evidence |
| `event_383` | 2025-09-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_384` | 2025-09-06 | debit | 706.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_385` | 2025-09-11 | debit | 968 | already reflected in the current balance; may remain recurrence evidence |
| `event_386` | 2025-09-10 | debit | 721.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_387` | 2025-09-13 | debit | 840.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_388` | 2025-09-12 | debit | 113.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_389` | 2025-09-12 | debit | 420.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_390` | 2025-10-15 | credit | 14740 | already reflected in the current balance; may remain recurrence evidence |
| `event_391` | 2025-10-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_392` | 2025-10-06 | debit | 713.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_393` | 2025-10-11 | debit | 968 | already reflected in the current balance; may remain recurrence evidence |
| `event_394` | 2025-10-10 | debit | 722.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_395` | 2025-10-13 | debit | 840.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_396` | 2025-10-12 | debit | 113.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_397` | 2025-10-12 | debit | 362.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_398` | 2025-11-02 | debit | 4972 | already reflected in the current balance; may remain recurrence evidence |
| `event_399` | 2025-05-13 | debit | 784.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_400` | 2025-05-20 | debit | 818.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_401` | 2025-05-27 | debit | 680.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_402` | 2025-06-03 | debit | 530.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_403` | 2025-06-10 | debit | 695.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_404` | 2025-06-17 | debit | 835 | already reflected in the current balance; may remain recurrence evidence |
| `event_405` | 2025-06-24 | debit | 635.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_406` | 2025-07-01 | debit | 661.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_407` | 2025-07-08 | debit | 567.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_408` | 2025-07-15 | debit | 767.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_409` | 2025-07-22 | debit | 807.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_410` | 2025-07-29 | debit | 800.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_411` | 2025-08-05 | debit | 813.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_412` | 2025-08-12 | debit | 853.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_413` | 2025-08-19 | debit | 773.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_414` | 2025-08-26 | debit | 845.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_415` | 2025-09-02 | debit | 762.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_416` | 2025-09-09 | debit | 515.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_417` | 2025-09-16 | debit | 682.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_418` | 2025-09-23 | debit | 675.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_419` | 2025-09-30 | debit | 547.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_420` | 2025-10-07 | debit | 826.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_421` | 2025-10-14 | debit | 768.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_422` | 2025-10-21 | debit | 709.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_423` | 2025-10-28 | debit | 684.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_424` | 2025-11-04 | debit | 720.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_425` | 2025-05-14 | debit | 489.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_426` | 2025-05-28 | debit | 424.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_427` | 2025-06-11 | debit | 504.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_428` | 2025-06-25 | debit | 492.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_429` | 2025-07-09 | debit | 363.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_430` | 2025-07-23 | debit | 311 | already reflected in the current balance; may remain recurrence evidence |
| `event_431` | 2025-08-06 | debit | 431.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_432` | 2025-08-20 | debit | 354.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_433` | 2025-09-03 | debit | 485.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_434` | 2025-09-17 | debit | 411.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_435` | 2025-10-01 | debit | 377.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_436` | 2025-10-15 | debit | 352.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_437` | 2025-10-29 | debit | 388.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_438` | 2025-11-04 | debit | - | failed event |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_06 - user_06

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 603.3 | 620.4 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `payment_plan` | 2026-01-03:620.40 | 2026-01-03:620.4 |
| `earliest_date_for_full_payment` | 2026-01-15 | 2026-01-03 |
| `spending_changes_needed` | stop:event_476 | none |

### Balance diagnostics

- Current balance: `1942.4` EUR
- Required minimum: `800` EUR
- Baseline minimum before request payment: `1703.66` on `2026-01-14`
- Computed safe amount now: `620.4`
- Computed earliest safe full-payment date: `2026-01-03`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-01-06 | debit | -58.98 | 1942.4 | 1883.42 | `recurring:utilities` | recurring | `event_457`, `event_465`, `event_473` | - | history supports a fixed 30-day recurrence |
| 2 | 2026-01-07 | debit | -51.55 | 1883.42 | 1831.87 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 3 | 2026-01-07 | debit | -26 | 1831.87 | 1805.87 | `recurring:insurance` | recurring | `event_458`, `event_466`, `event_474` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-01-09 | debit | -19 | 1805.87 | 1786.87 | `recurring:streaming` | recurring | `event_460`, `event_468`, `event_476` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-01-12 | debit | -5 | 1786.87 | 1781.87 | `recurring:cloud_storage` | recurring | `event_459`, `event_467`, `event_475` | - | history supports a fixed 30-day recurrence |
| 6 | 2026-01-12 | debit | -39.88 | 1781.87 | 1741.99 | `recurring:shopping` | recurring | `event_461`, `event_469`, `event_477` | - | history supports a fixed 30-day recurrence |
| 7 | 2026-01-14 | debit | -38.33 | 1741.99 | 1703.66 | `recurring:entertainment` | recurring | `event_462`, `event_470`, `event_478` | - | history supports a fixed 30-day recurrence |
| 8 | 2026-01-14 | credit | 1037.52 | 1703.66 | 2741.18 | `recurring:salary` | recurring | `event_455`, `event_463`, `event_471` | `message_04` | history supports a fixed 30-day recurrence |
| 9 | 2026-01-17 | debit | -51.55 | 2741.18 | 2689.63 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 10 | 2026-01-27 | debit | -51.55 | 2689.63 | 2638.08 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 11 | 2026-02-01 | debit | -254.1 | 2638.08 | 2383.98 | `recurring:rent` | recurring | `event_456`, `event_464`, `event_472` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-02-05 | debit | -58.98 | 2383.98 | 2325 | `recurring:utilities` | recurring | `event_457`, `event_465`, `event_473` | - | history supports a fixed 30-day recurrence |
| 13 | 2026-02-06 | debit | -51.55 | 2325 | 2273.45 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 14 | 2026-02-06 | debit | -26 | 2273.45 | 2247.45 | `recurring:insurance` | recurring | `event_458`, `event_466`, `event_474` | - | history supports a fixed 30-day recurrence |
| 15 | 2026-02-08 | debit | -19 | 2247.45 | 2228.45 | `recurring:streaming` | recurring | `event_460`, `event_468`, `event_476` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-02-11 | debit | -5 | 2228.45 | 2223.45 | `recurring:cloud_storage` | recurring | `event_459`, `event_467`, `event_475` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-02-11 | debit | -39.88 | 2223.45 | 2183.57 | `recurring:shopping` | recurring | `event_461`, `event_469`, `event_477` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-02-13 | debit | -38.33 | 2183.57 | 2145.24 | `recurring:entertainment` | recurring | `event_462`, `event_470`, `event_478` | - | history supports a fixed 30-day recurrence |
| 19 | 2026-02-13 | credit | 1037.52 | 2145.24 | 3182.76 | `recurring:salary` | recurring | `event_455`, `event_463`, `event_471` | `message_04` | history supports a fixed 30-day recurrence |
| 20 | 2026-02-16 | debit | -51.55 | 3182.76 | 3131.21 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 21 | 2026-02-26 | debit | -51.55 | 3131.21 | 3079.66 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 22 | 2026-03-03 | debit | -254.1 | 3079.66 | 2825.56 | `recurring:rent` | recurring | `event_456`, `event_464`, `event_472` | - | history supports a fixed 30-day recurrence |
| 23 | 2026-03-07 | debit | -58.98 | 2825.56 | 2766.58 | `recurring:utilities` | recurring | `event_457`, `event_465`, `event_473` | - | history supports a fixed 30-day recurrence |
| 24 | 2026-03-08 | debit | -51.55 | 2766.58 | 2715.03 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 25 | 2026-03-08 | debit | -26 | 2715.03 | 2689.03 | `recurring:insurance` | recurring | `event_458`, `event_466`, `event_474` | - | history supports a fixed 30-day recurrence |
| 26 | 2026-03-10 | debit | -19 | 2689.03 | 2670.03 | `recurring:streaming` | recurring | `event_460`, `event_468`, `event_476` | - | history supports a fixed 30-day recurrence |
| 27 | 2026-03-13 | debit | -5 | 2670.03 | 2665.03 | `recurring:cloud_storage` | recurring | `event_459`, `event_467`, `event_475` | - | history supports a fixed 30-day recurrence |
| 28 | 2026-03-13 | debit | -39.88 | 2665.03 | 2625.15 | `recurring:shopping` | recurring | `event_461`, `event_469`, `event_477` | - | history supports a fixed 30-day recurrence |
| 29 | 2026-03-15 | debit | -38.33 | 2625.15 | 2586.82 | `recurring:entertainment` | recurring | `event_462`, `event_470`, `event_478` | - | history supports a fixed 30-day recurrence |
| 30 | 2026-03-15 | credit | 1037.52 | 2586.82 | 3624.34 | `recurring:salary` | recurring | `event_455`, `event_463`, `event_471` | `message_04` | history supports a fixed 30-day recurrence |
| 31 | 2026-03-18 | debit | -51.55 | 3624.34 | 3572.79 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 32 | 2026-03-28 | debit | -51.55 | 3572.79 | 3521.24 | `recurring:groceries` | recurring | `event_487`, `event_488`, `event_489` | - | history supports a fixed 10-day recurrence |
| 33 | 2026-04-02 | debit | -254.1 | 3521.24 | 3267.14 | `recurring:rent` | recurring | `event_456`, `event_464`, `event_472` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_439` | 2025-08-15 | credit | 1441 | already reflected in the current balance; may remain recurrence evidence |
| `event_440` | 2025-08-03 | debit | 254.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_441` | 2025-08-07 | debit | 58.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_442` | 2025-08-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_443` | 2025-08-13 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_444` | 2025-08-10 | debit | 19 | already reflected in the current balance; may remain recurrence evidence |
| `event_445` | 2025-08-13 | debit | 41.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_446` | 2025-08-15 | debit | 32.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_447` | 2025-09-15 | credit | 1441 | already reflected in the current balance; may remain recurrence evidence |
| `event_448` | 2025-09-03 | debit | 254.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_449` | 2025-09-07 | debit | 52.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_450` | 2025-09-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_451` | 2025-09-13 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_452` | 2025-09-10 | debit | 19 | already reflected in the current balance; may remain recurrence evidence |
| `event_453` | 2025-09-13 | debit | 46.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_454` | 2025-09-15 | debit | 35.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_455` | 2025-10-15 | credit | 1441 | already reflected in the current balance; may remain recurrence evidence |
| `event_456` | 2025-10-03 | debit | 254.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_457` | 2025-10-07 | debit | 58.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_458` | 2025-10-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_459` | 2025-10-13 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_460` | 2025-10-10 | debit | 19 | already reflected in the current balance; may remain recurrence evidence |
| `event_461` | 2025-10-13 | debit | 39.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_462` | 2025-10-15 | debit | 32.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_463` | 2025-11-15 | credit | 1037.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_464` | 2025-11-03 | debit | 254.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_465` | 2025-11-07 | debit | 56.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_466` | 2025-11-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_467` | 2025-11-13 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_468` | 2025-11-10 | debit | 19 | already reflected in the current balance; may remain recurrence evidence |
| `event_469` | 2025-11-13 | debit | 37.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_470` | 2025-11-15 | debit | 37.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_471` | 2025-12-15 | credit | 1037.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_472` | 2025-12-03 | debit | 254.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_473` | 2025-12-07 | debit | 51.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_474` | 2025-12-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_475` | 2025-12-13 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_476` | 2025-12-10 | debit | 19 | already reflected in the current balance; may remain recurrence evidence |
| `event_477` | 2025-12-13 | debit | 39.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_478` | 2025-12-15 | debit | 38.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_479` | 2025-07-11 | debit | 43.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_480` | 2025-07-21 | debit | 53.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_481` | 2025-07-31 | debit | 49.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_482` | 2025-08-10 | debit | 43.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_483` | 2025-08-20 | debit | 31.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_484` | 2025-08-30 | debit | 50.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_485` | 2025-09-09 | debit | 51.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_486` | 2025-09-19 | debit | 48.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_487` | 2025-09-29 | debit | 51.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_488` | 2025-10-09 | debit | 46.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_489` | 2025-10-19 | debit | 32.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_490` | 2025-10-29 | debit | 51.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_491` | 2025-11-08 | debit | 34 | already reflected in the current balance; may remain recurrence evidence |
| `event_492` | 2025-11-18 | debit | 45.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_493` | 2025-11-28 | debit | 51.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_494` | 2025-12-08 | debit | 40.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_495` | 2025-12-18 | debit | 52.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_496` | 2025-12-28 | debit | 32.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_497` | 2025-07-12 | debit | 23.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_498` | 2025-07-17 | debit | 23.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_499` | 2025-07-22 | debit | 24.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_500` | 2025-07-27 | debit | 19.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_501` | 2025-08-01 | debit | 32.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_502` | 2025-08-06 | debit | 27.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_503` | 2025-08-11 | debit | 28.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_504` | 2025-08-16 | debit | 26.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_505` | 2025-08-21 | debit | 27.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_506` | 2025-08-26 | debit | 31.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_507` | 2025-08-31 | debit | 27.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_508` | 2025-09-05 | debit | 29.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_509` | 2025-09-10 | debit | 21.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_510` | 2025-09-15 | debit | 29.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_511` | 2025-09-20 | debit | 28.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_512` | 2025-09-25 | debit | 31.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_513` | 2025-09-30 | debit | 21.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_514` | 2025-10-05 | debit | 28.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_515` | 2025-10-10 | debit | 28.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_516` | 2025-10-15 | debit | 22.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_517` | 2025-10-20 | debit | 28.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_518` | 2025-10-25 | debit | 23.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_519` | 2025-10-30 | debit | 29.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_520` | 2025-11-04 | debit | 24.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_521` | 2025-11-09 | debit | 31.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_522` | 2025-11-14 | debit | 30.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_523` | 2025-11-19 | debit | 27.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_524` | 2025-11-24 | debit | 32.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_525` | 2025-11-29 | debit | 27.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_526` | 2025-12-04 | debit | 29.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_527` | 2025-12-09 | debit | 19.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_528` | 2025-12-14 | debit | 25.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_529` | 2025-12-19 | debit | 24.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_530` | 2025-12-24 | debit | 21.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_531` | 2025-12-29 | debit | 32.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_532` | 2025-07-13 | debit | 53.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_533` | 2025-07-20 | debit | 50.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_534` | 2025-07-27 | debit | 34.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_535` | 2025-08-03 | debit | 42.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_536` | 2025-08-10 | debit | 48.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_537` | 2025-08-17 | debit | 46.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_538` | 2025-08-24 | debit | 38.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_539` | 2025-08-31 | debit | 37.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_540` | 2025-09-07 | debit | 40.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_541` | 2025-09-14 | debit | 43.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_542` | 2025-09-21 | debit | 56.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_543` | 2025-09-28 | debit | 48.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_544` | 2025-10-05 | debit | 37.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_545` | 2025-10-12 | debit | 47.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_546` | 2025-10-19 | debit | 54.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_547` | 2025-10-26 | debit | 53.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_548` | 2025-11-02 | debit | 32.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_549` | 2025-11-09 | debit | 43.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_550` | 2025-11-16 | debit | 37.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_551` | 2025-11-23 | debit | 55.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_552` | 2025-11-30 | debit | 57.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_553` | 2025-12-07 | debit | 45.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_554` | 2025-12-14 | debit | 36 | already reflected in the current balance; may remain recurrence evidence |
| `event_555` | 2025-12-21 | debit | 57.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_556` | 2025-12-28 | debit | 48.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_557` | 2025-12-31 | debit | - | cancelled event |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| full_payment | 2026-01-03 | 2026-01-03 | 620.4 | 1 | `payment_option_16` | `(False, False, Decimal('620.4'), datetime.date(2026, 1, 3), 1, 'payment_option_16')` | selected |

## request_07 - user_07

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 87170.56 | 98080.53 |
| `earliest_date_for_full_payment` | 2024-10-23 | 2024-10-24 |

### Balance diagnostics

- Current balance: `218945.56` INR
- Required minimum: `93000` INR
- Baseline minimum before request payment: `191080.53` on `2024-09-20`
- Computed safe amount now: `98080.53`
- Computed earliest safe full-payment date: `2024-10-24`
- Immediate-full first breach: `2024-09-05` after `request_payment`, closing at `21545.56`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-09-07 | debit | -7387.41 | 218945.56 | 211558.15 | `recurring:utilities` | recurring | `event_570`, `event_575`, `event_580` | - | history supports a fixed 30-day recurrence |
| 2 | 2024-09-12 | debit | -15650 | 211558.15 | 195908.15 | `recurring:debt_repayment` | recurring | `event_571`, `event_576`, `event_581` | - | history supports a fixed 30-day recurrence |
| 3 | 2024-09-12 | debit | -1005 | 195908.15 | 194903.15 | `recurring:music_subscription` | recurring | `event_572`, `event_577`, `event_582` | - | history supports a fixed 30-day recurrence |
| 4 | 2024-09-20 | debit | -3822.62 | 194903.15 | 191080.53 | `recurring:transport` | recurring | `event_602`, `event_603`, `event_604` | - | history supports a fixed 21-day recurrence |
| 5 | 2024-09-23 | credit | 149000 | 191080.53 | 340080.53 | `recurring:salary` | recurring | `event_568`, `event_573`, `event_578` | `message_05` | history supports a fixed 30-day recurrence |
| 6 | 2024-10-05 | debit | -34200 | 340080.53 | 305880.53 | `recurring:rent` | recurring | `event_574`, `event_579`, `event_583` | - | history supports a fixed 31-day recurrence |
| 7 | 2024-10-07 | debit | -7387.41 | 305880.53 | 298493.12 | `recurring:utilities` | recurring | `event_570`, `event_575`, `event_580` | - | history supports a fixed 30-day recurrence |
| 8 | 2024-10-11 | debit | -3822.62 | 298493.12 | 294670.5 | `recurring:transport` | recurring | `event_602`, `event_603`, `event_604` | - | history supports a fixed 21-day recurrence |
| 9 | 2024-10-12 | debit | -15650 | 294670.5 | 279020.5 | `recurring:debt_repayment` | recurring | `event_571`, `event_576`, `event_581` | - | history supports a fixed 30-day recurrence |
| 10 | 2024-10-12 | debit | -1005 | 279020.5 | 278015.5 | `recurring:music_subscription` | recurring | `event_572`, `event_577`, `event_582` | - | history supports a fixed 30-day recurrence |
| 11 | 2024-10-23 | credit | 149000 | 278015.5 | 427015.5 | `recurring:salary` | recurring | `event_568`, `event_573`, `event_578` | `message_05` | history supports a fixed 30-day recurrence |
| 12 | 2024-11-01 | debit | -3822.62 | 427015.5 | 423192.88 | `recurring:transport` | recurring | `event_602`, `event_603`, `event_604` | - | history supports a fixed 21-day recurrence |
| 13 | 2024-11-05 | debit | -34200 | 423192.88 | 388992.88 | `recurring:rent` | recurring | `event_574`, `event_579`, `event_583` | - | history supports a fixed 31-day recurrence |
| 14 | 2024-11-06 | debit | -7387.41 | 388992.88 | 381605.47 | `recurring:utilities` | recurring | `event_570`, `event_575`, `event_580` | - | history supports a fixed 30-day recurrence |
| 15 | 2024-11-11 | debit | -15650 | 381605.47 | 365955.47 | `recurring:debt_repayment` | recurring | `event_571`, `event_576`, `event_581` | - | history supports a fixed 30-day recurrence |
| 16 | 2024-11-11 | debit | -1005 | 365955.47 | 364950.47 | `recurring:music_subscription` | recurring | `event_572`, `event_577`, `event_582` | - | history supports a fixed 30-day recurrence |
| 17 | 2024-11-22 | debit | -3822.62 | 364950.47 | 361127.85 | `recurring:transport` | recurring | `event_602`, `event_603`, `event_604` | - | history supports a fixed 21-day recurrence |
| 18 | 2024-11-22 | credit | 149000 | 361127.85 | 510127.85 | `recurring:salary` | recurring | `event_568`, `event_573`, `event_578` | `message_05` | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_558` | 2024-04-15 | credit | 149000 | already reflected in the current balance; may remain recurrence evidence |
| `event_559` | 2024-04-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_560` | 2024-04-08 | debit | 7219.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_561` | 2024-04-13 | debit | 15650 | already reflected in the current balance; may remain recurrence evidence |
| `event_562` | 2024-04-13 | debit | 1005 | already reflected in the current balance; may remain recurrence evidence |
| `event_563` | 2024-05-15 | credit | 149000 | already reflected in the current balance; may remain recurrence evidence |
| `event_564` | 2024-05-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_565` | 2024-05-08 | debit | 7049.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_566` | 2024-05-13 | debit | 15650 | already reflected in the current balance; may remain recurrence evidence |
| `event_567` | 2024-05-13 | debit | 1005 | already reflected in the current balance; may remain recurrence evidence |
| `event_568` | 2024-06-15 | credit | 149000 | already reflected in the current balance; may remain recurrence evidence |
| `event_569` | 2024-06-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_570` | 2024-06-08 | debit | 7387.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_571` | 2024-06-13 | debit | 15650 | already reflected in the current balance; may remain recurrence evidence |
| `event_572` | 2024-06-13 | debit | 1005 | already reflected in the current balance; may remain recurrence evidence |
| `event_573` | 2024-07-15 | credit | 149000 | already reflected in the current balance; may remain recurrence evidence |
| `event_574` | 2024-07-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_575` | 2024-07-08 | debit | 6081.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_576` | 2024-07-13 | debit | 15650 | already reflected in the current balance; may remain recurrence evidence |
| `event_577` | 2024-07-13 | debit | 1005 | already reflected in the current balance; may remain recurrence evidence |
| `event_578` | 2024-08-23 | credit | 149000 | already reflected in the current balance; may remain recurrence evidence |
| `event_579` | 2024-08-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_580` | 2024-08-08 | debit | 6209.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_581` | 2024-08-13 | debit | 15650 | already reflected in the current balance; may remain recurrence evidence |
| `event_582` | 2024-08-13 | debit | 1005 | already reflected in the current balance; may remain recurrence evidence |
| `event_583` | 2024-09-04 | debit | 34200 | already reflected in the current balance; may remain recurrence evidence |
| `event_584` | 2024-03-14 | debit | 8380.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_585` | 2024-03-28 | debit | 6433.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_586` | 2024-04-11 | debit | 6022.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_587` | 2024-04-25 | debit | 6789.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_588` | 2024-05-09 | debit | 8280.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_589` | 2024-05-23 | debit | 7329.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_590` | 2024-06-06 | debit | 7849.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_591` | 2024-06-20 | debit | 7968.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_592` | 2024-07-04 | debit | 6889.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_593` | 2024-07-18 | debit | 5665.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_594` | 2024-08-01 | debit | 7913.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_595` | 2024-08-15 | debit | 7280.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_596` | 2024-08-29 | debit | 5710.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_597` | 2024-03-15 | debit | 3690.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_598` | 2024-04-05 | debit | 3465.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_599` | 2024-04-26 | debit | 2786.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_600` | 2024-05-17 | debit | 3104.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_601` | 2024-06-07 | debit | 2439.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_602` | 2024-06-28 | debit | 3822.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_603` | 2024-07-19 | debit | 2751.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_604` | 2024-08-09 | debit | 3773.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_605` | 2024-08-30 | debit | 3145.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_606` | 2024-03-11 | debit | 7246.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_607` | 2024-04-01 | debit | 4111.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_608` | 2024-04-22 | debit | 6371.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_609` | 2024-05-13 | debit | 6313.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_610` | 2024-06-03 | debit | 5802.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_611` | 2024-06-24 | debit | 4541.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_612` | 2024-07-15 | debit | 6664.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_613` | 2024-08-05 | debit | 5799.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_614` | 2024-08-26 | debit | 6493.86 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| installments | 2024-09-12 | 2024-11-07 | 205296 | 3 | `payment_option_19` | `(False, False, Decimal('205296'), datetime.date(2024, 9, 12), 3, 'payment_option_19')` | selected |

## request_08 - user_08

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 284.57 | 521.57 |
| `payment_plan` | 2025-04-15:996.60 | 2025-02-15:996.6 |
| `earliest_date_for_full_payment` | 2025-04-15 | 2025-02-15 |

### Balance diagnostics

- Current balance: `1536.57` EUR
- Required minimum: `800` EUR
- Baseline minimum before request payment: `1321.57` on `2025-02-11`
- Computed safe amount now: `521.57`
- Computed earliest safe full-payment date: `2025-02-15`
- Immediate-full first breach: `2025-02-07` after `request_payment`, closing at `539.97`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-02-09 | debit | -177 | 1536.57 | 1359.57 | `recurring:debt_repayment` | recurring | `event_633`, `event_640`, `event_647` | - | history supports a fixed 30-day recurrence |
| 2 | 2025-02-09 | debit | -14 | 1359.57 | 1345.57 | `recurring:music_subscription` | recurring | `event_634`, `event_641`, `event_648` | - | history supports a fixed 30-day recurrence |
| 3 | 2025-02-11 | debit | -24 | 1345.57 | 1321.57 | `recurring:delivery_membership` | recurring | `event_635`, `event_642`, `event_649` | - | history supports a fixed 30-day recurrence |
| 4 | 2025-02-14 | credit | 1422.85 | 1321.57 | 2744.42 | `recurring:salary` | recurring | `event_629`, `event_636`, `event_643` | `message_06` | history supports a fixed 30-day recurrence |
| 5 | 2025-03-04 | debit | -467.5 | 2744.42 | 2276.92 | `recurring:rent` | recurring | `event_637`, `event_644`, `event_650` | - | history supports a fixed 31-day recurrence |
| 6 | 2025-03-08 | debit | -89 | 2276.92 | 2187.92 | `recurring:education` | recurring | `event_632`, `event_639`, `event_646` | - | history supports a fixed 30-day recurrence |
| 7 | 2025-03-08 | debit | -82.61 | 2187.92 | 2105.31 | `recurring:utilities` | recurring | `event_638`, `event_645`, `event_651` | - | history supports a fixed 31-day recurrence |
| 8 | 2025-03-11 | debit | -177 | 2105.31 | 1928.31 | `recurring:debt_repayment` | recurring | `event_633`, `event_640`, `event_647` | - | history supports a fixed 30-day recurrence |
| 9 | 2025-03-11 | debit | -14 | 1928.31 | 1914.31 | `recurring:music_subscription` | recurring | `event_634`, `event_641`, `event_648` | - | history supports a fixed 30-day recurrence |
| 10 | 2025-03-13 | debit | -24 | 1914.31 | 1890.31 | `recurring:delivery_membership` | recurring | `event_635`, `event_642`, `event_649` | - | history supports a fixed 30-day recurrence |
| 11 | 2025-03-16 | credit | 1422.85 | 1890.31 | 3313.16 | `recurring:salary` | recurring | `event_629`, `event_636`, `event_643` | `message_06` | history supports a fixed 30-day recurrence |
| 12 | 2025-04-04 | debit | -467.5 | 3313.16 | 2845.66 | `recurring:rent` | recurring | `event_637`, `event_644`, `event_650` | - | history supports a fixed 31-day recurrence |
| 13 | 2025-04-07 | debit | -89 | 2845.66 | 2756.66 | `recurring:education` | recurring | `event_632`, `event_639`, `event_646` | - | history supports a fixed 30-day recurrence |
| 14 | 2025-04-08 | debit | -82.61 | 2756.66 | 2674.05 | `recurring:utilities` | recurring | `event_638`, `event_645`, `event_651` | - | history supports a fixed 31-day recurrence |
| 15 | 2025-04-10 | debit | -177 | 2674.05 | 2497.05 | `recurring:debt_repayment` | recurring | `event_633`, `event_640`, `event_647` | - | history supports a fixed 30-day recurrence |
| 16 | 2025-04-10 | debit | -14 | 2497.05 | 2483.05 | `recurring:music_subscription` | recurring | `event_634`, `event_641`, `event_648` | - | history supports a fixed 30-day recurrence |
| 17 | 2025-04-12 | debit | -24 | 2483.05 | 2459.05 | `recurring:delivery_membership` | recurring | `event_635`, `event_642`, `event_649` | - | history supports a fixed 30-day recurrence |
| 18 | 2025-04-15 | credit | 1422.85 | 2459.05 | 3881.9 | `recurring:salary` | recurring | `event_629`, `event_636`, `event_643` | `message_06` | history supports a fixed 30-day recurrence |
| 19 | 2025-05-05 | debit | -467.5 | 3881.9 | 3414.4 | `recurring:rent` | recurring | `event_637`, `event_644`, `event_650` | - | history supports a fixed 31-day recurrence |
| 20 | 2025-05-07 | debit | -89 | 3414.4 | 3325.4 | `recurring:education` | recurring | `event_632`, `event_639`, `event_646` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_615` | 2024-09-15 | credit | 1422.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_616` | 2024-09-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_617` | 2024-09-05 | debit | 79.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_618` | 2024-09-07 | debit | 89 | already reflected in the current balance; may remain recurrence evidence |
| `event_619` | 2024-09-10 | debit | 177 | already reflected in the current balance; may remain recurrence evidence |
| `event_620` | 2024-09-10 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_621` | 2024-09-12 | debit | 24 | already reflected in the current balance; may remain recurrence evidence |
| `event_622` | 2024-10-15 | credit | 1422.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_623` | 2024-10-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_624` | 2024-10-05 | debit | 80.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_625` | 2024-10-07 | debit | 89 | already reflected in the current balance; may remain recurrence evidence |
| `event_626` | 2024-10-10 | debit | 177 | already reflected in the current balance; may remain recurrence evidence |
| `event_627` | 2024-10-10 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_628` | 2024-10-12 | debit | 24 | already reflected in the current balance; may remain recurrence evidence |
| `event_629` | 2024-11-15 | credit | 1422.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_630` | 2024-11-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_631` | 2024-11-05 | debit | 68.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_632` | 2024-11-07 | debit | 89 | already reflected in the current balance; may remain recurrence evidence |
| `event_633` | 2024-11-10 | debit | 177 | already reflected in the current balance; may remain recurrence evidence |
| `event_634` | 2024-11-10 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_635` | 2024-11-12 | debit | 24 | already reflected in the current balance; may remain recurrence evidence |
| `event_636` | 2024-12-15 | credit | 1422.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_637` | 2024-12-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_638` | 2024-12-05 | debit | 82.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_639` | 2024-12-07 | debit | 89 | already reflected in the current balance; may remain recurrence evidence |
| `event_640` | 2024-12-10 | debit | 177 | already reflected in the current balance; may remain recurrence evidence |
| `event_641` | 2024-12-10 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_642` | 2024-12-12 | debit | 24 | already reflected in the current balance; may remain recurrence evidence |
| `event_643` | 2025-01-15 | credit | 782.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_644` | 2025-01-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_645` | 2025-01-05 | debit | 69.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_646` | 2025-01-07 | debit | 89 | already reflected in the current balance; may remain recurrence evidence |
| `event_647` | 2025-01-10 | debit | 177 | already reflected in the current balance; may remain recurrence evidence |
| `event_648` | 2025-01-10 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_649` | 2025-01-12 | debit | 24 | already reflected in the current balance; may remain recurrence evidence |
| `event_650` | 2025-02-01 | debit | 467.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_651` | 2025-02-05 | debit | 80.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_652` | 2024-08-13 | debit | 78.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_653` | 2024-08-20 | debit | 77.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_654` | 2024-08-27 | debit | 51.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_655` | 2024-09-03 | debit | 52.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_656` | 2024-09-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_657` | 2024-09-17 | debit | 54.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_658` | 2024-09-24 | debit | 46.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_659` | 2024-10-01 | debit | 74.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_660` | 2024-10-08 | debit | 48.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_661` | 2024-10-15 | debit | 68.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_662` | 2024-10-22 | debit | 57.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_663` | 2024-10-29 | debit | 47.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_664` | 2024-11-05 | debit | 51.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_665` | 2024-11-12 | debit | 76.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_666` | 2024-11-19 | debit | 69.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_667` | 2024-11-26 | debit | 60.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_668` | 2024-12-03 | debit | 51 | already reflected in the current balance; may remain recurrence evidence |
| `event_669` | 2024-12-10 | debit | 56.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_670` | 2024-12-17 | debit | 55.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_671` | 2024-12-24 | debit | 53.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_672` | 2024-12-31 | debit | 51.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_673` | 2025-01-07 | debit | 48 | already reflected in the current balance; may remain recurrence evidence |
| `event_674` | 2025-01-14 | debit | 45.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_675` | 2025-01-21 | debit | 53.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_676` | 2025-01-28 | debit | 65.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_677` | 2025-02-04 | debit | 72.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_678` | 2024-08-14 | debit | 34.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_679` | 2024-08-21 | debit | 36.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_680` | 2024-08-28 | debit | 41.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_681` | 2024-09-04 | debit | 40.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_682` | 2024-09-11 | debit | 37.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_683` | 2024-09-18 | debit | 43.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_684` | 2024-09-25 | debit | 30.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_685` | 2024-10-02 | debit | 36.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_686` | 2024-10-09 | debit | 38.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_687` | 2024-10-16 | debit | 26.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_688` | 2024-10-23 | debit | 46.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_689` | 2024-10-30 | debit | 45.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_690` | 2024-11-06 | debit | 39.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_691` | 2024-11-13 | debit | 37 | already reflected in the current balance; may remain recurrence evidence |
| `event_692` | 2024-11-20 | debit | 40.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_693` | 2024-11-27 | debit | 35.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_694` | 2024-12-04 | debit | 29.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_695` | 2024-12-11 | debit | 35.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_696` | 2024-12-18 | debit | 43.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_697` | 2024-12-25 | debit | 43.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_698` | 2025-01-01 | debit | 31.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_699` | 2025-01-08 | debit | 41.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_700` | 2025-01-15 | debit | 32.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_701` | 2025-01-22 | debit | 31.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_702` | 2025-01-29 | debit | 28.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_703` | 2025-02-05 | debit | 47.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_704` | 2024-08-15 | debit | 51.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_705` | 2024-08-29 | debit | 59.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_706` | 2024-09-12 | debit | 46.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_707` | 2024-09-26 | debit | 60.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_708` | 2024-10-10 | debit | 48.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_709` | 2024-10-24 | debit | 41.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_710` | 2024-11-07 | debit | 58.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_711` | 2024-11-21 | debit | 45.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_712` | 2024-12-05 | debit | 46.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_713` | 2024-12-19 | debit | 49.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_714` | 2025-01-02 | debit | 56.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_715` | 2025-01-16 | debit | 53.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_716` | 2025-01-30 | debit | 42.33 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| wait | 2025-02-15 | 2025-02-15 | 996.6 | 1 | `-` | `(False, False, Decimal('996.6'), datetime.date(2025, 2, 15), 1, '')` | selected |

## request_10 - user_10

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 12700 | 266700 |

### Balance diagnostics

- Current balance: `750155` INR
- Required minimum: `225400` INR
- Baseline minimum before request payment: `662531.18` on `2025-03-06`
- Computed safe amount now: `266700`
- Computed earliest safe full-payment date: `2024-12-06`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-12-08 | debit | -17771.13 | 750155 | 732383.87 | `recurring:utilities` | recurring | `event_814`, `event_824`, `event_834` | - | history supports a fixed 31-day recurrence |
| 2 | 2024-12-12 | debit | -4860 | 732383.87 | 727523.87 | `recurring:gym` | recurring | `event_817`, `event_827`, `event_837` | - | history supports a fixed 31-day recurrence |
| 3 | 2024-12-13 | debit | -2800 | 727523.87 | 724723.87 | `recurring:music_subscription` | recurring | `event_815`, `event_825`, `event_835` | - | history supports a fixed 31-day recurrence |
| 4 | 2024-12-15 | debit | -1895 | 724723.87 | 722828.87 | `recurring:delivery_membership` | recurring | `event_816`, `event_826`, `event_836` | - | history supports a fixed 31-day recurrence |
| 5 | 2024-12-16 | debit | -4883.78 | 722828.87 | 717945.09 | `recurring:entertainment` | recurring | `event_818`, `event_828`, `event_838` | - | history supports a fixed 31-day recurrence |
| 6 | 2024-12-20 | credit | 47802.51 | 717945.09 | 765747.6 | `recurring:salary` | recurring | `event_829`, `event_831`, `event_839` | - | history supports a fixed 16-day recurrence |
| 7 | 2025-01-01 | debit | -7568.88 | 765747.6 | 758178.72 | `recurring:transport` | recurring | `event_873`, `event_877`, `event_882` | - | history supports a fixed 32-day recurrence |
| 8 | 2025-01-02 | debit | -69100 | 758178.72 | 689078.72 | `recurring:rent` | recurring | `event_823`, `event_833`, `event_840` | - | history supports a fixed 30-day recurrence |
| 9 | 2025-01-05 | credit | 47802.51 | 689078.72 | 736881.23 | `recurring:salary` | recurring | `event_829`, `event_831`, `event_839` | - | history supports a fixed 16-day recurrence |
| 10 | 2025-01-08 | debit | -17771.13 | 736881.23 | 719110.1 | `recurring:utilities` | recurring | `event_814`, `event_824`, `event_834` | - | history supports a fixed 31-day recurrence |
| 11 | 2025-01-12 | debit | -4860 | 719110.1 | 714250.1 | `recurring:gym` | recurring | `event_817`, `event_827`, `event_837` | - | history supports a fixed 31-day recurrence |
| 12 | 2025-01-13 | debit | -2800 | 714250.1 | 711450.1 | `recurring:music_subscription` | recurring | `event_815`, `event_825`, `event_835` | - | history supports a fixed 31-day recurrence |
| 13 | 2025-01-15 | debit | -1895 | 711450.1 | 709555.1 | `recurring:delivery_membership` | recurring | `event_816`, `event_826`, `event_836` | - | history supports a fixed 31-day recurrence |
| 14 | 2025-01-16 | debit | -4883.78 | 709555.1 | 704671.32 | `recurring:entertainment` | recurring | `event_818`, `event_828`, `event_838` | - | history supports a fixed 31-day recurrence |
| 15 | 2025-01-21 | credit | 47802.51 | 704671.32 | 752473.83 | `recurring:salary` | recurring | `event_829`, `event_831`, `event_839` | - | history supports a fixed 16-day recurrence |
| 16 | 2025-02-01 | debit | -69100 | 752473.83 | 683373.83 | `recurring:rent` | recurring | `event_823`, `event_833`, `event_840` | - | history supports a fixed 30-day recurrence |
| 17 | 2025-02-02 | debit | -7568.88 | 683373.83 | 675804.95 | `recurring:transport` | recurring | `event_873`, `event_877`, `event_882` | - | history supports a fixed 32-day recurrence |
| 18 | 2025-02-06 | credit | 47802.51 | 675804.95 | 723607.46 | `recurring:salary` | recurring | `event_829`, `event_831`, `event_839` | - | history supports a fixed 16-day recurrence |
| 19 | 2025-02-08 | debit | -17771.13 | 723607.46 | 705836.33 | `recurring:utilities` | recurring | `event_814`, `event_824`, `event_834` | - | history supports a fixed 31-day recurrence |
| 20 | 2025-02-12 | debit | -4860 | 705836.33 | 700976.33 | `recurring:gym` | recurring | `event_817`, `event_827`, `event_837` | - | history supports a fixed 31-day recurrence |
| 21 | 2025-02-13 | debit | -2800 | 700976.33 | 698176.33 | `recurring:music_subscription` | recurring | `event_815`, `event_825`, `event_835` | - | history supports a fixed 31-day recurrence |
| 22 | 2025-02-15 | debit | -1895 | 698176.33 | 696281.33 | `recurring:delivery_membership` | recurring | `event_816`, `event_826`, `event_836` | - | history supports a fixed 31-day recurrence |
| 23 | 2025-02-16 | debit | -4883.78 | 696281.33 | 691397.55 | `recurring:entertainment` | recurring | `event_818`, `event_828`, `event_838` | - | history supports a fixed 31-day recurrence |
| 24 | 2025-02-22 | credit | 47802.51 | 691397.55 | 739200.06 | `recurring:salary` | recurring | `event_829`, `event_831`, `event_839` | - | history supports a fixed 16-day recurrence |
| 25 | 2025-03-03 | debit | -69100 | 739200.06 | 670100.06 | `recurring:rent` | recurring | `event_823`, `event_833`, `event_840` | - | history supports a fixed 30-day recurrence |
| 26 | 2025-03-06 | debit | -7568.88 | 670100.06 | 662531.18 | `recurring:transport` | recurring | `event_873`, `event_877`, `event_882` | - | history supports a fixed 32-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_789` | 2024-07-04 | credit | 74420.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_790` | 2024-07-11 | credit | 74852.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_791` | 2024-07-18 | credit | 54774.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_792` | 2024-07-25 | credit | 82410.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_793` | 2024-07-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_794` | 2024-07-07 | debit | 19224.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_795` | 2024-07-12 | debit | 2800 | already reflected in the current balance; may remain recurrence evidence |
| `event_796` | 2024-07-14 | debit | 1895 | already reflected in the current balance; may remain recurrence evidence |
| `event_797` | 2024-07-11 | debit | 4860 | already reflected in the current balance; may remain recurrence evidence |
| `event_798` | 2024-07-15 | debit | 4770.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_799` | 2024-08-04 | credit | 72641.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_800` | 2024-08-11 | credit | 59553.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_801` | 2024-08-18 | credit | 65056.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_802` | 2024-08-25 | credit | 47245.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_803` | 2024-08-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_804` | 2024-08-07 | debit | 17538.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_805` | 2024-08-12 | debit | 2800 | already reflected in the current balance; may remain recurrence evidence |
| `event_806` | 2024-08-14 | debit | 1895 | already reflected in the current balance; may remain recurrence evidence |
| `event_807` | 2024-08-11 | debit | 4860 | already reflected in the current balance; may remain recurrence evidence |
| `event_808` | 2024-08-15 | debit | 4504.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_809` | 2024-09-04 | credit | 81755.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_810` | 2024-09-11 | credit | 67741.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_811` | 2024-09-18 | credit | 79168.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_812` | 2024-09-25 | credit | 69351.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_813` | 2024-09-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_814` | 2024-09-07 | debit | 15748.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_815` | 2024-09-12 | debit | 2800 | already reflected in the current balance; may remain recurrence evidence |
| `event_816` | 2024-09-14 | debit | 1895 | already reflected in the current balance; may remain recurrence evidence |
| `event_817` | 2024-09-11 | debit | 4860 | already reflected in the current balance; may remain recurrence evidence |
| `event_818` | 2024-09-15 | debit | 4700.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_819` | 2024-10-04 | credit | 78226.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_820` | 2024-10-11 | credit | 65488.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_821` | 2024-10-18 | credit | 60517.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_822` | 2024-10-25 | credit | 40977.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_823` | 2024-10-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_824` | 2024-10-07 | debit | 15236.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_825` | 2024-10-12 | debit | 2800 | already reflected in the current balance; may remain recurrence evidence |
| `event_826` | 2024-10-14 | debit | 1895 | already reflected in the current balance; may remain recurrence evidence |
| `event_827` | 2024-10-11 | debit | 4860 | already reflected in the current balance; may remain recurrence evidence |
| `event_828` | 2024-10-15 | debit | 4366.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_829` | 2024-11-04 | credit | 60877.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_830` | 2024-11-11 | credit | 44415.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_831` | 2024-11-18 | credit | 47802.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_832` | 2024-11-25 | credit | 82667.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_833` | 2024-11-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_834` | 2024-11-07 | debit | 17771.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_835` | 2024-11-12 | debit | 2800 | already reflected in the current balance; may remain recurrence evidence |
| `event_836` | 2024-11-14 | debit | 1895 | already reflected in the current balance; may remain recurrence evidence |
| `event_837` | 2024-11-11 | debit | 4860 | already reflected in the current balance; may remain recurrence evidence |
| `event_838` | 2024-11-15 | debit | 4883.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_839` | 2024-12-04 | credit | 52239.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_840` | 2024-12-03 | debit | 69100 | already reflected in the current balance; may remain recurrence evidence |
| `event_841` | 2024-06-13 | debit | 10089.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_842` | 2024-06-20 | debit | 12216.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_843` | 2024-06-27 | debit | 10431.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_844` | 2024-07-04 | debit | 12027.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_845` | 2024-07-11 | debit | 9512.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_846` | 2024-07-18 | debit | 10839.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_847` | 2024-07-25 | debit | 11898.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_848` | 2024-08-01 | debit | 12020.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_849` | 2024-08-08 | debit | 11986 | already reflected in the current balance; may remain recurrence evidence |
| `event_850` | 2024-08-15 | debit | 11074.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_851` | 2024-08-22 | debit | 9929.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_852` | 2024-08-29 | debit | 8855.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_853` | 2024-09-05 | debit | 12641.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_854` | 2024-09-12 | debit | 10087.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_855` | 2024-09-19 | debit | 11596.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_856` | 2024-09-26 | debit | 8809.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_857` | 2024-10-03 | debit | 9807.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_858` | 2024-10-10 | debit | 12589.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_859` | 2024-10-17 | debit | 13621.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_860` | 2024-10-24 | debit | 12767.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_861` | 2024-10-31 | debit | 9968.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_862` | 2024-11-07 | debit | 10392.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_863` | 2024-11-14 | debit | 12092.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_864` | 2024-11-21 | debit | 8157.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_865` | 2024-11-28 | debit | 8755.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_866` | 2024-12-05 | debit | 8011.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_867` | 2024-06-14 | debit | 6859.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_868` | 2024-06-21 | debit | 7100.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_869` | 2024-06-28 | debit | 4830.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_870` | 2024-07-05 | debit | 4956.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_871` | 2024-07-12 | debit | 5489.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_872` | 2024-07-19 | debit | 7530.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_873` | 2024-07-26 | debit | 7568.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_874` | 2024-08-02 | debit | 6683.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_875` | 2024-08-09 | debit | 6632.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_876` | 2024-08-16 | debit | 5641.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_877` | 2024-08-23 | debit | 5747.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_878` | 2024-08-30 | debit | 5753.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_879` | 2024-09-06 | debit | 7448.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_880` | 2024-09-13 | debit | 5018.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_881` | 2024-09-20 | debit | 6582.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_882` | 2024-09-27 | debit | 6785.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_883` | 2024-10-04 | debit | 4472.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_884` | 2024-10-11 | debit | 4570.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_885` | 2024-10-18 | debit | 5776.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_886` | 2024-10-25 | debit | 6245.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_887` | 2024-11-01 | debit | 6819.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_888` | 2024-11-08 | debit | 5350.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_889` | 2024-11-15 | debit | 4990.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_890` | 2024-11-22 | debit | 4356.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_891` | 2024-11-29 | debit | 6359.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_892` | 2024-06-15 | debit | 8813.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_893` | 2024-06-29 | debit | 9260.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_894` | 2024-07-13 | debit | 8274.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_895` | 2024-07-27 | debit | 6897.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_896` | 2024-08-10 | debit | 9399.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_897` | 2024-08-24 | debit | 9621.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_898` | 2024-09-07 | debit | 6375.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_899` | 2024-09-21 | debit | 10079.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_900` | 2024-10-05 | debit | 10525.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_901` | 2024-10-19 | debit | 8538.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_902` | 2024-11-02 | debit | 8480.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_903` | 2024-11-16 | debit | 8253.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_904` | 2024-11-30 | debit | 10370.83 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_11 - user_11

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 12510645 | 13110000 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `earliest_date_for_full_payment` | 2025-07-15 | 2025-05-03 |
| `spending_changes_needed` | reduce_to:event_989:665950 | none |

### Balance diagnostics

- Current balance: `63531795` IDR
- Required minimum: `34140600` IDR
- Baseline minimum before request payment: `50022241.52` on `2025-05-15`
- Computed safe amount now: `13110000`
- Computed earliest safe full-payment date: `2025-05-03`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-05-06 | debit | -2954500 | 63531795 | 60577295 | `recurring:housing` | recurring | `event_925`, `event_934`, `event_943` | - | history supports a fixed 31-day recurrence |
| 2 | 2025-05-09 | debit | -2796165.18 | 60577295 | 57781129.82 | `recurring:utilities` | recurring | `event_926`, `event_935`, `event_944` | - | history supports a fixed 31-day recurrence |
| 3 | 2025-05-10 | debit | -1881000 | 57781129.82 | 55900129.82 | `recurring:insurance` | recurring | `event_927`, `event_936`, `event_945` | - | history supports a fixed 31-day recurrence |
| 4 | 2025-05-11 | debit | -2544100 | 55900129.82 | 53356029.82 | `recurring:education` | recurring | `event_928`, `event_937`, `event_946` | - | history supports a fixed 31-day recurrence |
| 5 | 2025-05-13 | debit | -3165638.3 | 53356029.82 | 50190391.52 | `recurring:healthcare` | recurring | `event_929`, `event_938`, `event_947` | - | history supports a fixed 31-day recurrence |
| 6 | 2025-05-15 | debit | -168150 | 50190391.52 | 50022241.52 | `recurring:cloud_storage` | recurring | `event_931`, `event_940`, `event_949` | - | history supports a fixed 31-day recurrence |
| 7 | 2025-05-16 | credit | 38760000 | 50022241.52 | 88782241.52 | `recurring:salary` | recurring | `event_923`, `event_932`, `event_941` | `message_08` | history supports a fixed 31-day recurrence |
| 8 | 2025-05-17 | debit | -1674887.61 | 88782241.52 | 87107353.91 | `recurring:entertainment` | recurring | `event_930`, `event_939`, `event_948` | - | history supports a fixed 31-day recurrence |
| 9 | 2025-05-28 | credit | 38760000 | 87107353.91 | 125867353.91 | `recurring:salary` | recurring | `event_906`, `event_915`, `event_924` | `message_08` | history supports a fixed 31-day recurrence |
| 10 | 2025-06-06 | debit | -2954500 | 125867353.91 | 122912853.91 | `recurring:housing` | recurring | `event_925`, `event_934`, `event_943` | - | history supports a fixed 31-day recurrence |
| 11 | 2025-06-09 | debit | -2796165.18 | 122912853.91 | 120116688.73 | `recurring:utilities` | recurring | `event_926`, `event_935`, `event_944` | - | history supports a fixed 31-day recurrence |
| 12 | 2025-06-10 | debit | -1881000 | 120116688.73 | 118235688.73 | `recurring:insurance` | recurring | `event_927`, `event_936`, `event_945` | - | history supports a fixed 31-day recurrence |
| 13 | 2025-06-11 | debit | -2544100 | 118235688.73 | 115691588.73 | `recurring:education` | recurring | `event_928`, `event_937`, `event_946` | - | history supports a fixed 31-day recurrence |
| 14 | 2025-06-13 | debit | -3165638.3 | 115691588.73 | 112525950.43 | `recurring:healthcare` | recurring | `event_929`, `event_938`, `event_947` | - | history supports a fixed 31-day recurrence |
| 15 | 2025-06-15 | debit | -168150 | 112525950.43 | 112357800.43 | `recurring:cloud_storage` | recurring | `event_931`, `event_940`, `event_949` | - | history supports a fixed 31-day recurrence |
| 16 | 2025-06-16 | credit | 38760000 | 112357800.43 | 151117800.43 | `recurring:salary` | recurring | `event_923`, `event_932`, `event_941` | `message_08` | history supports a fixed 31-day recurrence |
| 17 | 2025-06-17 | debit | -1674887.61 | 151117800.43 | 149442912.82 | `recurring:entertainment` | recurring | `event_930`, `event_939`, `event_948` | - | history supports a fixed 31-day recurrence |
| 18 | 2025-06-28 | credit | 38760000 | 149442912.82 | 188202912.82 | `recurring:salary` | recurring | `event_906`, `event_915`, `event_924` | `message_08` | history supports a fixed 31-day recurrence |
| 19 | 2025-07-07 | debit | -2954500 | 188202912.82 | 185248412.82 | `recurring:housing` | recurring | `event_925`, `event_934`, `event_943` | - | history supports a fixed 31-day recurrence |
| 20 | 2025-07-10 | debit | -2796165.18 | 185248412.82 | 182452247.64 | `recurring:utilities` | recurring | `event_926`, `event_935`, `event_944` | - | history supports a fixed 31-day recurrence |
| 21 | 2025-07-11 | debit | -1881000 | 182452247.64 | 180571247.64 | `recurring:insurance` | recurring | `event_927`, `event_936`, `event_945` | - | history supports a fixed 31-day recurrence |
| 22 | 2025-07-12 | debit | -2544100 | 180571247.64 | 178027147.64 | `recurring:education` | recurring | `event_928`, `event_937`, `event_946` | - | history supports a fixed 31-day recurrence |
| 23 | 2025-07-14 | debit | -3165638.3 | 178027147.64 | 174861509.34 | `recurring:healthcare` | recurring | `event_929`, `event_938`, `event_947` | - | history supports a fixed 31-day recurrence |
| 24 | 2025-07-16 | debit | -168150 | 174861509.34 | 174693359.34 | `recurring:cloud_storage` | recurring | `event_931`, `event_940`, `event_949` | - | history supports a fixed 31-day recurrence |
| 25 | 2025-07-17 | credit | 38760000 | 174693359.34 | 213453359.34 | `recurring:salary` | recurring | `event_923`, `event_932`, `event_941` | `message_08` | history supports a fixed 31-day recurrence |
| 26 | 2025-07-18 | debit | -1674887.61 | 213453359.34 | 211778471.73 | `recurring:entertainment` | recurring | `event_930`, `event_939`, `event_948` | - | history supports a fixed 31-day recurrence |
| 27 | 2025-07-29 | credit | 38760000 | 211778471.73 | 250538471.73 | `recurring:salary` | recurring | `event_906`, `event_915`, `event_924` | `message_08` | history supports a fixed 31-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_905` | 2024-12-15 | credit | 23256000 | already reflected in the current balance; may remain recurrence evidence |
| `event_906` | 2024-12-24 | credit | 16715584.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_907` | 2024-12-05 | debit | 2954500 | already reflected in the current balance; may remain recurrence evidence |
| `event_908` | 2024-12-08 | debit | 2916312.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_909` | 2024-12-09 | debit | 1881000 | already reflected in the current balance; may remain recurrence evidence |
| `event_910` | 2024-12-10 | debit | 2544100 | already reflected in the current balance; may remain recurrence evidence |
| `event_911` | 2024-12-12 | debit | 2635764.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_912` | 2024-12-16 | debit | 1404572.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_913` | 2024-12-14 | debit | 168150 | already reflected in the current balance; may remain recurrence evidence |
| `event_914` | 2025-01-15 | credit | 23256000 | already reflected in the current balance; may remain recurrence evidence |
| `event_915` | 2025-01-24 | credit | 8908379.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_916` | 2025-01-05 | debit | 2954500 | already reflected in the current balance; may remain recurrence evidence |
| `event_917` | 2025-01-08 | debit | 2891149.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_918` | 2025-01-09 | debit | 1881000 | already reflected in the current balance; may remain recurrence evidence |
| `event_919` | 2025-01-10 | debit | 2544100 | already reflected in the current balance; may remain recurrence evidence |
| `event_920` | 2025-01-12 | debit | 3118089.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_921` | 2025-01-16 | debit | 1688239.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_922` | 2025-01-14 | debit | 168150 | already reflected in the current balance; may remain recurrence evidence |
| `event_923` | 2025-02-15 | credit | 23256000 | already reflected in the current balance; may remain recurrence evidence |
| `event_924` | 2025-02-24 | credit | 15989420 | already reflected in the current balance; may remain recurrence evidence |
| `event_925` | 2025-02-05 | debit | 2954500 | already reflected in the current balance; may remain recurrence evidence |
| `event_926` | 2025-02-08 | debit | 2508782.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_927` | 2025-02-09 | debit | 1881000 | already reflected in the current balance; may remain recurrence evidence |
| `event_928` | 2025-02-10 | debit | 2544100 | already reflected in the current balance; may remain recurrence evidence |
| `event_929` | 2025-02-12 | debit | 2973572.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_930` | 2025-02-16 | debit | 1587027.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_931` | 2025-02-14 | debit | 168150 | already reflected in the current balance; may remain recurrence evidence |
| `event_932` | 2025-03-15 | credit | 23256000 | already reflected in the current balance; may remain recurrence evidence |
| `event_933` | 2025-03-24 | credit | 20012106.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_934` | 2025-03-05 | debit | 2954500 | already reflected in the current balance; may remain recurrence evidence |
| `event_935` | 2025-03-08 | debit | 2488665.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_936` | 2025-03-09 | debit | 1881000 | already reflected in the current balance; may remain recurrence evidence |
| `event_937` | 2025-03-10 | debit | 2544100 | already reflected in the current balance; may remain recurrence evidence |
| `event_938` | 2025-03-12 | debit | 3165638.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_939` | 2025-03-16 | debit | 1649906.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_940` | 2025-03-14 | debit | 168150 | already reflected in the current balance; may remain recurrence evidence |
| `event_941` | 2025-04-15 | credit | 23256000 | already reflected in the current balance; may remain recurrence evidence |
| `event_942` | 2025-04-24 | credit | 8502888.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_943` | 2025-04-05 | debit | 2954500 | already reflected in the current balance; may remain recurrence evidence |
| `event_944` | 2025-04-08 | debit | 2796165.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_945` | 2025-04-09 | debit | 1881000 | already reflected in the current balance; may remain recurrence evidence |
| `event_946` | 2025-04-10 | debit | 2544100 | already reflected in the current balance; may remain recurrence evidence |
| `event_947` | 2025-04-12 | debit | 2826901.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_948` | 2025-04-16 | debit | 1674887.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_949` | 2025-04-14 | debit | 168150 | already reflected in the current balance; may remain recurrence evidence |
| `event_950` | 2024-11-09 | debit | 1053064.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_951` | 2024-11-19 | debit | 1565130.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_952` | 2024-11-29 | debit | 1714643.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_953` | 2024-12-09 | debit | 1644304.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_954` | 2024-12-19 | debit | 1406401.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_955` | 2024-12-29 | debit | 1063530.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_956` | 2025-01-08 | debit | 1395524.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_957` | 2025-01-18 | debit | 1578114.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_958` | 2025-01-28 | debit | 1763208.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_959` | 2025-02-07 | debit | 1241008.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_960` | 2025-02-17 | debit | 1222447.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_961` | 2025-02-27 | debit | 1614291.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_962` | 2025-03-09 | debit | 1655671.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_963` | 2025-03-19 | debit | 1311350.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_964` | 2025-03-29 | debit | 1292005.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_965` | 2025-04-08 | debit | 1590529.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_966` | 2025-04-18 | debit | 1131582.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_967` | 2025-04-28 | debit | 1341187.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_968` | 2024-11-10 | debit | 1230316.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_969` | 2024-11-24 | debit | 825660.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_970` | 2024-12-08 | debit | 788053.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_971` | 2024-12-22 | debit | 893623.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_972` | 2025-01-05 | debit | 1212904.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_973` | 2025-01-19 | debit | 1307205.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_974` | 2025-02-02 | debit | 785218.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_975` | 2025-02-16 | debit | 1185524.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_976` | 2025-03-02 | debit | 1200020.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_977` | 2025-03-16 | debit | 1244032.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_978` | 2025-03-30 | debit | 1122838.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_979` | 2025-04-13 | debit | 1103949.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_980` | 2025-04-27 | debit | 1244835.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_981` | 2024-11-06 | debit | 1018758.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_982` | 2024-11-27 | debit | 1485097.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_983` | 2024-12-18 | debit | 1528058.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_984` | 2025-01-08 | debit | 1697463.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_985` | 2025-01-29 | debit | 1052748.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_986` | 2025-02-19 | debit | 1365643.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_987` | 2025-03-12 | debit | 1335266.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_988` | 2025-04-02 | debit | 1503635.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_989` | 2025-04-23 | debit | 1163530.49 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| full_payment | 2025-05-03 | 2025-05-03 | 13110000 | 1 | `payment_option_29` | `(False, False, Decimal('13110000'), datetime.date(2025, 5, 3), 1, 'payment_option_29')` | selected |

## request_13 - user_13

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 433.4 | 941.6 |
| `affordability_status` | affordable_later | affordable_now |
| `recommended_payment_method` | wait | full_payment |
| `payment_plan` | 2024-05-15:941.60 | 2024-03-07:941.6 |
| `earliest_date_for_full_payment` | 2024-05-15 | 2024-03-07 |

### Balance diagnostics

- Current balance: `2789.52` EUR
- Required minimum: `1300` EUR
- Baseline minimum before request payment: `2678.52` on `2024-03-15`
- Computed safe amount now: `941.6`
- Computed earliest safe full-payment date: `2024-03-07`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-03-12 | debit | -61 | 2789.52 | 2728.52 | `recurring:gym` | recurring | `event_1077`, `event_1085`, `event_1092` | - | history supports a fixed 31-day recurrence |
| 2 | 2024-03-13 | debit | -29 | 2728.52 | 2699.52 | `recurring:music_subscription` | recurring | `event_1075`, `event_1083`, `event_1090` | - | history supports a fixed 31-day recurrence |
| 3 | 2024-03-15 | debit | -21 | 2699.52 | 2678.52 | `recurring:delivery_membership` | recurring | `event_1076`, `event_1084`, `event_1091` | - | history supports a fixed 31-day recurrence |
| 4 | 2024-03-15 | credit | 1343.54 | 2678.52 | 4022.06 | `event_1161` | explicit | `event_1161` | - | cash event |
| 5 | 2024-03-16 | debit | -37.9 | 4022.06 | 3984.16 | `recurring:entertainment` | recurring | `event_1078`, `event_1086`, `event_1093` | - | history supports a fixed 31-day recurrence |
| 6 | 2024-03-17 | credit | 1343.54 | 3984.16 | 5327.7 | `recurring:salary` | recurring | `event_1071`, `event_1079`, `event_1087` | - | history supports a fixed 31-day recurrence |
| 7 | 2024-03-22 | credit | 771.17 | 5327.7 | 6098.87 | `recurring:salary` | recurring | `event_1064`, `event_1072`, `event_1080` | - | history supports a fixed 31-day recurrence |
| 8 | 2024-04-01 | debit | -622.6 | 6098.87 | 5476.27 | `recurring:rent` | recurring | `event_1081`, `event_1088`, `event_1094` | - | history supports a fixed 30-day recurrence |
| 9 | 2024-04-03 | debit | -50.46 | 5476.27 | 5425.81 | `recurring:transport` | recurring | `event_1136`, `event_1140`, `event_1146` | - | history supports a fixed 35-day recurrence |
| 10 | 2024-04-05 | debit | -143.7 | 5425.81 | 5282.11 | `recurring:utilities` | recurring | `event_1082`, `event_1089`, `event_1095` | - | history supports a fixed 30-day recurrence |
| 11 | 2024-04-12 | debit | -61 | 5282.11 | 5221.11 | `recurring:gym` | recurring | `event_1077`, `event_1085`, `event_1092` | - | history supports a fixed 31-day recurrence |
| 12 | 2024-04-13 | debit | -29 | 5221.11 | 5192.11 | `recurring:music_subscription` | recurring | `event_1075`, `event_1083`, `event_1090` | - | history supports a fixed 31-day recurrence |
| 13 | 2024-04-15 | debit | -21 | 5192.11 | 5171.11 | `recurring:delivery_membership` | recurring | `event_1076`, `event_1084`, `event_1091` | - | history supports a fixed 31-day recurrence |
| 14 | 2024-04-16 | debit | -37.9 | 5171.11 | 5133.21 | `recurring:entertainment` | recurring | `event_1078`, `event_1086`, `event_1093` | - | history supports a fixed 31-day recurrence |
| 15 | 2024-04-17 | credit | 1343.54 | 5133.21 | 6476.75 | `recurring:salary` | recurring | `event_1071`, `event_1079`, `event_1087` | - | history supports a fixed 31-day recurrence |
| 16 | 2024-04-22 | credit | 771.17 | 6476.75 | 7247.92 | `recurring:salary` | recurring | `event_1064`, `event_1072`, `event_1080` | - | history supports a fixed 31-day recurrence |
| 17 | 2024-05-01 | debit | -622.6 | 7247.92 | 6625.32 | `recurring:rent` | recurring | `event_1081`, `event_1088`, `event_1094` | - | history supports a fixed 30-day recurrence |
| 18 | 2024-05-05 | debit | -143.7 | 6625.32 | 6481.62 | `recurring:utilities` | recurring | `event_1082`, `event_1089`, `event_1095` | - | history supports a fixed 30-day recurrence |
| 19 | 2024-05-08 | debit | -50.46 | 6481.62 | 6431.16 | `recurring:transport` | recurring | `event_1136`, `event_1140`, `event_1146` | - | history supports a fixed 35-day recurrence |
| 20 | 2024-05-13 | debit | -61 | 6431.16 | 6370.16 | `recurring:gym` | recurring | `event_1077`, `event_1085`, `event_1092` | - | history supports a fixed 31-day recurrence |
| 21 | 2024-05-14 | debit | -29 | 6370.16 | 6341.16 | `recurring:music_subscription` | recurring | `event_1075`, `event_1083`, `event_1090` | - | history supports a fixed 31-day recurrence |
| 22 | 2024-05-16 | debit | -21 | 6341.16 | 6320.16 | `recurring:delivery_membership` | recurring | `event_1076`, `event_1084`, `event_1091` | - | history supports a fixed 31-day recurrence |
| 23 | 2024-05-17 | debit | -37.9 | 6320.16 | 6282.26 | `recurring:entertainment` | recurring | `event_1078`, `event_1086`, `event_1093` | - | history supports a fixed 31-day recurrence |
| 24 | 2024-05-18 | credit | 1343.54 | 6282.26 | 7625.8 | `recurring:salary` | recurring | `event_1071`, `event_1079`, `event_1087` | - | history supports a fixed 31-day recurrence |
| 25 | 2024-05-23 | credit | 771.17 | 7625.8 | 8396.97 | `recurring:salary` | recurring | `event_1064`, `event_1072`, `event_1080` | - | history supports a fixed 31-day recurrence |
| 26 | 2024-05-31 | debit | -622.6 | 8396.97 | 7774.37 | `recurring:rent` | recurring | `event_1081`, `event_1088`, `event_1094` | - | history supports a fixed 30-day recurrence |
| 27 | 2024-06-04 | debit | -143.7 | 7774.37 | 7630.67 | `recurring:utilities` | recurring | `event_1082`, `event_1089`, `event_1095` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1055` | 2023-10-15 | credit | 1343.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1056` | 2023-10-20 | credit | 993.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1057` | 2023-10-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1058` | 2023-10-06 | debit | 162.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1059` | 2023-10-11 | debit | 29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1060` | 2023-10-13 | debit | 21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1061` | 2023-10-10 | debit | 61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1062` | 2023-10-14 | debit | 33.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_1063` | 2023-11-15 | credit | 1343.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1064` | 2023-11-20 | credit | 771.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1065` | 2023-11-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1066` | 2023-11-06 | debit | 143.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1067` | 2023-11-11 | debit | 29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1068` | 2023-11-13 | debit | 21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1069` | 2023-11-10 | debit | 61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1070` | 2023-11-14 | debit | 30.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1071` | 2023-12-15 | credit | 1343.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1072` | 2023-12-20 | credit | 948.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1073` | 2023-12-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1074` | 2023-12-06 | debit | 146.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1075` | 2023-12-11 | debit | 29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1076` | 2023-12-13 | debit | 21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1077` | 2023-12-10 | debit | 61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1078` | 2023-12-14 | debit | 37.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1079` | 2024-01-15 | credit | 1343.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1080` | 2024-01-20 | credit | 881.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_1081` | 2024-01-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1082` | 2024-01-06 | debit | 143.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1083` | 2024-01-11 | debit | 29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1084` | 2024-01-13 | debit | 21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1085` | 2024-01-10 | debit | 61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1086` | 2024-01-14 | debit | 31.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1087` | 2024-02-15 | credit | 1343.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1088` | 2024-02-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1089` | 2024-02-06 | debit | 131.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1090` | 2024-02-11 | debit | 29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1091` | 2024-02-13 | debit | 21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1092` | 2024-02-10 | debit | 61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1093` | 2024-02-14 | debit | 30.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1094` | 2024-03-02 | debit | 622.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1095` | 2024-03-06 | debit | 134.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1096` | 2023-09-12 | debit | 91.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1097` | 2023-09-19 | debit | 114.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1098` | 2023-09-26 | debit | 120.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_1099` | 2023-10-03 | debit | 82.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1100` | 2023-10-10 | debit | 115.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_1101` | 2023-10-17 | debit | 89.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_1102` | 2023-10-24 | debit | 91.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1103` | 2023-10-31 | debit | 108.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1104` | 2023-11-07 | debit | 101.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_1105` | 2023-11-14 | debit | 102.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1106` | 2023-11-21 | debit | 119.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1107` | 2023-11-28 | debit | 101.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1108` | 2023-12-05 | debit | 106.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1109` | 2023-12-12 | debit | 102.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1110` | 2023-12-19 | debit | 93.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1111` | 2023-12-26 | debit | 81.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_1112` | 2024-01-02 | debit | 86.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1113` | 2024-01-09 | debit | 94.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1114` | 2024-01-16 | debit | 84.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1115` | 2024-01-23 | debit | 120.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_1116` | 2024-01-30 | debit | 114.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1117` | 2024-02-06 | debit | 73.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_1118` | 2024-02-13 | debit | 98.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_1119` | 2024-02-20 | debit | 118.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_1120` | 2024-02-27 | debit | 85.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1121` | 2024-03-05 | debit | 93.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1122` | 2023-09-13 | debit | 44.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1123` | 2023-09-20 | debit | 35.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1124` | 2023-09-27 | debit | 34.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1125` | 2023-10-04 | debit | 34.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1126` | 2023-10-11 | debit | 50.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1127` | 2023-10-18 | debit | 55.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1128` | 2023-10-25 | debit | 34.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1129` | 2023-11-01 | debit | 54.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1130` | 2023-11-08 | debit | 33.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_1131` | 2023-11-15 | debit | 48.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1132` | 2023-11-22 | debit | 54.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_1133` | 2023-11-29 | debit | 38.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_1134` | 2023-12-06 | debit | 44.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_1135` | 2023-12-13 | debit | 50.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1136` | 2023-12-20 | debit | 49.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1137` | 2023-12-27 | debit | 46.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_1138` | 2024-01-03 | debit | 43.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1139` | 2024-01-10 | debit | 58.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_1140` | 2024-01-17 | debit | 33.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1141` | 2024-01-24 | debit | 56.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1142` | 2024-01-31 | debit | 46.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_1143` | 2024-02-07 | debit | 45.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1144` | 2024-02-14 | debit | 45.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_1145` | 2024-02-21 | debit | 39.48 | already reflected in the current balance; may remain recurrence evidence |
| `event_1146` | 2024-02-28 | debit | 50.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1147` | 2024-03-06 | debit | 37.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1148` | 2023-09-14 | debit | 75.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1149` | 2023-09-28 | debit | 68.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1150` | 2023-10-12 | debit | 80.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1151` | 2023-10-26 | debit | 62.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1152` | 2023-11-09 | debit | 53.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1153` | 2023-11-23 | debit | 80.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1154` | 2023-12-07 | debit | 64.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_1155` | 2023-12-21 | debit | 70.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_1156` | 2024-01-04 | debit | 61.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1157` | 2024-01-18 | debit | 48.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1158` | 2024-02-01 | debit | 60.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1159` | 2024-02-15 | debit | 48.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_1160` | 2024-02-29 | debit | 61.28 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| full_payment | 2024-03-07 | 2024-03-07 | 941.6 | 1 | `payment_option_36` | `(False, False, Decimal('941.6'), datetime.date(2024, 3, 7), 1, 'payment_option_36')` | selected |

## request_14 - user_14

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 597.74 | 0 |

### Balance diagnostics

- Current balance: `3931.74` EUR
- Required minimum: `2200` EUR
- Baseline minimum before request payment: `-1071.81` on `2025-11-01`
- Computed safe amount now: `0`
- Computed earliest safe full-payment date: ``
- Immediate-full first breach: `2025-08-04` after `request_payment`, closing at `-1482.46`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-08-06 | debit | -153.69 | 3931.74 | 3778.05 | `recurring:utilities` | recurring | `event_1179`, `event_1186`, `event_1194` | - | history supports a fixed 30-day recurrence |
| 2 | 2025-08-10 | debit | -95.17 | 3778.05 | 3682.88 | `recurring:healthcare` | recurring | `event_1181`, `event_1188`, `event_1196` | - | history supports a fixed 30-day recurrence |
| 3 | 2025-08-11 | debit | -350 | 3682.88 | 3332.88 | `recurring:debt_repayment` | recurring | `event_1180`, `event_1187`, `event_1195` | - | history supports a fixed 30-day recurrence |
| 4 | 2025-08-12 | debit | -14 | 3332.88 | 3318.88 | `recurring:cloud_storage` | recurring | `event_1183`, `event_1190`, `event_1198` | - | history supports a fixed 30-day recurrence |
| 5 | 2025-08-12 | debit | -140.39 | 3318.88 | 3178.49 | `recurring:shopping` | recurring | `event_1184`, `event_1191`, `event_1199` | - | history supports a fixed 30-day recurrence |
| 6 | 2025-08-13 | debit | -226 | 3178.49 | 2952.49 | `recurring:family_support` | recurring | `event_1182`, `event_1189`, `event_1197` | - | history supports a fixed 30-day recurrence |
| 7 | 2025-09-02 | debit | -688.6 | 2952.49 | 2263.89 | `recurring:rent` | recurring | `event_1185`, `event_1193`, `event_1200` | - | history supports a fixed 30-day recurrence |
| 8 | 2025-09-05 | debit | -153.69 | 2263.89 | 2110.2 | `recurring:utilities` | recurring | `event_1179`, `event_1186`, `event_1194` | - | history supports a fixed 30-day recurrence |
| 9 | 2025-09-09 | debit | -95.17 | 2110.2 | 2015.03 | `recurring:healthcare` | recurring | `event_1181`, `event_1188`, `event_1196` | - | history supports a fixed 30-day recurrence |
| 10 | 2025-09-10 | debit | -350 | 2015.03 | 1665.03 | `recurring:debt_repayment` | recurring | `event_1180`, `event_1187`, `event_1195` | - | history supports a fixed 30-day recurrence |
| 11 | 2025-09-11 | debit | -14 | 1665.03 | 1651.03 | `recurring:cloud_storage` | recurring | `event_1183`, `event_1190`, `event_1198` | - | history supports a fixed 30-day recurrence |
| 12 | 2025-09-11 | debit | -140.39 | 1651.03 | 1510.64 | `recurring:shopping` | recurring | `event_1184`, `event_1191`, `event_1199` | - | history supports a fixed 30-day recurrence |
| 13 | 2025-09-12 | debit | -226 | 1510.64 | 1284.64 | `recurring:family_support` | recurring | `event_1182`, `event_1189`, `event_1197` | - | history supports a fixed 30-day recurrence |
| 14 | 2025-10-02 | debit | -688.6 | 1284.64 | 596.04 | `recurring:rent` | recurring | `event_1185`, `event_1193`, `event_1200` | - | history supports a fixed 30-day recurrence |
| 15 | 2025-10-05 | debit | -153.69 | 596.04 | 442.35 | `recurring:utilities` | recurring | `event_1179`, `event_1186`, `event_1194` | - | history supports a fixed 30-day recurrence |
| 16 | 2025-10-09 | debit | -95.17 | 442.35 | 347.18 | `recurring:healthcare` | recurring | `event_1181`, `event_1188`, `event_1196` | - | history supports a fixed 30-day recurrence |
| 17 | 2025-10-10 | debit | -350 | 347.18 | -2.82 | `recurring:debt_repayment` | recurring | `event_1180`, `event_1187`, `event_1195` | - | history supports a fixed 30-day recurrence |
| 18 | 2025-10-11 | debit | -14 | -2.82 | -16.82 | `recurring:cloud_storage` | recurring | `event_1183`, `event_1190`, `event_1198` | - | history supports a fixed 30-day recurrence |
| 19 | 2025-10-11 | debit | -140.39 | -16.82 | -157.21 | `recurring:shopping` | recurring | `event_1184`, `event_1191`, `event_1199` | - | history supports a fixed 30-day recurrence |
| 20 | 2025-10-12 | debit | -226 | -157.21 | -383.21 | `recurring:family_support` | recurring | `event_1182`, `event_1189`, `event_1197` | - | history supports a fixed 30-day recurrence |
| 21 | 2025-11-01 | debit | -688.6 | -383.21 | -1071.81 | `recurring:rent` | recurring | `event_1185`, `event_1193`, `event_1200` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1162` | 2025-03-15 | credit | 2717 | already reflected in the current balance; may remain recurrence evidence |
| `event_1163` | 2025-03-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1164` | 2025-03-07 | debit | 141.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1165` | 2025-03-12 | debit | 350 | already reflected in the current balance; may remain recurrence evidence |
| `event_1166` | 2025-03-11 | debit | 92.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1167` | 2025-03-14 | debit | 226 | already reflected in the current balance; may remain recurrence evidence |
| `event_1168` | 2025-03-13 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1169` | 2025-03-13 | debit | 137.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1170` | 2025-04-15 | credit | 2717 | already reflected in the current balance; may remain recurrence evidence |
| `event_1171` | 2025-04-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1172` | 2025-04-07 | debit | 156.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1173` | 2025-04-12 | debit | 350 | already reflected in the current balance; may remain recurrence evidence |
| `event_1174` | 2025-04-11 | debit | 92.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1175` | 2025-04-14 | debit | 226 | already reflected in the current balance; may remain recurrence evidence |
| `event_1176` | 2025-04-13 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1177` | 2025-04-13 | debit | 123.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_1178` | 2025-05-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1179` | 2025-05-07 | debit | 143.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_1180` | 2025-05-12 | debit | 350 | already reflected in the current balance; may remain recurrence evidence |
| `event_1181` | 2025-05-11 | debit | 95.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1182` | 2025-05-14 | debit | 226 | already reflected in the current balance; may remain recurrence evidence |
| `event_1183` | 2025-05-13 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1184` | 2025-05-13 | debit | 123.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1185` | 2025-06-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1186` | 2025-06-07 | debit | 146.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1187` | 2025-06-12 | debit | 350 | already reflected in the current balance; may remain recurrence evidence |
| `event_1188` | 2025-06-11 | debit | 91.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1189` | 2025-06-14 | debit | 226 | already reflected in the current balance; may remain recurrence evidence |
| `event_1190` | 2025-06-13 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1191` | 2025-06-13 | debit | 123.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1192` | 2025-07-15 | credit | 2717 | already reflected in the current balance; may remain recurrence evidence |
| `event_1193` | 2025-07-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1194` | 2025-07-07 | debit | 153.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_1195` | 2025-07-12 | debit | 350 | already reflected in the current balance; may remain recurrence evidence |
| `event_1196` | 2025-07-11 | debit | 87.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1197` | 2025-07-14 | debit | 226 | already reflected in the current balance; may remain recurrence evidence |
| `event_1198` | 2025-07-13 | debit | 14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1199` | 2025-07-13 | debit | 140.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1200` | 2025-08-03 | debit | 688.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1201` | 2025-02-09 | debit | 103.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1202` | 2025-02-16 | debit | 95.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1203` | 2025-02-23 | debit | 104.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1204` | 2025-03-02 | debit | 81.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1205` | 2025-03-09 | debit | 92.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1206` | 2025-03-16 | debit | 121.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1207` | 2025-03-23 | debit | 87.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_1208` | 2025-03-30 | debit | 140.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1209` | 2025-04-06 | debit | 131.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_1210` | 2025-04-13 | debit | 83.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1211` | 2025-04-20 | debit | 93.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1212` | 2025-04-27 | debit | 90.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_1213` | 2025-05-04 | debit | 106.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_1214` | 2025-05-11 | debit | 93.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1215` | 2025-05-18 | debit | 96.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1216` | 2025-05-25 | debit | 101.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1217` | 2025-06-01 | debit | 129.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1218` | 2025-06-08 | debit | 123.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1219` | 2025-06-15 | debit | 94.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1220` | 2025-06-22 | debit | 86.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_1221` | 2025-06-29 | debit | 138.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1222` | 2025-07-06 | debit | 102.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1223` | 2025-07-13 | debit | 112.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_1224` | 2025-07-20 | debit | 96.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1225` | 2025-07-27 | debit | 86.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_1226` | 2025-08-03 | debit | 129.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_1227` | 2025-02-10 | debit | 46.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1228` | 2025-02-24 | debit | 58.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_1229` | 2025-03-10 | debit | 37.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1230` | 2025-03-24 | debit | 47.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_1231` | 2025-04-07 | debit | 53.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1232` | 2025-04-21 | debit | 56.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_1233` | 2025-05-05 | debit | 55.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_1234` | 2025-05-19 | debit | 52.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1235` | 2025-06-02 | debit | 50.48 | already reflected in the current balance; may remain recurrence evidence |
| `event_1236` | 2025-06-16 | debit | 55.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1237` | 2025-06-30 | debit | 62.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_1238` | 2025-07-14 | debit | 43.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1239` | 2025-07-28 | debit | 43.88 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_15 - user_15

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 83.05 | 0 |

### Balance diagnostics

- Current balance: `1770.05` EUR
- Required minimum: `1200` EUR
- Baseline minimum before request payment: `-816.32` on `2026-04-04`
- Computed safe amount now: `0`
- Computed earliest safe full-payment date: ``
- Immediate-full first breach: `2026-01-06` after `request_payment`, closing at `-1914.95`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-01-07 | debit | -90.39 | 1770.05 | 1679.66 | `recurring:utilities` | recurring | `event_1253`, `event_1260`, `event_1267` | - | history supports a fixed 30-day recurrence |
| 2 | 2026-01-09 | debit | -159 | 1679.66 | 1520.66 | `recurring:education` | recurring | `event_1254`, `event_1261`, `event_1268` | - | history supports a fixed 30-day recurrence |
| 3 | 2026-01-12 | debit | -84 | 1520.66 | 1436.66 | `recurring:debt_repayment` | recurring | `event_1255`, `event_1262`, `event_1269` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-01-12 | debit | -11 | 1436.66 | 1425.66 | `recurring:music_subscription` | recurring | `event_1256`, `event_1263`, `event_1270` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-01-14 | debit | -27 | 1425.66 | 1398.66 | `recurring:delivery_membership` | recurring | `event_1257`, `event_1264`, `event_1271` | - | history supports a fixed 30-day recurrence |
| 6 | 2026-01-21 | debit | -41.35 | 1398.66 | 1357.31 | `recurring:transport` | recurring | `event_1316`, `event_1319`, `event_1322` | - | history supports a fixed 21-day recurrence |
| 7 | 2026-02-03 | debit | -435.6 | 1357.31 | 921.71 | `recurring:rent` | recurring | `event_1259`, `event_1266`, `event_1272` | - | history supports a fixed 30-day recurrence |
| 8 | 2026-02-06 | debit | -90.39 | 921.71 | 831.32 | `recurring:utilities` | recurring | `event_1253`, `event_1260`, `event_1267` | - | history supports a fixed 30-day recurrence |
| 9 | 2026-02-08 | debit | -159 | 831.32 | 672.32 | `recurring:education` | recurring | `event_1254`, `event_1261`, `event_1268` | - | history supports a fixed 30-day recurrence |
| 10 | 2026-02-11 | debit | -84 | 672.32 | 588.32 | `recurring:debt_repayment` | recurring | `event_1255`, `event_1262`, `event_1269` | - | history supports a fixed 30-day recurrence |
| 11 | 2026-02-11 | debit | -11 | 588.32 | 577.32 | `recurring:music_subscription` | recurring | `event_1256`, `event_1263`, `event_1270` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-02-11 | debit | -41.35 | 577.32 | 535.97 | `recurring:transport` | recurring | `event_1316`, `event_1319`, `event_1322` | - | history supports a fixed 21-day recurrence |
| 13 | 2026-02-13 | debit | -27 | 535.97 | 508.97 | `recurring:delivery_membership` | recurring | `event_1257`, `event_1264`, `event_1271` | - | history supports a fixed 30-day recurrence |
| 14 | 2026-03-04 | debit | -41.35 | 508.97 | 467.62 | `recurring:transport` | recurring | `event_1316`, `event_1319`, `event_1322` | - | history supports a fixed 21-day recurrence |
| 15 | 2026-03-05 | debit | -435.6 | 467.62 | 32.02 | `recurring:rent` | recurring | `event_1259`, `event_1266`, `event_1272` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-03-08 | debit | -90.39 | 32.02 | -58.37 | `recurring:utilities` | recurring | `event_1253`, `event_1260`, `event_1267` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-03-10 | debit | -159 | -58.37 | -217.37 | `recurring:education` | recurring | `event_1254`, `event_1261`, `event_1268` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-03-13 | debit | -84 | -217.37 | -301.37 | `recurring:debt_repayment` | recurring | `event_1255`, `event_1262`, `event_1269` | - | history supports a fixed 30-day recurrence |
| 19 | 2026-03-13 | debit | -11 | -301.37 | -312.37 | `recurring:music_subscription` | recurring | `event_1256`, `event_1263`, `event_1270` | - | history supports a fixed 30-day recurrence |
| 20 | 2026-03-15 | debit | -27 | -312.37 | -339.37 | `recurring:delivery_membership` | recurring | `event_1257`, `event_1264`, `event_1271` | - | history supports a fixed 30-day recurrence |
| 21 | 2026-03-25 | debit | -41.35 | -339.37 | -380.72 | `recurring:transport` | recurring | `event_1316`, `event_1319`, `event_1322` | - | history supports a fixed 21-day recurrence |
| 22 | 2026-04-04 | debit | -435.6 | -380.72 | -816.32 | `recurring:rent` | recurring | `event_1259`, `event_1266`, `event_1272` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1240` | 2025-08-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1241` | 2025-08-08 | debit | 84.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1242` | 2025-08-10 | debit | 159 | already reflected in the current balance; may remain recurrence evidence |
| `event_1243` | 2025-08-13 | debit | 84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1244` | 2025-08-13 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1245` | 2025-08-15 | debit | 27 | already reflected in the current balance; may remain recurrence evidence |
| `event_1246` | 2025-09-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1247` | 2025-09-08 | debit | 85.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1248` | 2025-09-10 | debit | 159 | already reflected in the current balance; may remain recurrence evidence |
| `event_1249` | 2025-09-13 | debit | 84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1250` | 2025-09-13 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1251` | 2025-09-15 | debit | 27 | already reflected in the current balance; may remain recurrence evidence |
| `event_1252` | 2025-10-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1253` | 2025-10-08 | debit | 90.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1254` | 2025-10-10 | debit | 159 | already reflected in the current balance; may remain recurrence evidence |
| `event_1255` | 2025-10-13 | debit | 84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1256` | 2025-10-13 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1257` | 2025-10-15 | debit | 27 | already reflected in the current balance; may remain recurrence evidence |
| `event_1258` | 2025-11-15 | credit | 1661 | already reflected in the current balance; may remain recurrence evidence |
| `event_1259` | 2025-11-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1260` | 2025-11-08 | debit | 87.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1261` | 2025-11-10 | debit | 159 | already reflected in the current balance; may remain recurrence evidence |
| `event_1262` | 2025-11-13 | debit | 84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1263` | 2025-11-13 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1264` | 2025-11-15 | debit | 27 | already reflected in the current balance; may remain recurrence evidence |
| `event_1265` | 2025-12-15 | credit | 1661 | already reflected in the current balance; may remain recurrence evidence |
| `event_1266` | 2025-12-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1267` | 2025-12-08 | debit | 84.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1268` | 2025-12-10 | debit | 159 | already reflected in the current balance; may remain recurrence evidence |
| `event_1269` | 2025-12-13 | debit | 84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1270` | 2025-12-13 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1271` | 2025-12-15 | debit | 27 | already reflected in the current balance; may remain recurrence evidence |
| `event_1272` | 2026-01-04 | debit | 435.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1273` | 2025-07-15 | debit | 51.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_1274` | 2025-07-22 | debit | 63.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1275` | 2025-07-29 | debit | 64.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1276` | 2025-08-05 | debit | 55.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1277` | 2025-08-12 | debit | 68.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1278` | 2025-08-19 | debit | 46.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_1279` | 2025-08-26 | debit | 71.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_1280` | 2025-09-02 | debit | 49.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1281` | 2025-09-09 | debit | 73.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1282` | 2025-09-16 | debit | 71.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_1283` | 2025-09-23 | debit | 72.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_1284` | 2025-09-30 | debit | 59.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1285` | 2025-10-07 | debit | 48.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1286` | 2025-10-14 | debit | 69.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_1287` | 2025-10-21 | debit | 62.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1288` | 2025-10-28 | debit | 68.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1289` | 2025-11-04 | debit | 56.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1290` | 2025-11-11 | debit | 52.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1291` | 2025-11-18 | debit | 53.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1292` | 2025-11-25 | debit | 47.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1293` | 2025-12-02 | debit | 64.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1294` | 2025-12-09 | debit | 64.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1295` | 2025-12-16 | debit | 52.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_1296` | 2025-12-23 | debit | 49.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1297` | 2025-12-30 | debit | 64.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1298` | 2025-07-16 | debit | 29.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1299` | 2025-07-23 | debit | 39.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_1300` | 2025-07-30 | debit | 42.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1301` | 2025-08-06 | debit | 29.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1302` | 2025-08-13 | debit | 26.48 | already reflected in the current balance; may remain recurrence evidence |
| `event_1303` | 2025-08-20 | debit | 26.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1304` | 2025-08-27 | debit | 25.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1305` | 2025-09-03 | debit | 37.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_1306` | 2025-09-10 | debit | 29.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_1307` | 2025-09-17 | debit | 35.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1308` | 2025-09-24 | debit | 31.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1309` | 2025-10-01 | debit | 29.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_1310` | 2025-10-08 | debit | 26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1311` | 2025-10-15 | debit | 25.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_1312` | 2025-10-22 | debit | 25.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1313` | 2025-10-29 | debit | 34.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1314` | 2025-11-05 | debit | 31.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1315` | 2025-11-12 | debit | 32.48 | already reflected in the current balance; may remain recurrence evidence |
| `event_1316` | 2025-11-19 | debit | 36.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1317` | 2025-11-26 | debit | 38.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1318` | 2025-12-03 | debit | 25.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1319` | 2025-12-10 | debit | 41.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1320` | 2025-12-17 | debit | 36.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1321` | 2025-12-24 | debit | 27.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1322` | 2025-12-31 | debit | 30.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_1323` | 2025-07-12 | debit | 33.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1324` | 2025-07-26 | debit | 41.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1325` | 2025-08-09 | debit | 45.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1326` | 2025-08-23 | debit | 44.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1327` | 2025-09-06 | debit | 53.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1328` | 2025-09-20 | debit | 36.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1329` | 2025-10-04 | debit | 32.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1330` | 2025-10-18 | debit | 34.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1331` | 2025-11-01 | debit | 38.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_1332` | 2025-11-15 | debit | 51.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1333` | 2025-11-29 | debit | 32.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_1334` | 2025-12-13 | debit | 38.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_1335` | 2025-12-27 | debit | 49.35 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_17 - user_17

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 243849.58 | 274600 |
| `earliest_date_for_full_payment` | 2026-03-15 | 2026-03-01 |

### Balance diagnostics

- Current balance: `550379.58` INR
- Required minimum: `166100` INR
- Baseline minimum before request payment: `444618.05` on `2026-03-14`
- Computed safe amount now: `274600`
- Computed earliest safe full-payment date: `2026-03-01`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-03-05 | debit | -49600 | 550379.58 | 500779.58 | `recurring:rent` | recurring | `event_1458`, `event_1465`, `event_1472` | - | history supports a fixed 31-day recurrence |
| 2 | 2026-03-09 | debit | -10246.53 | 500779.58 | 490533.05 | `recurring:utilities` | recurring | `event_1459`, `event_1466`, `event_1473` | - | history supports a fixed 31-day recurrence |
| 3 | 2026-03-11 | debit | -13660 | 490533.05 | 476873.05 | `recurring:education` | recurring | `event_1460`, `event_1467`, `event_1474` | - | history supports a fixed 31-day recurrence |
| 4 | 2026-03-14 | debit | -30200 | 476873.05 | 446673.05 | `recurring:debt_repayment` | recurring | `event_1461`, `event_1468`, `event_1475` | - | history supports a fixed 31-day recurrence |
| 5 | 2026-03-14 | debit | -2055 | 446673.05 | 444618.05 | `recurring:music_subscription` | recurring | `event_1462`, `event_1469`, `event_1476` | - | history supports a fixed 31-day recurrence |
| 6 | 2026-03-15 | credit | 206000 | 444618.05 | 650618.05 | `event_1546` | explicit | `event_1546` | - | cash event |
| 7 | 2026-03-16 | debit | -1675 | 650618.05 | 648943.05 | `recurring:delivery_membership` | recurring | `event_1463`, `event_1470`, `event_1477` | - | history supports a fixed 31-day recurrence |
| 8 | 2026-03-18 | credit | 206000 | 648943.05 | 854943.05 | `recurring:salary` | recurring | `event_1457`, `event_1464`, `event_1471` | - | history supports a fixed 31-day recurrence |
| 9 | 2026-04-05 | debit | -49600 | 854943.05 | 805343.05 | `recurring:rent` | recurring | `event_1458`, `event_1465`, `event_1472` | - | history supports a fixed 31-day recurrence |
| 10 | 2026-04-09 | debit | -10246.53 | 805343.05 | 795096.52 | `recurring:utilities` | recurring | `event_1459`, `event_1466`, `event_1473` | - | history supports a fixed 31-day recurrence |
| 11 | 2026-04-11 | debit | -13660 | 795096.52 | 781436.52 | `recurring:education` | recurring | `event_1460`, `event_1467`, `event_1474` | - | history supports a fixed 31-day recurrence |
| 12 | 2026-04-14 | debit | -30200 | 781436.52 | 751236.52 | `recurring:debt_repayment` | recurring | `event_1461`, `event_1468`, `event_1475` | - | history supports a fixed 31-day recurrence |
| 13 | 2026-04-14 | debit | -2055 | 751236.52 | 749181.52 | `recurring:music_subscription` | recurring | `event_1462`, `event_1469`, `event_1476` | - | history supports a fixed 31-day recurrence |
| 14 | 2026-04-16 | debit | -1675 | 749181.52 | 747506.52 | `recurring:delivery_membership` | recurring | `event_1463`, `event_1470`, `event_1477` | - | history supports a fixed 31-day recurrence |
| 15 | 2026-04-18 | credit | 206000 | 747506.52 | 953506.52 | `recurring:salary` | recurring | `event_1457`, `event_1464`, `event_1471` | - | history supports a fixed 31-day recurrence |
| 16 | 2026-05-06 | debit | -49600 | 953506.52 | 903906.52 | `recurring:rent` | recurring | `event_1458`, `event_1465`, `event_1472` | - | history supports a fixed 31-day recurrence |
| 17 | 2026-05-10 | debit | -10246.53 | 903906.52 | 893659.99 | `recurring:utilities` | recurring | `event_1459`, `event_1466`, `event_1473` | - | history supports a fixed 31-day recurrence |
| 18 | 2026-05-12 | debit | -13660 | 893659.99 | 879999.99 | `recurring:education` | recurring | `event_1460`, `event_1467`, `event_1474` | - | history supports a fixed 31-day recurrence |
| 19 | 2026-05-15 | debit | -30200 | 879999.99 | 849799.99 | `recurring:debt_repayment` | recurring | `event_1461`, `event_1468`, `event_1475` | - | history supports a fixed 31-day recurrence |
| 20 | 2026-05-15 | debit | -2055 | 849799.99 | 847744.99 | `recurring:music_subscription` | recurring | `event_1462`, `event_1469`, `event_1476` | - | history supports a fixed 31-day recurrence |
| 21 | 2026-05-17 | debit | -1675 | 847744.99 | 846069.99 | `recurring:delivery_membership` | recurring | `event_1463`, `event_1470`, `event_1477` | - | history supports a fixed 31-day recurrence |
| 22 | 2026-05-19 | credit | 206000 | 846069.99 | 1052069.99 | `recurring:salary` | recurring | `event_1457`, `event_1464`, `event_1471` | - | history supports a fixed 31-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1443` | 2025-10-15 | credit | 206000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1444` | 2025-10-02 | debit | 49600 | already reflected in the current balance; may remain recurrence evidence |
| `event_1445` | 2025-10-06 | debit | 9481.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1446` | 2025-10-08 | debit | 13660 | already reflected in the current balance; may remain recurrence evidence |
| `event_1447` | 2025-10-11 | debit | 30200 | already reflected in the current balance; may remain recurrence evidence |
| `event_1448` | 2025-10-11 | debit | 2055 | already reflected in the current balance; may remain recurrence evidence |
| `event_1449` | 2025-10-13 | debit | 1675 | already reflected in the current balance; may remain recurrence evidence |
| `event_1450` | 2025-11-15 | credit | 206000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1451` | 2025-11-02 | debit | 49600 | already reflected in the current balance; may remain recurrence evidence |
| `event_1452` | 2025-11-06 | debit | 9530.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1453` | 2025-11-08 | debit | 13660 | already reflected in the current balance; may remain recurrence evidence |
| `event_1454` | 2025-11-11 | debit | 30200 | already reflected in the current balance; may remain recurrence evidence |
| `event_1455` | 2025-11-11 | debit | 2055 | already reflected in the current balance; may remain recurrence evidence |
| `event_1456` | 2025-11-13 | debit | 1675 | already reflected in the current balance; may remain recurrence evidence |
| `event_1457` | 2025-12-15 | credit | 206000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1458` | 2025-12-02 | debit | 49600 | already reflected in the current balance; may remain recurrence evidence |
| `event_1459` | 2025-12-06 | debit | 10246.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1460` | 2025-12-08 | debit | 13660 | already reflected in the current balance; may remain recurrence evidence |
| `event_1461` | 2025-12-11 | debit | 30200 | already reflected in the current balance; may remain recurrence evidence |
| `event_1462` | 2025-12-11 | debit | 2055 | already reflected in the current balance; may remain recurrence evidence |
| `event_1463` | 2025-12-13 | debit | 1675 | already reflected in the current balance; may remain recurrence evidence |
| `event_1464` | 2026-01-15 | credit | 206000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1465` | 2026-01-02 | debit | 49600 | already reflected in the current balance; may remain recurrence evidence |
| `event_1466` | 2026-01-06 | debit | 9948.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1467` | 2026-01-08 | debit | 13660 | already reflected in the current balance; may remain recurrence evidence |
| `event_1468` | 2026-01-11 | debit | 30200 | already reflected in the current balance; may remain recurrence evidence |
| `event_1469` | 2026-01-11 | debit | 2055 | already reflected in the current balance; may remain recurrence evidence |
| `event_1470` | 2026-01-13 | debit | 1675 | already reflected in the current balance; may remain recurrence evidence |
| `event_1471` | 2026-02-15 | credit | 206000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1472` | 2026-02-02 | debit | 49600 | already reflected in the current balance; may remain recurrence evidence |
| `event_1473` | 2026-02-06 | debit | 8487.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1474` | 2026-02-08 | debit | 13660 | already reflected in the current balance; may remain recurrence evidence |
| `event_1475` | 2026-02-11 | debit | 30200 | already reflected in the current balance; may remain recurrence evidence |
| `event_1476` | 2026-02-11 | debit | 2055 | already reflected in the current balance; may remain recurrence evidence |
| `event_1477` | 2026-02-13 | debit | 1675 | already reflected in the current balance; may remain recurrence evidence |
| `event_1478` | 2025-09-05 | debit | 9392.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1479` | 2025-09-12 | debit | 7679.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1480` | 2025-09-19 | debit | 10039.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1481` | 2025-09-26 | debit | 9785.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1482` | 2025-10-03 | debit | 7187.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_1483` | 2025-10-10 | debit | 8574.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_1484` | 2025-10-17 | debit | 11380.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1485` | 2025-10-24 | debit | 6706.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1486` | 2025-10-31 | debit | 7585.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_1487` | 2025-11-07 | debit | 7446.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1488` | 2025-11-14 | debit | 10300.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_1489` | 2025-11-21 | debit | 8500.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1490` | 2025-11-28 | debit | 7237.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_1491` | 2025-12-05 | debit | 8836.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_1492` | 2025-12-12 | debit | 10690 | already reflected in the current balance; may remain recurrence evidence |
| `event_1493` | 2025-12-19 | debit | 10432.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1494` | 2025-12-26 | debit | 11392.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_1495` | 2026-01-02 | debit | 8124.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_1496` | 2026-01-09 | debit | 11433.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1497` | 2026-01-16 | debit | 7093.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_1498` | 2026-01-23 | debit | 8638.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1499` | 2026-01-30 | debit | 8581.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_1500` | 2026-02-06 | debit | 11342.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_1501` | 2026-02-13 | debit | 10873.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1502` | 2026-02-20 | debit | 8543.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_1503` | 2026-02-27 | debit | 8716.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1504` | 2025-09-06 | debit | 3913.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1505` | 2025-09-13 | debit | 6046.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1506` | 2025-09-20 | debit | 3972.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1507` | 2025-09-27 | debit | 5639.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1508` | 2025-10-04 | debit | 4445.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1509` | 2025-10-11 | debit | 6225.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_1510` | 2025-10-18 | debit | 5386.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1511` | 2025-10-25 | debit | 5421.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_1512` | 2025-11-01 | debit | 5936.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1513` | 2025-11-08 | debit | 6420.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1514` | 2025-11-15 | debit | 4008.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1515` | 2025-11-22 | debit | 5126.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1516` | 2025-11-29 | debit | 5036.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1517` | 2025-12-06 | debit | 6170.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1518` | 2025-12-13 | debit | 5790.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_1519` | 2025-12-20 | debit | 4328.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1520` | 2025-12-27 | debit | 5080.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_1521` | 2026-01-03 | debit | 4844.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1522` | 2026-01-10 | debit | 5940.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_1523` | 2026-01-17 | debit | 6406.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1524` | 2026-01-24 | debit | 5758.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_1525` | 2026-01-31 | debit | 4661.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1526` | 2026-02-07 | debit | 5650.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_1527` | 2026-02-14 | debit | 3902.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1528` | 2026-02-21 | debit | 5741.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1529` | 2026-02-28 | debit | 5372.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1530` | 2025-09-07 | debit | 5641.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_1531` | 2025-09-21 | debit | 4425.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_1532` | 2025-10-05 | debit | 4695.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_1533` | 2025-10-19 | debit | 5554.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1534` | 2025-11-02 | debit | 6027.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1535` | 2025-11-16 | debit | 5593.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1536` | 2025-11-30 | debit | 6839.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_1537` | 2025-12-14 | debit | 6048.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1538` | 2025-12-28 | debit | 6795.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1539` | 2026-01-11 | debit | 6797.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1540` | 2026-01-25 | debit | 5254.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1541` | 2026-02-08 | debit | 6688.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_1542` | 2026-02-22 | debit | 4747.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_1543` | 2026-01-26 | debit | 12360 | superseded transaction lifecycle record |
| `event_1544` | 2026-02-26 | credit | 12360 | already reflected in the current balance; may remain recurrence evidence |
| `event_1545` | 2026-02-27 | debit | - | amount requires linked image review |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| installments | 2026-03-01 | 2026-04-30 | 285584.01 | 3 | `payment_option_47` | `(False, False, Decimal('285584.01'), datetime.date(2026, 3, 1), 3, 'payment_option_47')` | selected |

## request_18 - user_18

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 462 | 787.59 |
| `payment_plan` | 2026-09-15:3246.10 | 2026-08-15:3246.1 |
| `earliest_date_for_full_payment` | 2026-09-15 | 2026-08-15 |

### Balance diagnostics

- Current balance: `2486` EUR
- Required minimum: `1400` EUR
- Baseline minimum before request payment: `2187.59` on `2026-07-11`
- Computed safe amount now: `787.59`
- Computed earliest safe full-payment date: `2026-08-15`
- Immediate-full first breach: `2026-07-07` after `request_payment`, closing at `-760.1`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-07-08 | debit | -68 | 2486 | 2418 | `recurring:insurance` | recurring | `event_1562`, `event_1568`, `event_1574` | - | history supports a fixed 30-day recurrence |
| 2 | 2026-07-10 | debit | -68 | 2418 | 2350 | `recurring:streaming` | recurring | `event_1564`, `event_1570`, `event_1576` | - | history supports a fixed 30-day recurrence |
| 3 | 2026-07-11 | debit | -162.41 | 2350 | 2187.59 | `recurring:healthcare` | recurring | `event_1563`, `event_1569`, `event_1575` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-07-15 | credit | 2310 | 2187.59 | 4497.59 | `recurring:salary` | recurring | `event_1559`, `event_1565`, `event_1571` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-08-03 | debit | -167 | 4497.59 | 4330.59 | `recurring:housing` | recurring | `event_1566`, `event_1572`, `event_1577` | - | history supports a fixed 30-day recurrence |
| 6 | 2026-08-06 | debit | -125.4 | 4330.59 | 4205.19 | `recurring:utilities` | recurring | `event_1561`, `event_1567`, `event_1573` | - | history supports a fixed 30-day recurrence |
| 7 | 2026-08-07 | debit | -68 | 4205.19 | 4137.19 | `recurring:insurance` | recurring | `event_1562`, `event_1568`, `event_1574` | - | history supports a fixed 30-day recurrence |
| 8 | 2026-08-09 | debit | -68 | 4137.19 | 4069.19 | `recurring:streaming` | recurring | `event_1564`, `event_1570`, `event_1576` | - | history supports a fixed 30-day recurrence |
| 9 | 2026-08-10 | debit | -162.41 | 4069.19 | 3906.78 | `recurring:healthcare` | recurring | `event_1563`, `event_1569`, `event_1575` | - | history supports a fixed 30-day recurrence |
| 10 | 2026-08-14 | credit | 2310 | 3906.78 | 6216.78 | `recurring:salary` | recurring | `event_1559`, `event_1565`, `event_1571` | - | history supports a fixed 30-day recurrence |
| 11 | 2026-09-02 | debit | -167 | 6216.78 | 6049.78 | `recurring:housing` | recurring | `event_1566`, `event_1572`, `event_1577` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-09-05 | debit | -125.4 | 6049.78 | 5924.38 | `recurring:utilities` | recurring | `event_1561`, `event_1567`, `event_1573` | - | history supports a fixed 30-day recurrence |
| 13 | 2026-09-06 | debit | -68 | 5924.38 | 5856.38 | `recurring:insurance` | recurring | `event_1562`, `event_1568`, `event_1574` | - | history supports a fixed 30-day recurrence |
| 14 | 2026-09-08 | debit | -68 | 5856.38 | 5788.38 | `recurring:streaming` | recurring | `event_1564`, `event_1570`, `event_1576` | - | history supports a fixed 30-day recurrence |
| 15 | 2026-09-09 | debit | -162.41 | 5788.38 | 5625.97 | `recurring:healthcare` | recurring | `event_1563`, `event_1569`, `event_1575` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-09-13 | credit | 2310 | 5625.97 | 7935.97 | `recurring:salary` | recurring | `event_1559`, `event_1565`, `event_1571` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-10-02 | debit | -167 | 7935.97 | 7768.97 | `recurring:housing` | recurring | `event_1566`, `event_1572`, `event_1577` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-10-05 | debit | -125.4 | 7768.97 | 7643.57 | `recurring:utilities` | recurring | `event_1561`, `event_1567`, `event_1573` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1547` | 2026-02-15 | credit | 2310 | already reflected in the current balance; may remain recurrence evidence |
| `event_1548` | 2026-02-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1549` | 2026-02-07 | debit | 100.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1550` | 2026-02-08 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1551` | 2026-02-11 | debit | 164.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_1552` | 2026-02-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1553` | 2026-03-15 | credit | 2310 | already reflected in the current balance; may remain recurrence evidence |
| `event_1554` | 2026-03-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1555` | 2026-03-07 | debit | 101.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_1556` | 2026-03-08 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1557` | 2026-03-11 | debit | 150.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1558` | 2026-03-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1559` | 2026-04-15 | credit | 2310 | already reflected in the current balance; may remain recurrence evidence |
| `event_1560` | 2026-04-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1561` | 2026-04-07 | debit | 125.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_1562` | 2026-04-08 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1563` | 2026-04-11 | debit | 152.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1564` | 2026-04-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1565` | 2026-05-15 | credit | 2310 | already reflected in the current balance; may remain recurrence evidence |
| `event_1566` | 2026-05-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1567` | 2026-05-07 | debit | 121.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1568` | 2026-05-08 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1569` | 2026-05-11 | debit | 162.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1570` | 2026-05-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1571` | 2026-06-15 | credit | 2310 | already reflected in the current balance; may remain recurrence evidence |
| `event_1572` | 2026-06-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1573` | 2026-06-07 | debit | 107.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_1574` | 2026-06-08 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1575` | 2026-06-11 | debit | 147.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1576` | 2026-06-10 | debit | 68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1577` | 2026-07-04 | debit | 167 | already reflected in the current balance; may remain recurrence evidence |
| `event_1578` | 2026-01-12 | debit | 64.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1579` | 2026-01-22 | debit | 101.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1580` | 2026-02-01 | debit | 96.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1581` | 2026-02-11 | debit | 101.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1582` | 2026-02-21 | debit | 87.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1583` | 2026-03-03 | debit | 106.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_1584` | 2026-03-13 | debit | 66.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_1585` | 2026-03-23 | debit | 108.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1586` | 2026-04-02 | debit | 110.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1587` | 2026-04-12 | debit | 82.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1588` | 2026-04-22 | debit | 94.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_1589` | 2026-05-02 | debit | 115 | already reflected in the current balance; may remain recurrence evidence |
| `event_1590` | 2026-05-12 | debit | 83.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1591` | 2026-05-22 | debit | 87.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1592` | 2026-06-01 | debit | 71.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_1593` | 2026-06-11 | debit | 101.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1594` | 2026-06-21 | debit | 90.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1595` | 2026-07-01 | debit | 111.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1596` | 2026-01-13 | debit | 36.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1597` | 2026-01-27 | debit | 35.48 | already reflected in the current balance; may remain recurrence evidence |
| `event_1598` | 2026-02-10 | debit | 54.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1599` | 2026-02-24 | debit | 53.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1600` | 2026-03-10 | debit | 38.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1601` | 2026-03-24 | debit | 52.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1602` | 2026-04-07 | debit | 36.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_1603` | 2026-04-21 | debit | 47.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1604` | 2026-05-05 | debit | 50.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_1605` | 2026-05-19 | debit | 34.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1606` | 2026-06-02 | debit | 36.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1607` | 2026-06-16 | debit | 49.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_1608` | 2026-06-30 | debit | 43.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_1609` | 2026-01-14 | debit | 66.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1610` | 2026-01-28 | debit | 69.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1611` | 2026-02-11 | debit | 92.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_1612` | 2026-02-25 | debit | 98.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_1613` | 2026-03-11 | debit | 108.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1614` | 2026-03-25 | debit | 75.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1615` | 2026-04-08 | debit | 66.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1616` | 2026-04-22 | debit | 103.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1617` | 2026-05-06 | debit | 81.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1618` | 2026-05-20 | debit | 101.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1619` | 2026-06-03 | debit | 62.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1620` | 2026-06-17 | debit | 82.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1621` | 2026-07-01 | debit | 101.88 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| wait | 2026-08-15 | 2026-08-15 | 3246.1 | 1 | `-` | `(False, False, Decimal('3246.1'), datetime.date(2026, 8, 15), 1, '')` | selected |

## request_19 - user_19

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 28820 | 39660 |
| `recommended_payment_method` | partial_payment | installments |
| `payment_plan` | 2024-09-04:28820\|2024-09-15:10840 | 2024-09-04:20623.2\|2024-10-02:20623.2 |
| `earliest_date_for_full_payment` | 2024-09-15 | 2024-09-04 |

### Balance diagnostics

- Current balance: `199545` INR
- Required minimum: `92800` INR
- Baseline minimum before request payment: `147735.02` on `2024-09-14`
- Computed safe amount now: `39660`
- Computed earliest safe full-payment date: `2024-09-04`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-09-07 | debit | -6129.19 | 199545 | 193415.81 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence |
| 2 | 2024-09-11 | debit | -8645.36 | 193415.81 | 184770.45 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence |
| 3 | 2024-09-12 | debit | -11850 | 184770.45 | 172920.45 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence |
| 4 | 2024-09-12 | debit | -6070.85 | 172920.45 | 166849.6 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence |
| 5 | 2024-09-13 | debit | -395 | 166849.6 | 166454.6 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence |
| 6 | 2024-09-13 | debit | -6069.58 | 166454.6 | 160385.02 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence |
| 7 | 2024-09-14 | debit | -12650 | 160385.02 | 147735.02 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence |
| 8 | 2024-09-14 | credit | 131000 | 147735.02 | 278735.02 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence |
| 9 | 2024-10-03 | debit | -36100 | 278735.02 | 242635.02 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence |
| 10 | 2024-10-06 | debit | -6070.85 | 242635.02 | 236564.17 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence |
| 11 | 2024-10-07 | debit | -6129.19 | 236564.17 | 230434.98 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence |
| 12 | 2024-10-11 | debit | -8645.36 | 230434.98 | 221789.62 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence |
| 13 | 2024-10-12 | debit | -11850 | 221789.62 | 209939.62 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence |
| 14 | 2024-10-13 | debit | -395 | 209939.62 | 209544.62 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence |
| 15 | 2024-10-13 | debit | -6069.58 | 209544.62 | 203475.04 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence |
| 16 | 2024-10-14 | debit | -12650 | 203475.04 | 190825.04 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence |
| 17 | 2024-10-14 | credit | 131000 | 190825.04 | 321825.04 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence |
| 18 | 2024-10-30 | debit | -6070.85 | 321825.04 | 315754.19 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence |
| 19 | 2024-11-02 | debit | -36100 | 315754.19 | 279654.19 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence |
| 20 | 2024-11-06 | debit | -6129.19 | 279654.19 | 273525 | `recurring:utilities` | recurring | `event_1640`, `event_1648`, `event_1656` | - | history supports a fixed 30-day recurrence |
| 21 | 2024-11-10 | debit | -8645.36 | 273525 | 264879.64 | `recurring:healthcare` | recurring | `event_1642`, `event_1650`, `event_1658` | - | history supports a fixed 30-day recurrence |
| 22 | 2024-11-11 | debit | -11850 | 264879.64 | 253029.64 | `recurring:debt_repayment` | recurring | `event_1641`, `event_1649`, `event_1657` | - | history supports a fixed 30-day recurrence |
| 23 | 2024-11-12 | debit | -395 | 253029.64 | 252634.64 | `recurring:cloud_storage` | recurring | `event_1644`, `event_1652`, `event_1660` | - | history supports a fixed 30-day recurrence |
| 24 | 2024-11-12 | debit | -6069.58 | 252634.64 | 246565.06 | `recurring:shopping` | recurring | `event_1645`, `event_1653`, `event_1661` | - | history supports a fixed 30-day recurrence |
| 25 | 2024-11-13 | debit | -12650 | 246565.06 | 233915.06 | `recurring:family_support` | recurring | `event_1643`, `event_1651`, `event_1659` | - | history supports a fixed 30-day recurrence |
| 26 | 2024-11-13 | credit | 131000 | 233915.06 | 364915.06 | `recurring:salary` | recurring | `event_1638`, `event_1646`, `event_1654` | - | history supports a fixed 30-day recurrence |
| 27 | 2024-11-23 | debit | -6070.85 | 364915.06 | 358844.21 | `recurring:groceries` | recurring | `event_1664`, `event_1668`, `event_1671` | - | history supports a fixed 24-day recurrence |
| 28 | 2024-12-02 | debit | -36100 | 358844.21 | 322744.21 | `recurring:rent` | recurring | `event_1639`, `event_1647`, `event_1655` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1622` | 2024-04-15 | credit | 131000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1623` | 2024-04-04 | debit | 36100 | already reflected in the current balance; may remain recurrence evidence |
| `event_1624` | 2024-04-08 | debit | 6141.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1625` | 2024-04-13 | debit | 11850 | already reflected in the current balance; may remain recurrence evidence |
| `event_1626` | 2024-04-12 | debit | 8946.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1627` | 2024-04-15 | debit | 12650 | already reflected in the current balance; may remain recurrence evidence |
| `event_1628` | 2024-04-14 | debit | 395 | already reflected in the current balance; may remain recurrence evidence |
| `event_1629` | 2024-04-14 | debit | 6302.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1630` | 2024-05-15 | credit | 131000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1631` | 2024-05-04 | debit | 36100 | already reflected in the current balance; may remain recurrence evidence |
| `event_1632` | 2024-05-08 | debit | 5525.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1633` | 2024-05-13 | debit | 11850 | already reflected in the current balance; may remain recurrence evidence |
| `event_1634` | 2024-05-12 | debit | 9619.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1635` | 2024-05-15 | debit | 12650 | already reflected in the current balance; may remain recurrence evidence |
| `event_1636` | 2024-05-14 | debit | 395 | already reflected in the current balance; may remain recurrence evidence |
| `event_1637` | 2024-05-14 | debit | 5593.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1638` | 2024-06-15 | credit | 131000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1639` | 2024-06-04 | debit | 36100 | already reflected in the current balance; may remain recurrence evidence |
| `event_1640` | 2024-06-08 | debit | 6029.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1641` | 2024-06-13 | debit | 11850 | already reflected in the current balance; may remain recurrence evidence |
| `event_1642` | 2024-06-12 | debit | 8335.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1643` | 2024-06-15 | debit | 12650 | already reflected in the current balance; may remain recurrence evidence |
| `event_1644` | 2024-06-14 | debit | 395 | already reflected in the current balance; may remain recurrence evidence |
| `event_1645` | 2024-06-14 | debit | 6069.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1646` | 2024-07-15 | credit | 131000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1647` | 2024-07-04 | debit | 36100 | already reflected in the current balance; may remain recurrence evidence |
| `event_1648` | 2024-07-08 | debit | 5951.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_1649` | 2024-07-13 | debit | 11850 | already reflected in the current balance; may remain recurrence evidence |
| `event_1650` | 2024-07-12 | debit | 8496.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1651` | 2024-07-15 | debit | 12650 | already reflected in the current balance; may remain recurrence evidence |
| `event_1652` | 2024-07-14 | debit | 395 | already reflected in the current balance; may remain recurrence evidence |
| `event_1653` | 2024-07-14 | debit | 5772.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_1654` | 2024-08-15 | credit | 131000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1655` | 2024-08-04 | debit | 36100 | already reflected in the current balance; may remain recurrence evidence |
| `event_1656` | 2024-08-08 | debit | 6129.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_1657` | 2024-08-13 | debit | 11850 | already reflected in the current balance; may remain recurrence evidence |
| `event_1658` | 2024-08-12 | debit | 8645.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_1659` | 2024-08-15 | debit | 12650 | already reflected in the current balance; may remain recurrence evidence |
| `event_1660` | 2024-08-14 | debit | 395 | already reflected in the current balance; may remain recurrence evidence |
| `event_1661` | 2024-08-14 | debit | 5431.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1662` | 2024-03-13 | debit | 4418.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1663` | 2024-03-20 | debit | 4871.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_1664` | 2024-03-27 | debit | 6070.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1665` | 2024-04-03 | debit | 5452.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1666` | 2024-04-10 | debit | 5912.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_1667` | 2024-04-17 | debit | 3877.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_1668` | 2024-04-24 | debit | 4056.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1669` | 2024-05-01 | debit | 4744.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1670` | 2024-05-08 | debit | 3593.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1671` | 2024-05-15 | debit | 3852.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1672` | 2024-05-22 | debit | 5406.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1673` | 2024-05-29 | debit | 5542.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1674` | 2024-06-05 | debit | 4738.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1675` | 2024-06-12 | debit | 3575.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_1676` | 2024-06-19 | debit | 5146.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1677` | 2024-06-26 | debit | 5908.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1678` | 2024-07-03 | debit | 4444.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_1679` | 2024-07-10 | debit | 4667.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1680` | 2024-07-17 | debit | 4493.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1681` | 2024-07-24 | debit | 5184.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_1682` | 2024-07-31 | debit | 3460.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1683` | 2024-08-07 | debit | 6005.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1684` | 2024-08-14 | debit | 4963.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1685` | 2024-08-21 | debit | 4864.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_1686` | 2024-08-28 | debit | 4068.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1687` | 2024-03-14 | debit | 3054.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_1688` | 2024-03-28 | debit | 3298.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1689` | 2024-04-11 | debit | 3476.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_1690` | 2024-04-25 | debit | 3849.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1691` | 2024-05-09 | debit | 2640.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1692` | 2024-05-23 | debit | 3432.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_1693` | 2024-06-06 | debit | 2610.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_1694` | 2024-06-20 | debit | 2788.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1695` | 2024-07-04 | debit | 3242.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1696` | 2024-07-18 | debit | 3659.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1697` | 2024-08-01 | debit | 2759.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_1698` | 2024-08-15 | debit | 2462.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1699` | 2024-08-29 | debit | 2765.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_1700` | 2024-09-03 | debit | - | amount requires linked image review |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| installments | 2024-09-04 | 2024-10-02 | 41246.4 | 2 | `payment_option_53` | `(False, False, Decimal('41246.4'), datetime.date(2024, 9, 4), 2, 'payment_option_53')` | selected |

## request_20 - user_20

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 5400 | 24503.8 |

### Balance diagnostics

- Current balance: `102609.05` INR
- Required minimum: `64500` INR
- Baseline minimum before request payment: `89003.8` on `2026-02-12`
- Computed safe amount now: `24503.8`
- Computed earliest safe full-payment date: ``
- Immediate-full first breach: `2026-02-07` after `request_payment`, closing at `-201090.95`

### Included 90-day forecast ledger

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

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1701` | 2025-09-15 | credit | 108000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1702` | 2025-09-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1703` | 2025-09-05 | debit | 7784.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1704` | 2025-09-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1705` | 2025-09-07 | debit | 8740 | already reflected in the current balance; may remain recurrence evidence |
| `event_1706` | 2025-09-09 | debit | 5968.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1707` | 2025-09-13 | debit | 2298.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_1708` | 2025-09-11 | debit | 365 | already reflected in the current balance; may remain recurrence evidence |
| `event_1709` | 2025-10-15 | credit | 108000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1710` | 2025-10-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1711` | 2025-10-05 | debit | 7977.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1712` | 2025-10-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1713` | 2025-10-07 | debit | 8740 | already reflected in the current balance; may remain recurrence evidence |
| `event_1714` | 2025-10-09 | debit | 6648.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1715` | 2025-10-13 | debit | 2279.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1716` | 2025-10-11 | debit | 365 | already reflected in the current balance; may remain recurrence evidence |
| `event_1717` | 2025-11-15 | credit | 108000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1718` | 2025-11-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1719` | 2025-11-05 | debit | 8058.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1720` | 2025-11-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1721` | 2025-11-07 | debit | 8740 | already reflected in the current balance; may remain recurrence evidence |
| `event_1722` | 2025-11-09 | debit | 5907.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_1723` | 2025-11-13 | debit | 2115.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_1724` | 2025-11-11 | debit | 365 | already reflected in the current balance; may remain recurrence evidence |
| `event_1725` | 2025-12-15 | credit | 108000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1726` | 2025-12-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1727` | 2025-12-05 | debit | 6848.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_1728` | 2025-12-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1729` | 2025-12-07 | debit | 8740 | already reflected in the current balance; may remain recurrence evidence |
| `event_1730` | 2025-12-09 | debit | 6505.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_1731` | 2025-12-13 | debit | 1949.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1732` | 2025-12-11 | debit | 365 | already reflected in the current balance; may remain recurrence evidence |
| `event_1733` | 2026-01-15 | credit | 108000 | already reflected in the current balance; may remain recurrence evidence |
| `event_1734` | 2026-01-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1735` | 2026-01-05 | debit | 7551.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_1736` | 2026-01-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1737` | 2026-01-07 | debit | 8740 | already reflected in the current balance; may remain recurrence evidence |
| `event_1738` | 2026-01-09 | debit | 6654.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1739` | 2026-01-13 | debit | 2097.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1740` | 2026-01-11 | debit | 365 | already reflected in the current balance; may remain recurrence evidence |
| `event_1741` | 2026-02-02 | debit | 7950 | already reflected in the current balance; may remain recurrence evidence |
| `event_1742` | 2026-02-05 | debit | 7769.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1743` | 2026-02-06 | debit | 3290 | already reflected in the current balance; may remain recurrence evidence |
| `event_1744` | 2025-08-13 | debit | 3866.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1745` | 2025-08-23 | debit | 3724.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_1746` | 2025-09-02 | debit | 3127.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_1747` | 2025-09-12 | debit | 4104.17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1748` | 2025-09-22 | debit | 2968.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_1749` | 2025-10-02 | debit | 4660.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1750` | 2025-10-12 | debit | 4109.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1751` | 2025-10-22 | debit | 2812.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_1752` | 2025-11-01 | debit | 3525.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_1753` | 2025-11-11 | debit | 3386.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1754` | 2025-11-21 | debit | 3796.24 | already reflected in the current balance; may remain recurrence evidence |
| `event_1755` | 2025-12-01 | debit | 3016.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1756` | 2025-12-11 | debit | 4683.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_1757` | 2025-12-21 | debit | 3067.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1758` | 2025-12-31 | debit | 3588.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_1759` | 2026-01-10 | debit | 3752.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1760` | 2026-01-20 | debit | 3702.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_1761` | 2026-01-30 | debit | 4719.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1762` | 2025-08-14 | debit | 2046.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1763` | 2025-08-28 | debit | 2060.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1764` | 2025-09-11 | debit | 2195.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1765` | 2025-09-25 | debit | 2632 | already reflected in the current balance; may remain recurrence evidence |
| `event_1766` | 2025-10-09 | debit | 3063.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1767` | 2025-10-23 | debit | 2359.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1768` | 2025-11-06 | debit | 2628.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1769` | 2025-11-20 | debit | 2836.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1770` | 2025-12-04 | debit | 2570.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1771` | 2025-12-18 | debit | 3145.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1772` | 2026-01-01 | debit | 2838.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1773` | 2026-01-15 | debit | 3150.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1774` | 2026-01-29 | debit | 3243.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1775` | 2025-08-15 | debit | 3150.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_1776` | 2025-09-05 | debit | 3075.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1777` | 2025-09-26 | debit | 3365.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1778` | 2025-10-17 | debit | 4270.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_1779` | 2025-11-07 | debit | 2857.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_1780` | 2025-11-28 | debit | 4308.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1781` | 2025-12-19 | debit | 2629.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1782` | 2026-01-09 | debit | 3352.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1783` | 2026-01-30 | debit | 3803.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1784` | 2026-01-15 | debit | 8640 | superseded transaction lifecycle record |
| `event_1785` | 2026-02-14 | credit | - | explicit statement that the related credit is not yet available; evidence message_14 |
| `event_1786` | 2026-02-09 | debit | - | amount requires linked image review |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_21 - user_21

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 1543.35 | 1574.4 |
| `affordability_status` | affordable_with_plan | affordable_now |
| `payment_plan` | 2026-04-03:1574.40 | 2026-04-03:1574.4 |
| `earliest_date_for_full_payment` | 2026-04-15 | 2026-04-03 |
| `spending_changes_needed` | stop:event_1815\|reduce_to:event_1816:23.50 | none |

### Balance diagnostics

- Current balance: `3911.35` USD
- Required minimum: `1800` USD
- Baseline minimum before request payment: `3549.89` on `2026-04-11`
- Computed safe amount now: `1574.4`
- Computed earliest safe full-payment date: `2026-04-03`
- Immediate-full first breach: none

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-04-05 | debit | -53 | 3911.35 | 3858.35 | `event_1857` | explicit | `event_1857` | - | pending debit retained as a conservative liability |
| 2 | 2026-04-05 | debit | -124.08 | 3858.35 | 3734.27 | `recurring:utilities` | recurring | `event_1802`, `event_1808`, `event_1814` | - | history supports a fixed 30-day recurrence |
| 3 | 2026-04-08 | debit | -47 | 3734.27 | 3687.27 | `recurring:streaming` | recurring | `event_1804`, `event_1810`, `event_1816` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-04-11 | debit | -11 | 3687.27 | 3676.27 | `recurring:cloud_storage` | recurring | `event_1803`, `event_1809`, `event_1815` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-04-11 | debit | -126.38 | 3676.27 | 3549.89 | `recurring:shopping` | recurring | `event_1805`, `event_1811`, `event_1817` | - | history supports a fixed 30-day recurrence |
| 6 | 2026-04-14 | credit | 2256 | 3549.89 | 5805.89 | `recurring:salary` | recurring | `event_1800`, `event_1806`, `event_1812` | - | history supports a fixed 30-day recurrence |
| 7 | 2026-04-15 | credit | 2256 | 5805.89 | 8061.89 | `event_1858` | explicit | `event_1858` | - | cash event |
| 8 | 2026-05-03 | debit | -718.8 | 8061.89 | 7343.09 | `recurring:rent` | recurring | `event_1807`, `event_1813`, `event_1818` | - | history supports a fixed 31-day recurrence |
| 9 | 2026-05-05 | debit | -124.08 | 7343.09 | 7219.01 | `recurring:utilities` | recurring | `event_1802`, `event_1808`, `event_1814` | - | history supports a fixed 30-day recurrence |
| 10 | 2026-05-08 | debit | -47 | 7219.01 | 7172.01 | `recurring:streaming` | recurring | `event_1804`, `event_1810`, `event_1816` | - | history supports a fixed 30-day recurrence |
| 11 | 2026-05-11 | debit | -11 | 7172.01 | 7161.01 | `recurring:cloud_storage` | recurring | `event_1803`, `event_1809`, `event_1815` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-05-11 | debit | -126.38 | 7161.01 | 7034.63 | `recurring:shopping` | recurring | `event_1805`, `event_1811`, `event_1817` | - | history supports a fixed 30-day recurrence |
| 13 | 2026-05-14 | credit | 2256 | 7034.63 | 9290.63 | `recurring:salary` | recurring | `event_1800`, `event_1806`, `event_1812` | - | history supports a fixed 30-day recurrence |
| 14 | 2026-06-03 | debit | -718.8 | 9290.63 | 8571.83 | `recurring:rent` | recurring | `event_1807`, `event_1813`, `event_1818` | - | history supports a fixed 31-day recurrence |
| 15 | 2026-06-04 | debit | -124.08 | 8571.83 | 8447.75 | `recurring:utilities` | recurring | `event_1802`, `event_1808`, `event_1814` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-06-07 | debit | -47 | 8447.75 | 8400.75 | `recurring:streaming` | recurring | `event_1804`, `event_1810`, `event_1816` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-06-10 | debit | -11 | 8400.75 | 8389.75 | `recurring:cloud_storage` | recurring | `event_1803`, `event_1809`, `event_1815` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-06-10 | debit | -126.38 | 8389.75 | 8263.37 | `recurring:shopping` | recurring | `event_1805`, `event_1811`, `event_1817` | - | history supports a fixed 30-day recurrence |
| 19 | 2026-06-13 | credit | 2256 | 8263.37 | 10519.37 | `recurring:salary` | recurring | `event_1800`, `event_1806`, `event_1812` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1788` | 2025-11-15 | credit | 2256 | already reflected in the current balance; may remain recurrence evidence |
| `event_1789` | 2025-11-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1790` | 2025-11-06 | debit | 115.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_1791` | 2025-11-12 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1792` | 2025-11-09 | debit | 47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1793` | 2025-11-12 | debit | 133.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1794` | 2025-12-15 | credit | 2256 | already reflected in the current balance; may remain recurrence evidence |
| `event_1795` | 2025-12-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1796` | 2025-12-06 | debit | 123.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_1797` | 2025-12-12 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1798` | 2025-12-09 | debit | 47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1799` | 2025-12-12 | debit | 115.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1800` | 2026-01-15 | credit | 2256 | already reflected in the current balance; may remain recurrence evidence |
| `event_1801` | 2026-01-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1802` | 2026-01-06 | debit | 120.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1803` | 2026-01-12 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1804` | 2026-01-09 | debit | 47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1805` | 2026-01-12 | debit | 120.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_1806` | 2026-02-15 | credit | 2256 | already reflected in the current balance; may remain recurrence evidence |
| `event_1807` | 2026-02-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1808` | 2026-02-06 | debit | 122.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1809` | 2026-02-12 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1810` | 2026-02-09 | debit | 47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1811` | 2026-02-12 | debit | 115.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1812` | 2026-03-15 | credit | 2256 | already reflected in the current balance; may remain recurrence evidence |
| `event_1813` | 2026-03-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1814` | 2026-03-06 | debit | 124.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1815` | 2026-03-12 | debit | 11 | already reflected in the current balance; may remain recurrence evidence |
| `event_1816` | 2026-03-09 | debit | 47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1817` | 2026-03-12 | debit | 126.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1818` | 2026-04-02 | debit | 718.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_1819` | 2025-10-08 | debit | 65.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_1820` | 2025-10-18 | debit | 104.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1821` | 2025-10-28 | debit | 92.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_1822` | 2025-11-07 | debit | 68.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1823` | 2025-11-17 | debit | 95.62 | already reflected in the current balance; may remain recurrence evidence |
| `event_1824` | 2025-11-27 | debit | 104.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_1825` | 2025-12-07 | debit | 72.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_1826` | 2025-12-17 | debit | 101.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1827` | 2025-12-27 | debit | 84.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1828` | 2026-01-06 | debit | 77.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1829` | 2026-01-16 | debit | 79 | already reflected in the current balance; may remain recurrence evidence |
| `event_1830` | 2026-01-26 | debit | 66.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_1831` | 2026-02-05 | debit | 85.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1832` | 2026-02-15 | debit | 90.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_1833` | 2026-02-25 | debit | 71.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1834` | 2026-03-07 | debit | 70.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_1835` | 2026-03-17 | debit | 77.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1836` | 2026-03-27 | debit | 97.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_1837` | 2025-10-09 | debit | 38.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1838` | 2025-10-30 | debit | 37.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_1839` | 2025-11-20 | debit | 34.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_1840` | 2025-12-11 | debit | 50 | already reflected in the current balance; may remain recurrence evidence |
| `event_1841` | 2026-01-01 | debit | 40.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1842` | 2026-01-22 | debit | 33.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1843` | 2026-02-12 | debit | 51.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_1844` | 2026-03-05 | debit | 47.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1845` | 2026-03-26 | debit | 36.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_1846` | 2025-10-10 | debit | 82.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_1847` | 2025-10-31 | debit | 68.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_1848` | 2025-11-21 | debit | 85.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_1849` | 2025-12-12 | debit | 60.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_1850` | 2026-01-02 | debit | 88.07 | already reflected in the current balance; may remain recurrence evidence |
| `event_1851` | 2026-01-23 | debit | 100.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1852` | 2026-02-13 | debit | 97.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1853` | 2026-03-06 | debit | 98.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1854` | 2026-03-27 | debit | 69.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_1855` | 2025-12-29 | debit | 676.8 | superseded transaction lifecycle record |
| `event_1856` | 2026-04-01 | non_cash | - | unrealized event |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| full_payment | 2026-04-03 | 2026-04-03 | 1574.4 | 1 | `payment_option_57` | `(False, False, Decimal('1574.4'), datetime.date(2026, 4, 3), 1, 'payment_option_57')` | selected |

## request_22 - user_22

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 475.46 | 506.65 |
| `earliest_date_for_full_payment` | 2025-01-15 | 2024-12-17 |

### Balance diagnostics

- Current balance: `1132.46` EUR
- Required minimum: `500` EUR
- Baseline minimum before request payment: `1006.65` on `2024-12-16`
- Computed safe amount now: `506.65`
- Computed earliest safe full-payment date: `2024-12-17`
- Immediate-full first breach: `2024-12-05` after `request_payment`, closing at `400.96`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-12-08 | debit | -43 | 1132.46 | 1089.46 | `event_1961` | explicit | `event_1961` | - | pending debit retained as a conservative liability |
| 2 | 2024-12-08 | debit | -31.52 | 1089.46 | 1057.94 | `recurring:utilities` | recurring | `event_1875`, `event_1882`, `event_1889` | - | history supports a fixed 31-day recurrence |
| 3 | 2024-12-12 | debit | -17 | 1057.94 | 1040.94 | `recurring:gym` | recurring | `event_1878`, `event_1885`, `event_1892` | - | history supports a fixed 31-day recurrence |
| 4 | 2024-12-13 | debit | -6 | 1040.94 | 1034.94 | `recurring:music_subscription` | recurring | `event_1876`, `event_1883`, `event_1890` | - | history supports a fixed 31-day recurrence |
| 5 | 2024-12-15 | debit | -5 | 1034.94 | 1029.94 | `recurring:delivery_membership` | recurring | `event_1877`, `event_1884`, `event_1891` | - | history supports a fixed 31-day recurrence |
| 6 | 2024-12-16 | debit | -23.29 | 1029.94 | 1006.65 | `recurring:entertainment` | recurring | `event_1879`, `event_1886`, `event_1893` | - | history supports a fixed 31-day recurrence |
| 7 | 2024-12-16 | credit | 616 | 1006.65 | 1622.65 | `recurring:salary` | recurring | `event_1873`, `event_1880`, `event_1887` | - | history supports a fixed 31-day recurrence |
| 8 | 2024-12-28 | debit | -12.7 | 1622.65 | 1609.95 | `recurring:transport` | recurring | `event_1922`, `event_1926`, `event_1931` | - | history supports a fixed 32-day recurrence |
| 9 | 2025-01-02 | debit | -178.2 | 1609.95 | 1431.75 | `recurring:rent` | recurring | `event_1881`, `event_1888`, `event_1894` | - | history supports a fixed 30-day recurrence |
| 10 | 2025-01-08 | debit | -31.52 | 1431.75 | 1400.23 | `recurring:utilities` | recurring | `event_1875`, `event_1882`, `event_1889` | - | history supports a fixed 31-day recurrence |
| 11 | 2025-01-12 | debit | -17 | 1400.23 | 1383.23 | `recurring:gym` | recurring | `event_1878`, `event_1885`, `event_1892` | - | history supports a fixed 31-day recurrence |
| 12 | 2025-01-13 | debit | -6 | 1383.23 | 1377.23 | `recurring:music_subscription` | recurring | `event_1876`, `event_1883`, `event_1890` | - | history supports a fixed 31-day recurrence |
| 13 | 2025-01-15 | debit | -5 | 1377.23 | 1372.23 | `recurring:delivery_membership` | recurring | `event_1877`, `event_1884`, `event_1891` | - | history supports a fixed 31-day recurrence |
| 14 | 2025-01-16 | debit | -23.29 | 1372.23 | 1348.94 | `recurring:entertainment` | recurring | `event_1879`, `event_1886`, `event_1893` | - | history supports a fixed 31-day recurrence |
| 15 | 2025-01-16 | credit | 616 | 1348.94 | 1964.94 | `recurring:salary` | recurring | `event_1873`, `event_1880`, `event_1887` | - | history supports a fixed 31-day recurrence |
| 16 | 2025-01-29 | debit | -12.7 | 1964.94 | 1952.24 | `recurring:transport` | recurring | `event_1922`, `event_1926`, `event_1931` | - | history supports a fixed 32-day recurrence |
| 17 | 2025-02-01 | debit | -178.2 | 1952.24 | 1774.04 | `recurring:rent` | recurring | `event_1881`, `event_1888`, `event_1894` | - | history supports a fixed 30-day recurrence |
| 18 | 2025-02-08 | debit | -31.52 | 1774.04 | 1742.52 | `recurring:utilities` | recurring | `event_1875`, `event_1882`, `event_1889` | - | history supports a fixed 31-day recurrence |
| 19 | 2025-02-12 | debit | -17 | 1742.52 | 1725.52 | `recurring:gym` | recurring | `event_1878`, `event_1885`, `event_1892` | - | history supports a fixed 31-day recurrence |
| 20 | 2025-02-13 | debit | -6 | 1725.52 | 1719.52 | `recurring:music_subscription` | recurring | `event_1876`, `event_1883`, `event_1890` | - | history supports a fixed 31-day recurrence |
| 21 | 2025-02-15 | debit | -5 | 1719.52 | 1714.52 | `recurring:delivery_membership` | recurring | `event_1877`, `event_1884`, `event_1891` | - | history supports a fixed 31-day recurrence |
| 22 | 2025-02-16 | debit | -23.29 | 1714.52 | 1691.23 | `recurring:entertainment` | recurring | `event_1879`, `event_1886`, `event_1893` | - | history supports a fixed 31-day recurrence |
| 23 | 2025-02-16 | credit | 616 | 1691.23 | 2307.23 | `recurring:salary` | recurring | `event_1873`, `event_1880`, `event_1887` | - | history supports a fixed 31-day recurrence |
| 24 | 2025-03-02 | debit | -12.7 | 2307.23 | 2294.53 | `recurring:transport` | recurring | `event_1922`, `event_1926`, `event_1931` | - | history supports a fixed 32-day recurrence |
| 25 | 2025-03-03 | debit | -178.2 | 2294.53 | 2116.33 | `recurring:rent` | recurring | `event_1881`, `event_1888`, `event_1894` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1859` | 2024-07-15 | credit | 616 | already reflected in the current balance; may remain recurrence evidence |
| `event_1860` | 2024-07-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1861` | 2024-07-07 | debit | 32.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1862` | 2024-07-12 | debit | 6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1863` | 2024-07-14 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1864` | 2024-07-11 | debit | 17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1865` | 2024-07-15 | debit | 19.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_1866` | 2024-08-15 | credit | 616 | already reflected in the current balance; may remain recurrence evidence |
| `event_1867` | 2024-08-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1868` | 2024-08-07 | debit | 33.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_1869` | 2024-08-12 | debit | 6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1870` | 2024-08-14 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1871` | 2024-08-11 | debit | 17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1872` | 2024-08-15 | debit | 18.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1873` | 2024-09-15 | credit | 616 | already reflected in the current balance; may remain recurrence evidence |
| `event_1874` | 2024-09-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1875` | 2024-09-07 | debit | 31.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_1876` | 2024-09-12 | debit | 6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1877` | 2024-09-14 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1878` | 2024-09-11 | debit | 17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1879` | 2024-09-15 | debit | 23.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_1880` | 2024-10-15 | credit | 616 | already reflected in the current balance; may remain recurrence evidence |
| `event_1881` | 2024-10-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1882` | 2024-10-07 | debit | 27.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1883` | 2024-10-12 | debit | 6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1884` | 2024-10-14 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1885` | 2024-10-11 | debit | 17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1886` | 2024-10-15 | debit | 22.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1887` | 2024-11-15 | credit | 616 | already reflected in the current balance; may remain recurrence evidence |
| `event_1888` | 2024-11-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1889` | 2024-11-07 | debit | 27.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1890` | 2024-11-12 | debit | 6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1891` | 2024-11-14 | debit | 5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1892` | 2024-11-11 | debit | 17 | already reflected in the current balance; may remain recurrence evidence |
| `event_1893` | 2024-11-15 | debit | 20.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_1894` | 2024-12-03 | debit | 178.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1895` | 2024-06-12 | debit | 23.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1896` | 2024-06-19 | debit | 29.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1897` | 2024-06-26 | debit | 22.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1898` | 2024-07-03 | debit | 20.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1899` | 2024-07-10 | debit | 26.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_1900` | 2024-07-17 | debit | 28.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_1901` | 2024-07-24 | debit | 22.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_1902` | 2024-07-31 | debit | 25.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_1903` | 2024-08-07 | debit | 20.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_1904` | 2024-08-14 | debit | 22.19 | already reflected in the current balance; may remain recurrence evidence |
| `event_1905` | 2024-08-21 | debit | 21.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_1906` | 2024-08-28 | debit | 23.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1907` | 2024-09-04 | debit | 23.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_1908` | 2024-09-11 | debit | 28.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1909` | 2024-09-18 | debit | 22.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_1910` | 2024-09-25 | debit | 19.54 | already reflected in the current balance; may remain recurrence evidence |
| `event_1911` | 2024-10-02 | debit | 29.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1912` | 2024-10-09 | debit | 27.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1913` | 2024-10-16 | debit | 23.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1914` | 2024-10-23 | debit | 21.58 | already reflected in the current balance; may remain recurrence evidence |
| `event_1915` | 2024-10-30 | debit | 29.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_1916` | 2024-11-06 | debit | 27.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1917` | 2024-11-13 | debit | 18.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_1918` | 2024-11-20 | debit | 18.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_1919` | 2024-11-27 | debit | 18.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_1920` | 2024-12-04 | debit | 26.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1921` | 2024-06-13 | debit | 16.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1922` | 2024-06-20 | debit | 11.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1923` | 2024-06-27 | debit | 16.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1924` | 2024-07-04 | debit | 10.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_1925` | 2024-07-11 | debit | 12.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1926` | 2024-07-18 | debit | 12.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1927` | 2024-07-25 | debit | 12.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_1928` | 2024-08-01 | debit | 12.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1929` | 2024-08-08 | debit | 9.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_1930` | 2024-08-15 | debit | 10.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1931` | 2024-08-22 | debit | 10.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_1932` | 2024-08-29 | debit | 11.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1933` | 2024-09-05 | debit | 12.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1934` | 2024-09-12 | debit | 15.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_1935` | 2024-09-19 | debit | 10.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_1936` | 2024-09-26 | debit | 15.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1937` | 2024-10-03 | debit | 13.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1938` | 2024-10-10 | debit | 9.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1939` | 2024-10-17 | debit | 15.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_1940` | 2024-10-24 | debit | 15.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_1941` | 2024-10-31 | debit | 15.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1942` | 2024-11-07 | debit | 14.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_1943` | 2024-11-14 | debit | 11.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_1944` | 2024-11-21 | debit | 15.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_1945` | 2024-11-28 | debit | 15.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_1946` | 2024-06-14 | debit | 12.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_1947` | 2024-06-28 | debit | 18.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_1948` | 2024-07-12 | debit | 13.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_1949` | 2024-07-26 | debit | 14.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_1950` | 2024-08-09 | debit | 20.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1951` | 2024-08-23 | debit | 15.63 | already reflected in the current balance; may remain recurrence evidence |
| `event_1952` | 2024-09-06 | debit | 17.66 | already reflected in the current balance; may remain recurrence evidence |
| `event_1953` | 2024-09-20 | debit | 16.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_1954` | 2024-10-04 | debit | 14.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1955` | 2024-10-18 | debit | 18.53 | already reflected in the current balance; may remain recurrence evidence |
| `event_1956` | 2024-11-01 | debit | 12.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_1957` | 2024-11-15 | debit | 15.84 | already reflected in the current balance; may remain recurrence evidence |
| `event_1958` | 2024-11-29 | debit | 18.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_1959` | 2024-09-01 | debit | 184.8 | superseded transaction lifecycle record |
| `event_1960` | 2024-12-03 | non_cash | - | unrealized event |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| installments | 2024-12-08 | 2025-02-02 | 760.77 | 3 | `payment_option_61` | `(False, False, Decimal('760.77'), datetime.date(2024, 12, 8), 3, 'payment_option_61')` | selected |

## request_23 - user_23

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 9152 | 7241.63 |
| `affordability_status` | affordable_later | not_affordable |
| `recommended_payment_method` | wait | not_recommended |
| `payment_plan` | 2025-07-15:38016 | none |
| `earliest_date_for_full_payment` | 2025-07-15 |  |

### Balance diagnostics

- Current balance: `51957.9` ZAR
- Required minimum: `27000` ZAR
- Baseline minimum before request payment: `34241.63` on `2025-05-16`
- Computed safe amount now: `7241.63`
- Computed earliest safe full-payment date: `2025-07-18`
- Immediate-full first breach: `2025-05-07` after `request_payment`, closing at `13941.9`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2025-05-09 | debit | -2915.67 | 51957.9 | 49042.23 | `recurring:utilities` | recurring | `event_1980`, `event_1988`, `event_1996` | - | history supports a fixed 31-day recurrence |
| 2 | 2025-05-11 | debit | -1553.2 | 49042.23 | 47489.03 | `event_2042` | explicit | `event_2042` | - | pending debit retained as a conservative liability |
| 3 | 2025-05-13 | debit | -1439.91 | 47489.03 | 46049.12 | `recurring:healthcare` | recurring | `event_1982`, `event_1990`, `event_1998` | - | history supports a fixed 31-day recurrence |
| 4 | 2025-05-14 | debit | -5852 | 46049.12 | 40197.12 | `recurring:debt_repayment` | recurring | `event_1981`, `event_1989`, `event_1997` | - | history supports a fixed 31-day recurrence |
| 5 | 2025-05-15 | debit | -295.9 | 40197.12 | 39901.22 | `recurring:cloud_storage` | recurring | `event_1984`, `event_1992`, `event_2000` | - | history supports a fixed 31-day recurrence |
| 6 | 2025-05-15 | debit | -1389.39 | 39901.22 | 38511.83 | `recurring:shopping` | recurring | `event_1985`, `event_1993`, `event_2001` | - | history supports a fixed 31-day recurrence |
| 7 | 2025-05-16 | debit | -4270.2 | 38511.83 | 34241.63 | `recurring:family_support` | recurring | `event_1983`, `event_1991`, `event_1999` | - | history supports a fixed 31-day recurrence |
| 8 | 2025-05-16 | credit | 45760 | 34241.63 | 80001.63 | `recurring:salary` | recurring | `event_1978`, `event_1986`, `event_1994` | - | history supports a fixed 31-day recurrence |
| 9 | 2025-06-03 | debit | -15312 | 80001.63 | 64689.63 | `recurring:rent` | recurring | `event_1987`, `event_1995`, `event_2002` | - | history supports a fixed 30-day recurrence |
| 10 | 2025-06-09 | debit | -2915.67 | 64689.63 | 61773.96 | `recurring:utilities` | recurring | `event_1980`, `event_1988`, `event_1996` | - | history supports a fixed 31-day recurrence |
| 11 | 2025-06-13 | debit | -1439.91 | 61773.96 | 60334.05 | `recurring:healthcare` | recurring | `event_1982`, `event_1990`, `event_1998` | - | history supports a fixed 31-day recurrence |
| 12 | 2025-06-14 | debit | -5852 | 60334.05 | 54482.05 | `recurring:debt_repayment` | recurring | `event_1981`, `event_1989`, `event_1997` | - | history supports a fixed 31-day recurrence |
| 13 | 2025-06-15 | debit | -295.9 | 54482.05 | 54186.15 | `recurring:cloud_storage` | recurring | `event_1984`, `event_1992`, `event_2000` | - | history supports a fixed 31-day recurrence |
| 14 | 2025-06-15 | debit | -1389.39 | 54186.15 | 52796.76 | `recurring:shopping` | recurring | `event_1985`, `event_1993`, `event_2001` | - | history supports a fixed 31-day recurrence |
| 15 | 2025-06-16 | debit | -4270.2 | 52796.76 | 48526.56 | `recurring:family_support` | recurring | `event_1983`, `event_1991`, `event_1999` | - | history supports a fixed 31-day recurrence |
| 16 | 2025-06-16 | credit | 45760 | 48526.56 | 94286.56 | `recurring:salary` | recurring | `event_1978`, `event_1986`, `event_1994` | - | history supports a fixed 31-day recurrence |
| 17 | 2025-07-03 | debit | -15312 | 94286.56 | 78974.56 | `recurring:rent` | recurring | `event_1987`, `event_1995`, `event_2002` | - | history supports a fixed 30-day recurrence |
| 18 | 2025-07-10 | debit | -2915.67 | 78974.56 | 76058.89 | `recurring:utilities` | recurring | `event_1980`, `event_1988`, `event_1996` | - | history supports a fixed 31-day recurrence |
| 19 | 2025-07-14 | debit | -1439.91 | 76058.89 | 74618.98 | `recurring:healthcare` | recurring | `event_1982`, `event_1990`, `event_1998` | - | history supports a fixed 31-day recurrence |
| 20 | 2025-07-15 | debit | -5852 | 74618.98 | 68766.98 | `recurring:debt_repayment` | recurring | `event_1981`, `event_1989`, `event_1997` | - | history supports a fixed 31-day recurrence |
| 21 | 2025-07-16 | debit | -295.9 | 68766.98 | 68471.08 | `recurring:cloud_storage` | recurring | `event_1984`, `event_1992`, `event_2000` | - | history supports a fixed 31-day recurrence |
| 22 | 2025-07-16 | debit | -1389.39 | 68471.08 | 67081.69 | `recurring:shopping` | recurring | `event_1985`, `event_1993`, `event_2001` | - | history supports a fixed 31-day recurrence |
| 23 | 2025-07-17 | debit | -4270.2 | 67081.69 | 62811.49 | `recurring:family_support` | recurring | `event_1983`, `event_1991`, `event_1999` | - | history supports a fixed 31-day recurrence |
| 24 | 2025-07-17 | credit | 45760 | 62811.49 | 108571.49 | `recurring:salary` | recurring | `event_1978`, `event_1986`, `event_1994` | - | history supports a fixed 31-day recurrence |
| 25 | 2025-08-02 | debit | -15312 | 108571.49 | 93259.49 | `recurring:rent` | recurring | `event_1987`, `event_1995`, `event_2002` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_1962` | 2024-12-15 | credit | 45760 | already reflected in the current balance; may remain recurrence evidence |
| `event_1963` | 2024-12-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_1964` | 2024-12-08 | debit | 2877.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_1965` | 2024-12-13 | debit | 5852 | already reflected in the current balance; may remain recurrence evidence |
| `event_1966` | 2024-12-12 | debit | 1341.05 | already reflected in the current balance; may remain recurrence evidence |
| `event_1967` | 2024-12-15 | debit | 4270.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1968` | 2024-12-14 | debit | 295.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1969` | 2024-12-14 | debit | 1279.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1970` | 2025-01-15 | credit | 45760 | already reflected in the current balance; may remain recurrence evidence |
| `event_1971` | 2025-01-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_1972` | 2025-01-08 | debit | 2484.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_1973` | 2025-01-13 | debit | 5852 | already reflected in the current balance; may remain recurrence evidence |
| `event_1974` | 2025-01-12 | debit | 1331.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_1975` | 2025-01-15 | debit | 4270.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1976` | 2025-01-14 | debit | 295.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1977` | 2025-01-14 | debit | 1396.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_1978` | 2025-02-15 | credit | 45760 | already reflected in the current balance; may remain recurrence evidence |
| `event_1979` | 2025-02-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_1980` | 2025-02-08 | debit | 2915.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_1981` | 2025-02-13 | debit | 5852 | already reflected in the current balance; may remain recurrence evidence |
| `event_1982` | 2025-02-12 | debit | 1439.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_1983` | 2025-02-15 | debit | 4270.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1984` | 2025-02-14 | debit | 295.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1985` | 2025-02-14 | debit | 1389.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_1986` | 2025-03-15 | credit | 45760 | already reflected in the current balance; may remain recurrence evidence |
| `event_1987` | 2025-03-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_1988` | 2025-03-08 | debit | 2813.94 | already reflected in the current balance; may remain recurrence evidence |
| `event_1989` | 2025-03-13 | debit | 5852 | already reflected in the current balance; may remain recurrence evidence |
| `event_1990` | 2025-03-12 | debit | 1317.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_1991` | 2025-03-15 | debit | 4270.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_1992` | 2025-03-14 | debit | 295.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_1993` | 2025-03-14 | debit | 1232.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_1994` | 2025-04-15 | credit | 45760 | already reflected in the current balance; may remain recurrence evidence |
| `event_1995` | 2025-04-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_1996` | 2025-04-08 | debit | 2680.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_1997` | 2025-04-13 | debit | 5852 | already reflected in the current balance; may remain recurrence evidence |
| `event_1998` | 2025-04-12 | debit | 1377.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_1999` | 2025-04-15 | debit | 4270.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2000` | 2025-04-14 | debit | 295.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_2001` | 2025-04-14 | debit | 1281.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_2002` | 2025-05-04 | debit | 15312 | already reflected in the current balance; may remain recurrence evidence |
| `event_2003` | 2024-11-13 | debit | 1401.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_2004` | 2024-11-20 | debit | 1332.28 | already reflected in the current balance; may remain recurrence evidence |
| `event_2005` | 2024-11-27 | debit | 1586.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_2006` | 2024-12-04 | debit | 1372.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_2007` | 2024-12-11 | debit | 1821.15 | already reflected in the current balance; may remain recurrence evidence |
| `event_2008` | 2024-12-18 | debit | 2207.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_2009` | 2024-12-25 | debit | 1981.14 | already reflected in the current balance; may remain recurrence evidence |
| `event_2010` | 2025-01-01 | debit | 2178.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_2011` | 2025-01-08 | debit | 1927.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_2012` | 2025-01-15 | debit | 2125.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_2013` | 2025-01-22 | debit | 1544.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_2014` | 2025-01-29 | debit | 1914.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_2015` | 2025-02-05 | debit | 1421.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_2016` | 2025-02-12 | debit | 1556.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_2017` | 2025-02-19 | debit | 2186.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_2018` | 2025-02-26 | debit | 2146.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_2019` | 2025-03-05 | debit | 1717.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2020` | 2025-03-12 | debit | 2074.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_2021` | 2025-03-19 | debit | 1372.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_2022` | 2025-03-26 | debit | 1706.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_2023` | 2025-04-02 | debit | 1487.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_2024` | 2025-04-09 | debit | 1794.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2025` | 2025-04-16 | debit | 1678.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_2026` | 2025-04-23 | debit | 1514.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_2027` | 2025-04-30 | debit | 1257.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_2028` | 2024-11-14 | debit | 682.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_2029` | 2024-11-28 | debit | 1121.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_2030` | 2024-12-12 | debit | 747.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_2031` | 2024-12-26 | debit | 777.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_2032` | 2025-01-09 | debit | 896.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_2033` | 2025-01-23 | debit | 904.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_2034` | 2025-02-06 | debit | 968.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_2035` | 2025-02-20 | debit | 1046.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_2036` | 2025-03-06 | debit | 738.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_2037` | 2025-03-20 | debit | 956.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_2038` | 2025-04-03 | debit | 1092.98 | already reflected in the current balance; may remain recurrence evidence |
| `event_2039` | 2025-04-17 | debit | 834 | already reflected in the current balance; may remain recurrence evidence |
| `event_2040` | 2025-05-01 | debit | 783.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_2041` | 2025-02-01 | debit | 13728 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_24 - user_24

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 13420 | 23553.06 |

### Balance diagnostics

- Current balance: `85045` INR
- Required minimum: `51000` INR
- Baseline minimum before request payment: `74553.06` on `2026-01-12`
- Computed safe amount now: `23553.06`
- Computed earliest safe full-payment date: `2026-03-16`
- Immediate-full first breach: `2026-01-04` after `request_payment`, closing at `-24555`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2026-01-05 | debit | -2510 | 85045 | 82535 | `recurring:insurance` | recurring | `event_2062`, `event_2070`, `event_2078` | - | history supports a fixed 30-day recurrence |
| 2 | 2026-01-07 | debit | -1200 | 82535 | 81335 | `recurring:streaming` | recurring | `event_2064`, `event_2072`, `event_2080` | - | history supports a fixed 30-day recurrence |
| 3 | 2026-01-10 | debit | -355 | 81335 | 80980 | `recurring:cloud_storage` | recurring | `event_2063`, `event_2071`, `event_2079` | - | history supports a fixed 30-day recurrence |
| 4 | 2026-01-10 | debit | -2680.78 | 80980 | 78299.22 | `recurring:shopping` | recurring | `event_2065`, `event_2073`, `event_2081` | - | history supports a fixed 30-day recurrence |
| 5 | 2026-01-11 | debit | -1830 | 78299.22 | 76469.22 | `event_2166` | explicit | `event_2166` | - | cash event |
| 6 | 2026-01-12 | debit | -1916.16 | 76469.22 | 74553.06 | `recurring:entertainment` | recurring | `event_2066`, `event_2074`, `event_2082` | - | history supports a fixed 30-day recurrence |
| 7 | 2026-01-14 | credit | 61000 | 74553.06 | 135553.06 | `recurring:salary` | recurring | `event_2059`, `event_2067`, `event_2075` | - | history supports a fixed 30-day recurrence |
| 8 | 2026-01-28 | debit | -2151.71 | 135553.06 | 133401.35 | `recurring:dining` | recurring | `event_2153`, `event_2157`, `event_2162` | - | history supports a fixed 32-day recurrence |
| 9 | 2026-01-31 | debit | -18600 | 133401.35 | 114801.35 | `recurring:rent` | recurring | `event_2068`, `event_2076`, `event_2083` | - | history supports a fixed 30-day recurrence |
| 10 | 2026-02-03 | debit | -3490.5 | 114801.35 | 111310.85 | `recurring:utilities` | recurring | `event_2061`, `event_2069`, `event_2077` | - | history supports a fixed 30-day recurrence |
| 11 | 2026-02-04 | debit | -2510 | 111310.85 | 108800.85 | `recurring:insurance` | recurring | `event_2062`, `event_2070`, `event_2078` | - | history supports a fixed 30-day recurrence |
| 12 | 2026-02-05 | debit | -2137.71 | 108800.85 | 106663.14 | `recurring:dining` | recurring | `event_2145`, `event_2149`, `event_2154` | - | history supports a fixed 32-day recurrence |
| 13 | 2026-02-06 | debit | -1200 | 106663.14 | 105463.14 | `recurring:streaming` | recurring | `event_2064`, `event_2072`, `event_2080` | - | history supports a fixed 30-day recurrence |
| 14 | 2026-02-09 | debit | -355 | 105463.14 | 105108.14 | `recurring:cloud_storage` | recurring | `event_2063`, `event_2071`, `event_2079` | - | history supports a fixed 30-day recurrence |
| 15 | 2026-02-09 | debit | -2680.78 | 105108.14 | 102427.36 | `recurring:shopping` | recurring | `event_2065`, `event_2073`, `event_2081` | - | history supports a fixed 30-day recurrence |
| 16 | 2026-02-11 | debit | -1916.16 | 102427.36 | 100511.2 | `recurring:entertainment` | recurring | `event_2066`, `event_2074`, `event_2082` | - | history supports a fixed 30-day recurrence |
| 17 | 2026-02-13 | credit | 61000 | 100511.2 | 161511.2 | `recurring:salary` | recurring | `event_2059`, `event_2067`, `event_2075` | - | history supports a fixed 30-day recurrence |
| 18 | 2026-03-01 | debit | -2151.71 | 161511.2 | 159359.49 | `recurring:dining` | recurring | `event_2153`, `event_2157`, `event_2162` | - | history supports a fixed 32-day recurrence |
| 19 | 2026-03-02 | debit | -18600 | 159359.49 | 140759.49 | `recurring:rent` | recurring | `event_2068`, `event_2076`, `event_2083` | - | history supports a fixed 30-day recurrence |
| 20 | 2026-03-05 | debit | -3490.5 | 140759.49 | 137268.99 | `recurring:utilities` | recurring | `event_2061`, `event_2069`, `event_2077` | - | history supports a fixed 30-day recurrence |
| 21 | 2026-03-06 | debit | -2510 | 137268.99 | 134758.99 | `recurring:insurance` | recurring | `event_2062`, `event_2070`, `event_2078` | - | history supports a fixed 30-day recurrence |
| 22 | 2026-03-08 | debit | -1200 | 134758.99 | 133558.99 | `recurring:streaming` | recurring | `event_2064`, `event_2072`, `event_2080` | - | history supports a fixed 30-day recurrence |
| 23 | 2026-03-09 | debit | -2137.71 | 133558.99 | 131421.28 | `recurring:dining` | recurring | `event_2145`, `event_2149`, `event_2154` | - | history supports a fixed 32-day recurrence |
| 24 | 2026-03-11 | debit | -355 | 131421.28 | 131066.28 | `recurring:cloud_storage` | recurring | `event_2063`, `event_2071`, `event_2079` | - | history supports a fixed 30-day recurrence |
| 25 | 2026-03-11 | debit | -2680.78 | 131066.28 | 128385.5 | `recurring:shopping` | recurring | `event_2065`, `event_2073`, `event_2081` | - | history supports a fixed 30-day recurrence |
| 26 | 2026-03-13 | debit | -1916.16 | 128385.5 | 126469.34 | `recurring:entertainment` | recurring | `event_2066`, `event_2074`, `event_2082` | - | history supports a fixed 30-day recurrence |
| 27 | 2026-03-15 | credit | 61000 | 126469.34 | 187469.34 | `recurring:salary` | recurring | `event_2059`, `event_2067`, `event_2075` | - | history supports a fixed 30-day recurrence |
| 28 | 2026-04-01 | debit | -18600 | 187469.34 | 168869.34 | `recurring:rent` | recurring | `event_2068`, `event_2076`, `event_2083` | - | history supports a fixed 30-day recurrence |
| 29 | 2026-04-02 | debit | -2151.71 | 168869.34 | 166717.63 | `recurring:dining` | recurring | `event_2153`, `event_2157`, `event_2162` | - | history supports a fixed 32-day recurrence |
| 30 | 2026-04-04 | debit | -3490.5 | 166717.63 | 163227.13 | `recurring:utilities` | recurring | `event_2061`, `event_2069`, `event_2077` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_2043` | 2025-08-15 | credit | 61000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2044` | 2025-08-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2045` | 2025-08-05 | debit | 3049.81 | already reflected in the current balance; may remain recurrence evidence |
| `event_2046` | 2025-08-06 | debit | 2510 | already reflected in the current balance; may remain recurrence evidence |
| `event_2047` | 2025-08-11 | debit | 355 | already reflected in the current balance; may remain recurrence evidence |
| `event_2048` | 2025-08-08 | debit | 1200 | already reflected in the current balance; may remain recurrence evidence |
| `event_2049` | 2025-08-11 | debit | 2409.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_2050` | 2025-08-13 | debit | 1870.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_2051` | 2025-09-15 | credit | 61000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2052` | 2025-09-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2053` | 2025-09-05 | debit | 3226.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_2054` | 2025-09-06 | debit | 2510 | already reflected in the current balance; may remain recurrence evidence |
| `event_2055` | 2025-09-11 | debit | 355 | already reflected in the current balance; may remain recurrence evidence |
| `event_2056` | 2025-09-08 | debit | 1200 | already reflected in the current balance; may remain recurrence evidence |
| `event_2057` | 2025-09-11 | debit | 2514.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_2058` | 2025-09-13 | debit | 2124.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_2059` | 2025-10-15 | credit | 61000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2060` | 2025-10-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2061` | 2025-10-05 | debit | 3417.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_2062` | 2025-10-06 | debit | 2510 | already reflected in the current balance; may remain recurrence evidence |
| `event_2063` | 2025-10-11 | debit | 355 | already reflected in the current balance; may remain recurrence evidence |
| `event_2064` | 2025-10-08 | debit | 1200 | already reflected in the current balance; may remain recurrence evidence |
| `event_2065` | 2025-10-11 | debit | 2680.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_2066` | 2025-10-13 | debit | 1916.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_2067` | 2025-11-15 | credit | 61000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2068` | 2025-11-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2069` | 2025-11-05 | debit | 3335.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_2070` | 2025-11-06 | debit | 2510 | already reflected in the current balance; may remain recurrence evidence |
| `event_2071` | 2025-11-11 | debit | 355 | already reflected in the current balance; may remain recurrence evidence |
| `event_2072` | 2025-11-08 | debit | 1200 | already reflected in the current balance; may remain recurrence evidence |
| `event_2073` | 2025-11-11 | debit | 2398.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2074` | 2025-11-13 | debit | 1845.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_2075` | 2025-12-15 | credit | 61000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2076` | 2025-12-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2077` | 2025-12-05 | debit | 3490.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_2078` | 2025-12-06 | debit | 2510 | already reflected in the current balance; may remain recurrence evidence |
| `event_2079` | 2025-12-11 | debit | 355 | already reflected in the current balance; may remain recurrence evidence |
| `event_2080` | 2025-12-08 | debit | 1200 | already reflected in the current balance; may remain recurrence evidence |
| `event_2081` | 2025-12-11 | debit | 2564 | already reflected in the current balance; may remain recurrence evidence |
| `event_2082` | 2025-12-13 | debit | 1896.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_2083` | 2026-01-01 | debit | 18600 | already reflected in the current balance; may remain recurrence evidence |
| `event_2084` | 2025-07-10 | debit | 2886.9 | already reflected in the current balance; may remain recurrence evidence |
| `event_2085` | 2025-07-20 | debit | 2024.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_2086` | 2025-07-30 | debit | 2236.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_2087` | 2025-08-09 | debit | 2439.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_2088` | 2025-08-19 | debit | 2564.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_2089` | 2025-08-29 | debit | 2201.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2090` | 2025-09-08 | debit | 2601.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_2091` | 2025-09-18 | debit | 2958.79 | already reflected in the current balance; may remain recurrence evidence |
| `event_2092` | 2025-09-28 | debit | 2042.7 | already reflected in the current balance; may remain recurrence evidence |
| `event_2093` | 2025-10-08 | debit | 2145.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_2094` | 2025-10-18 | debit | 1843.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2095` | 2025-10-28 | debit | 2358.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_2096` | 2025-11-07 | debit | 2295.12 | already reflected in the current balance; may remain recurrence evidence |
| `event_2097` | 2025-11-17 | debit | 1824.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_2098` | 2025-11-27 | debit | 2113.95 | already reflected in the current balance; may remain recurrence evidence |
| `event_2099` | 2025-12-07 | debit | 2260.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_2100` | 2025-12-17 | debit | 2106.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_2101` | 2025-12-27 | debit | 2321.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_2102` | 2025-07-11 | debit | 1663.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_2103` | 2025-07-16 | debit | 1021.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_2104` | 2025-07-21 | debit | 1760.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_2105` | 2025-07-26 | debit | 1208.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2106` | 2025-07-31 | debit | 1232.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_2107` | 2025-08-05 | debit | 1319.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2108` | 2025-08-10 | debit | 1536.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_2109` | 2025-08-15 | debit | 1122.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2110` | 2025-08-20 | debit | 1576.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_2111` | 2025-08-25 | debit | 1091.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_2112` | 2025-08-30 | debit | 1119.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_2113` | 2025-09-04 | debit | 1370.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_2114` | 2025-09-09 | debit | 1401.3 | already reflected in the current balance; may remain recurrence evidence |
| `event_2115` | 2025-09-14 | debit | 1393.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_2116` | 2025-09-19 | debit | 1153.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_2117` | 2025-09-24 | debit | 1586.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_2118` | 2025-09-29 | debit | 1218.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_2119` | 2025-10-04 | debit | 1750.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_2120` | 2025-10-09 | debit | 1585.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_2121` | 2025-10-14 | debit | 1069.31 | already reflected in the current balance; may remain recurrence evidence |
| `event_2122` | 2025-10-19 | debit | 1314.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_2123` | 2025-10-24 | debit | 1731.13 | already reflected in the current balance; may remain recurrence evidence |
| `event_2124` | 2025-10-29 | debit | 1110.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_2125` | 2025-11-03 | debit | 1256.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_2126` | 2025-11-08 | debit | 1514.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_2127` | 2025-11-13 | debit | 1600.18 | already reflected in the current balance; may remain recurrence evidence |
| `event_2128` | 2025-11-18 | debit | 1534.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_2129` | 2025-11-23 | debit | 1050.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_2130` | 2025-11-28 | debit | 1187.92 | already reflected in the current balance; may remain recurrence evidence |
| `event_2131` | 2025-12-03 | debit | 1270.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_2132` | 2025-12-08 | debit | 1485.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_2133` | 2025-12-13 | debit | 1341.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_2134` | 2025-12-18 | debit | 1059.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_2135` | 2025-12-23 | debit | 1438 | already reflected in the current balance; may remain recurrence evidence |
| `event_2136` | 2025-12-28 | debit | 1255.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_2137` | 2026-01-02 | debit | 1593.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_2138` | 2025-07-12 | debit | 1757.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_2139` | 2025-07-19 | debit | 1886.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_2140` | 2025-07-26 | debit | 2149.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_2141` | 2025-08-02 | debit | 2239.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_2142` | 2025-08-09 | debit | 1328.72 | already reflected in the current balance; may remain recurrence evidence |
| `event_2143` | 2025-08-16 | debit | 1291.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_2144` | 2025-08-23 | debit | 2105.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_2145` | 2025-08-30 | debit | 2046.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_2146` | 2025-09-06 | debit | 2288.09 | already reflected in the current balance; may remain recurrence evidence |
| `event_2147` | 2025-09-13 | debit | 1893.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_2148` | 2025-09-20 | debit | 1783.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_2149` | 2025-09-27 | debit | 2137.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_2150` | 2025-10-04 | debit | 1985.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_2151` | 2025-10-11 | debit | 1496.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_2152` | 2025-10-18 | debit | 1662.99 | already reflected in the current balance; may remain recurrence evidence |
| `event_2153` | 2025-10-25 | debit | 1942.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_2154` | 2025-11-01 | debit | 1818.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2155` | 2025-11-08 | debit | 1423.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_2156` | 2025-11-15 | debit | 2198 | already reflected in the current balance; may remain recurrence evidence |
| `event_2157` | 2025-11-22 | debit | 1345.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2158` | 2025-11-29 | debit | 1415.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_2159` | 2025-12-06 | debit | 1842.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2160` | 2025-12-13 | debit | 1911.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_2161` | 2025-12-20 | debit | 2184.47 | already reflected in the current balance; may remain recurrence evidence |
| `event_2162` | 2025-12-27 | debit | 2151.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_2163` | 2026-01-03 | debit | 1918.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_2164` | 2025-10-01 | debit | 18300 | already reflected in the current balance; may remain recurrence evidence |
| `event_2165` | 2025-12-28 | credit | 33550 | already reflected in the current balance; may remain recurrence evidence |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |

## request_25 - user_25

### Expected versus actual

| Field | Expected | Actual |
| --- | --- | --- |
| `amount_safe_to_pay` | 1425000 | 4567587.32 |

### Balance diagnostics

- Current balance: `32063050` IDR
- Required minimum: `23379100` IDR
- Baseline minimum before request payment: `27946687.32` on `2024-03-14`
- Computed safe amount now: `4567587.32`
- Computed earliest safe full-payment date: `2024-04-18`
- Immediate-full first breach: `2024-03-06` after `request_payment`, closing at `-28432950`

### Included 90-day forecast ledger

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- |
| 1 | 2024-03-08 | debit | -1341541.39 | 32063050 | 30721508.61 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence |
| 2 | 2024-03-09 | debit | -904400 | 30721508.61 | 29817108.61 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence |
| 3 | 2024-03-11 | debit | -573800 | 29817108.61 | 29243308.61 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence |
| 4 | 2024-03-14 | debit | -126350 | 29243308.61 | 29116958.61 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence |
| 5 | 2024-03-14 | debit | -1170271.29 | 29116958.61 | 27946687.32 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence |
| 6 | 2024-03-15 | credit | 28499994 | 27946687.32 | 56446681.32 | `event_2288` | explicit | `event_2288` | - | cash event |
| 7 | 2024-03-16 | debit | -504697.37 | 56446681.32 | 55941983.95 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence |
| 8 | 2024-03-17 | credit | 28499994 | 55941983.95 | 84441977.95 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence |
| 9 | 2024-04-01 | debit | -6954000 | 84441977.95 | 77487977.95 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence |
| 10 | 2024-04-08 | debit | -1341541.39 | 77487977.95 | 76146436.56 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence |
| 11 | 2024-04-09 | debit | -904400 | 76146436.56 | 75242036.56 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence |
| 12 | 2024-04-11 | debit | -573800 | 75242036.56 | 74668236.56 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence |
| 13 | 2024-04-14 | debit | -126350 | 74668236.56 | 74541886.56 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence |
| 14 | 2024-04-14 | debit | -1170271.29 | 74541886.56 | 73371615.27 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence |
| 15 | 2024-04-16 | debit | -504697.37 | 73371615.27 | 72866917.9 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence |
| 16 | 2024-04-17 | credit | 28499994 | 72866917.9 | 101366911.9 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence |
| 17 | 2024-05-01 | debit | -6954000 | 101366911.9 | 94412911.9 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence |
| 18 | 2024-05-09 | debit | -1341541.39 | 94412911.9 | 93071370.51 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence |
| 19 | 2024-05-10 | debit | -904400 | 93071370.51 | 92166970.51 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence |
| 20 | 2024-05-12 | debit | -573800 | 92166970.51 | 91593170.51 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence |
| 21 | 2024-05-15 | debit | -126350 | 91593170.51 | 91466820.51 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence |
| 22 | 2024-05-15 | debit | -1170271.29 | 91466820.51 | 90296549.22 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence |
| 23 | 2024-05-17 | debit | -504697.37 | 90296549.22 | 89791851.85 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence |
| 24 | 2024-05-18 | credit | 28499994 | 89791851.85 | 118291845.85 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence |
| 25 | 2024-05-31 | debit | -6954000 | 118291845.85 | 111337845.85 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence |

### Excluded source events

| Event | Cash date | Direction | Home amount | Reason |
| --- | --- | --- | ---: | --- |
| `event_2167` | 2023-10-15 | credit | 28499994 | already reflected in the current balance; may remain recurrence evidence |
| `event_2168` | 2023-10-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2169` | 2023-10-06 | debit | 1338903.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_2170` | 2023-10-07 | debit | 904400 | already reflected in the current balance; may remain recurrence evidence |
| `event_2171` | 2023-10-12 | debit | 126350 | already reflected in the current balance; may remain recurrence evidence |
| `event_2172` | 2023-10-09 | debit | 573800 | already reflected in the current balance; may remain recurrence evidence |
| `event_2173` | 2023-10-12 | debit | 966785.96 | already reflected in the current balance; may remain recurrence evidence |
| `event_2174` | 2023-10-14 | debit | 451681.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_2175` | 2023-11-15 | credit | 28499994 | already reflected in the current balance; may remain recurrence evidence |
| `event_2176` | 2023-11-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2177` | 2023-11-06 | debit | 1401205.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_2178` | 2023-11-07 | debit | 904400 | already reflected in the current balance; may remain recurrence evidence |
| `event_2179` | 2023-11-12 | debit | 126350 | already reflected in the current balance; may remain recurrence evidence |
| `event_2180` | 2023-11-09 | debit | 573800 | already reflected in the current balance; may remain recurrence evidence |
| `event_2181` | 2023-11-12 | debit | 1054608.5 | already reflected in the current balance; may remain recurrence evidence |
| `event_2182` | 2023-11-14 | debit | 415734.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_2183` | 2023-12-15 | credit | 28499994 | already reflected in the current balance; may remain recurrence evidence |
| `event_2184` | 2023-12-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2185` | 2023-12-06 | debit | 1334719.89 | already reflected in the current balance; may remain recurrence evidence |
| `event_2186` | 2023-12-07 | debit | 904400 | already reflected in the current balance; may remain recurrence evidence |
| `event_2187` | 2023-12-12 | debit | 126350 | already reflected in the current balance; may remain recurrence evidence |
| `event_2188` | 2023-12-09 | debit | 573800 | already reflected in the current balance; may remain recurrence evidence |
| `event_2189` | 2023-12-12 | debit | 1000693.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_2190` | 2023-12-14 | debit | 499510.22 | already reflected in the current balance; may remain recurrence evidence |
| `event_2191` | 2024-01-15 | credit | 28499994 | already reflected in the current balance; may remain recurrence evidence |
| `event_2192` | 2024-01-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2193` | 2024-01-06 | debit | 1341541.39 | already reflected in the current balance; may remain recurrence evidence |
| `event_2194` | 2024-01-07 | debit | 904400 | already reflected in the current balance; may remain recurrence evidence |
| `event_2195` | 2024-01-12 | debit | 126350 | already reflected in the current balance; may remain recurrence evidence |
| `event_2196` | 2024-01-09 | debit | 573800 | already reflected in the current balance; may remain recurrence evidence |
| `event_2197` | 2024-01-12 | debit | 1102784.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_2198` | 2024-01-14 | debit | 504697.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_2199` | 2024-02-15 | credit | 28499994 | already reflected in the current balance; may remain recurrence evidence |
| `event_2200` | 2024-02-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2201` | 2024-02-06 | debit | 1201903.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_2202` | 2024-02-07 | debit | 904400 | already reflected in the current balance; may remain recurrence evidence |
| `event_2203` | 2024-02-12 | debit | 126350 | already reflected in the current balance; may remain recurrence evidence |
| `event_2204` | 2024-02-09 | debit | 573800 | already reflected in the current balance; may remain recurrence evidence |
| `event_2205` | 2024-02-12 | debit | 1170271.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_2206` | 2024-02-14 | debit | 426338.4 | already reflected in the current balance; may remain recurrence evidence |
| `event_2207` | 2024-03-02 | debit | 6954000 | already reflected in the current balance; may remain recurrence evidence |
| `event_2208` | 2023-09-11 | debit | 1348940.42 | already reflected in the current balance; may remain recurrence evidence |
| `event_2209` | 2023-09-21 | debit | 1510693.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_2210` | 2023-10-01 | debit | 1490390.69 | already reflected in the current balance; may remain recurrence evidence |
| `event_2211` | 2023-10-11 | debit | 1211444.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_2212` | 2023-10-21 | debit | 1048982.51 | already reflected in the current balance; may remain recurrence evidence |
| `event_2213` | 2023-10-31 | debit | 1066197.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_2214` | 2023-11-10 | debit | 893559.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_2215` | 2023-11-20 | debit | 1252001.65 | already reflected in the current balance; may remain recurrence evidence |
| `event_2216` | 2023-11-30 | debit | 1101344.82 | already reflected in the current balance; may remain recurrence evidence |
| `event_2217` | 2023-12-10 | debit | 876032.86 | already reflected in the current balance; may remain recurrence evidence |
| `event_2218` | 2023-12-20 | debit | 917586.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_2219` | 2023-12-30 | debit | 1454933.56 | already reflected in the current balance; may remain recurrence evidence |
| `event_2220` | 2024-01-09 | debit | 983053.43 | already reflected in the current balance; may remain recurrence evidence |
| `event_2221` | 2024-01-19 | debit | 1388569.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_2222` | 2024-01-29 | debit | 1335295.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2223` | 2024-02-08 | debit | 1369082.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_2224` | 2024-02-18 | debit | 864688.59 | already reflected in the current balance; may remain recurrence evidence |
| `event_2225` | 2024-02-28 | debit | 1472349.1 | already reflected in the current balance; may remain recurrence evidence |
| `event_2226` | 2023-09-12 | debit | 725793.85 | already reflected in the current balance; may remain recurrence evidence |
| `event_2227` | 2023-09-17 | debit | 447746.71 | already reflected in the current balance; may remain recurrence evidence |
| `event_2228` | 2023-09-22 | debit | 579668.34 | already reflected in the current balance; may remain recurrence evidence |
| `event_2229` | 2023-09-27 | debit | 636547.25 | already reflected in the current balance; may remain recurrence evidence |
| `event_2230` | 2023-10-02 | debit | 724399.08 | already reflected in the current balance; may remain recurrence evidence |
| `event_2231` | 2023-10-07 | debit | 591314.74 | already reflected in the current balance; may remain recurrence evidence |
| `event_2232` | 2023-10-12 | debit | 458415.57 | already reflected in the current balance; may remain recurrence evidence |
| `event_2233` | 2023-10-17 | debit | 445484.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_2234` | 2023-10-22 | debit | 617815.52 | already reflected in the current balance; may remain recurrence evidence |
| `event_2235` | 2023-10-27 | debit | 567772.41 | already reflected in the current balance; may remain recurrence evidence |
| `event_2236` | 2023-11-01 | debit | 507090.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_2237` | 2023-11-06 | debit | 454432.04 | already reflected in the current balance; may remain recurrence evidence |
| `event_2238` | 2023-11-11 | debit | 617984.73 | already reflected in the current balance; may remain recurrence evidence |
| `event_2239` | 2023-11-16 | debit | 557483.97 | already reflected in the current balance; may remain recurrence evidence |
| `event_2240` | 2023-11-21 | debit | 627417.61 | already reflected in the current balance; may remain recurrence evidence |
| `event_2241` | 2023-11-26 | debit | 547424.01 | already reflected in the current balance; may remain recurrence evidence |
| `event_2242` | 2023-12-01 | debit | 522613.77 | already reflected in the current balance; may remain recurrence evidence |
| `event_2243` | 2023-12-06 | debit | 695049.46 | already reflected in the current balance; may remain recurrence evidence |
| `event_2244` | 2023-12-11 | debit | 721981.78 | already reflected in the current balance; may remain recurrence evidence |
| `event_2245` | 2023-12-16 | debit | 732740.37 | already reflected in the current balance; may remain recurrence evidence |
| `event_2246` | 2023-12-21 | debit | 593848.06 | already reflected in the current balance; may remain recurrence evidence |
| `event_2247` | 2023-12-26 | debit | 639058 | already reflected in the current balance; may remain recurrence evidence |
| `event_2248` | 2023-12-31 | debit | 721837.88 | already reflected in the current balance; may remain recurrence evidence |
| `event_2249` | 2024-01-05 | debit | 637250.91 | already reflected in the current balance; may remain recurrence evidence |
| `event_2250` | 2024-01-10 | debit | 562442.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_2251` | 2024-01-15 | debit | 542331.16 | already reflected in the current balance; may remain recurrence evidence |
| `event_2252` | 2024-01-20 | debit | 463292.75 | already reflected in the current balance; may remain recurrence evidence |
| `event_2253` | 2024-01-25 | debit | 745983.26 | already reflected in the current balance; may remain recurrence evidence |
| `event_2254` | 2024-01-30 | debit | 549524.6 | already reflected in the current balance; may remain recurrence evidence |
| `event_2255` | 2024-02-04 | debit | 664768.21 | already reflected in the current balance; may remain recurrence evidence |
| `event_2256` | 2024-02-09 | debit | 448075.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_2257` | 2024-02-14 | debit | 560613.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2258` | 2024-02-19 | debit | 458596.67 | already reflected in the current balance; may remain recurrence evidence |
| `event_2259` | 2024-02-24 | debit | 663001.49 | already reflected in the current balance; may remain recurrence evidence |
| `event_2260` | 2024-02-29 | debit | 729004.44 | already reflected in the current balance; may remain recurrence evidence |
| `event_2261` | 2024-03-05 | debit | 571596.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_2262` | 2023-09-13 | debit | 979886.38 | already reflected in the current balance; may remain recurrence evidence |
| `event_2263` | 2023-09-20 | debit | 1028620.35 | already reflected in the current balance; may remain recurrence evidence |
| `event_2264` | 2023-09-27 | debit | 1117067.23 | already reflected in the current balance; may remain recurrence evidence |
| `event_2265` | 2023-10-04 | debit | 756322.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2266` | 2023-10-11 | debit | 1249486.33 | already reflected in the current balance; may remain recurrence evidence |
| `event_2267` | 2023-10-18 | debit | 1232054.29 | already reflected in the current balance; may remain recurrence evidence |
| `event_2268` | 2023-10-25 | debit | 1115260.36 | already reflected in the current balance; may remain recurrence evidence |
| `event_2269` | 2023-11-01 | debit | 1261355.55 | already reflected in the current balance; may remain recurrence evidence |
| `event_2270` | 2023-11-08 | debit | 921922.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_2271` | 2023-11-15 | debit | 1142868.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2272` | 2023-11-22 | debit | 897310.27 | already reflected in the current balance; may remain recurrence evidence |
| `event_2273` | 2023-11-29 | debit | 740801.32 | already reflected in the current balance; may remain recurrence evidence |
| `event_2274` | 2023-12-06 | debit | 1022655.76 | already reflected in the current balance; may remain recurrence evidence |
| `event_2275` | 2023-12-13 | debit | 1128974.93 | already reflected in the current balance; may remain recurrence evidence |
| `event_2276` | 2023-12-20 | debit | 956749.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_2277` | 2023-12-27 | debit | 1095978.2 | already reflected in the current balance; may remain recurrence evidence |
| `event_2278` | 2024-01-03 | debit | 868921.02 | already reflected in the current balance; may remain recurrence evidence |
| `event_2279` | 2024-01-10 | debit | 925855.11 | already reflected in the current balance; may remain recurrence evidence |
| `event_2280` | 2024-01-17 | debit | 1204804.45 | already reflected in the current balance; may remain recurrence evidence |
| `event_2281` | 2024-01-24 | debit | 1057617.64 | already reflected in the current balance; may remain recurrence evidence |
| `event_2282` | 2024-01-31 | debit | 1251981.8 | already reflected in the current balance; may remain recurrence evidence |
| `event_2283` | 2024-02-07 | debit | 949118.03 | already reflected in the current balance; may remain recurrence evidence |
| `event_2284` | 2024-02-14 | debit | 1051249.87 | already reflected in the current balance; may remain recurrence evidence |
| `event_2285` | 2024-02-21 | debit | 777034.83 | already reflected in the current balance; may remain recurrence evidence |
| `event_2286` | 2024-02-28 | debit | 1133036.68 | already reflected in the current balance; may remain recurrence evidence |
| `event_2287` | 2024-03-04 | debit | - | failed event |

### Safe no-change plan candidates

| Method | Start | Complete | Total | Payments | Option | Selector rank | Result |
| --- | --- | --- | ---: | ---: | --- | --- | --- |
| - | - | - | - | - | - | - | No eligible safe candidate |
