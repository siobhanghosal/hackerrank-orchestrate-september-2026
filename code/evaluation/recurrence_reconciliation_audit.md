# Recurrence reconciliation audit

> Status: rejected candidate. The hybrid calendar-month and explicit-event reconciliation implementation was evaluated and reverted because exact status, method, and earliest-date matches regressed. This file preserves the candidate's measured cadence/suppression analysis.

This audit is derived from deterministic forecast inputs. It does not use solved output fields.

## request_01 — user_01

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Apartment rent transfer | rent | debit | monthly (30d estimate) | 2024-04-02 | `event_19`, `event_26`, `event_32` |
| Household utility payment | utilities | debit | monthly (31d estimate) | 2024-03-06 | `event_14`, `event_20`, `event_27` |
| Professional training fee | education | debit | monthly (31d estimate) | 2024-03-08 | `event_15`, `event_21`, `event_28` |
| Education loan instalment | debt_repayment | debit | monthly (31d estimate) | 2024-03-11 | `event_16`, `event_22`, `event_29` |
| Music service subscription | music_subscription | debit | monthly (31d estimate) | 2024-03-11 | `event_17`, `event_23`, `event_30` |
| Delivery service plan | delivery_membership | debit | monthly (31d estimate) | 2024-03-13 | `event_18`, `event_24`, `event_31` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-04-02 | Inferred recurring Apartment rent transfer | -5148 |
| 2024-05-02 | Inferred recurring Apartment rent transfer | -5148 |
| 2024-03-06 | Inferred recurring Household utility payment | -1651.81 |
| 2024-04-06 | Inferred recurring Household utility payment | -1651.81 |
| 2024-05-06 | Inferred recurring Household utility payment | -1651.81 |
| 2024-03-08 | Inferred recurring Professional training fee | -1821.6 |
| 2024-04-08 | Inferred recurring Professional training fee | -1821.6 |
| 2024-05-08 | Inferred recurring Professional training fee | -1821.6 |
| 2024-03-11 | Inferred recurring Education loan instalment | -3487 |
| 2024-04-11 | Inferred recurring Education loan instalment | -3487 |
| 2024-05-11 | Inferred recurring Education loan instalment | -3487 |
| 2024-03-11 | Inferred recurring Music service subscription | -235.4 |
| 2024-04-11 | Inferred recurring Music service subscription | -235.4 |
| 2024-05-11 | Inferred recurring Music service subscription | -235.4 |
| 2024-03-13 | Inferred recurring Delivery service plan | -306.9 |
| 2024-04-13 | Inferred recurring Delivery service plan | -306.9 |
| 2024-05-13 | Inferred recurring Delivery service plan | -306.9 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-03-05 | `event_102` | explicit | transport | -567.6 |
| 2024-03-06 | `recurring:utilities` | recurring | utilities | -1651.81 |
| 2024-03-08 | `recurring:education` | recurring | education | -1821.6 |
| 2024-03-11 | `recurring:debt_repayment` | recurring | debt_repayment | -3487 |
| 2024-03-11 | `recurring:music_subscription` | recurring | music_subscription | -235.4 |
| 2024-03-13 | `recurring:delivery_membership` | recurring | delivery_membership | -306.9 |
| 2024-03-15 | `event_103` | explicit | salary | 23320 |
| 2024-04-02 | `recurring:rent` | recurring | rent | -5148 |
| 2024-04-06 | `recurring:utilities` | recurring | utilities | -1651.81 |
| 2024-04-08 | `recurring:education` | recurring | education | -1821.6 |
| 2024-04-11 | `recurring:debt_repayment` | recurring | debt_repayment | -3487 |
| 2024-04-11 | `recurring:music_subscription` | recurring | music_subscription | -235.4 |
| 2024-04-13 | `recurring:delivery_membership` | recurring | delivery_membership | -306.9 |
| 2024-05-02 | `recurring:rent` | recurring | rent | -5148 |
| 2024-05-06 | `recurring:utilities` | recurring | utilities | -1651.81 |
| 2024-05-08 | `recurring:education` | recurring | education | -1821.6 |
| 2024-05-11 | `recurring:debt_repayment` | recurring | debt_repayment | -3487 |
| 2024-05-11 | `recurring:music_subscription` | recurring | music_subscription | -235.4 |
| 2024-05-13 | `recurring:delivery_membership` | recurring | delivery_membership | -306.9 |

## request_02 — user_02

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2025-08-15 | `event_120`, `event_128`, `event_136` |
| Home repair reserve | housing | debit | monthly (30d estimate) | 2025-09-04 | `event_129`, `event_137`, `event_144` |
| Municipal utilities | utilities | debit | monthly (30d estimate) | 2025-08-07 | `event_122`, `event_130`, `event_138` |
| Household insurance | insurance | debit | monthly (30d estimate) | 2025-08-08 | `event_123`, `event_131`, `event_139` |
| Course tuition | education | debit | monthly (30d estimate) | 2025-08-09 | `event_124`, `event_132`, `event_140` |
| Clinic payment | healthcare | debit | monthly (30d estimate) | 2025-08-11 | `event_125`, `event_133`, `event_141` |
| Cinema and events | entertainment | debit | monthly (30d estimate) | 2025-08-15 | `event_126`, `event_134`, `event_142` |
| Shared storage plan | cloud_storage | debit | monthly (30d estimate) | 2025-08-13 | `event_127`, `event_135`, `event_143` |
| Local market purchase | groceries | debit | days (35d estimate) | 2025-08-14 | `event_153`, `event_156`, `event_160` |
| Ride-hailing trip | transport | debit | days (14d estimate) | 2025-08-12 | `event_166`, `event_167`, `event_168` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-08-15 | Inferred recurring Payroll credit | 42750000 |
| 2025-09-15 | Inferred recurring Payroll credit | 42750000 |
| 2025-10-15 | Inferred recurring Payroll credit | 42750000 |
| 2025-09-04 | Inferred recurring Home repair reserve | -3534000 |
| 2025-10-04 | Inferred recurring Home repair reserve | -3534000 |
| 2025-08-07 | Inferred recurring Municipal utilities | -2141849.94 |
| 2025-09-07 | Inferred recurring Municipal utilities | -2141849.94 |
| 2025-10-07 | Inferred recurring Municipal utilities | -2141849.94 |
| 2025-08-08 | Inferred recurring Household insurance | -1132400 |
| 2025-09-08 | Inferred recurring Household insurance | -1132400 |
| 2025-10-08 | Inferred recurring Household insurance | -1132400 |
| 2025-08-09 | Inferred recurring Course tuition | -3040000 |
| 2025-09-09 | Inferred recurring Course tuition | -3040000 |
| 2025-10-09 | Inferred recurring Course tuition | -3040000 |
| 2025-08-11 | Inferred recurring Clinic payment | -1641668.72 |
| 2025-09-11 | Inferred recurring Clinic payment | -1641668.72 |
| 2025-10-11 | Inferred recurring Clinic payment | -1641668.72 |
| 2025-08-15 | Inferred recurring Cinema and events | -1352563.79 |
| 2025-09-15 | Inferred recurring Cinema and events | -1352563.79 |
| 2025-10-15 | Inferred recurring Cinema and events | -1352563.79 |
| 2025-08-13 | Inferred recurring Shared storage plan | -369550 |
| 2025-09-13 | Inferred recurring Shared storage plan | -369550 |
| 2025-10-13 | Inferred recurring Shared storage plan | -369550 |
| 2025-08-14 | Inferred recurring Local market purchase | -2218141.61 |
| 2025-09-18 | Inferred recurring Local market purchase | -2218141.61 |
| 2025-10-23 | Inferred recurring Local market purchase | -2218141.61 |
| 2025-08-12 | Inferred recurring Ride-hailing trip | -1440242.94 |
| 2025-08-26 | Inferred recurring Ride-hailing trip | -1440242.94 |
| 2025-09-09 | Inferred recurring Ride-hailing trip | -1440242.94 |
| 2025-09-23 | Inferred recurring Ride-hailing trip | -1440242.94 |
| 2025-10-07 | Inferred recurring Ride-hailing trip | -1440242.94 |
| 2025-10-21 | Inferred recurring Ride-hailing trip | -1440242.94 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-08-07 | `recurring:utilities` | recurring | utilities | -2141849.94 |
| 2025-08-08 | `event_185` | explicit | shopping | -1651100 |
| 2025-08-08 | `recurring:insurance` | recurring | insurance | -1132400 |
| 2025-08-09 | `recurring:education` | recurring | education | -3040000 |
| 2025-08-11 | `recurring:healthcare` | recurring | healthcare | -1641668.72 |
| 2025-08-12 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-08-13 | `recurring:cloud_storage` | recurring | cloud_storage | -369550 |
| 2025-08-14 | `recurring:groceries` | recurring | groceries | -2218141.61 |
| 2025-08-15 | `recurring:entertainment` | recurring | entertainment | -1352563.79 |
| 2025-08-15 | `recurring:salary` | recurring | salary | 42750000 |
| 2025-08-26 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-09-04 | `recurring:housing` | recurring | housing | -3534000 |
| 2025-09-07 | `recurring:utilities` | recurring | utilities | -2141849.94 |
| 2025-09-08 | `recurring:insurance` | recurring | insurance | -1132400 |
| 2025-09-09 | `recurring:education` | recurring | education | -3040000 |
| 2025-09-09 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-09-11 | `recurring:healthcare` | recurring | healthcare | -1641668.72 |
| 2025-09-13 | `recurring:cloud_storage` | recurring | cloud_storage | -369550 |
| 2025-09-15 | `recurring:entertainment` | recurring | entertainment | -1352563.79 |
| 2025-09-15 | `recurring:salary` | recurring | salary | 42750000 |
| 2025-09-18 | `recurring:groceries` | recurring | groceries | -2218141.61 |
| 2025-09-23 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-10-04 | `recurring:housing` | recurring | housing | -3534000 |
| 2025-10-07 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-10-07 | `recurring:utilities` | recurring | utilities | -2141849.94 |
| 2025-10-08 | `recurring:insurance` | recurring | insurance | -1132400 |
| 2025-10-09 | `recurring:education` | recurring | education | -3040000 |
| 2025-10-11 | `recurring:healthcare` | recurring | healthcare | -1641668.72 |
| 2025-10-13 | `recurring:cloud_storage` | recurring | cloud_storage | -369550 |
| 2025-10-15 | `recurring:entertainment` | recurring | entertainment | -1352563.79 |
| 2025-10-15 | `recurring:salary` | recurring | salary | 42750000 |
| 2025-10-21 | `recurring:transport` | recurring | transport | -1440242.94 |
| 2025-10-23 | `recurring:groceries` | recurring | groceries | -2218141.61 |

## request_03 — user_03

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2019-09-15 | `event_198`, `event_204`, `event_210` |
| Landlord standing order | rent | debit | monthly (30d estimate) | 2019-09-04 | `event_199`, `event_205`, `event_212` |
| Water and power payment | utilities | debit | monthly (30d estimate) | 2019-09-08 | `event_200`, `event_206`, `event_213` |
| Shared storage plan | cloud_storage | debit | monthly (30d estimate) | 2019-09-14 | `event_201`, `event_207`, `event_214` |
| Video streaming plan | streaming | debit | monthly (30d estimate) | 2019-09-11 | `event_202`, `event_208`, `event_215` |
| Clothing and household items | shopping | debit | monthly (30d estimate) | 2019-09-14 | `event_203`, `event_209`, `event_216` |
| Bulk pantry shop | groceries | debit | days (10d estimate) | 2019-09-08 | `event_217`, `event_218`, `event_219` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2019-09-15 | Inferred recurring Payroll credit | 4365000 |
| 2019-10-15 | Inferred recurring Payroll credit | 4365000 |
| 2019-11-15 | Inferred recurring Payroll credit | 4365000 |
| 2019-09-04 | Inferred recurring Landlord standing order | -1140000 |
| 2019-10-04 | Inferred recurring Landlord standing order | -1140000 |
| 2019-11-04 | Inferred recurring Landlord standing order | -1140000 |
| 2019-09-08 | Inferred recurring Water and power payment | -303042.45 |
| 2019-10-08 | Inferred recurring Water and power payment | -303042.45 |
| 2019-11-08 | Inferred recurring Water and power payment | -303042.45 |
| 2019-09-14 | Inferred recurring Shared storage plan | -20900 |
| 2019-10-14 | Inferred recurring Shared storage plan | -20900 |
| 2019-11-14 | Inferred recurring Shared storage plan | -20900 |
| 2019-09-11 | Inferred recurring Video streaming plan | -117800 |
| 2019-10-11 | Inferred recurring Video streaming plan | -117800 |
| 2019-11-11 | Inferred recurring Video streaming plan | -117800 |
| 2019-09-14 | Inferred recurring Clothing and household items | -180395.29 |
| 2019-10-14 | Inferred recurring Clothing and household items | -180395.29 |
| 2019-11-14 | Inferred recurring Clothing and household items | -180395.29 |
| 2019-09-08 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-09-18 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-09-28 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-10-08 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-10-18 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-10-28 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-11-07 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-11-17 | Inferred recurring Bulk pantry shop | -234390.87 |
| 2019-11-27 | Inferred recurring Bulk pantry shop | -234390.87 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2019-09-04 | `recurring:rent` | recurring | rent | -1140000 |
| 2019-09-07 | `event_254` | explicit | healthcare | -95000 |
| 2019-09-08 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-09-08 | `recurring:utilities` | recurring | utilities | -303042.45 |
| 2019-09-11 | `recurring:streaming` | recurring | streaming | -117800 |
| 2019-09-14 | `recurring:cloud_storage` | recurring | cloud_storage | -20900 |
| 2019-09-14 | `recurring:shopping` | recurring | shopping | -180395.29 |
| 2019-09-15 | `recurring:salary` | recurring | salary | 4365000 |
| 2019-09-18 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-09-28 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-10-04 | `recurring:rent` | recurring | rent | -1140000 |
| 2019-10-08 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-10-08 | `recurring:utilities` | recurring | utilities | -303042.45 |
| 2019-10-11 | `recurring:streaming` | recurring | streaming | -117800 |
| 2019-10-14 | `recurring:cloud_storage` | recurring | cloud_storage | -20900 |
| 2019-10-14 | `recurring:shopping` | recurring | shopping | -180395.29 |
| 2019-10-15 | `recurring:salary` | recurring | salary | 4365000 |
| 2019-10-18 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-10-28 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-11-04 | `recurring:rent` | recurring | rent | -1140000 |
| 2019-11-07 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-11-08 | `recurring:utilities` | recurring | utilities | -303042.45 |
| 2019-11-11 | `recurring:streaming` | recurring | streaming | -117800 |
| 2019-11-14 | `recurring:cloud_storage` | recurring | cloud_storage | -20900 |
| 2019-11-14 | `recurring:shopping` | recurring | shopping | -180395.29 |
| 2019-11-15 | `recurring:salary` | recurring | salary | 4365000 |
| 2019-11-17 | `recurring:groceries` | recurring | groceries | -234390.87 |
| 2019-11-27 | `recurring:groceries` | recurring | groceries | -234390.87 |

