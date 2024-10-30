# EndUseOptions
|            Enumerator            |          Description           | Notes |
| -------------------------------- | ------------------------------ | ----- |
| `INTERIOR_LIGHTING`              | Interior lighting              |       |
| `EXTERIOR_LIGHTING`              | Exterior lighting              |       |
| `SPACE_HEATING`                  | Space heating                  |       |
| `HEAT_PUMP_SUPPLEMENTAL_HEATING` | Heat pump supplemental heating |       |
| `SPACE_COOLING`                  | Space cooling                  |       |
| `PUMPS`                          | Pumps                          |       |
| `HEAT_REJECTION`                 | Heat rejection                 |       |
| `FANS_INTERIOR_VENTILATION`      | Fans - interior ventilation    |       |
| `FANS_PARKING_GARAGE`            | Fans - parking garage          |       |
| `HUMIDIFICATION`                 | Humidification                 |       |
| `HEAT_RECOVERY`                  | Heat recovery                  |       |
| `SERVICE_WATER_HEATING`          | Service water heating          |       |
| `MOTORS`                         | Motors                         |       |
| `TRANSFORMERS`                   | Transformers                   |       |
| `OFFICE_EQUIPMENT`               | Office equipment               |       |
| `COMPUTERS_SERVERS`              | Computers and servers          |       |
| `COMMERCIAL_COOKING`             | Commercial cooking             |       |
| `MISC_EQUIPMENT`                 | Misc equipment                 |       |
| `INDUSTRIAL_PROCESS`             | Industrial process             |       |
| `REFRIGERATION_EQUIPMENT`        | Refrigeration equipment        |       |
| `ELEVATORS_ESCALATORS`           | Elevators and escalators       |       |
| `OTHER`                          | Other                          |       |

# EnergySourceOptions
|        Enumerator         |       Description       |             Notes              |
| ------------------------- | ----------------------- | ------------------------------ |
| `ELECTRICITY`             | Electricity             |                                |
| `NATURAL_GAS`             | Natural gas             |                                |
| `PROPANE`                 | Propane                 |                                |
| `FUEL_OIL`                | Fuel oil                |                                |
| `STEAM`                   | Steam                   |                                |
| `PURCHASED_HOT_WATER`     | Purchased hot water     |                                |
| `PURCHASED_CHILLED_WATER` | Purchased chilled water |                                |
| `ON_SITE_RENEWABLES`      | On-site renewables      | Used primarily in AnnualResult |
| `OTHER`                   | Other                   |                                |

# Output2019ASHRAE901
|                               Name                               |                                 Description                                  |     Data Type      | Units | Range | Req |                                                                    Notes                                                                     |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------------- | ------------------ | ----- | ----- | --- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                             | Scope-unique reference identifier for instances of this data group.          | `ID`               |       |       | ✓   |                                                                                                                                              |
| `reporting_name`                                                 | Descriptive name used in RCT reports if id is not already a descriptive name | `String`           |       |       |     |                                                                                                                                              |
| `notes`                                                          | Supplementary information to provide context to the model reviewer           | `String`           |       |       |     |                                                                                                                                              |
| `output_instance`                                                | References output that correspond to specific simulation model.              | `{OutputInstance}` |       |       |     | A seperate file is expected for each simulation model including outputs that correspond with building rotations.                             |
| `performance_cost_index`                                         | Performance cost index for the project                                       | `Numeric`          |       |       |     | This output is appropriate for the overall project not specific instance of a model.                                                         |
| `baseline_building_unregulated_energy_cost`                      | baseline building unregulated energy cost.                                   | `Numeric`          |       |       |     | The units are the local monetary units such as dollars. This output is appropriate for the overall project not specific instance of a model. |
| `baseline_building_regulated_energy_cost`                        | baseline building regulated energy cost.                                     | `Numeric`          |       |       |     | The units are the local monetary units such as dollars. This output is appropriate for the overall project not specific instance of a model. |
| `baseline_building_performance_energy_cost`                      | baseline building performance energy cost.                                   | `Numeric`          |       |       |     | The units are the local monetary units such as dollars. This output is appropriate for the overall project not specific instance of a model. |
| `total_area_weighted_building_performance_factor`                | Total area weighted building performance factor                              | `Numeric`          |       |       |     | This output is appropriate for the overall project not specific instance of a model.                                                         |
| `performance_cost_index_target`                                  | Performance cost index target for the project                                | `Numeric`          |       |       |     | This output is appropriate for the overall project not specific instance of a model.                                                         |
| `total_proposed_building_energy_cost_including_renewable_energy` | Total proposed building energy cost including renewable energy.              | `Numeric`          |       |       |     | The units are the local monetary units such as dollars. This output is appropriate for the overall project not specific instance of a model. |
| `total_proposed_building_energy_cost_excluding_renewable_energy` | Total proposed building energy cost excluding renewable energy.              | `Numeric`          |       |       |     | The units are the local monetary units such as dollars. This output is appropriate for the overall project not specific instance of a model. |
| `percent_renewable_energy_savings`                               | Percent renewable energy savings                                             | `Numeric`          |       |       |     | This output is appropriate for the overall project not specific instance of a model.                                                         |

