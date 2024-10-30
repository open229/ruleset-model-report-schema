# RulesetModelOptions2019T24Com
|    Enumerator     |                 Description                 | Notes |
| ----------------- | ------------------------------------------- | ----- |
| `PROPOSED_SIZING` | The proposed building model used for sizing |       |
| `BASELINE_SIZING` | The baseline building model used for sizing |       |
| `BASELINE`        | The baseline building model                 |       |

# RulesetModelOptions2019T24Res
| Enumerator |                             Description                              | Notes |
| ---------- | -------------------------------------------------------------------- | ----- |
| `USER`     | The building model as described without consideration of the ruleset |       |
| `PROPOSED` | The proposed building model                                          |       |
| `STANDARD` | The standard building model                                          |       |
| `BASELINE` | The baseline building model                                          |       |

# ConstructionClassificationOptions2019T24
|  Enumerator   | Description |                                                      Notes                                                       |
| ------------- | ----------- | ---------------------------------------------------------------------------------------------------------------- |
| `MASS_LIGHT`  | Mass, light | Light mass walls are walls with a heat capacity of at least 7.0 Btu/ft^2^-^o^F and less than 15.0 Btu/ft^2^-^o^F |
| `MASS_HEAVY`  | Mass, heavy | Heavy mass walls are walls with a heat capacity of at least 15.0 Btu/ft^2^-^o^F                                  |
| `RAISED_MASS` | Raised mass | Heavy mass walls are walls with a heat capacity of at least 15.0 Btu/ft^2^-^o^F                                  |

# ServiceWaterHeatingDistributionCompactnessOptions2019T24Com
|    Enumerator     |   Description   | Notes |
| ----------------- | --------------- | ----- |
| `NOT_COMPACT`     | Not compact     |       |
| `BASIC_COMPACT`   | Basic compact   |       |
| `EXPANDED_CREDIT` | Expanded credit |       |
| `OTHER`           | Other           |       |

# ServiceWaterHeatingControlOptions2019T24Com
|               Enumerator                |              Description              | Notes |
| --------------------------------------- | ------------------------------------- | ----- |
| `DEMAND_CONTROL`                        | Demand control                        |       |
| `NO_CONTROL`                            | No control                            |       |
| `NO_LOOP_OR_CENTRAL_SYSTEM_PUMP`        | No loop or central system pump        |       |
| `TEMPERATURE_MODULATION`                | Temperature modulation                |       |
| `TEMPERATURE_MODULATION_AND_MONITORING` | Temperature modulation and monitoring |       |
| `OTHER`                                 | Other                                 |       |

# OutputSchemaOptions2019T24
|           Enumerator            |              Description               | Notes |
| ------------------------------- | -------------------------------------- | ----- |
| `OUTPUT_SCHEMA_T24_RESIDENTIAL` | Output schema for Title 24 Residential |       |
| `OUTPUT_SCHEMA_T24_COMMERCIAL`  | Output schema for Title 24 Commercial  |       |