## request_04 — user_04

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2024-06-15 | `event_269`, `event_277`, `event_284` |
| Residential rent payment | rent | debit | monthly (30d estimate) | 2024-07-01 | `event_278`, `event_285`, `event_291` |
| Municipal utilities | utilities | debit | monthly (30d estimate) | 2024-06-05 | `event_272`, `event_279`, `event_286` |
| Music service subscription | music_subscription | debit | monthly (30d estimate) | 2024-06-10 | `event_273`, `event_280`, `event_287` |
| Food delivery membership | delivery_membership | debit | monthly (30d estimate) | 2024-06-12 | `event_274`, `event_281`, `event_288` |
| Gym membership | gym | debit | monthly (30d estimate) | 2024-06-09 | `event_275`, `event_282`, `event_289` |
| Local event tickets | entertainment | debit | monthly (30d estimate) | 2024-06-13 | `event_276`, `event_283`, `event_290` |
| Family dinner | dining | debit | days (35d estimate) | 2024-07-08 | `event_349`, `event_351`, `event_354` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-06-15 | Inferred recurring Payroll credit | 38190000 |
| 2024-07-15 | Inferred recurring Payroll credit | 38190000 |
| 2024-08-15 | Inferred recurring Payroll credit | 38190000 |
| 2024-07-01 | Inferred recurring Residential rent payment | -12293000 |
| 2024-08-01 | Inferred recurring Residential rent payment | -12293000 |
| 2024-09-01 | Inferred recurring Residential rent payment | -12293000 |
| 2024-06-05 | Inferred recurring Municipal utilities | -2033868.83 |
| 2024-07-05 | Inferred recurring Municipal utilities | -2033868.83 |
| 2024-08-05 | Inferred recurring Municipal utilities | -2033868.83 |
| 2024-06-10 | Inferred recurring Music service subscription | -332500 |
| 2024-07-10 | Inferred recurring Music service subscription | -332500 |
| 2024-08-10 | Inferred recurring Music service subscription | -332500 |
| 2024-06-12 | Inferred recurring Food delivery membership | -377150 |
| 2024-07-12 | Inferred recurring Food delivery membership | -377150 |
| 2024-08-12 | Inferred recurring Food delivery membership | -377150 |
| 2024-06-09 | Inferred recurring Gym membership | -1027900 |
| 2024-07-09 | Inferred recurring Gym membership | -1027900 |
| 2024-08-09 | Inferred recurring Gym membership | -1027900 |
| 2024-06-13 | Inferred recurring Local event tickets | -1542620 |
| 2024-07-13 | Inferred recurring Local event tickets | -1542620 |
| 2024-08-13 | Inferred recurring Local event tickets | -1542620 |
| 2024-07-08 | Inferred recurring Family dinner | -2102251.18 |
| 2024-08-12 | Inferred recurring Family dinner | -2102251.18 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-06-05 | `recurring:utilities` | recurring | utilities | -2033868.83 |
| 2024-06-09 | `recurring:gym` | recurring | gym | -1027900 |
| 2024-06-10 | `recurring:music_subscription` | recurring | music_subscription | -332500 |
| 2024-06-11 | `event_357` | explicit | education | -1704300 |
| 2024-06-12 | `recurring:delivery_membership` | recurring | delivery_membership | -377150 |
| 2024-06-13 | `recurring:entertainment` | recurring | entertainment | -1542620 |
| 2024-06-15 | `recurring:salary` | recurring | salary | 38190000 |
| 2024-07-01 | `recurring:rent` | recurring | rent | -12293000 |
| 2024-07-05 | `recurring:utilities` | recurring | utilities | -2033868.83 |
| 2024-07-08 | `recurring:dining` | recurring | dining | -2102251.18 |
| 2024-07-09 | `recurring:gym` | recurring | gym | -1027900 |
| 2024-07-10 | `recurring:music_subscription` | recurring | music_subscription | -332500 |
| 2024-07-12 | `recurring:delivery_membership` | recurring | delivery_membership | -377150 |
| 2024-07-13 | `recurring:entertainment` | recurring | entertainment | -1542620 |
| 2024-07-15 | `recurring:salary` | recurring | salary | 38190000 |
| 2024-08-01 | `recurring:rent` | recurring | rent | -12293000 |
| 2024-08-05 | `recurring:utilities` | recurring | utilities | -2033868.83 |
| 2024-08-09 | `recurring:gym` | recurring | gym | -1027900 |
| 2024-08-10 | `recurring:music_subscription` | recurring | music_subscription | -332500 |
| 2024-08-12 | `recurring:delivery_membership` | recurring | delivery_membership | -377150 |
| 2024-08-12 | `recurring:dining` | recurring | dining | -2102251.18 |
| 2024-08-13 | `recurring:entertainment` | recurring | entertainment | -1542620 |
| 2024-08-15 | `recurring:salary` | recurring | salary | 38190000 |
| 2024-09-01 | `recurring:rent` | recurring | rent | -12293000 |

## request_05 — user_05

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (31d estimate) | 2025-11-15 | `event_366`, `event_374`, `event_382` |
| Apartment rent transfer | rent | debit | monthly (31d estimate) | 2025-12-02 | `event_383`, `event_391`, `event_398` |
| Municipal utilities | utilities | debit | monthly (30d estimate) | 2025-12-06 | `event_376`, `event_384`, `event_392` |
| Vehicle loan payment | debt_repayment | debit | monthly (30d estimate) | 2025-11-11 | `event_377`, `event_385`, `event_393` |
| Therapy appointment | healthcare | debit | monthly (30d estimate) | 2025-11-10 | `event_378`, `event_386`, `event_394` |
| Dependent care payment | family_support | debit | monthly (30d estimate) | 2025-11-13 | `event_379`, `event_387`, `event_395` |
| Cloud storage plan | cloud_storage | debit | monthly (30d estimate) | 2025-11-12 | `event_380`, `event_388`, `event_396` |
| Personal shopping | shopping | debit | monthly (30d estimate) | 2025-11-12 | `event_381`, `event_389`, `event_397` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-11-15 | Inferred recurring Payroll credit | 14740 |
| 2025-12-15 | Inferred recurring Payroll credit | 14740 |
| 2026-01-15 | Inferred recurring Payroll credit | 14740 |
| 2025-12-02 | Inferred recurring Apartment rent transfer | -4972 |
| 2026-01-02 | Inferred recurring Apartment rent transfer | -4972 |
| 2026-02-02 | Inferred recurring Apartment rent transfer | -4972 |
| 2025-12-06 | Inferred recurring Municipal utilities | -750.89 |
| 2026-01-06 | Inferred recurring Municipal utilities | -750.89 |
| 2025-11-11 | Inferred recurring Vehicle loan payment | -968 |
| 2025-12-11 | Inferred recurring Vehicle loan payment | -968 |
| 2026-01-11 | Inferred recurring Vehicle loan payment | -968 |
| 2025-11-10 | Inferred recurring Therapy appointment | -722.37 |
| 2025-12-10 | Inferred recurring Therapy appointment | -722.37 |
| 2026-01-10 | Inferred recurring Therapy appointment | -722.37 |
| 2025-11-13 | Inferred recurring Dependent care payment | -840.4 |
| 2025-12-13 | Inferred recurring Dependent care payment | -840.4 |
| 2026-01-13 | Inferred recurring Dependent care payment | -840.4 |
| 2025-11-12 | Inferred recurring Cloud storage plan | -113.3 |
| 2025-12-12 | Inferred recurring Cloud storage plan | -113.3 |
| 2026-01-12 | Inferred recurring Cloud storage plan | -113.3 |
| 2025-11-12 | Inferred recurring Personal shopping | -422.67 |
| 2025-12-12 | Inferred recurring Personal shopping | -422.67 |
| 2026-01-12 | Inferred recurring Personal shopping | -422.67 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-11-10 | `recurring:healthcare` | recurring | healthcare | -722.37 |
| 2025-11-11 | `recurring:debt_repayment` | recurring | debt_repayment | -968 |
| 2025-11-12 | `recurring:cloud_storage` | recurring | cloud_storage | -113.3 |
| 2025-11-12 | `recurring:shopping` | recurring | shopping | -422.67 |
| 2025-11-13 | `recurring:family_support` | recurring | family_support | -840.4 |
| 2025-11-15 | `recurring:salary` | recurring | salary | 14740 |
| 2025-12-02 | `recurring:rent` | recurring | rent | -4972 |
| 2025-12-06 | `recurring:utilities` | recurring | utilities | -750.89 |
| 2025-12-10 | `recurring:healthcare` | recurring | healthcare | -722.37 |
| 2025-12-11 | `recurring:debt_repayment` | recurring | debt_repayment | -968 |
| 2025-12-12 | `recurring:cloud_storage` | recurring | cloud_storage | -113.3 |
| 2025-12-12 | `recurring:shopping` | recurring | shopping | -422.67 |
| 2025-12-13 | `recurring:family_support` | recurring | family_support | -840.4 |
| 2025-12-15 | `recurring:salary` | recurring | salary | 14740 |
| 2026-01-02 | `recurring:rent` | recurring | rent | -4972 |
| 2026-01-06 | `recurring:utilities` | recurring | utilities | -750.89 |
| 2026-01-10 | `recurring:healthcare` | recurring | healthcare | -722.37 |
| 2026-01-11 | `recurring:debt_repayment` | recurring | debt_repayment | -968 |
| 2026-01-12 | `recurring:cloud_storage` | recurring | cloud_storage | -113.3 |
| 2026-01-12 | `recurring:shopping` | recurring | shopping | -422.67 |
| 2026-01-13 | `recurring:family_support` | recurring | family_support | -840.4 |
| 2026-01-15 | `recurring:salary` | recurring | salary | 14740 |
| 2026-02-02 | `recurring:rent` | recurring | rent | -4972 |

## request_06 — user_06

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2026-01-15 | `event_455`, `event_463`, `event_471` |
| Monthly rent | rent | debit | monthly (30d estimate) | 2026-02-03 | `event_456`, `event_464`, `event_472` |
| Water and power payment | utilities | debit | monthly (30d estimate) | 2026-01-07 | `event_457`, `event_465`, `event_473` |
| Vehicle insurance premium | insurance | debit | monthly (30d estimate) | 2026-01-08 | `event_458`, `event_466`, `event_474` |
| Shared storage plan | cloud_storage | debit | monthly (30d estimate) | 2026-01-13 | `event_459`, `event_467`, `event_475` |
| Family streaming plan | streaming | debit | monthly (30d estimate) | 2026-01-10 | `event_460`, `event_468`, `event_476` |
| Household shopping | shopping | debit | monthly (30d estimate) | 2026-01-13 | `event_461`, `event_469`, `event_477` |
| Monthly entertainment spend | entertainment | debit | monthly (30d estimate) | 2026-01-15 | `event_462`, `event_470`, `event_478` |
| Fresh food shop | groceries | debit | days (10d estimate) | 2026-01-07 | `event_487`, `event_488`, `event_489` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-01-15 | Inferred recurring Payroll credit | 1037.52 |
| 2026-02-15 | Inferred recurring Payroll credit | 1037.52 |
| 2026-03-15 | Inferred recurring Payroll credit | 1037.52 |
| 2026-02-03 | Inferred recurring Monthly rent | -254.1 |
| 2026-03-03 | Inferred recurring Monthly rent | -254.1 |
| 2026-04-03 | Inferred recurring Monthly rent | -254.1 |
| 2026-01-07 | Inferred recurring Water and power payment | -58.98 |
| 2026-02-07 | Inferred recurring Water and power payment | -58.98 |
| 2026-03-07 | Inferred recurring Water and power payment | -58.98 |
| 2026-01-08 | Inferred recurring Vehicle insurance premium | -26 |
| 2026-02-08 | Inferred recurring Vehicle insurance premium | -26 |
| 2026-03-08 | Inferred recurring Vehicle insurance premium | -26 |
| 2026-01-13 | Inferred recurring Shared storage plan | -5 |
| 2026-02-13 | Inferred recurring Shared storage plan | -5 |
| 2026-03-13 | Inferred recurring Shared storage plan | -5 |
| 2026-01-10 | Inferred recurring Family streaming plan | -19 |
| 2026-02-10 | Inferred recurring Family streaming plan | -19 |
| 2026-03-10 | Inferred recurring Family streaming plan | -19 |
| 2026-01-13 | Inferred recurring Household shopping | -39.88 |
| 2026-02-13 | Inferred recurring Household shopping | -39.88 |
| 2026-03-13 | Inferred recurring Household shopping | -39.88 |
| 2026-01-15 | Inferred recurring Monthly entertainment spend | -38.33 |
| 2026-02-15 | Inferred recurring Monthly entertainment spend | -38.33 |
| 2026-03-15 | Inferred recurring Monthly entertainment spend | -38.33 |
| 2026-01-07 | Inferred recurring Fresh food shop | -51.55 |
| 2026-01-17 | Inferred recurring Fresh food shop | -51.55 |
| 2026-01-27 | Inferred recurring Fresh food shop | -51.55 |
| 2026-02-06 | Inferred recurring Fresh food shop | -51.55 |
| 2026-02-16 | Inferred recurring Fresh food shop | -51.55 |
| 2026-02-26 | Inferred recurring Fresh food shop | -51.55 |
| 2026-03-08 | Inferred recurring Fresh food shop | -51.55 |
| 2026-03-18 | Inferred recurring Fresh food shop | -51.55 |
| 2026-03-28 | Inferred recurring Fresh food shop | -51.55 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-01-07 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-01-07 | `recurring:utilities` | recurring | utilities | -58.98 |
| 2026-01-08 | `recurring:insurance` | recurring | insurance | -26 |
| 2026-01-10 | `recurring:streaming` | recurring | streaming | -19 |
| 2026-01-13 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-01-13 | `recurring:shopping` | recurring | shopping | -39.88 |
| 2026-01-15 | `recurring:entertainment` | recurring | entertainment | -38.33 |
| 2026-01-15 | `recurring:salary` | recurring | salary | 1037.52 |
| 2026-01-17 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-01-27 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-02-03 | `recurring:rent` | recurring | rent | -254.1 |
| 2026-02-06 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-02-07 | `recurring:utilities` | recurring | utilities | -58.98 |
| 2026-02-08 | `recurring:insurance` | recurring | insurance | -26 |
| 2026-02-10 | `recurring:streaming` | recurring | streaming | -19 |
| 2026-02-13 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-02-13 | `recurring:shopping` | recurring | shopping | -39.88 |
| 2026-02-15 | `recurring:entertainment` | recurring | entertainment | -38.33 |
| 2026-02-15 | `recurring:salary` | recurring | salary | 1037.52 |
| 2026-02-16 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-02-26 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-03-03 | `recurring:rent` | recurring | rent | -254.1 |
| 2026-03-07 | `recurring:utilities` | recurring | utilities | -58.98 |
| 2026-03-08 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-03-08 | `recurring:insurance` | recurring | insurance | -26 |
| 2026-03-10 | `recurring:streaming` | recurring | streaming | -19 |
| 2026-03-13 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-03-13 | `recurring:shopping` | recurring | shopping | -39.88 |
| 2026-03-15 | `recurring:entertainment` | recurring | entertainment | -38.33 |
| 2026-03-15 | `recurring:salary` | recurring | salary | 1037.52 |
| 2026-03-18 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-03-28 | `recurring:groceries` | recurring | groceries | -51.55 |
| 2026-04-03 | `recurring:rent` | recurring | rent | -254.1 |