# OutputInstance
|                Name                 |                                    Description                                    |              Data Type               | Units |   Range    | Req |                                                                  Notes                                                                  |
| ----------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------ | ----- | ---------- | --- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                | Scope-unique reference identifier for instances of this data group.               | `ID`                                 |       |            | ✓   |                                                                                                                                         |
| `reporting_name`                    | Descriptive name used in RCT reports if id is not already a descriptive name      | `String`                             |       |            |     |                                                                                                                                         |
| `notes`                             | Supplementary information to provide context to the model reviewer                | `String`                             |       |            |     |                                                                                                                                         |
| `ruleset_model_type`                | Describes the current model instance for rulesets with multiple simulation models | `<RulesetModelOptions2019ASHRAE901>` |       |            |     |                                                                                                                                         |
| `rotation_angle`                    | Rotation angle of the building model.                                             | `Numeric`                            |       | `≥0, <360` |     | Usually 0, 90, 180, or 270.                                                                                                             |
| `unmet_load_hours`                  | Unmet load hours for heating and cooling                                          | `Numeric`                            | hr    |            | ✓   | This would be the coincident unmet load hours so if the same hour is during heating and during cooling it would only count as one hour. |
| `unmet_load_hours_heating`          | Unmet load hours for heating                                                      | `Numeric`                            | hr    |            | ✓   |                                                                                                                                         |
| `unmet_occupied_load_hours_heating` | Unmet load hours for heating when the zone is occupied                            | `Numeric`                            | hr    |            | ✓   |                                                                                                                                         |
| `unmet_load_hours_cooling`          | Unmet load hours for cooling                                                      | `Numeric`                            | hr    |            | ✓   |                                                                                                                                         |
| `unmet_occupied_load_hours_cooling` | Unmet load hours for cooling when the zone is occupied                            | `Numeric`                            | hr    |            | ✓   |                                                                                                                                         |
| `annual_source_results`             | Annual results by source                                                          | `[{SourceResult}]`                   |       |            |     | Contains a list of results by energy source.                                                                                            |
| `building_peak_cooling_load`        | Building peak cooling load                                                        | `Numeric`                            | W     |            | ✓   |                                                                                                                                         |
| `annual_end_use_results`            | Annual end use results                                                            | `[{EndUseResult}]`                   |       |            |     | Contains a list of results by end use and energy source.                                                                                |

# SourceResult
|         Name         |                                 Description                                  |        Data Type        | Units | Range | Req |                                                        Notes                                                         |
| -------------------- | ---------------------------------------------------------------------------- | ----------------------- | ----- | ----- | --- | -------------------------------------------------------------------------------------------------------------------- |
| `id`                 | Scope-unique reference identifier for instances of this data group.          | `ID`                    |       |       | ✓   |                                                                                                                      |
| `reporting_name`     | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                |       |       |     |                                                                                                                      |
| `notes`              | Supplementary information to provide context to the model reviewer           | `String`                |       |       |     |                                                                                                                      |
| `energy_source`      | End use type                                                                 | `<EnergySourceOptions>` |       |       | ✓   |                                                                                                                      |
| `annual_consumption` | Annual energy consumption                                                    | `Numeric`               | J     |       | ✓   | For energy_source ON_SITE_RENEWABLES this value is negative.                                                         |
| `annual_demand`      | Annual site demand                                                           | `Numeric`               | J     |       | ✓   | This corresponds to the coincident demand for end-use results.                                                       |
| `annual_cost`        | Annual cost                                                                  | `Numeric`               |       |       | ✓   | The units are the local monetary units such as dollars. For energy_source ON_SITE_RENEWABLES this value is negative. |

# EndUseResult
|                Name                 |                                 Description                                  |        Data Type        | Units | Range | Req | Notes |
| ----------------------------------- | ---------------------------------------------------------------------------- | ----------------------- | ----- | ----- | --- | ----- |
| `id`                                | Scope-unique reference identifier for instances of this data group.          | `ID`                    |       |       | ✓   |       |
| `reporting_name`                    | Descriptive name used in RCT reports if id is not already a descriptive name | `String`                |       |       |     |       |
| `notes`                             | Supplementary information to provide context to the model reviewer           | `String`                |       |       |     |       |
| `type`                              | End use type                                                                 | `<EndUseOptions>`       |       |       | ✓   |       |
| `energy_source`                     | End source                                                                   | `<EnergySourceOptions>` |       |       | ✓   |       |
| `annual_site_energy_use`            | Annual site energy use                                                       | `Numeric`               | J     |       | ✓   |       |
| `annual_site_coincident_demand`     | Annual site coincident demand                                                | `Numeric`               | J     |       | ✓   |       |
| `annual_site_non_coincident_demand` | Annual site non-coincident demand                                            | `Numeric`               | J     |       | ✓   |       |
| `is_regulated`                      | Indicates whether the end use consumption is from regulated equipment        | `Boolean`               |       |       |     |       |

