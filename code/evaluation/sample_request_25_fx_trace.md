# Trace: request_25

As of `2024-03-06`, current balance is `32063050` IDR.

## Supplied post-request events counted

- `event_2288` — 2024-03-15: 28499994 (Next confirmed salary; explicit).

## Dated FX conversions

- `event_2288` on 2024-03-15: 1800 USD x 15833.33 = 28499994 IDR (fx_direct_pair).

## Inferred recurring commitments counted

- `International employer payroll` (`salary`): credit 28499994 every 31 days, starting 2024-03-17; evidence: event_2183, event_2191, event_2199.
- `Monthly rent` (`rent`): debit 6954000 every 30 days, starting 2024-04-01; evidence: event_2192, event_2200, event_2207.
- `Household utility payment` (`utilities`): debit 1341541.39 every 31 days, starting 2024-03-08; evidence: event_2185, event_2193, event_2201.
- `Insurance policy payment` (`insurance`): debit 904400 every 31 days, starting 2024-03-09; evidence: event_2186, event_2194, event_2202.
- `Cloud storage plan` (`cloud_storage`): debit 126350 every 31 days, starting 2024-03-14; evidence: event_2187, event_2195, event_2203.
- `Video streaming plan` (`streaming`): debit 573800 every 31 days, starting 2024-03-11; evidence: event_2188, event_2196, event_2204.
- `Monthly shopping spend` (`shopping`): debit 1170271.29 every 31 days, starting 2024-03-14; evidence: event_2189, event_2197, event_2205.
- `Games and recreation` (`entertainment`): debit 504697.37 every 31 days, starting 2024-03-16; evidence: event_2190, event_2198, event_2206.

## Lifecycle records excluded

- `event_2287` — failed event.

## Safe no-change payment candidates

- None; no safe permitted no-change payment candidate completes by the desired date.

## Authorized spending-change search

- No authorized changes to supported future recurring streams.
- Candidate/guard simulations: 0.

## Baseline 90-day result

- Minimum projected balance before this request: 27946687.32 on 2024-03-14.
- First minimum-balance breach: none.

## Ordered ledger for the recommended output

Same-day rule: debits first, then credits; ties use source ID, kind, category, and exact Decimal amount.

| # | Date | Direction | Change | Opening | Closing | Source | Kind | Source events | Evidence | Inclusion reason | Original | FX rate rule |
| ---: | --- | --- | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2024-03-08 | debit | -1341541.39 | 32063050 | 30721508.61 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence | - | - |
| 2 | 2024-03-09 | debit | -904400 | 30721508.61 | 29817108.61 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence | - | - |
| 3 | 2024-03-11 | debit | -573800 | 29817108.61 | 29243308.61 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence | - | - |
| 4 | 2024-03-14 | debit | -126350 | 29243308.61 | 29116958.61 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence | - | - |
| 5 | 2024-03-14 | debit | -1170271.29 | 29116958.61 | 27946687.32 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence | - | - |
| 6 | 2024-03-15 | credit | 28499994 | 27946687.32 | 56446681.32 | `event_2288` | explicit | `event_2288` | - | cash event | 1800 USD | 15833.33 (fx_direct_pair) |
| 7 | 2024-03-16 | debit | -504697.37 | 56446681.32 | 55941983.95 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence | - | - |
| 8 | 2024-03-17 | credit | 28499994 | 55941983.95 | 84441977.95 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence | - | - |
| 9 | 2024-04-01 | debit | -6954000 | 84441977.95 | 77487977.95 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence | - | - |
| 10 | 2024-04-08 | debit | -1341541.39 | 77487977.95 | 76146436.56 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence | - | - |
| 11 | 2024-04-09 | debit | -904400 | 76146436.56 | 75242036.56 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence | - | - |
| 12 | 2024-04-11 | debit | -573800 | 75242036.56 | 74668236.56 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence | - | - |
| 13 | 2024-04-14 | debit | -126350 | 74668236.56 | 74541886.56 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence | - | - |
| 14 | 2024-04-14 | debit | -1170271.29 | 74541886.56 | 73371615.27 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence | - | - |
| 15 | 2024-04-16 | debit | -504697.37 | 73371615.27 | 72866917.9 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence | - | - |
| 16 | 2024-04-17 | credit | 28499994 | 72866917.9 | 101366911.9 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence | - | - |
| 17 | 2024-05-01 | debit | -6954000 | 101366911.9 | 94412911.9 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence | - | - |
| 18 | 2024-05-09 | debit | -1341541.39 | 94412911.9 | 93071370.51 | `recurring:utilities` | recurring | `event_2185`, `event_2193`, `event_2201` | - | history supports a fixed 31-day recurrence | - | - |
| 19 | 2024-05-10 | debit | -904400 | 93071370.51 | 92166970.51 | `recurring:insurance` | recurring | `event_2186`, `event_2194`, `event_2202` | - | history supports a fixed 31-day recurrence | - | - |
| 20 | 2024-05-12 | debit | -573800 | 92166970.51 | 91593170.51 | `recurring:streaming` | recurring | `event_2188`, `event_2196`, `event_2204` | - | history supports a fixed 31-day recurrence | - | - |
| 21 | 2024-05-15 | debit | -126350 | 91593170.51 | 91466820.51 | `recurring:cloud_storage` | recurring | `event_2187`, `event_2195`, `event_2203` | - | history supports a fixed 31-day recurrence | - | - |
| 22 | 2024-05-15 | debit | -1170271.29 | 91466820.51 | 90296549.22 | `recurring:shopping` | recurring | `event_2189`, `event_2197`, `event_2205` | - | history supports a fixed 31-day recurrence | - | - |
| 23 | 2024-05-17 | debit | -504697.37 | 90296549.22 | 89791851.85 | `recurring:entertainment` | recurring | `event_2190`, `event_2198`, `event_2206` | - | history supports a fixed 31-day recurrence | - | - |
| 24 | 2024-05-18 | credit | 28499994 | 89791851.85 | 118291845.85 | `recurring:salary` | recurring | `event_2183`, `event_2191`, `event_2199` | - | history supports a fixed 31-day recurrence | - | - |
| 25 | 2024-05-31 | debit | -6954000 | 118291845.85 | 111337845.85 | `recurring:rent` | recurring | `event_2192`, `event_2200`, `event_2207` | - | history supports a fixed 30-day recurrence | - | - |

First recommended-plan breach: none.