## request_07 — user_07

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Monthly rent | rent | debit | monthly (31d estimate) | 2024-10-04 | `event_574`, `event_579`, `event_583` |
| Electricity bill | utilities | debit | monthly (30d estimate) | 2024-09-08 | `event_570`, `event_575`, `event_580` |
| Personal loan payment | debt_repayment | debit | monthly (30d estimate) | 2024-09-13 | `event_571`, `event_576`, `event_581` |
| Music subscription | music_subscription | debit | monthly (30d estimate) | 2024-09-13 | `event_572`, `event_577`, `event_582` |
| Rail pass | transport | debit | days (21d estimate) | 2024-09-20 | `event_602`, `event_603`, `event_604` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-10-04 | Inferred recurring Monthly rent | -34200 |
| 2024-11-04 | Inferred recurring Monthly rent | -34200 |
| 2024-12-04 | Inferred recurring Monthly rent | -34200 |
| 2024-09-08 | Inferred recurring Electricity bill | -7387.41 |
| 2024-10-08 | Inferred recurring Electricity bill | -7387.41 |
| 2024-11-08 | Inferred recurring Electricity bill | -7387.41 |
| 2024-09-13 | Inferred recurring Personal loan payment | -15650 |
| 2024-10-13 | Inferred recurring Personal loan payment | -15650 |
| 2024-11-13 | Inferred recurring Personal loan payment | -15650 |
| 2024-09-13 | Inferred recurring Music subscription | -1005 |
| 2024-10-13 | Inferred recurring Music subscription | -1005 |
| 2024-11-13 | Inferred recurring Music subscription | -1005 |
| 2024-09-20 | Inferred recurring Rail pass | -3822.62 |
| 2024-10-11 | Inferred recurring Rail pass | -3822.62 |
| 2024-11-01 | Inferred recurring Rail pass | -3822.62 |
| 2024-11-22 | Inferred recurring Rail pass | -3822.62 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-09-08 | `recurring:utilities` | recurring | utilities | -7387.41 |
| 2024-09-13 | `recurring:debt_repayment` | recurring | debt_repayment | -15650 |
| 2024-09-13 | `recurring:music_subscription` | recurring | music_subscription | -1005 |
| 2024-09-20 | `recurring:transport` | recurring | transport | -3822.62 |
| 2024-10-04 | `recurring:rent` | recurring | rent | -34200 |
| 2024-10-08 | `recurring:utilities` | recurring | utilities | -7387.41 |
| 2024-10-11 | `recurring:transport` | recurring | transport | -3822.62 |
| 2024-10-13 | `recurring:debt_repayment` | recurring | debt_repayment | -15650 |
| 2024-10-13 | `recurring:music_subscription` | recurring | music_subscription | -1005 |
| 2024-11-01 | `recurring:transport` | recurring | transport | -3822.62 |
| 2024-11-04 | `recurring:rent` | recurring | rent | -34200 |
| 2024-11-08 | `recurring:utilities` | recurring | utilities | -7387.41 |
| 2024-11-13 | `recurring:debt_repayment` | recurring | debt_repayment | -15650 |
| 2024-11-13 | `recurring:music_subscription` | recurring | music_subscription | -1005 |
| 2024-11-22 | `recurring:transport` | recurring | transport | -3822.62 |
| 2024-12-04 | `recurring:rent` | recurring | rent | -34200 |

## request_08 — user_08

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2025-02-15 | `event_629`, `event_636`, `event_643` |
| Apartment rent transfer | rent | debit | monthly (31d estimate) | 2025-03-01 | `event_637`, `event_644`, `event_650` |
| Municipal utilities | utilities | debit | monthly (31d estimate) | 2025-03-05 | `event_638`, `event_645`, `event_651` |
| School fee payment | education | debit | monthly (30d estimate) | 2025-03-07 | `event_632`, `event_639`, `event_646` |
| Personal loan payment | debt_repayment | debit | monthly (30d estimate) | 2025-02-10 | `event_633`, `event_640`, `event_647` |
| Music subscription | music_subscription | debit | monthly (30d estimate) | 2025-02-10 | `event_634`, `event_641`, `event_648` |
| Grocery delivery membership | delivery_membership | debit | monthly (30d estimate) | 2025-02-12 | `event_635`, `event_642`, `event_649` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-02-15 | Inferred recurring Payroll credit | 1422.85 |
| 2025-03-15 | Inferred recurring Payroll credit | 1422.85 |
| 2025-04-15 | Inferred recurring Payroll credit | 1422.85 |
| 2025-03-01 | Inferred recurring Apartment rent transfer | -467.5 |
| 2025-04-01 | Inferred recurring Apartment rent transfer | -467.5 |
| 2025-05-01 | Inferred recurring Apartment rent transfer | -467.5 |
| 2025-03-05 | Inferred recurring Municipal utilities | -82.61 |
| 2025-04-05 | Inferred recurring Municipal utilities | -82.61 |
| 2025-05-05 | Inferred recurring Municipal utilities | -82.61 |
| 2025-03-07 | Inferred recurring School fee payment | -89 |
| 2025-04-07 | Inferred recurring School fee payment | -89 |
| 2025-05-07 | Inferred recurring School fee payment | -89 |
| 2025-02-10 | Inferred recurring Personal loan payment | -177 |
| 2025-03-10 | Inferred recurring Personal loan payment | -177 |
| 2025-04-10 | Inferred recurring Personal loan payment | -177 |
| 2025-02-10 | Inferred recurring Music subscription | -14 |
| 2025-03-10 | Inferred recurring Music subscription | -14 |
| 2025-04-10 | Inferred recurring Music subscription | -14 |
| 2025-02-12 | Inferred recurring Grocery delivery membership | -24 |
| 2025-03-12 | Inferred recurring Grocery delivery membership | -24 |
| 2025-04-12 | Inferred recurring Grocery delivery membership | -24 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-02-10 | `recurring:debt_repayment` | recurring | debt_repayment | -177 |
| 2025-02-10 | `recurring:music_subscription` | recurring | music_subscription | -14 |
| 2025-02-12 | `recurring:delivery_membership` | recurring | delivery_membership | -24 |
| 2025-02-15 | `recurring:salary` | recurring | salary | 1422.85 |
| 2025-03-01 | `recurring:rent` | recurring | rent | -467.5 |
| 2025-03-05 | `recurring:utilities` | recurring | utilities | -82.61 |
| 2025-03-07 | `recurring:education` | recurring | education | -89 |
| 2025-03-10 | `recurring:debt_repayment` | recurring | debt_repayment | -177 |
| 2025-03-10 | `recurring:music_subscription` | recurring | music_subscription | -14 |
| 2025-03-12 | `recurring:delivery_membership` | recurring | delivery_membership | -24 |
| 2025-03-15 | `recurring:salary` | recurring | salary | 1422.85 |
| 2025-04-01 | `recurring:rent` | recurring | rent | -467.5 |
| 2025-04-05 | `recurring:utilities` | recurring | utilities | -82.61 |
| 2025-04-07 | `recurring:education` | recurring | education | -89 |
| 2025-04-10 | `recurring:debt_repayment` | recurring | debt_repayment | -177 |
| 2025-04-10 | `recurring:music_subscription` | recurring | music_subscription | -14 |
| 2025-04-12 | `recurring:delivery_membership` | recurring | delivery_membership | -24 |
| 2025-04-15 | `recurring:salary` | recurring | salary | 1422.85 |
| 2025-05-01 | `recurring:rent` | recurring | rent | -467.5 |
| 2025-05-05 | `recurring:utilities` | recurring | utilities | -82.61 |
| 2025-05-07 | `recurring:education` | recurring | education | -89 |

## request_09 — user_09

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Monthly rent | rent | debit | monthly (30d estimate) | 2026-08-02 | `event_740`, `event_747`, `event_752` |
| Water and power payment | utilities | debit | monthly (30d estimate) | 2026-07-06 | `event_734`, `event_741`, `event_748` |
| Cloud storage plan | cloud_storage | debit | monthly (30d estimate) | 2026-07-12 | `event_735`, `event_742`, `event_749` |
| Video streaming plan | streaming | debit | monthly (30d estimate) | 2026-07-09 | `event_736`, `event_743`, `event_750` |
| Household shopping | shopping | debit | monthly (30d estimate) | 2026-07-12 | `event_737`, `event_744`, `event_751` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-08-02 | Inferred recurring Monthly rent | -211.2 |
| 2026-09-02 | Inferred recurring Monthly rent | -211.2 |
| 2026-10-02 | Inferred recurring Monthly rent | -211.2 |
| 2026-07-06 | Inferred recurring Water and power payment | -71.04 |
| 2026-08-06 | Inferred recurring Water and power payment | -71.04 |
| 2026-09-06 | Inferred recurring Water and power payment | -71.04 |
| 2026-07-12 | Inferred recurring Cloud storage plan | -5 |
| 2026-08-12 | Inferred recurring Cloud storage plan | -5 |
| 2026-09-12 | Inferred recurring Cloud storage plan | -5 |
| 2026-07-09 | Inferred recurring Video streaming plan | -20 |
| 2026-08-09 | Inferred recurring Video streaming plan | -20 |
| 2026-09-09 | Inferred recurring Video streaming plan | -20 |
| 2026-07-12 | Inferred recurring Household shopping | -28.32 |
| 2026-08-12 | Inferred recurring Household shopping | -28.32 |
| 2026-09-12 | Inferred recurring Household shopping | -28.32 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-07-06 | `recurring:utilities` | recurring | utilities | -71.04 |
| 2026-07-09 | `recurring:streaming` | recurring | streaming | -20 |
| 2026-07-12 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-07-12 | `recurring:shopping` | recurring | shopping | -28.32 |
| 2026-08-02 | `recurring:rent` | recurring | rent | -211.2 |
| 2026-08-06 | `recurring:utilities` | recurring | utilities | -71.04 |
| 2026-08-09 | `recurring:streaming` | recurring | streaming | -20 |
| 2026-08-12 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-08-12 | `recurring:shopping` | recurring | shopping | -28.32 |
| 2026-09-02 | `recurring:rent` | recurring | rent | -211.2 |
| 2026-09-06 | `recurring:utilities` | recurring | utilities | -71.04 |
| 2026-09-09 | `recurring:streaming` | recurring | streaming | -20 |
| 2026-09-12 | `recurring:cloud_storage` | recurring | cloud_storage | -5 |
| 2026-09-12 | `recurring:shopping` | recurring | shopping | -28.32 |
| 2026-10-02 | `recurring:rent` | recurring | rent | -211.2 |

## request_10 — user_10

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Monthly rent | rent | debit | monthly (30d estimate) | 2025-01-03 | `event_823`, `event_833`, `event_840` |
| Electricity and water bill | utilities | debit | monthly (31d estimate) | 2024-12-07 | `event_814`, `event_824`, `event_834` |
| Music subscription | music_subscription | debit | monthly (31d estimate) | 2024-12-12 | `event_815`, `event_825`, `event_835` |
| Delivery service plan | delivery_membership | debit | monthly (31d estimate) | 2024-12-14 | `event_816`, `event_826`, `event_836` |
| Community fitness plan | gym | debit | monthly (31d estimate) | 2024-12-11 | `event_817`, `event_827`, `event_837` |
| Cinema and events | entertainment | debit | monthly (31d estimate) | 2024-12-15 | `event_818`, `event_828`, `event_838` |
| Driver platform payout | salary | credit | days (16d estimate) | 2024-12-20 | `event_829`, `event_831`, `event_839` |
| Parking and tolls | transport | debit | days (32d estimate) | 2025-01-01 | `event_873`, `event_877`, `event_882` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-01-03 | Inferred recurring Monthly rent | -69100 |
| 2025-02-03 | Inferred recurring Monthly rent | -69100 |
| 2025-03-03 | Inferred recurring Monthly rent | -69100 |
| 2024-12-07 | Inferred recurring Electricity and water bill | -17771.13 |
| 2025-01-07 | Inferred recurring Electricity and water bill | -17771.13 |
| 2025-02-07 | Inferred recurring Electricity and water bill | -17771.13 |
| 2024-12-12 | Inferred recurring Music subscription | -2800 |
| 2025-01-12 | Inferred recurring Music subscription | -2800 |
| 2025-02-12 | Inferred recurring Music subscription | -2800 |
| 2024-12-14 | Inferred recurring Delivery service plan | -1895 |
| 2025-01-14 | Inferred recurring Delivery service plan | -1895 |
| 2025-02-14 | Inferred recurring Delivery service plan | -1895 |
| 2024-12-11 | Inferred recurring Community fitness plan | -4860 |
| 2025-01-11 | Inferred recurring Community fitness plan | -4860 |
| 2025-02-11 | Inferred recurring Community fitness plan | -4860 |
| 2024-12-15 | Inferred recurring Cinema and events | -4883.78 |
| 2025-01-15 | Inferred recurring Cinema and events | -4883.78 |
| 2025-02-15 | Inferred recurring Cinema and events | -4883.78 |
| 2024-12-20 | Inferred recurring Driver platform payout | 47802.51 |
| 2025-01-05 | Inferred recurring Driver platform payout | 47802.51 |
| 2025-01-21 | Inferred recurring Driver platform payout | 47802.51 |
| 2025-02-06 | Inferred recurring Driver platform payout | 47802.51 |
| 2025-02-22 | Inferred recurring Driver platform payout | 47802.51 |
| 2025-01-01 | Inferred recurring Parking and tolls | -7568.88 |
| 2025-02-02 | Inferred recurring Parking and tolls | -7568.88 |
| 2025-03-06 | Inferred recurring Parking and tolls | -7568.88 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-12-07 | `recurring:utilities` | recurring | utilities | -17771.13 |
| 2024-12-11 | `recurring:gym` | recurring | gym | -4860 |
| 2024-12-12 | `recurring:music_subscription` | recurring | music_subscription | -2800 |
| 2024-12-14 | `recurring:delivery_membership` | recurring | delivery_membership | -1895 |
| 2024-12-15 | `recurring:entertainment` | recurring | entertainment | -4883.78 |
| 2024-12-20 | `recurring:salary` | recurring | salary | 47802.51 |
| 2025-01-01 | `recurring:transport` | recurring | transport | -7568.88 |
| 2025-01-03 | `recurring:rent` | recurring | rent | -69100 |
| 2025-01-05 | `recurring:salary` | recurring | salary | 47802.51 |
| 2025-01-07 | `recurring:utilities` | recurring | utilities | -17771.13 |
| 2025-01-11 | `recurring:gym` | recurring | gym | -4860 |
| 2025-01-12 | `recurring:music_subscription` | recurring | music_subscription | -2800 |
| 2025-01-14 | `recurring:delivery_membership` | recurring | delivery_membership | -1895 |
| 2025-01-15 | `recurring:entertainment` | recurring | entertainment | -4883.78 |
| 2025-01-21 | `recurring:salary` | recurring | salary | 47802.51 |
| 2025-02-02 | `recurring:transport` | recurring | transport | -7568.88 |
| 2025-02-03 | `recurring:rent` | recurring | rent | -69100 |
| 2025-02-06 | `recurring:salary` | recurring | salary | 47802.51 |
| 2025-02-07 | `recurring:utilities` | recurring | utilities | -17771.13 |
| 2025-02-11 | `recurring:gym` | recurring | gym | -4860 |
| 2025-02-12 | `recurring:music_subscription` | recurring | music_subscription | -2800 |
| 2025-02-14 | `recurring:delivery_membership` | recurring | delivery_membership | -1895 |
| 2025-02-15 | `recurring:entertainment` | recurring | entertainment | -4883.78 |
| 2025-02-22 | `recurring:salary` | recurring | salary | 47802.51 |
| 2025-03-03 | `recurring:rent` | recurring | rent | -69100 |
| 2025-03-06 | `recurring:transport` | recurring | transport | -7568.88 |

## request_11 — user_11

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Base salary | salary | credit | monthly (31d estimate) | 2025-05-15 | `event_923`, `event_932`, `event_941` |
| Performance commission | salary | credit | monthly (31d estimate) | 2025-05-24 | `event_906`, `event_915`, `event_924` |
| Home association fee | housing | debit | monthly (31d estimate) | 2025-05-05 | `event_925`, `event_934`, `event_943` |
| Municipal utilities | utilities | debit | monthly (31d estimate) | 2025-05-08 | `event_926`, `event_935`, `event_944` |
| Vehicle insurance premium | insurance | debit | monthly (31d estimate) | 2025-05-09 | `event_927`, `event_936`, `event_945` |
| Child education fee | education | debit | monthly (31d estimate) | 2025-05-10 | `event_928`, `event_937`, `event_946` |
| Regular medicine purchase | healthcare | debit | monthly (31d estimate) | 2025-05-12 | `event_929`, `event_938`, `event_947` |
| Games and recreation | entertainment | debit | monthly (31d estimate) | 2025-05-16 | `event_930`, `event_939`, `event_948` |
| Cloud storage plan | cloud_storage | debit | monthly (31d estimate) | 2025-05-14 | `event_931`, `event_940`, `event_949` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-05-15 | Inferred recurring Base salary | 38760000 |
| 2025-06-15 | Inferred recurring Base salary | 38760000 |
| 2025-07-15 | Inferred recurring Base salary | 38760000 |
| 2025-05-24 | Inferred recurring Performance commission | 38760000 |
| 2025-06-24 | Inferred recurring Performance commission | 38760000 |
| 2025-07-24 | Inferred recurring Performance commission | 38760000 |
| 2025-05-05 | Inferred recurring Home association fee | -2954500 |
| 2025-06-05 | Inferred recurring Home association fee | -2954500 |
| 2025-07-05 | Inferred recurring Home association fee | -2954500 |
| 2025-05-08 | Inferred recurring Municipal utilities | -2796165.18 |
| 2025-06-08 | Inferred recurring Municipal utilities | -2796165.18 |
| 2025-07-08 | Inferred recurring Municipal utilities | -2796165.18 |
| 2025-05-09 | Inferred recurring Vehicle insurance premium | -1881000 |
| 2025-06-09 | Inferred recurring Vehicle insurance premium | -1881000 |
| 2025-07-09 | Inferred recurring Vehicle insurance premium | -1881000 |
| 2025-05-10 | Inferred recurring Child education fee | -2544100 |
| 2025-06-10 | Inferred recurring Child education fee | -2544100 |
| 2025-07-10 | Inferred recurring Child education fee | -2544100 |
| 2025-05-12 | Inferred recurring Regular medicine purchase | -3165638.3 |
| 2025-06-12 | Inferred recurring Regular medicine purchase | -3165638.3 |
| 2025-07-12 | Inferred recurring Regular medicine purchase | -3165638.3 |
| 2025-05-16 | Inferred recurring Games and recreation | -1674887.61 |
| 2025-06-16 | Inferred recurring Games and recreation | -1674887.61 |
| 2025-07-16 | Inferred recurring Games and recreation | -1674887.61 |
| 2025-05-14 | Inferred recurring Cloud storage plan | -168150 |
| 2025-06-14 | Inferred recurring Cloud storage plan | -168150 |
| 2025-07-14 | Inferred recurring Cloud storage plan | -168150 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-05-05 | `recurring:housing` | recurring | housing | -2954500 |
| 2025-05-08 | `recurring:utilities` | recurring | utilities | -2796165.18 |
| 2025-05-09 | `recurring:insurance` | recurring | insurance | -1881000 |
| 2025-05-10 | `recurring:education` | recurring | education | -2544100 |
| 2025-05-12 | `recurring:healthcare` | recurring | healthcare | -3165638.3 |
| 2025-05-14 | `recurring:cloud_storage` | recurring | cloud_storage | -168150 |
| 2025-05-15 | `recurring:salary` | recurring | salary | 38760000 |
| 2025-05-16 | `recurring:entertainment` | recurring | entertainment | -1674887.61 |
| 2025-05-24 | `recurring:salary` | recurring | salary | 38760000 |
| 2025-06-05 | `recurring:housing` | recurring | housing | -2954500 |
| 2025-06-08 | `recurring:utilities` | recurring | utilities | -2796165.18 |
| 2025-06-09 | `recurring:insurance` | recurring | insurance | -1881000 |
| 2025-06-10 | `recurring:education` | recurring | education | -2544100 |
| 2025-06-12 | `recurring:healthcare` | recurring | healthcare | -3165638.3 |
| 2025-06-14 | `recurring:cloud_storage` | recurring | cloud_storage | -168150 |
| 2025-06-15 | `recurring:salary` | recurring | salary | 38760000 |
| 2025-06-16 | `recurring:entertainment` | recurring | entertainment | -1674887.61 |
| 2025-06-24 | `recurring:salary` | recurring | salary | 38760000 |
| 2025-07-05 | `recurring:housing` | recurring | housing | -2954500 |
| 2025-07-08 | `recurring:utilities` | recurring | utilities | -2796165.18 |
| 2025-07-09 | `recurring:insurance` | recurring | insurance | -1881000 |
| 2025-07-10 | `recurring:education` | recurring | education | -2544100 |
| 2025-07-12 | `recurring:healthcare` | recurring | healthcare | -3165638.3 |
| 2025-07-14 | `recurring:cloud_storage` | recurring | cloud_storage | -168150 |
| 2025-07-15 | `recurring:salary` | recurring | salary | 38760000 |
| 2025-07-16 | `recurring:entertainment` | recurring | entertainment | -1674887.61 |
| 2025-07-24 | `recurring:salary` | recurring | salary | 38760000 |

## request_12 — user_12

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Monthly rent | rent | debit | monthly (31d estimate) | 2026-05-01 | `event_1008`, `event_1013`, `event_1018` |
| Water and power payment | utilities | debit | monthly (30d estimate) | 2026-05-05 | `event_1004`, `event_1009`, `event_1014` |
| Shared storage plan | cloud_storage | debit | monthly (30d estimate) | 2026-04-11 | `event_1005`, `event_1010`, `event_1015` |
| Family streaming plan | streaming | debit | monthly (30d estimate) | 2026-04-08 | `event_1006`, `event_1011`, `event_1016` |
| Monthly shopping spend | shopping | debit | monthly (30d estimate) | 2026-04-11 | `event_1007`, `event_1012`, `event_1017` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-05-01 | Inferred recurring Monthly rent | -11792 |
| 2026-06-01 | Inferred recurring Monthly rent | -11792 |
| 2026-07-01 | Inferred recurring Monthly rent | -11792 |
| 2026-05-05 | Inferred recurring Water and power payment | -3755.96 |
| 2026-06-05 | Inferred recurring Water and power payment | -3755.96 |
| 2026-04-11 | Inferred recurring Shared storage plan | -447.7 |
| 2026-05-11 | Inferred recurring Shared storage plan | -447.7 |
| 2026-06-11 | Inferred recurring Shared storage plan | -447.7 |
| 2026-04-08 | Inferred recurring Family streaming plan | -1504.8 |
| 2026-05-08 | Inferred recurring Family streaming plan | -1504.8 |
| 2026-06-08 | Inferred recurring Family streaming plan | -1504.8 |
| 2026-04-11 | Inferred recurring Monthly shopping spend | -1401.99 |
| 2026-05-11 | Inferred recurring Monthly shopping spend | -1401.99 |
| 2026-06-11 | Inferred recurring Monthly shopping spend | -1401.99 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-04-08 | `recurring:streaming` | recurring | streaming | -1504.8 |
| 2026-04-11 | `recurring:cloud_storage` | recurring | cloud_storage | -447.7 |
| 2026-04-11 | `recurring:shopping` | recurring | shopping | -1401.99 |
| 2026-05-01 | `recurring:rent` | recurring | rent | -11792 |
| 2026-05-05 | `recurring:utilities` | recurring | utilities | -3755.96 |
| 2026-05-08 | `recurring:streaming` | recurring | streaming | -1504.8 |
| 2026-05-11 | `recurring:cloud_storage` | recurring | cloud_storage | -447.7 |
| 2026-05-11 | `recurring:shopping` | recurring | shopping | -1401.99 |
| 2026-06-01 | `recurring:rent` | recurring | rent | -11792 |
| 2026-06-05 | `recurring:utilities` | recurring | utilities | -3755.96 |
| 2026-06-08 | `recurring:streaming` | recurring | streaming | -1504.8 |
| 2026-06-11 | `recurring:cloud_storage` | recurring | cloud_storage | -447.7 |
| 2026-06-11 | `recurring:shopping` | recurring | shopping | -1401.99 |
| 2026-07-01 | `recurring:rent` | recurring | rent | -11792 |

## request_13 — user_13

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Primary household salary | salary | credit | monthly (31d estimate) | 2024-03-15 | `event_1071`, `event_1079`, `event_1087` |
| Second household income | salary | credit | monthly (31d estimate) | 2024-03-20 | `event_1064`, `event_1072`, `event_1080` |
| Shared housing rent | rent | debit | monthly (30d estimate) | 2024-04-02 | `event_1081`, `event_1088`, `event_1094` |
| Water and power payment | utilities | debit | monthly (30d estimate) | 2024-04-06 | `event_1082`, `event_1089`, `event_1095` |
| Music subscription | music_subscription | debit | monthly (31d estimate) | 2024-03-11 | `event_1075`, `event_1083`, `event_1090` |
| Delivery service plan | delivery_membership | debit | monthly (31d estimate) | 2024-03-13 | `event_1076`, `event_1084`, `event_1091` |
| Community fitness plan | gym | debit | monthly (31d estimate) | 2024-03-10 | `event_1077`, `event_1085`, `event_1092` |
| Local event tickets | entertainment | debit | monthly (31d estimate) | 2024-03-14 | `event_1078`, `event_1086`, `event_1093` |
| Ride-hailing trip | transport | debit | days (35d estimate) | 2024-04-03 | `event_1136`, `event_1140`, `event_1146` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-03-15 | Inferred recurring Primary household salary | 1343.54 |
| 2024-04-15 | Inferred recurring Primary household salary | 1343.54 |
| 2024-05-15 | Inferred recurring Primary household salary | 1343.54 |
| 2024-03-20 | Inferred recurring Second household income | 771.17 |
| 2024-04-20 | Inferred recurring Second household income | 771.17 |
| 2024-05-20 | Inferred recurring Second household income | 771.17 |
| 2024-04-02 | Inferred recurring Shared housing rent | -622.6 |
| 2024-05-02 | Inferred recurring Shared housing rent | -622.6 |
| 2024-06-02 | Inferred recurring Shared housing rent | -622.6 |
| 2024-04-06 | Inferred recurring Water and power payment | -143.7 |
| 2024-05-06 | Inferred recurring Water and power payment | -143.7 |
| 2024-03-11 | Inferred recurring Music subscription | -29 |
| 2024-04-11 | Inferred recurring Music subscription | -29 |
| 2024-05-11 | Inferred recurring Music subscription | -29 |
| 2024-03-13 | Inferred recurring Delivery service plan | -21 |
| 2024-04-13 | Inferred recurring Delivery service plan | -21 |
| 2024-05-13 | Inferred recurring Delivery service plan | -21 |
| 2024-03-10 | Inferred recurring Community fitness plan | -61 |
| 2024-04-10 | Inferred recurring Community fitness plan | -61 |
| 2024-05-10 | Inferred recurring Community fitness plan | -61 |
| 2024-03-14 | Inferred recurring Local event tickets | -37.9 |
| 2024-04-14 | Inferred recurring Local event tickets | -37.9 |
| 2024-05-14 | Inferred recurring Local event tickets | -37.9 |
| 2024-04-03 | Inferred recurring Ride-hailing trip | -50.46 |
| 2024-05-08 | Inferred recurring Ride-hailing trip | -50.46 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| Primary household salary / 2024-03-15 | `event_1161` / 2024-03-15 | explicit event_1161 matches salary/credit within 3 days |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-03-10 | `recurring:gym` | recurring | gym | -61 |
| 2024-03-11 | `recurring:music_subscription` | recurring | music_subscription | -29 |
| 2024-03-13 | `recurring:delivery_membership` | recurring | delivery_membership | -21 |
| 2024-03-14 | `recurring:entertainment` | recurring | entertainment | -37.9 |
| 2024-03-15 | `event_1161` | explicit | salary | 1343.54 |
| 2024-03-20 | `recurring:salary` | recurring | salary | 771.17 |
| 2024-04-02 | `recurring:rent` | recurring | rent | -622.6 |
| 2024-04-03 | `recurring:transport` | recurring | transport | -50.46 |
| 2024-04-06 | `recurring:utilities` | recurring | utilities | -143.7 |
| 2024-04-10 | `recurring:gym` | recurring | gym | -61 |
| 2024-04-11 | `recurring:music_subscription` | recurring | music_subscription | -29 |
| 2024-04-13 | `recurring:delivery_membership` | recurring | delivery_membership | -21 |
| 2024-04-14 | `recurring:entertainment` | recurring | entertainment | -37.9 |
| 2024-04-15 | `recurring:salary` | recurring | salary | 1343.54 |
| 2024-04-20 | `recurring:salary` | recurring | salary | 771.17 |
| 2024-05-02 | `recurring:rent` | recurring | rent | -622.6 |
| 2024-05-06 | `recurring:utilities` | recurring | utilities | -143.7 |
| 2024-05-08 | `recurring:transport` | recurring | transport | -50.46 |
| 2024-05-10 | `recurring:gym` | recurring | gym | -61 |
| 2024-05-11 | `recurring:music_subscription` | recurring | music_subscription | -29 |
| 2024-05-13 | `recurring:delivery_membership` | recurring | delivery_membership | -21 |
| 2024-05-14 | `recurring:entertainment` | recurring | entertainment | -37.9 |
| 2024-05-15 | `recurring:salary` | recurring | salary | 1343.54 |
| 2024-05-20 | `recurring:salary` | recurring | salary | 771.17 |
| 2024-06-02 | `recurring:rent` | recurring | rent | -622.6 |

## request_14 — user_14

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Monthly rent | rent | debit | monthly (30d estimate) | 2025-09-03 | `event_1185`, `event_1193`, `event_1200` |
| Energy provider bill | utilities | debit | monthly (30d estimate) | 2025-08-07 | `event_1179`, `event_1186`, `event_1194` |
| Credit card repayment | debt_repayment | debit | monthly (30d estimate) | 2025-08-12 | `event_1180`, `event_1187`, `event_1195` |
| Family healthcare expense | healthcare | debit | monthly (30d estimate) | 2025-08-11 | `event_1181`, `event_1188`, `event_1196` |
| Family support payment | family_support | debit | monthly (30d estimate) | 2025-08-14 | `event_1182`, `event_1189`, `event_1197` |
| Cloud storage plan | cloud_storage | debit | monthly (30d estimate) | 2025-08-13 | `event_1183`, `event_1190`, `event_1198` |
| Online retail purchases | shopping | debit | monthly (30d estimate) | 2025-08-13 | `event_1184`, `event_1191`, `event_1199` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-09-03 | Inferred recurring Monthly rent | -688.6 |
| 2025-10-03 | Inferred recurring Monthly rent | -688.6 |
| 2025-08-07 | Inferred recurring Energy provider bill | -153.69 |
| 2025-09-07 | Inferred recurring Energy provider bill | -153.69 |
| 2025-10-07 | Inferred recurring Energy provider bill | -153.69 |
| 2025-08-12 | Inferred recurring Credit card repayment | -350 |
| 2025-09-12 | Inferred recurring Credit card repayment | -350 |
| 2025-10-12 | Inferred recurring Credit card repayment | -350 |
| 2025-08-11 | Inferred recurring Family healthcare expense | -95.17 |
| 2025-09-11 | Inferred recurring Family healthcare expense | -95.17 |
| 2025-10-11 | Inferred recurring Family healthcare expense | -95.17 |
| 2025-08-14 | Inferred recurring Family support payment | -226 |
| 2025-09-14 | Inferred recurring Family support payment | -226 |
| 2025-10-14 | Inferred recurring Family support payment | -226 |
| 2025-08-13 | Inferred recurring Cloud storage plan | -14 |
| 2025-09-13 | Inferred recurring Cloud storage plan | -14 |
| 2025-10-13 | Inferred recurring Cloud storage plan | -14 |
| 2025-08-13 | Inferred recurring Online retail purchases | -140.39 |
| 2025-09-13 | Inferred recurring Online retail purchases | -140.39 |
| 2025-10-13 | Inferred recurring Online retail purchases | -140.39 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-08-07 | `recurring:utilities` | recurring | utilities | -153.69 |
| 2025-08-11 | `recurring:healthcare` | recurring | healthcare | -95.17 |
| 2025-08-12 | `recurring:debt_repayment` | recurring | debt_repayment | -350 |
| 2025-08-13 | `recurring:cloud_storage` | recurring | cloud_storage | -14 |
| 2025-08-13 | `recurring:shopping` | recurring | shopping | -140.39 |
| 2025-08-14 | `recurring:family_support` | recurring | family_support | -226 |
| 2025-09-03 | `recurring:rent` | recurring | rent | -688.6 |
| 2025-09-07 | `recurring:utilities` | recurring | utilities | -153.69 |
| 2025-09-11 | `recurring:healthcare` | recurring | healthcare | -95.17 |
| 2025-09-12 | `recurring:debt_repayment` | recurring | debt_repayment | -350 |
| 2025-09-13 | `recurring:cloud_storage` | recurring | cloud_storage | -14 |
| 2025-09-13 | `recurring:shopping` | recurring | shopping | -140.39 |
| 2025-09-14 | `recurring:family_support` | recurring | family_support | -226 |
| 2025-10-03 | `recurring:rent` | recurring | rent | -688.6 |
| 2025-10-07 | `recurring:utilities` | recurring | utilities | -153.69 |
| 2025-10-11 | `recurring:healthcare` | recurring | healthcare | -95.17 |
| 2025-10-12 | `recurring:debt_repayment` | recurring | debt_repayment | -350 |
| 2025-10-13 | `recurring:cloud_storage` | recurring | cloud_storage | -14 |
| 2025-10-13 | `recurring:shopping` | recurring | shopping | -140.39 |
| 2025-10-14 | `recurring:family_support` | recurring | family_support | -226 |

## request_15 — user_15

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Landlord standing order | rent | debit | monthly (30d estimate) | 2026-02-04 | `event_1259`, `event_1266`, `event_1272` |
| Energy provider bill | utilities | debit | monthly (30d estimate) | 2026-01-08 | `event_1253`, `event_1260`, `event_1267` |
| School fee payment | education | debit | monthly (30d estimate) | 2026-01-10 | `event_1254`, `event_1261`, `event_1268` |
| Credit card repayment | debt_repayment | debit | monthly (30d estimate) | 2026-01-13 | `event_1255`, `event_1262`, `event_1269` |
| Music subscription | music_subscription | debit | monthly (30d estimate) | 2026-01-13 | `event_1256`, `event_1263`, `event_1270` |
| Food delivery membership | delivery_membership | debit | monthly (30d estimate) | 2026-01-15 | `event_1257`, `event_1264`, `event_1271` |
| Ride-hailing trip | transport | debit | days (21d estimate) | 2026-01-21 | `event_1316`, `event_1319`, `event_1322` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-02-04 | Inferred recurring Landlord standing order | -435.6 |
| 2026-03-04 | Inferred recurring Landlord standing order | -435.6 |
| 2026-04-04 | Inferred recurring Landlord standing order | -435.6 |
| 2026-01-08 | Inferred recurring Energy provider bill | -90.39 |
| 2026-02-08 | Inferred recurring Energy provider bill | -90.39 |
| 2026-03-08 | Inferred recurring Energy provider bill | -90.39 |
| 2026-01-10 | Inferred recurring School fee payment | -159 |
| 2026-02-10 | Inferred recurring School fee payment | -159 |
| 2026-03-10 | Inferred recurring School fee payment | -159 |
| 2026-01-13 | Inferred recurring Credit card repayment | -84 |
| 2026-02-13 | Inferred recurring Credit card repayment | -84 |
| 2026-03-13 | Inferred recurring Credit card repayment | -84 |
| 2026-01-13 | Inferred recurring Music subscription | -11 |
| 2026-02-13 | Inferred recurring Music subscription | -11 |
| 2026-03-13 | Inferred recurring Music subscription | -11 |
| 2026-01-15 | Inferred recurring Food delivery membership | -27 |
| 2026-02-15 | Inferred recurring Food delivery membership | -27 |
| 2026-03-15 | Inferred recurring Food delivery membership | -27 |
| 2026-01-21 | Inferred recurring Ride-hailing trip | -41.35 |
| 2026-02-11 | Inferred recurring Ride-hailing trip | -41.35 |
| 2026-03-04 | Inferred recurring Ride-hailing trip | -41.35 |
| 2026-03-25 | Inferred recurring Ride-hailing trip | -41.35 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-01-08 | `recurring:utilities` | recurring | utilities | -90.39 |
| 2026-01-10 | `recurring:education` | recurring | education | -159 |
| 2026-01-13 | `recurring:debt_repayment` | recurring | debt_repayment | -84 |
| 2026-01-13 | `recurring:music_subscription` | recurring | music_subscription | -11 |
| 2026-01-15 | `recurring:delivery_membership` | recurring | delivery_membership | -27 |
| 2026-01-21 | `recurring:transport` | recurring | transport | -41.35 |
| 2026-02-04 | `recurring:rent` | recurring | rent | -435.6 |
| 2026-02-08 | `recurring:utilities` | recurring | utilities | -90.39 |
| 2026-02-10 | `recurring:education` | recurring | education | -159 |
| 2026-02-11 | `recurring:transport` | recurring | transport | -41.35 |
| 2026-02-13 | `recurring:debt_repayment` | recurring | debt_repayment | -84 |
| 2026-02-13 | `recurring:music_subscription` | recurring | music_subscription | -11 |
| 2026-02-15 | `recurring:delivery_membership` | recurring | delivery_membership | -27 |
| 2026-03-04 | `recurring:rent` | recurring | rent | -435.6 |
| 2026-03-04 | `recurring:transport` | recurring | transport | -41.35 |
| 2026-03-08 | `recurring:utilities` | recurring | utilities | -90.39 |
| 2026-03-10 | `recurring:education` | recurring | education | -159 |
| 2026-03-13 | `recurring:debt_repayment` | recurring | debt_repayment | -84 |
| 2026-03-13 | `recurring:music_subscription` | recurring | music_subscription | -11 |
| 2026-03-15 | `recurring:delivery_membership` | recurring | delivery_membership | -27 |
| 2026-03-25 | `recurring:transport` | recurring | transport | -41.35 |
| 2026-04-04 | `recurring:rent` | recurring | rent | -435.6 |

## request_16 — user_16

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2023-08-15 | `event_1350`, `event_1357`, `event_1364` |
| Monthly rent | rent | debit | monthly (30d estimate) | 2023-09-01 | `event_1358`, `event_1365`, `event_1371` |
| Energy provider bill | utilities | debit | monthly (30d estimate) | 2023-09-05 | `event_1359`, `event_1366`, `event_1372` |
| Vehicle loan payment | debt_repayment | debit | monthly (30d estimate) | 2023-09-10 | `event_1360`, `event_1367`, `event_1373` |
| Video streaming plan | streaming | debit | monthly (30d estimate) | 2023-09-08 | `event_1361`, `event_1368`, `event_1374` |
| Cloud storage plan | cloud_storage | debit | monthly (30d estimate) | 2023-09-11 | `event_1362`, `event_1369`, `event_1375` |
| Clothing and household items | shopping | debit | monthly (30d estimate) | 2023-09-11 | `event_1363`, `event_1370`, `event_1376` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2023-08-15 | Inferred recurring Payroll credit | 173000 |
| 2023-09-15 | Inferred recurring Payroll credit | 173000 |
| 2023-10-15 | Inferred recurring Payroll credit | 173000 |
| 2023-09-01 | Inferred recurring Monthly rent | -57100 |
| 2023-10-01 | Inferred recurring Monthly rent | -57100 |
| 2023-11-01 | Inferred recurring Monthly rent | -57100 |
| 2023-09-05 | Inferred recurring Energy provider bill | -11512.87 |
| 2023-10-05 | Inferred recurring Energy provider bill | -11512.87 |
| 2023-11-05 | Inferred recurring Energy provider bill | -11512.87 |
| 2023-09-10 | Inferred recurring Vehicle loan payment | -17750 |
| 2023-10-10 | Inferred recurring Vehicle loan payment | -17750 |
| 2023-11-10 | Inferred recurring Vehicle loan payment | -17750 |
| 2023-09-08 | Inferred recurring Video streaming plan | -3510 |
| 2023-10-08 | Inferred recurring Video streaming plan | -3510 |
| 2023-11-08 | Inferred recurring Video streaming plan | -3510 |
| 2023-09-11 | Inferred recurring Cloud storage plan | -1055 |
| 2023-10-11 | Inferred recurring Cloud storage plan | -1055 |
| 2023-09-11 | Inferred recurring Clothing and household items | -10178.56 |
| 2023-10-11 | Inferred recurring Clothing and household items | -10178.56 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2023-08-15 | `recurring:salary` | recurring | salary | 173000 |
| 2023-09-01 | `recurring:rent` | recurring | rent | -57100 |
| 2023-09-05 | `recurring:utilities` | recurring | utilities | -11512.87 |
| 2023-09-08 | `recurring:streaming` | recurring | streaming | -3510 |
| 2023-09-10 | `recurring:debt_repayment` | recurring | debt_repayment | -17750 |
| 2023-09-11 | `recurring:cloud_storage` | recurring | cloud_storage | -1055 |
| 2023-09-11 | `recurring:shopping` | recurring | shopping | -10178.56 |
| 2023-09-15 | `recurring:salary` | recurring | salary | 173000 |
| 2023-10-01 | `recurring:rent` | recurring | rent | -57100 |
| 2023-10-05 | `recurring:utilities` | recurring | utilities | -11512.87 |
| 2023-10-08 | `recurring:streaming` | recurring | streaming | -3510 |
| 2023-10-10 | `recurring:debt_repayment` | recurring | debt_repayment | -17750 |
| 2023-10-11 | `recurring:cloud_storage` | recurring | cloud_storage | -1055 |
| 2023-10-11 | `recurring:shopping` | recurring | shopping | -10178.56 |
| 2023-10-15 | `recurring:salary` | recurring | salary | 173000 |
| 2023-11-01 | `recurring:rent` | recurring | rent | -57100 |
| 2023-11-05 | `recurring:utilities` | recurring | utilities | -11512.87 |
| 2023-11-08 | `recurring:streaming` | recurring | streaming | -3510 |
| 2023-11-10 | `recurring:debt_repayment` | recurring | debt_repayment | -17750 |

## request_17 — user_17

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (31d estimate) | 2026-03-15 | `event_1457`, `event_1464`, `event_1471` |
| Apartment rent transfer | rent | debit | monthly (31d estimate) | 2026-03-02 | `event_1458`, `event_1465`, `event_1472` |
| Municipal utilities | utilities | debit | monthly (31d estimate) | 2026-03-06 | `event_1459`, `event_1466`, `event_1473` |
| Course tuition | education | debit | monthly (31d estimate) | 2026-03-08 | `event_1460`, `event_1467`, `event_1474` |
| Credit card repayment | debt_repayment | debit | monthly (31d estimate) | 2026-03-11 | `event_1461`, `event_1468`, `event_1475` |
| Music subscription | music_subscription | debit | monthly (31d estimate) | 2026-03-11 | `event_1462`, `event_1469`, `event_1476` |
| Food delivery membership | delivery_membership | debit | monthly (31d estimate) | 2026-03-13 | `event_1463`, `event_1470`, `event_1477` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-03-15 | Inferred recurring Payroll credit | 206000 |
| 2026-04-15 | Inferred recurring Payroll credit | 206000 |
| 2026-05-15 | Inferred recurring Payroll credit | 206000 |
| 2026-03-02 | Inferred recurring Apartment rent transfer | -49600 |
| 2026-04-02 | Inferred recurring Apartment rent transfer | -49600 |
| 2026-05-02 | Inferred recurring Apartment rent transfer | -49600 |
| 2026-03-06 | Inferred recurring Municipal utilities | -10246.53 |
| 2026-04-06 | Inferred recurring Municipal utilities | -10246.53 |
| 2026-05-06 | Inferred recurring Municipal utilities | -10246.53 |
| 2026-03-08 | Inferred recurring Course tuition | -13660 |
| 2026-04-08 | Inferred recurring Course tuition | -13660 |
| 2026-05-08 | Inferred recurring Course tuition | -13660 |
| 2026-03-11 | Inferred recurring Credit card repayment | -30200 |
| 2026-04-11 | Inferred recurring Credit card repayment | -30200 |
| 2026-05-11 | Inferred recurring Credit card repayment | -30200 |
| 2026-03-11 | Inferred recurring Music subscription | -2055 |
| 2026-04-11 | Inferred recurring Music subscription | -2055 |
| 2026-05-11 | Inferred recurring Music subscription | -2055 |
| 2026-03-13 | Inferred recurring Food delivery membership | -1675 |
| 2026-04-13 | Inferred recurring Food delivery membership | -1675 |
| 2026-05-13 | Inferred recurring Food delivery membership | -1675 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| Payroll credit / 2026-03-15 | `event_1546` / 2026-03-15 | explicit event_1546 matches salary/credit within 3 days |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-03-02 | `recurring:rent` | recurring | rent | -49600 |
| 2026-03-06 | `recurring:utilities` | recurring | utilities | -10246.53 |
| 2026-03-08 | `recurring:education` | recurring | education | -13660 |
| 2026-03-11 | `recurring:debt_repayment` | recurring | debt_repayment | -30200 |
| 2026-03-11 | `recurring:music_subscription` | recurring | music_subscription | -2055 |
| 2026-03-13 | `recurring:delivery_membership` | recurring | delivery_membership | -1675 |
| 2026-03-15 | `event_1546` | explicit | salary | 206000 |
| 2026-04-02 | `recurring:rent` | recurring | rent | -49600 |
| 2026-04-06 | `recurring:utilities` | recurring | utilities | -10246.53 |
| 2026-04-08 | `recurring:education` | recurring | education | -13660 |
| 2026-04-11 | `recurring:debt_repayment` | recurring | debt_repayment | -30200 |
| 2026-04-11 | `recurring:music_subscription` | recurring | music_subscription | -2055 |
| 2026-04-13 | `recurring:delivery_membership` | recurring | delivery_membership | -1675 |
| 2026-04-15 | `recurring:salary` | recurring | salary | 206000 |
| 2026-05-02 | `recurring:rent` | recurring | rent | -49600 |
| 2026-05-06 | `recurring:utilities` | recurring | utilities | -10246.53 |
| 2026-05-08 | `recurring:education` | recurring | education | -13660 |
| 2026-05-11 | `recurring:debt_repayment` | recurring | debt_repayment | -30200 |
| 2026-05-11 | `recurring:music_subscription` | recurring | music_subscription | -2055 |
| 2026-05-13 | `recurring:delivery_membership` | recurring | delivery_membership | -1675 |
| 2026-05-15 | `recurring:salary` | recurring | salary | 206000 |

## request_18 — user_18

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2026-07-15 | `event_1559`, `event_1565`, `event_1571` |
| Building maintenance payment | housing | debit | monthly (30d estimate) | 2026-08-04 | `event_1566`, `event_1572`, `event_1577` |
| Energy provider bill | utilities | debit | monthly (30d estimate) | 2026-08-07 | `event_1561`, `event_1567`, `event_1573` |
| Household insurance | insurance | debit | monthly (30d estimate) | 2026-07-08 | `event_1562`, `event_1568`, `event_1574` |
| Clinic payment | healthcare | debit | monthly (30d estimate) | 2026-07-11 | `event_1563`, `event_1569`, `event_1575` |
| Family streaming plan | streaming | debit | monthly (30d estimate) | 2026-07-10 | `event_1564`, `event_1570`, `event_1576` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-07-15 | Inferred recurring Payroll credit | 2310 |
| 2026-08-15 | Inferred recurring Payroll credit | 2310 |
| 2026-09-15 | Inferred recurring Payroll credit | 2310 |
| 2026-08-04 | Inferred recurring Building maintenance payment | -167 |
| 2026-09-04 | Inferred recurring Building maintenance payment | -167 |
| 2026-10-04 | Inferred recurring Building maintenance payment | -167 |
| 2026-08-07 | Inferred recurring Energy provider bill | -125.4 |
| 2026-09-07 | Inferred recurring Energy provider bill | -125.4 |
| 2026-07-08 | Inferred recurring Household insurance | -68 |
| 2026-08-08 | Inferred recurring Household insurance | -68 |
| 2026-09-08 | Inferred recurring Household insurance | -68 |
| 2026-07-11 | Inferred recurring Clinic payment | -162.41 |
| 2026-08-11 | Inferred recurring Clinic payment | -162.41 |
| 2026-09-11 | Inferred recurring Clinic payment | -162.41 |
| 2026-07-10 | Inferred recurring Family streaming plan | -68 |
| 2026-08-10 | Inferred recurring Family streaming plan | -68 |
| 2026-09-10 | Inferred recurring Family streaming plan | -68 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-07-08 | `recurring:insurance` | recurring | insurance | -68 |
| 2026-07-10 | `recurring:streaming` | recurring | streaming | -68 |
| 2026-07-11 | `recurring:healthcare` | recurring | healthcare | -162.41 |
| 2026-07-15 | `recurring:salary` | recurring | salary | 2310 |
| 2026-08-04 | `recurring:housing` | recurring | housing | -167 |
| 2026-08-07 | `recurring:utilities` | recurring | utilities | -125.4 |
| 2026-08-08 | `recurring:insurance` | recurring | insurance | -68 |
| 2026-08-10 | `recurring:streaming` | recurring | streaming | -68 |
| 2026-08-11 | `recurring:healthcare` | recurring | healthcare | -162.41 |
| 2026-08-15 | `recurring:salary` | recurring | salary | 2310 |
| 2026-09-04 | `recurring:housing` | recurring | housing | -167 |
| 2026-09-07 | `recurring:utilities` | recurring | utilities | -125.4 |
| 2026-09-08 | `recurring:insurance` | recurring | insurance | -68 |
| 2026-09-10 | `recurring:streaming` | recurring | streaming | -68 |
| 2026-09-11 | `recurring:healthcare` | recurring | healthcare | -162.41 |
| 2026-09-15 | `recurring:salary` | recurring | salary | 2310 |
| 2026-10-04 | `recurring:housing` | recurring | housing | -167 |

## request_19 — user_19

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2024-09-15 | `event_1638`, `event_1646`, `event_1654` |
| Residential rent payment | rent | debit | monthly (30d estimate) | 2024-10-04 | `event_1639`, `event_1647`, `event_1655` |
| Municipal utilities | utilities | debit | monthly (30d estimate) | 2024-09-08 | `event_1640`, `event_1648`, `event_1656` |
| Loan repayment | debt_repayment | debit | monthly (30d estimate) | 2024-09-13 | `event_1641`, `event_1649`, `event_1657` |
| Clinic payment | healthcare | debit | monthly (30d estimate) | 2024-09-12 | `event_1642`, `event_1650`, `event_1658` |
| Childcare contribution | family_support | debit | monthly (30d estimate) | 2024-09-15 | `event_1643`, `event_1651`, `event_1659` |
| Online backup subscription | cloud_storage | debit | monthly (30d estimate) | 2024-09-14 | `event_1644`, `event_1652`, `event_1660` |
| Clothing and household items | shopping | debit | monthly (30d estimate) | 2024-09-14 | `event_1645`, `event_1653`, `event_1661` |
| Fresh food shop | groceries | debit | days (24d estimate) | 2024-09-12 | `event_1664`, `event_1668`, `event_1671` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-09-15 | Inferred recurring Payroll credit | 131000 |
| 2024-10-15 | Inferred recurring Payroll credit | 131000 |
| 2024-11-15 | Inferred recurring Payroll credit | 131000 |
| 2024-10-04 | Inferred recurring Residential rent payment | -36100 |
| 2024-11-04 | Inferred recurring Residential rent payment | -36100 |
| 2024-09-08 | Inferred recurring Municipal utilities | -6129.19 |
| 2024-10-08 | Inferred recurring Municipal utilities | -6129.19 |
| 2024-11-08 | Inferred recurring Municipal utilities | -6129.19 |
| 2024-09-13 | Inferred recurring Loan repayment | -11850 |
| 2024-10-13 | Inferred recurring Loan repayment | -11850 |
| 2024-11-13 | Inferred recurring Loan repayment | -11850 |
| 2024-09-12 | Inferred recurring Clinic payment | -8645.36 |
| 2024-10-12 | Inferred recurring Clinic payment | -8645.36 |
| 2024-11-12 | Inferred recurring Clinic payment | -8645.36 |
| 2024-09-15 | Inferred recurring Childcare contribution | -12650 |
| 2024-10-15 | Inferred recurring Childcare contribution | -12650 |
| 2024-11-15 | Inferred recurring Childcare contribution | -12650 |
| 2024-09-14 | Inferred recurring Online backup subscription | -395 |
| 2024-10-14 | Inferred recurring Online backup subscription | -395 |
| 2024-11-14 | Inferred recurring Online backup subscription | -395 |
| 2024-09-14 | Inferred recurring Clothing and household items | -6069.58 |
| 2024-10-14 | Inferred recurring Clothing and household items | -6069.58 |
| 2024-11-14 | Inferred recurring Clothing and household items | -6069.58 |
| 2024-09-12 | Inferred recurring Fresh food shop | -6070.85 |
| 2024-10-06 | Inferred recurring Fresh food shop | -6070.85 |
| 2024-10-30 | Inferred recurring Fresh food shop | -6070.85 |
| 2024-11-23 | Inferred recurring Fresh food shop | -6070.85 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-09-08 | `recurring:utilities` | recurring | utilities | -6129.19 |
| 2024-09-12 | `recurring:groceries` | recurring | groceries | -6070.85 |
| 2024-09-12 | `recurring:healthcare` | recurring | healthcare | -8645.36 |
| 2024-09-13 | `recurring:debt_repayment` | recurring | debt_repayment | -11850 |
| 2024-09-14 | `recurring:cloud_storage` | recurring | cloud_storage | -395 |
| 2024-09-14 | `recurring:shopping` | recurring | shopping | -6069.58 |
| 2024-09-15 | `recurring:family_support` | recurring | family_support | -12650 |
| 2024-09-15 | `recurring:salary` | recurring | salary | 131000 |
| 2024-10-04 | `recurring:rent` | recurring | rent | -36100 |
| 2024-10-06 | `recurring:groceries` | recurring | groceries | -6070.85 |
| 2024-10-08 | `recurring:utilities` | recurring | utilities | -6129.19 |
| 2024-10-12 | `recurring:healthcare` | recurring | healthcare | -8645.36 |
| 2024-10-13 | `recurring:debt_repayment` | recurring | debt_repayment | -11850 |
| 2024-10-14 | `recurring:cloud_storage` | recurring | cloud_storage | -395 |
| 2024-10-14 | `recurring:shopping` | recurring | shopping | -6069.58 |
| 2024-10-15 | `recurring:family_support` | recurring | family_support | -12650 |
| 2024-10-15 | `recurring:salary` | recurring | salary | 131000 |
| 2024-10-30 | `recurring:groceries` | recurring | groceries | -6070.85 |
| 2024-11-04 | `recurring:rent` | recurring | rent | -36100 |
| 2024-11-08 | `recurring:utilities` | recurring | utilities | -6129.19 |
| 2024-11-12 | `recurring:healthcare` | recurring | healthcare | -8645.36 |
| 2024-11-13 | `recurring:debt_repayment` | recurring | debt_repayment | -11850 |
| 2024-11-14 | `recurring:cloud_storage` | recurring | cloud_storage | -395 |
| 2024-11-14 | `recurring:shopping` | recurring | shopping | -6069.58 |
| 2024-11-15 | `recurring:family_support` | recurring | family_support | -12650 |
| 2024-11-15 | `recurring:salary` | recurring | salary | 131000 |
| 2024-11-23 | `recurring:groceries` | recurring | groceries | -6070.85 |

## request_20 — user_20

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2026-02-15 | `event_1717`, `event_1725`, `event_1733` |
| Home association fee | housing | debit | monthly (31d estimate) | 2026-03-02 | `event_1726`, `event_1734`, `event_1741` |
| Municipal utilities | utilities | debit | monthly (31d estimate) | 2026-03-05 | `event_1727`, `event_1735`, `event_1742` |
| Household insurance | insurance | debit | monthly (31d estimate) | 2026-03-06 | `event_1728`, `event_1736`, `event_1743` |
| School fee payment | education | debit | monthly (30d estimate) | 2026-03-07 | `event_1721`, `event_1729`, `event_1737` |
| Family healthcare expense | healthcare | debit | monthly (30d estimate) | 2026-02-09 | `event_1722`, `event_1730`, `event_1738` |
| Cinema and events | entertainment | debit | monthly (30d estimate) | 2026-02-13 | `event_1723`, `event_1731`, `event_1739` |
| Shared storage plan | cloud_storage | debit | monthly (30d estimate) | 2026-02-11 | `event_1724`, `event_1732`, `event_1740` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-02-15 | Inferred recurring Payroll credit | 108000 |
| 2026-03-15 | Inferred recurring Payroll credit | 108000 |
| 2026-04-15 | Inferred recurring Payroll credit | 108000 |
| 2026-03-02 | Inferred recurring Home association fee | -7950 |
| 2026-04-02 | Inferred recurring Home association fee | -7950 |
| 2026-05-02 | Inferred recurring Home association fee | -7950 |
| 2026-03-05 | Inferred recurring Municipal utilities | -7769.87 |
| 2026-04-05 | Inferred recurring Municipal utilities | -7769.87 |
| 2026-05-05 | Inferred recurring Municipal utilities | -7769.87 |
| 2026-03-06 | Inferred recurring Household insurance | -3290 |
| 2026-04-06 | Inferred recurring Household insurance | -3290 |
| 2026-05-06 | Inferred recurring Household insurance | -3290 |
| 2026-03-07 | Inferred recurring School fee payment | -8740 |
| 2026-04-07 | Inferred recurring School fee payment | -8740 |
| 2026-05-07 | Inferred recurring School fee payment | -8740 |
| 2026-02-09 | Inferred recurring Family healthcare expense | -6654.33 |
| 2026-03-09 | Inferred recurring Family healthcare expense | -6654.33 |
| 2026-04-09 | Inferred recurring Family healthcare expense | -6654.33 |
| 2026-02-13 | Inferred recurring Cinema and events | -2115.92 |
| 2026-03-13 | Inferred recurring Cinema and events | -2115.92 |
| 2026-04-13 | Inferred recurring Cinema and events | -2115.92 |
| 2026-02-11 | Inferred recurring Shared storage plan | -365 |
| 2026-03-11 | Inferred recurring Shared storage plan | -365 |
| 2026-04-11 | Inferred recurring Shared storage plan | -365 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-02-08 | `event_1787` | explicit | shopping | -4470 |
| 2026-02-09 | `recurring:healthcare` | recurring | healthcare | -6654.33 |
| 2026-02-11 | `recurring:cloud_storage` | recurring | cloud_storage | -365 |
| 2026-02-13 | `recurring:entertainment` | recurring | entertainment | -2115.92 |
| 2026-02-15 | `recurring:salary` | recurring | salary | 108000 |
| 2026-03-02 | `recurring:housing` | recurring | housing | -7950 |
| 2026-03-05 | `recurring:utilities` | recurring | utilities | -7769.87 |
| 2026-03-06 | `recurring:insurance` | recurring | insurance | -3290 |
| 2026-03-07 | `recurring:education` | recurring | education | -8740 |
| 2026-03-09 | `recurring:healthcare` | recurring | healthcare | -6654.33 |
| 2026-03-11 | `recurring:cloud_storage` | recurring | cloud_storage | -365 |
| 2026-03-13 | `recurring:entertainment` | recurring | entertainment | -2115.92 |
| 2026-03-15 | `recurring:salary` | recurring | salary | 108000 |
| 2026-04-02 | `recurring:housing` | recurring | housing | -7950 |
| 2026-04-05 | `recurring:utilities` | recurring | utilities | -7769.87 |
| 2026-04-06 | `recurring:insurance` | recurring | insurance | -3290 |
| 2026-04-07 | `recurring:education` | recurring | education | -8740 |
| 2026-04-09 | `recurring:healthcare` | recurring | healthcare | -6654.33 |
| 2026-04-11 | `recurring:cloud_storage` | recurring | cloud_storage | -365 |
| 2026-04-13 | `recurring:entertainment` | recurring | entertainment | -2115.92 |
| 2026-04-15 | `recurring:salary` | recurring | salary | 108000 |
| 2026-05-02 | `recurring:housing` | recurring | housing | -7950 |
| 2026-05-05 | `recurring:utilities` | recurring | utilities | -7769.87 |
| 2026-05-06 | `recurring:insurance` | recurring | insurance | -3290 |
| 2026-05-07 | `recurring:education` | recurring | education | -8740 |

## request_21 — user_21

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2026-04-15 | `event_1800`, `event_1806`, `event_1812` |
| Residential rent payment | rent | debit | monthly (31d estimate) | 2026-05-02 | `event_1807`, `event_1813`, `event_1818` |
| Municipal utilities | utilities | debit | monthly (30d estimate) | 2026-04-06 | `event_1802`, `event_1808`, `event_1814` |
| Online backup subscription | cloud_storage | debit | monthly (30d estimate) | 2026-04-12 | `event_1803`, `event_1809`, `event_1815` |
| Streaming subscription | streaming | debit | monthly (30d estimate) | 2026-04-09 | `event_1804`, `event_1810`, `event_1816` |
| Monthly shopping spend | shopping | debit | monthly (30d estimate) | 2026-04-12 | `event_1805`, `event_1811`, `event_1817` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-04-15 | Inferred recurring Payroll credit | 2256 |
| 2026-05-15 | Inferred recurring Payroll credit | 2256 |
| 2026-06-15 | Inferred recurring Payroll credit | 2256 |
| 2026-05-02 | Inferred recurring Residential rent payment | -718.8 |
| 2026-06-02 | Inferred recurring Residential rent payment | -718.8 |
| 2026-07-02 | Inferred recurring Residential rent payment | -718.8 |
| 2026-04-06 | Inferred recurring Municipal utilities | -124.08 |
| 2026-05-06 | Inferred recurring Municipal utilities | -124.08 |
| 2026-06-06 | Inferred recurring Municipal utilities | -124.08 |
| 2026-04-12 | Inferred recurring Online backup subscription | -11 |
| 2026-05-12 | Inferred recurring Online backup subscription | -11 |
| 2026-06-12 | Inferred recurring Online backup subscription | -11 |
| 2026-04-09 | Inferred recurring Streaming subscription | -47 |
| 2026-05-09 | Inferred recurring Streaming subscription | -47 |
| 2026-06-09 | Inferred recurring Streaming subscription | -47 |
| 2026-04-12 | Inferred recurring Monthly shopping spend | -126.38 |
| 2026-05-12 | Inferred recurring Monthly shopping spend | -126.38 |
| 2026-06-12 | Inferred recurring Monthly shopping spend | -126.38 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| Payroll credit / 2026-04-15 | `event_1858` / 2026-04-15 | explicit event_1858 matches salary/credit within 3 days |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-04-05 | `event_1857` | explicit | transport | -53 |
| 2026-04-06 | `recurring:utilities` | recurring | utilities | -124.08 |
| 2026-04-09 | `recurring:streaming` | recurring | streaming | -47 |
| 2026-04-12 | `recurring:cloud_storage` | recurring | cloud_storage | -11 |
| 2026-04-12 | `recurring:shopping` | recurring | shopping | -126.38 |
| 2026-04-15 | `event_1858` | explicit | salary | 2256 |
| 2026-05-02 | `recurring:rent` | recurring | rent | -718.8 |
| 2026-05-06 | `recurring:utilities` | recurring | utilities | -124.08 |
| 2026-05-09 | `recurring:streaming` | recurring | streaming | -47 |
| 2026-05-12 | `recurring:cloud_storage` | recurring | cloud_storage | -11 |
| 2026-05-12 | `recurring:shopping` | recurring | shopping | -126.38 |
| 2026-05-15 | `recurring:salary` | recurring | salary | 2256 |
| 2026-06-02 | `recurring:rent` | recurring | rent | -718.8 |
| 2026-06-06 | `recurring:utilities` | recurring | utilities | -124.08 |
| 2026-06-09 | `recurring:streaming` | recurring | streaming | -47 |
| 2026-06-12 | `recurring:cloud_storage` | recurring | cloud_storage | -11 |
| 2026-06-12 | `recurring:shopping` | recurring | shopping | -126.38 |
| 2026-06-15 | `recurring:salary` | recurring | salary | 2256 |
| 2026-07-02 | `recurring:rent` | recurring | rent | -718.8 |

## request_22 — user_22

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (31d estimate) | 2024-12-15 | `event_1873`, `event_1880`, `event_1887` |
| Apartment rent transfer | rent | debit | monthly (30d estimate) | 2025-01-03 | `event_1881`, `event_1888`, `event_1894` |
| Electricity and water bill | utilities | debit | monthly (31d estimate) | 2024-12-07 | `event_1875`, `event_1882`, `event_1889` |
| Music service subscription | music_subscription | debit | monthly (31d estimate) | 2024-12-12 | `event_1876`, `event_1883`, `event_1890` |
| Food delivery membership | delivery_membership | debit | monthly (31d estimate) | 2024-12-14 | `event_1877`, `event_1884`, `event_1891` |
| Gym membership | gym | debit | monthly (31d estimate) | 2024-12-11 | `event_1878`, `event_1885`, `event_1892` |
| Weekend entertainment | entertainment | debit | monthly (31d estimate) | 2024-12-15 | `event_1879`, `event_1886`, `event_1893` |
| Commuter pass | transport | debit | days (32d estimate) | 2024-12-28 | `event_1922`, `event_1926`, `event_1931` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-12-15 | Inferred recurring Payroll credit | 616 |
| 2025-01-15 | Inferred recurring Payroll credit | 616 |
| 2025-02-15 | Inferred recurring Payroll credit | 616 |
| 2025-01-03 | Inferred recurring Apartment rent transfer | -178.2 |
| 2025-02-03 | Inferred recurring Apartment rent transfer | -178.2 |
| 2025-03-03 | Inferred recurring Apartment rent transfer | -178.2 |
| 2024-12-07 | Inferred recurring Electricity and water bill | -31.52 |
| 2025-01-07 | Inferred recurring Electricity and water bill | -31.52 |
| 2025-02-07 | Inferred recurring Electricity and water bill | -31.52 |
| 2024-12-12 | Inferred recurring Music service subscription | -6 |
| 2025-01-12 | Inferred recurring Music service subscription | -6 |
| 2025-02-12 | Inferred recurring Music service subscription | -6 |
| 2024-12-14 | Inferred recurring Food delivery membership | -5 |
| 2025-01-14 | Inferred recurring Food delivery membership | -5 |
| 2025-02-14 | Inferred recurring Food delivery membership | -5 |
| 2024-12-11 | Inferred recurring Gym membership | -17 |
| 2025-01-11 | Inferred recurring Gym membership | -17 |
| 2025-02-11 | Inferred recurring Gym membership | -17 |
| 2024-12-15 | Inferred recurring Weekend entertainment | -23.29 |
| 2025-01-15 | Inferred recurring Weekend entertainment | -23.29 |
| 2025-02-15 | Inferred recurring Weekend entertainment | -23.29 |
| 2024-12-28 | Inferred recurring Commuter pass | -12.7 |
| 2025-01-29 | Inferred recurring Commuter pass | -12.7 |
| 2025-03-02 | Inferred recurring Commuter pass | -12.7 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-12-07 | `recurring:utilities` | recurring | utilities | -31.52 |
| 2024-12-08 | `event_1961` | explicit | shopping | -43 |
| 2024-12-11 | `recurring:gym` | recurring | gym | -17 |
| 2024-12-12 | `recurring:music_subscription` | recurring | music_subscription | -6 |
| 2024-12-14 | `recurring:delivery_membership` | recurring | delivery_membership | -5 |
| 2024-12-15 | `recurring:entertainment` | recurring | entertainment | -23.29 |
| 2024-12-15 | `recurring:salary` | recurring | salary | 616 |
| 2024-12-28 | `recurring:transport` | recurring | transport | -12.7 |
| 2025-01-03 | `recurring:rent` | recurring | rent | -178.2 |
| 2025-01-07 | `recurring:utilities` | recurring | utilities | -31.52 |
| 2025-01-11 | `recurring:gym` | recurring | gym | -17 |
| 2025-01-12 | `recurring:music_subscription` | recurring | music_subscription | -6 |
| 2025-01-14 | `recurring:delivery_membership` | recurring | delivery_membership | -5 |
| 2025-01-15 | `recurring:entertainment` | recurring | entertainment | -23.29 |
| 2025-01-15 | `recurring:salary` | recurring | salary | 616 |
| 2025-01-29 | `recurring:transport` | recurring | transport | -12.7 |
| 2025-02-03 | `recurring:rent` | recurring | rent | -178.2 |
| 2025-02-07 | `recurring:utilities` | recurring | utilities | -31.52 |
| 2025-02-11 | `recurring:gym` | recurring | gym | -17 |
| 2025-02-12 | `recurring:music_subscription` | recurring | music_subscription | -6 |
| 2025-02-14 | `recurring:delivery_membership` | recurring | delivery_membership | -5 |
| 2025-02-15 | `recurring:entertainment` | recurring | entertainment | -23.29 |
| 2025-02-15 | `recurring:salary` | recurring | salary | 616 |
| 2025-03-02 | `recurring:transport` | recurring | transport | -12.7 |
| 2025-03-03 | `recurring:rent` | recurring | rent | -178.2 |

## request_23 — user_23

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (31d estimate) | 2025-05-15 | `event_1978`, `event_1986`, `event_1994` |
| Shared housing rent | rent | debit | monthly (30d estimate) | 2025-06-04 | `event_1987`, `event_1995`, `event_2002` |
| Electricity bill | utilities | debit | monthly (31d estimate) | 2025-05-08 | `event_1980`, `event_1988`, `event_1996` |
| Education loan instalment | debt_repayment | debit | monthly (31d estimate) | 2025-05-13 | `event_1981`, `event_1989`, `event_1997` |
| Clinic payment | healthcare | debit | monthly (31d estimate) | 2025-05-12 | `event_1982`, `event_1990`, `event_1998` |
| Childcare contribution | family_support | debit | monthly (31d estimate) | 2025-05-15 | `event_1983`, `event_1991`, `event_1999` |
| Cloud storage plan | cloud_storage | debit | monthly (31d estimate) | 2025-05-14 | `event_1984`, `event_1992`, `event_2000` |
| Personal shopping | shopping | debit | monthly (31d estimate) | 2025-05-14 | `event_1985`, `event_1993`, `event_2001` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2025-05-15 | Inferred recurring Payroll credit | 45760 |
| 2025-06-15 | Inferred recurring Payroll credit | 45760 |
| 2025-07-15 | Inferred recurring Payroll credit | 45760 |
| 2025-06-04 | Inferred recurring Shared housing rent | -15312 |
| 2025-07-04 | Inferred recurring Shared housing rent | -15312 |
| 2025-08-04 | Inferred recurring Shared housing rent | -15312 |
| 2025-05-08 | Inferred recurring Electricity bill | -2915.67 |
| 2025-06-08 | Inferred recurring Electricity bill | -2915.67 |
| 2025-07-08 | Inferred recurring Electricity bill | -2915.67 |
| 2025-05-13 | Inferred recurring Education loan instalment | -5852 |
| 2025-06-13 | Inferred recurring Education loan instalment | -5852 |
| 2025-07-13 | Inferred recurring Education loan instalment | -5852 |
| 2025-05-12 | Inferred recurring Clinic payment | -1439.91 |
| 2025-06-12 | Inferred recurring Clinic payment | -1439.91 |
| 2025-07-12 | Inferred recurring Clinic payment | -1439.91 |
| 2025-05-15 | Inferred recurring Childcare contribution | -4270.2 |
| 2025-06-15 | Inferred recurring Childcare contribution | -4270.2 |
| 2025-07-15 | Inferred recurring Childcare contribution | -4270.2 |
| 2025-05-14 | Inferred recurring Cloud storage plan | -295.9 |
| 2025-06-14 | Inferred recurring Cloud storage plan | -295.9 |
| 2025-07-14 | Inferred recurring Cloud storage plan | -295.9 |
| 2025-05-14 | Inferred recurring Personal shopping | -1389.39 |
| 2025-06-14 | Inferred recurring Personal shopping | -1389.39 |
| 2025-07-14 | Inferred recurring Personal shopping | -1389.39 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| Clinic payment / 2025-05-12 | `event_2042` / 2025-05-11 | explicit event_2042 matches healthcare/debit within 3 days |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2025-05-08 | `recurring:utilities` | recurring | utilities | -2915.67 |
| 2025-05-11 | `event_2042` | explicit | healthcare | -1553.2 |
| 2025-05-13 | `recurring:debt_repayment` | recurring | debt_repayment | -5852 |
| 2025-05-14 | `recurring:cloud_storage` | recurring | cloud_storage | -295.9 |
| 2025-05-14 | `recurring:shopping` | recurring | shopping | -1389.39 |
| 2025-05-15 | `recurring:family_support` | recurring | family_support | -4270.2 |
| 2025-05-15 | `recurring:salary` | recurring | salary | 45760 |
| 2025-06-04 | `recurring:rent` | recurring | rent | -15312 |
| 2025-06-08 | `recurring:utilities` | recurring | utilities | -2915.67 |
| 2025-06-12 | `recurring:healthcare` | recurring | healthcare | -1439.91 |
| 2025-06-13 | `recurring:debt_repayment` | recurring | debt_repayment | -5852 |
| 2025-06-14 | `recurring:cloud_storage` | recurring | cloud_storage | -295.9 |
| 2025-06-14 | `recurring:shopping` | recurring | shopping | -1389.39 |
| 2025-06-15 | `recurring:family_support` | recurring | family_support | -4270.2 |
| 2025-06-15 | `recurring:salary` | recurring | salary | 45760 |
| 2025-07-04 | `recurring:rent` | recurring | rent | -15312 |
| 2025-07-08 | `recurring:utilities` | recurring | utilities | -2915.67 |
| 2025-07-12 | `recurring:healthcare` | recurring | healthcare | -1439.91 |
| 2025-07-13 | `recurring:debt_repayment` | recurring | debt_repayment | -5852 |
| 2025-07-14 | `recurring:cloud_storage` | recurring | cloud_storage | -295.9 |
| 2025-07-14 | `recurring:shopping` | recurring | shopping | -1389.39 |
| 2025-07-15 | `recurring:family_support` | recurring | family_support | -4270.2 |
| 2025-07-15 | `recurring:salary` | recurring | salary | 45760 |
| 2025-08-04 | `recurring:rent` | recurring | rent | -15312 |

## request_24 — user_24

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| Payroll credit | salary | credit | monthly (30d estimate) | 2026-01-15 | `event_2059`, `event_2067`, `event_2075` |
| Landlord standing order | rent | debit | monthly (30d estimate) | 2026-02-01 | `event_2068`, `event_2076`, `event_2083` |
| Household utility payment | utilities | debit | monthly (30d estimate) | 2026-01-05 | `event_2061`, `event_2069`, `event_2077` |
| Insurance policy payment | insurance | debit | monthly (30d estimate) | 2026-01-06 | `event_2062`, `event_2070`, `event_2078` |
| Online backup subscription | cloud_storage | debit | monthly (30d estimate) | 2026-01-11 | `event_2063`, `event_2071`, `event_2079` |
| Family streaming plan | streaming | debit | monthly (30d estimate) | 2026-01-08 | `event_2064`, `event_2072`, `event_2080` |
| Monthly shopping spend | shopping | debit | monthly (30d estimate) | 2026-01-11 | `event_2065`, `event_2073`, `event_2081` |
| Local event tickets | entertainment | debit | monthly (30d estimate) | 2026-01-13 | `event_2066`, `event_2074`, `event_2082` |
| Lunch with colleagues | dining | debit | days (32d estimate) | 2026-02-05 | `event_2145`, `event_2149`, `event_2154` |
| Family dinner | dining | debit | days (32d estimate) | 2026-01-28 | `event_2153`, `event_2157`, `event_2162` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2026-01-15 | Inferred recurring Payroll credit | 61000 |
| 2026-02-15 | Inferred recurring Payroll credit | 61000 |
| 2026-03-15 | Inferred recurring Payroll credit | 61000 |
| 2026-02-01 | Inferred recurring Landlord standing order | -18600 |
| 2026-03-01 | Inferred recurring Landlord standing order | -18600 |
| 2026-04-01 | Inferred recurring Landlord standing order | -18600 |
| 2026-01-05 | Inferred recurring Household utility payment | -3490.5 |
| 2026-02-05 | Inferred recurring Household utility payment | -3490.5 |
| 2026-03-05 | Inferred recurring Household utility payment | -3490.5 |
| 2026-01-06 | Inferred recurring Insurance policy payment | -2510 |
| 2026-02-06 | Inferred recurring Insurance policy payment | -2510 |
| 2026-03-06 | Inferred recurring Insurance policy payment | -2510 |
| 2026-01-11 | Inferred recurring Online backup subscription | -355 |
| 2026-02-11 | Inferred recurring Online backup subscription | -355 |
| 2026-03-11 | Inferred recurring Online backup subscription | -355 |
| 2026-01-08 | Inferred recurring Family streaming plan | -1200 |
| 2026-02-08 | Inferred recurring Family streaming plan | -1200 |
| 2026-03-08 | Inferred recurring Family streaming plan | -1200 |
| 2026-01-11 | Inferred recurring Monthly shopping spend | -2680.78 |
| 2026-02-11 | Inferred recurring Monthly shopping spend | -2680.78 |
| 2026-03-11 | Inferred recurring Monthly shopping spend | -2680.78 |
| 2026-01-13 | Inferred recurring Local event tickets | -1916.16 |
| 2026-02-13 | Inferred recurring Local event tickets | -1916.16 |
| 2026-03-13 | Inferred recurring Local event tickets | -1916.16 |
| 2026-02-05 | Inferred recurring Lunch with colleagues | -2137.71 |
| 2026-03-09 | Inferred recurring Lunch with colleagues | -2137.71 |
| 2026-01-28 | Inferred recurring Family dinner | -2151.71 |
| 2026-03-01 | Inferred recurring Family dinner | -2151.71 |
| 2026-04-02 | Inferred recurring Family dinner | -2151.71 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| — | — | No matching explicit future event |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2026-01-05 | `recurring:utilities` | recurring | utilities | -3490.5 |
| 2026-01-06 | `recurring:insurance` | recurring | insurance | -2510 |
| 2026-01-08 | `recurring:streaming` | recurring | streaming | -1200 |
| 2026-01-11 | `event_2166` | explicit | insurance | -1830 |
| 2026-01-11 | `recurring:cloud_storage` | recurring | cloud_storage | -355 |
| 2026-01-11 | `recurring:shopping` | recurring | shopping | -2680.78 |
| 2026-01-13 | `recurring:entertainment` | recurring | entertainment | -1916.16 |
| 2026-01-15 | `recurring:salary` | recurring | salary | 61000 |
| 2026-01-28 | `recurring:dining` | recurring | dining | -2151.71 |
| 2026-02-01 | `recurring:rent` | recurring | rent | -18600 |
| 2026-02-05 | `recurring:dining` | recurring | dining | -2137.71 |
| 2026-02-05 | `recurring:utilities` | recurring | utilities | -3490.5 |
| 2026-02-06 | `recurring:insurance` | recurring | insurance | -2510 |
| 2026-02-08 | `recurring:streaming` | recurring | streaming | -1200 |
| 2026-02-11 | `recurring:cloud_storage` | recurring | cloud_storage | -355 |
| 2026-02-11 | `recurring:shopping` | recurring | shopping | -2680.78 |
| 2026-02-13 | `recurring:entertainment` | recurring | entertainment | -1916.16 |
| 2026-02-15 | `recurring:salary` | recurring | salary | 61000 |
| 2026-03-01 | `recurring:dining` | recurring | dining | -2151.71 |
| 2026-03-01 | `recurring:rent` | recurring | rent | -18600 |
| 2026-03-05 | `recurring:utilities` | recurring | utilities | -3490.5 |
| 2026-03-06 | `recurring:insurance` | recurring | insurance | -2510 |
| 2026-03-08 | `recurring:streaming` | recurring | streaming | -1200 |
| 2026-03-09 | `recurring:dining` | recurring | dining | -2137.71 |
| 2026-03-11 | `recurring:cloud_storage` | recurring | cloud_storage | -355 |
| 2026-03-11 | `recurring:shopping` | recurring | shopping | -2680.78 |
| 2026-03-13 | `recurring:entertainment` | recurring | entertainment | -1916.16 |
| 2026-03-15 | `recurring:salary` | recurring | salary | 61000 |
| 2026-04-01 | `recurring:rent` | recurring | rent | -18600 |
| 2026-04-02 | `recurring:dining` | recurring | dining | -2151.71 |

## request_25 — user_25

### Inferred cadence and anchor

| Stream | Category | Direction | Cadence | Anchor | Historical evidence |
| --- | --- | --- | --- | --- | --- |
| International employer payroll | salary | credit | monthly (31d estimate) | 2024-03-15 | `event_2183`, `event_2191`, `event_2199` |
| Monthly rent | rent | debit | monthly (30d estimate) | 2024-04-02 | `event_2192`, `event_2200`, `event_2207` |
| Household utility payment | utilities | debit | monthly (31d estimate) | 2024-04-06 | `event_2185`, `event_2193`, `event_2201` |
| Insurance policy payment | insurance | debit | monthly (31d estimate) | 2024-03-07 | `event_2186`, `event_2194`, `event_2202` |
| Cloud storage plan | cloud_storage | debit | monthly (31d estimate) | 2024-03-12 | `event_2187`, `event_2195`, `event_2203` |
| Video streaming plan | streaming | debit | monthly (31d estimate) | 2024-03-09 | `event_2188`, `event_2196`, `event_2204` |
| Monthly shopping spend | shopping | debit | monthly (31d estimate) | 2024-03-12 | `event_2189`, `event_2197`, `event_2205` |
| Games and recreation | entertainment | debit | monthly (31d estimate) | 2024-03-14 | `event_2190`, `event_2198`, `event_2206` |

### Generated occurrences before reconciliation

| Date | Stream | Amount |
| --- | --- | ---: |
| 2024-03-15 | Inferred recurring International employer payroll | 28499994 |
| 2024-04-15 | Inferred recurring International employer payroll | 28499994 |
| 2024-05-15 | Inferred recurring International employer payroll | 28499994 |
| 2024-04-02 | Inferred recurring Monthly rent | -6954000 |
| 2024-05-02 | Inferred recurring Monthly rent | -6954000 |
| 2024-06-02 | Inferred recurring Monthly rent | -6954000 |
| 2024-04-06 | Inferred recurring Household utility payment | -1341541.39 |
| 2024-05-06 | Inferred recurring Household utility payment | -1341541.39 |
| 2024-03-07 | Inferred recurring Insurance policy payment | -904400 |
| 2024-04-07 | Inferred recurring Insurance policy payment | -904400 |
| 2024-05-07 | Inferred recurring Insurance policy payment | -904400 |
| 2024-03-12 | Inferred recurring Cloud storage plan | -126350 |
| 2024-04-12 | Inferred recurring Cloud storage plan | -126350 |
| 2024-05-12 | Inferred recurring Cloud storage plan | -126350 |
| 2024-03-09 | Inferred recurring Video streaming plan | -573800 |
| 2024-04-09 | Inferred recurring Video streaming plan | -573800 |
| 2024-05-09 | Inferred recurring Video streaming plan | -573800 |
| 2024-03-12 | Inferred recurring Monthly shopping spend | -1170271.29 |
| 2024-04-12 | Inferred recurring Monthly shopping spend | -1170271.29 |
| 2024-05-12 | Inferred recurring Monthly shopping spend | -1170271.29 |
| 2024-03-14 | Inferred recurring Games and recreation | -504697.37 |
| 2024-04-14 | Inferred recurring Games and recreation | -504697.37 |
| 2024-05-14 | Inferred recurring Games and recreation | -504697.37 |

### Explicit future events that supersede recurrence

| Generated stream/date | Explicit event/date | Matching reason |
| --- | --- | --- |
| International employer payroll / 2024-03-15 | `event_2288` / 2024-03-15 | explicit event_2288 matches salary/credit within 3 days |

### Final occurrences used in forecast

| Date | Source | Kind | Category | Amount |
| --- | --- | --- | --- | ---: |
| 2024-03-07 | `recurring:insurance` | recurring | insurance | -904400 |
| 2024-03-09 | `recurring:streaming` | recurring | streaming | -573800 |
| 2024-03-12 | `recurring:cloud_storage` | recurring | cloud_storage | -126350 |
| 2024-03-12 | `recurring:shopping` | recurring | shopping | -1170271.29 |
| 2024-03-14 | `recurring:entertainment` | recurring | entertainment | -504697.37 |
| 2024-03-15 | `event_2288` | explicit | salary | 28499994 |
| 2024-04-02 | `recurring:rent` | recurring | rent | -6954000 |
| 2024-04-06 | `recurring:utilities` | recurring | utilities | -1341541.39 |
| 2024-04-07 | `recurring:insurance` | recurring | insurance | -904400 |
| 2024-04-09 | `recurring:streaming` | recurring | streaming | -573800 |
| 2024-04-12 | `recurring:cloud_storage` | recurring | cloud_storage | -126350 |
| 2024-04-12 | `recurring:shopping` | recurring | shopping | -1170271.29 |
| 2024-04-14 | `recurring:entertainment` | recurring | entertainment | -504697.37 |
| 2024-04-15 | `recurring:salary` | recurring | salary | 28499994 |
| 2024-05-02 | `recurring:rent` | recurring | rent | -6954000 |
| 2024-05-06 | `recurring:utilities` | recurring | utilities | -1341541.39 |
| 2024-05-07 | `recurring:insurance` | recurring | insurance | -904400 |
| 2024-05-09 | `recurring:streaming` | recurring | streaming | -573800 |
| 2024-05-12 | `recurring:cloud_storage` | recurring | cloud_storage | -126350 |
| 2024-05-12 | `recurring:shopping` | recurring | shopping | -1170271.29 |
| 2024-05-14 | `recurring:entertainment` | recurring | entertainment | -504697.37 |
| 2024-05-15 | `recurring:salary` | recurring | salary | 28499994 |
| 2024-06-02 | `recurring:rent` | recurring | rent | -6954000 |
