# Data Types
| Data Type |                                                     Description                                                      | JSON Schema Type |          Examples           |
|-----------|----------------------------------------------------------------------------------------------------------------------|------------------|-----------------------------|
| `Integer` | A positive or negative whole number (i.e., a number that can be written without a fractional part).                  | integer          | 3, 19, -4                   |
| `Numeric` | A number that may include a fractional part with optional leading sign and optional exponent (engineering notation). | number           | 3.43, 0, -4, 1.03e4         |
| `Boolean` | True or false.                                                                                                       | boolean          | true, false                 |
| `String`  | A sequence of characters of any length using any (specified) character set.                                          | string           | Indirect evaporative cooler |
| `Null`    | Indicator that no value is provided. Only used in combination with other data types, e.g., 'Number/Null'.            | null             | null                        |

# ConditioningType
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `HEATED_AND_COOLED` | Heated and cooled |       |
| `HEATED_ONLY`       | Heated only       |       |
| `SEMIHEATED`        | Semiheated        |       |
| `UNCONDITIONED`     | Unconditioned     |       |
| `PLENUM`            | Plenum            |       |

# SpaceFunctionType
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `LABORATORY` | Laboratory  |       |
| `KITCHEN`    | Kitchen     |       |
| `OTHER`      | Other       |       |

# InfiltrationMethodType
|    Enumerator    |                                                                                              Description                                                                                              | Notes |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| `WEATHER_DRIVEN` | Weather Driven. The amount of air leakage is determined by a correlation usually involving windspeed, height, and the difference between indoor and outdoor temperature.                              |       |
| `PRESSURE_BASED` | Pressure Based. The amount of air leakage is determined by induced airflows from pressure differences between zones, air distribution system components, the outside due to wind speed and direction. |       |
| `CONSTANT`       | Constant. The amount of air leakage is fixed.                                                                                                                                                         |       |

# SurfaceClassificationType
| Enumerator |           Description            | Notes |
|------------|----------------------------------|-------|
| `WALL`     | Vertical or nearly vertical wall |       |
| `FLOOR`    | Floor                            |       |
| `CEILING`  | Ceiling                          |       |

# SurfaceAdjacentTo
| Enumerator  |                                                                                                 Description                                                                                                  | Notes |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| `EXTERIOR`  | Exterior wall or roof which is adjacent to the exterior environment.                                                                                                                                         |       |
| `GROUND`    | Slab-on-grad or below grade surface if adjacent to ground.                                                                                                                                                   |       |
| `INTERIOR`  | Interior surface if adjacent to another space which is explicity modeled.                                                                                                                                    |       |
| `IDENTICAL` | Surface adjacent to a environment identical to the space. Sometimes this is described as adiabatic surface since no heat is transfered. The space on the other side of the surface is not explicity modeled. |       |
| `UNDEFINED` | The surface adjacency cannot be determined by the software.                                                                                                                                                  |       |

# SurfaceConstructionInputOptions
|  Enumerator  |               Description                | Notes |
|--------------|------------------------------------------|-------|
| `LAYERS`     | Construction is entered layer-by-layer.  |       |
| `SIMPLIFIED` | Construction is entered by R-value only. |       |

# FenestrationClassificationType
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `WINDOW`   | Window      |       |
| `SKYLIGHT` | Skylight    |       |
| `DOOR`     | Door        |       |

# MiscellaneousEquipmentType
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `PLUG`     | Plug        |       |
| `PROCESS`  | Process     |       |
| `OTHER`    | Other       |       |

# TransformerType
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `DRY_TYPE`     | Dry Type     |       |
| `FLUID_FILLED` | Fluid Filled |       |
| `OTHER`        | Other        |       |

# ElectricalPhase
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `SINGLE_PHASE` | Single Phase |       |
| `THREE_PHASE`  | Three Phase  |       |

# ScheduleSequenceTypeOptions
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `HOURLY`   | Hourly      |       |
| `EVENT`    | Event       |       |

# ScheduleTypeOptions
|         Enumerator         |       Description        | Notes |
|----------------------------|--------------------------|-------|
| `MULTIPLIER_DIMENSIONLESS` | Multiplier dimensionless |       |
| `TEMPERATURE`              | Temperature              |       |
| `POWER`                    | Power                    |       |
| `FLOW_RATE`                | Flow rate                |       |

# DayOfWeek
| Enumerator  | Description | Notes |
|-------------|-------------|-------|
| `SUNDAY`    | Sunday      |       |
| `MONDAY`    | Monday      |       |
| `TUESDAY`   | Tuesday     |       |
| `WEDNESDAY` | Wednesday   |       |
| `THURSDAY`  | Thursday    |       |
| `FRIDAY`    | Friday      |       |
| `SATURDAY`  | Saturday    |       |

# FluidLoopTypeOptions
|      Enumerator       |     Description     | Notes |
|-----------------------|---------------------|-------|
| `HEATING`             | Heating             |       |
| `COOLING`             | Cooling             |       |
| `HEATING_AND_COOLING` | Heating and cooling |       |
| `CONDENSER`           | Condenser           |       |
| `OTHER`               | Other               |       |

# TemperatureResetTypeOptions
|     Enumerator      |    Description    | Notes |
|---------------------|-------------------|-------|
| `NO_RESET`          | No Reset          |       |
| `CONSTANT`          | Constant          |       |
| `OUTSIDE_AIR_RESET` | Outside air reste |       |
| `LOAD_RESET`        | Load Reset        |       |
| `OTHER`             | Other             |       |

# FluidLoopOperationOptions
|   Enumerator   | Description  | Notes |
|----------------|--------------|-------|
| `CONTINUOUS`   | Continuous   |       |
| `INTERMITTENT` | Intermittent |       |

# PumpSpeedControlOptions
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `FIXED_SPEED`    | Fixed speed    |       |
| `TWO_SPEED`      | Two speed      |       |
| `VARIABLE_SPEED` | Variable speed |       |

# PumpFlowControlOptions
|    Enumerator    |  Description  | Notes |
|------------------|---------------|-------|
| `FIXED_FLOW`     | Fixed flow    |       |
| `VARIABLE_SPEED` | Variable flow |       |

# PumpSpecificationMethodOptions
| Enumerator | Description |                                         Notes                                          |
|------------|-------------|----------------------------------------------------------------------------------------|
| `SIMPLE`   | Simple      | Specify the electric power input of pump                                               |
| `DETAILED` | Detailed    | Specify the motor nameplate power, design head, impelllor efficiency, motor efficiency |

# BoilerCombustionOptions
| Enumerator | Description | Notes |
|------------|-------------|-------|
| `NATURAL`  | Natural     |       |
| `FORCED`   | Forced      |       |

# BoilerEfficiencyMetricTypeOptions
|        Enumerator         |            Description             | Notes |
|---------------------------|------------------------------------|-------|
| `ANNUAL_FUEL_UTILIZATION` | Annual fuel utilization efficiency |       |
| `THERMAL`                 | Thermal efficiency                 |       |
| `COMBUSION`               | Combustion efficiency              |       |

# ChillerCompressorTypeOptions
|                Enumerator                 |               Description               | Notes |
|-------------------------------------------|-----------------------------------------|-------|
| `SCREW`                                   | Screw                                   |       |
| `CENTRIFUGAL`                             | Centrifugal                             |       |
| `RECIPROCATING`                           | Reciprocating                           |       |
| `SCROLL`                                  | Scroll                                  |       |
| `POSITIVE_DISPLACEMENT`                   | Positive displacement                   |       |
| `SINGLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Single-effect indirect-fired absorption |       |
| `DOUBLE_EFFECT_INDIRECT_FIRED_ABSORPTION` | Double-effect indirect-fired absorption |       |
| `SINGLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Single-effect direct-fired absorption   |       |
| `DOUBLE_EFFECT_DIRECT_FIRED_ABSORPTION`   | Double-effect direct-fired absorption   |       |
| `OTHER`                                   | Other                                   |       |

# HeatRejectionTypeOptions
|           Enumerator           |                 Description                  | Notes |
|--------------------------------|----------------------------------------------|-------|
| `OPEN_CIRCUIT_COOLING_TOWER`   | Open-circuit cooling tower                   |       |
| `CLOSED_CIRCUIT_COOLING_TOWER` | Closed-circuit cooling tower or fluid cooler |       |
| `DRY_COOLER`                   | Dry-cooler or air-cooled fluid cooler        |       |
| `EVAPORATIVE_CONDENSER`        | Evaporative condenser                        |       |
| `AIR_COOLED_CONDENSER`         | Air cooled condenser                         |       |
| `OTHER`                        | Other                                        |       |

# HeatRejectionFanTypeOptions
|  Enumerator   |    Description     | Notes |
|---------------|--------------------|-------|
| `AXIAL`       | Axial or Propellor |       |
| `CENTRIFUGAL` | Centrifugal        |       |
| `OTHER`       | Other              |       |

# HeatRejectionFluidOptions
|  Enumerator   | Description |      Notes       |
|---------------|-------------|------------------|
| `WATER`       | Water       |                  |
| `REFRIGERANT` | Refrigerant | Including R-448A |
| `AMMONIA`     | Ammonia     |                  |
| `OTHER`       | Other       |                  |

# HeatRejectionResetOptions
|  Enumerator  | Description | Notes |
|--------------|-------------|-------|
| `CONSTANT`   | Constant    |       |
| `LOAD_RESET` | Load reset  |       |
| `OTHER`      | Other       |       |

# HeatRejectionFanSpeedControlOptions
|    Enumerator    |  Description   | Notes |
|------------------|----------------|-------|
| `CONSTANT`       | Constant       |       |
| `TWO_SPEED`      | Two Speed      |       |
| `VARIABLE_SPEED` | Variable Speed |       |
| `OTHER`          | Other          |       |

# ExternalFluidSourceTypeOptions
|   Enumerator    |  Description  | Notes |
|-----------------|---------------|-------|
| `CHILLED_WATER` | Chilled water |       |
| `HOT_WATER`     | Hot water     |       |
| `STEAM`         | Steam         |       |

# ServiceWaterHeatingEnteringWaterTemperatureInputOptions
|    Enumerator    |                   Description                    | Notes |
|------------------|--------------------------------------------------|-------|
| `ANNUAL_MAIN`    | Annual main entering water temperature option    |       |
| `MONTHLY_MAIN`   | Monthly main entering water temperature option   |       |
| `ANNUAL_GROUND`  | Annual ground entering water temperature option  |       |
| `MONTHLY_GROUND` | Monthly ground entering water temperature option |       |

# FuelTypeOptions
|  Enumerator   | Description | Notes |
|---------------|-------------|-------|
| `ELECTRICITY` | Electricity |       |
| `NATURAL_GAS` | Natural gas |       |
| `OTHER`       | Other       |       |

# ASHRAE229
|                Name                |                                           Description                                           |                              Data Type                              |  Units  | Range | Req |                                                                             Notes                                                                              |
|------------------------------------|-------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|---------|-------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `transformers`                     | Electrical transformers at the building site                                                    | `[{Transformer}]`                                                   |         |       |     | Contains a list of transformers that convert electricity from a higher voltage to one used by the building, exterior lighting, and other services at the site. |
| `buildings`                        | Buildings on the site                                                                           | `[{Building}]`                                                      |         |       |     | Contains a list of buildings on the site (often just one).                                                                                                     |
| `calendar`                         | Information on the calendar used with the simulation.                                           | `{Calendar}`                                                        |         |       |     |                                                                                                                                                                |
| `schedules`                        | Schedules for internal loads, thermostats, equipment operation and control, and any other need. | `[{Schedule}]`                                                      |         |       |     | Contains a list of schedules used in model.                                                                                                                    |
| `weather`                          | Information on the local weather conditions used with the simulation.                           | `{Weather}`                                                         |         |       |     |                                                                                                                                                                |
| `infiltration_pressure_difference` | Differential pressure difference assumed for infiltration values.                               | `Numeric`                                                           | Pa      | `≥0`  |     | Often 50 Pa or 75 Pa and used as rating conditions for air leakage for a building.                                                                             |
| `overall_simulation_outputs`       | Outputs from the simluation summed for all buildings in the simulation.                         | `{OverallSimulationOutputs}`                                        |         |       |     |                                                                                                                                                                |
| `building_rotation_angles`         | A list of angles that building simulations are performed and results are provided.              | `[Numeric]`                                                         | degrees |       |     | List of angles that the building has been rotated.                                                                                                             |
| `fluid_loops`                      | Fluid loops on the site                                                                         | `[{FluidLoop}]`                                                     |         |       |     | Contains a list of fluid loops on the site.                                                                                                                    |
| `conditioning_components`          | Links to all conditioning components used on the site                                           | `[{Pump},{Boiler},{Chiller},{HeatRejection}, {DistrictFluidMeter}]` |         |       |     | Contains a list of fluid loops on the site.                                                                                                                    |

# Building
|            Name            |                                                                  Description                                                                  |              Data Type              | Units |   Range   | Req |                                                                                                                   Notes                                                                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|-------|-----------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                       | Unique Identification Number                                                                                                                  | `Numeric`                           |       |           | ✓   |                                                                                                                                                                                                                                           |
| `name`                     | Name of the Building                                                                                                                          | `String`                            |       |           | ✓   |                                                                                                                                                                                                                                           |
| `number_of_floors`         | Number of floors                                                                                                                              | `Numeric`                           |       | `≥0`      |     |                                                                                                                                                                                                                                           |
| `building_segments`        | Large portions of a building that share a building area type                                                                                  | `[{BuildingSegment}]`               |       |           |     | Contains a list of building segments in the building.                                                                                                                                                                                     |
| `is_all_new`               | Indicates whether building is completely new construction (true) or existing (false).                                                         | `Boolean`                           |       |           |     | Projects that include additions should be False. Projects with additional instead may be modeled as two buildings - one new and one existing, as curtain rules such as baseline fenestration area will apply differently to each portion. |
| `compliance_path`          | Indicates the chosen compliance path if the ruleset has multiple compliance paths such as 90.1 Appendix G has code compliance and beyond code | `<CompliancePathType2019ASHRAE901>` |       |           |     |                                                                                                                                                                                                                                           |
| `elevators`                | Elevators                                                                                                                                     | `[{Elevator}]`                      |       |           |     | Contains a list of elevators in the building.                                                                                                                                                                                             |
| `refrigeration_components` | Refrigeration                                                                                                                                 | `[{Refrigeration}]`                 |       |           |     | Contains a list of refrigeration components in the building.                                                                                                                                                                              |
| `open_time`                | Time that the building opens.                                                                                                                 | `Numeric`                           |       | `≥1, ≤24` |     | The general time that the building is first opened during normal weekdays from 1 to 24                                                                                                                                                    |
| `close_time`               | Time that the building closes.                                                                                                                | `Numeric`                           |       | `≥1, ≤24` |     | The general time that the building is closed during normal weekdays from 1 to 24                                                                                                                                                          |

# BuildingSegment
|                      Name                      |                         Description                         |                       Data Type                       | Units | Range | Req |                               Notes                               |
|------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------|-------|-------|-----|-------------------------------------------------------------------|
| `id`                                           | Unique Identification Number                                | `Numeric`                                             |       |       | ✓   |                                                                   |
| `name`                                         | Name of the Building Segment                                | `String`                                              |       |       | ✓   |                                                                   |
| `thermal_blocks`                               | Thermal blocks in the building                              | `[{ThermalBlock}]`                                    |       |       |     | Contains a list of thermal blocks in the building.                |
| `heating_ventilation_air_conditioning_systems` | HVAC systems in the building                                | `[{HeatingVentilationAirConditioningSystem}]`         |       |       |     | Contains a list of HVAC systems in the building.                  |
| `service_water_heating_systems`                | Service water heating systems in the building               | `[{ServiceWaterHeatingSystem}]`                       |       |       |     | Contains a list of service water heating systems in the building. |
| `area_type_vertical_fenestration`              | Building area classification used for vertical fenestration | `<VerticalFenestrationBuildingAreaType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used.                    |
| `lighting_building_area_type`                  | Building area lighting area type                            | `<LightingSpaceType2019ASHRAE901T951TG38>`            |       |       |     |                                                                   |

# ThermalBlock
|                           Name                           |                       Description                        | Data Type  | Units | Range | Req |                                                                        Notes                                                                         |
|----------------------------------------------------------|----------------------------------------------------------|------------|-------|-------|-----|------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                                     | Unique Identification Number                             | `Numeric`  |       |       | ✓   |                                                                                                                                                      |
| `name`                                                   | Name of the thermal block                                | `String`   |       |       | ✓   |                                                                                                                                                      |
| `zones`                                                  | Zones in the building                                    | `[{Zone}]` |       |       |     | Contains a list of zones in the building.                                                                                                            |
| `served_by_heating_ventilation_air_conditioning_systems` | HVAC systems serving the thermal block                   | `[String]` |       |       |     | Contains a list of IDs of the HVAC systems serving the thermal block - from Unique Identification Number in HeatingVentilationAirConditioningSystem. |
| `served_by_service_water_heating_system`                 | A service water heating system serving the thermal block | `String`   |       |       |     | Contains a single ID of the service water heating system serving the thermal block - from Unique Identification Number in ServiceWaterHeatingSystem. |

# Zone
|      Name      |          Description          |    Data Type     | Units | Range | Req |                       Notes                       |
|----------------|-------------------------------|------------------|-------|-------|-----|---------------------------------------------------|
| `id`           | Unique Identification Number  | `Numeric`        |       |       | ✓   |                                                   |
| `name`         | Name of the Zone              | `String`         |       |       | ✓   |                                                   |
| `spaces`       | Spaces in the building        | `[{Space}]`      |       |       |     | Contains a list of spaces in the building.        |
| `volume`       | Volume of the space           | `Numeric`        | m3    | `≥0`  |     |                                                   |
| `surfaces`     | Surfaces surrounding the zone | `[{Surface}]`    |       |       |     | Contains a list of surfaces that define the zone. |
| `infiltration` | Airleakage into the space.    | `{Infiltration}` |       |       |     | References a single infiltration data group.      |

# Space
|                Name                 |                                                                                                                                                                                                                                               Description                                                                                                                                                                                                                                               |                   Data Type                   | Units | Range | Req |                     Notes                      |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------|-------|-------|-----|------------------------------------------------|
| `id`                                | Unique Identification Number                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `Numeric`                                     |       |       | ✓   |                                                |
| `name`                              | Name of the Space                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `String`                                      |       |       | ✓   |                                                |
| `interior_lighting`                 | Internal lighting that produce internal gains for a space.                                                                                                                                                                                                                                                                                                                                                                                                                                              | `[{InteriorLighting}]`                        |       |       |     |                                                |
| `miscellaneous_equipment`           | Miscellaneous equipment loads that produce internal gains for a space.                                                                                                                                                                                                                                                                                                                                                                                                                                  | `[{MiscellaneousEquipment}]`                  |       |       |     |                                                |
| `floor_area`                        | The floor area of a space within the building, including basements, mezzanine and intermediate-floored tiers, and penthouses with a headroom height of 7.5 ft or greater. It is measured from the exterior faces of walls or from the center-line of walls separating buildings, but excluding covered walkways, open roofed-over areas, porches and similar spaces, pipe trenches, exterior terraces or steps, chimneys, roof overhangs, and similar features. This is the floor area that is modeled. | `Numeric`                                     | m2    | `≥0`  |     |                                                |
| `number_of_occupants`               | Number of occupants in the space                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `Numeric`                                     |       | `≥0`  |     |                                                |
| `occupant_multiplier_schedule_name` | Number of occupant multiplier schedule name                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `String`                                      |       |       |     |                                                |
| `conditioning_type`                 | Space conditioning category                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | `<ConditioningType>`                          |       |       |     |                                                |
| `status_type`                       | Choice of new, existing, addition, or alteration.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `<SpaceStatusType2019ASHRAE901>`              |       |       |     |                                                |
| `space_function`                    | Generic function for the space.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `<SpaceFunctionType>`                         |       |       |     | The enumeration is based on the standard used. |
| `lighting_space_type`               | Lighting space type classification                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `<LightingSpaceType2019ASHRAE901TG37>`        |       |       |     | The enumeration is based on the standard used. |
| `ventilations_space_type`           | Ventilation space type classification                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `<VentilationSpaceType2019ASHRAE901>`         |       |       |     | The enumeration is based on the standard used. |
| `service_water_heating_space_type`  | Service water heating space type classification                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `<ServiceWaterHeatingSpaceType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used. |

# Infiltration
|            Name            |                        Description                        |         Data Type          | Units | Range | Req |                                     Notes                                      |
|----------------------------|-----------------------------------------------------------|----------------------------|-------|-------|-----|--------------------------------------------------------------------------------|
| `id`                       | Unique Identification Number                              | `Numeric`                  |       |       | ✓   |                                                                                |
| `name`                     | Name of the Infiltration data group                       | `String`                   |       |       | ✓   |                                                                                |
| `modeling_method`          | The software methodology chosen for modeling infiltration | `<InfiltrationMethodType>` |       |       |     |                                                                                |
| `air_leakage_rate`         | Air leakage rate from infiltration of outside air         | `Numeric`                  | m3/s  | `≥0`  |     | Based on the pressure described in ASHRAE229.infiltration_pressure_difference. |
| `multiplier_schedule_name` | Infiltration multiplier schedule name                     | `String`                   |       |       |     |                                                                                |

# Surface
|             Name             |                                                               Description                                                                |                                               Data Type                                                |  Units  | Range | Req |                                                    Notes                                                     |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|---------|-------|-----|--------------------------------------------------------------------------------------------------------------|
| `id`                         | Unique Identification Number                                                                                                             | `Numeric`                                                                                              |         |       | ✓   |                                                                                                              |
| `name`                       | Name of the Surface                                                                                                                      | `String`                                                                                               |         |       | ✓   |                                                                                                              |
| `fenestration_subsurfaces`   | Fenestration suburfaces that are on the surface                                                                                          | `[{Fenestration}]`                                                                                     |         |       |     | Contains a list of surfaces that define the space.                                                           |
| `classification`             | Classification for the surface.                                                                                                          | `<SurfaceClassificationType>`                                                                          |         |       |     | Options for surface being interior or exterior wall, floor, or ceiling.                                      |
| `area`                       | area of the surface                                                                                                                      | `Numeric`                                                                                              | m2      | `≥0`  |     | Measured from interior face area. It is the gross area of the wall and includes the area of all subsurfaces. |
| `tilt`                       | Angle between vertical and the surface outward normal                                                                                    | `Numeric`                                                                                              | degrees |       |     | Example value would be 0 = roof, 90 = wall, 180 = downward facing surface (exterior floor)                   |
| `azimuth`                    | Clockwise angle between North and the horizontal projection of the wall's outward normal.                                                | `Numeric`                                                                                              | degrees | `≥0`  |     | Example values would be 0 = north, 90 = East, 180 = South, 270 = West                                        |
| `adjacent_to`                | Used to classify the conditions on the surface.                                                                                          | `(<SurfaceAdjacentTo>,<AdditionalSurfaceAdjacentToRESNET>,<AdditionalSurfaceAdjacentTo2019ASHRAE901>)` |         |       |     | Determines whether the other side of the surface is modeled and if not what assumptions should be used.      |
| `adjacent_zone_id`           | ID of the adjacent zone for interior surface. Only required when adjacent zone is explicity modeled when adjacent_to is set to INTERIOR. | `String`                                                                                               |         |       |     |                                                                                                              |
| `does_cast_shade`            | Determines whether the surface is modeled as casting shade on other exterior surfaces                                                    | `Boolean`                                                                                              |         |       |     |                                                                                                              |
| `construction`               | Construction description of surface.                                                                                                     | `{Construction}`                                                                                       |         |       |     |                                                                                                              |
| `surface_optical_properties` | Optical properties of the surface.                                                                                                       | `{SurfaceOpticalProperties}`                                                                           |         |       |     |                                                                                                              |

# Construction
|                Name                 |                                           Description                                           |              Data Type              | Units  |  Range  | Req |                                                                                                  Notes                                                                                                   |
|-------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------|--------|---------|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                | Unique Identification Number                                                                    | `Numeric`                           |        |         | ✓   |                                                                                                                                                                                                          |
| `name`                              | Name of the Construction                                                                        | `String`                            |        |         | ✓   |                                                                                                                                                                                                          |
| `surface_construction_input_option` | Identifies whether construction is entered layer-by-layer or simplified (R-value)               | `<SurfaceConstructionInputOptions>` |        |         |     |                                                                                                                                                                                                          |
| `fraction_framing`                  | Fraction of the construction that is framing.                                                   | `Numeric`                           |        | `≥0,≤1` |     | Fraction of the construction using framing_layers, the remaining portion uses the primary_layers. If blank, assume zero framing.                                                                         |
| `primary_layers`                    | List of names of layer descriptions starting from the outside surface for primary heat path     | `[{Material}]`                      |        |         |     | For constructions with framing and cavity heat transfer paths, use this for the cavity. For homogeneous constructions, use this element only. Air films should not be included in the list of layers.    |
| `framing_layers`                    | List of names of layer descriptions starting from the outside surface for the framing heat path | `[{Material}]`                      |        |         |     | For constructions with framing and cavity heat transfer paths, use this for the framing. For homogeneous constructions, do not use this element. Air films should not be included in the list of layers. |
| `insulation_location`               | The location of the insulation related to the surface                                           | `String`                            |        |         |     |                                                                                                                                                                                                          |
| `u_factor`                          | suface U-factor                                                                                 | `Numeric`                           | W/m2-K | `≥0`    |     | Includes interior and exterior air films as specified by the referenced standard.                                                                                                                        |
| `c_factor`                          | surface C-factor                                                                                | `Numeric`                           | W/m2-K | `≥0`    |     |                                                                                                                                                                                                          |
| `f_factor`                          | surface F-factor                                                                                | `Numeric`                           | W/m-K  | `≥0`    |     |                                                                                                                                                                                                          |
| `r_value`                           | r-value of the insulation for the surface                                                       | `Numeric`                           | K-m2/W | `≥0`    |     |                                                                                                                                                                                                          |
| `has_radiant_heating`               | Includes embedded radiant heating elements                                                      | `Boolean`                           |        |         |     |                                                                                                                                                                                                          |
| `has_radiant_cooling`               | Includes embedded radiant cooling elements                                                      | `Boolean`                           |        |         |     |                                                                                                                                                                                                          |

# Material
|          Name          |                   Description                    | Data Type | Units  | Range | Req |                                                       Notes                                                        |
|------------------------|--------------------------------------------------|-----------|--------|-------|-----|--------------------------------------------------------------------------------------------------------------------|
| `id`                   | Unique Identification Number                     | `Numeric` |        |       | ✓   |                                                                                                                    |
| `name`                 | Name of the Material                             | `String`  |        |       | ✓   |                                                                                                                    |
| `thickness`            | The thickness of the material layer              | `Numeric` | m      | `>0`  |     |                                                                                                                    |
| `thermal_conductivity` | The thermal conductivity of the material layer   | `Numeric` | W/m-K  | `≥0`  |     | When thermal_conductivity is specified, r_value should not be provided.                                            |
| `density`              | The density of the material layer                | `Numeric` | kg/m3  | `≥0`  |     |                                                                                                                    |
| `specific_heat`        | The specific heat of the material layer          | `Numeric` | J/kg-K | `≥0`  |     |                                                                                                                    |
| `r_value`              | r-value of the insulation for the material layer | `Numeric` | K-m2/W | `≥0`  |     | When r_value is specified, thermal_conductivity should not be provided. Typically used for insulation or air gaps. |

# SurfaceOpticalProperties
|              Name              |                                Description                                 | Data Type | Units | Range | Req | Notes |
|--------------------------------|----------------------------------------------------------------------------|-----------|-------|-------|-----|-------|
| `id`                           | Unique Identification Number                                               | `Numeric` |       |       | ✓   |       |
| `name`                         | Name of the surface optics                                                 | `String`  |       |       | ✓   |       |
| `absorptance_thermal_exterior` | Thermal absorptance of long wavelength radiation on the exterior surface.  | `Numeric` |       | `≥0`  |     |       |
| `absorptance_solar_exterior`   | Thermal absorptance of short wavelength radiation on the exterior surface. | `Numeric` |       | `≥0`  |     |       |
| `absorptance_visible_exterior` | Thermal absorptance of visible radiation on the exterior surface.          | `Numeric` |       | `≥0`  |     |       |
| `absorptance_thermal_interior` | Thermal absorptance of long wavelength radiation on the interior surface.  | `Numeric` |       | `≥0`  |     |       |
| `absorptance_solar_interior`   | Thermal absorptance of short wavelength radiation on the interior surface. | `Numeric` |       | `≥0`  |     |       |
| `absorptance_visible_interior` | Thermal absorptance of visible radiation on the interior surface.          | `Numeric` |       | `≥0`  |     |       |

# Fenestration
|                  Name                   |                                        Description                                         |               Data Type                | Units  | Range | Req |                                       Notes                                       |
|-----------------------------------------|--------------------------------------------------------------------------------------------|----------------------------------------|--------|-------|-----|-----------------------------------------------------------------------------------|
| `id`                                    | Unique Identification Number                                                               | `Numeric`                              |        |       | ✓   |                                                                                   |
| `name`                                  | Name of the fenestration subsurface                                                        | `String`                               |        |       | ✓   |                                                                                   |
| `classification`                        | Classification for the fenestration being window, skylight, door.                          | `<FenestrationClassificationType>`     |        |       |     |                                                                                   |
| `is_operable`                           | Identifies whether fenestration can be opened and closed including by pivoting or sliding. | `Boolean`                              |        |       |     |                                                                                   |
| `framing_type`                          | The material of the framing.                                                               | `<FenestrationFrameType2019ASHRAE901>` |        |       |     |                                                                                   |
| `glazed_area`                           | Area of fenestration including glass and transparent surfaces                              | `Numeric`                              | m2     | `≥0`  |     |                                                                                   |
| `opaque_area`                           | Area of fenestration framing for a window or skylight or opaque portion for a door.        | `Numeric`                              | m2     | `≥0`  |     |                                                                                   |
| `u_factor`                              | Overall Fenestration U-factor                                                              | `Numeric`                              | W/m2-K | `≥0`  |     | Includes interior and exterior air films as specified by the referenced standard. |
| `solar_heat_gain_coefficient`           | Fenestration SHGC                                                                          | `Numeric`                              |        | `≥0`  |     |                                                                                   |
| `visible_transmittance`                 | Fenestration VT                                                                            | `Numeric`                              |        | `≥0`  |     |                                                                                   |
| `depth_of_overhang`                     | Distance from the edge of the overhang to the fenestration surface.                        | `Numeric`                              | m      | `≥0`  |     |                                                                                   |
| `has_shading_overhang`                  | Identifies whether fenestration has overhangs                                              | `Boolean`                              |        |       |     |                                                                                   |
| `has_shading_sidefins`                  | Identifies whether fenestration has sidefins                                               | `Boolean`                              |        |       |     |                                                                                   |
| `has_manual_interior_shades`            | Are there manually-operated interior shading such as blinds, curtains or shades            | `Boolean`                              |        |       |     |                                                                                   |
| `solar_transmittance_multiplier_summer` | Solar transmittance multiplier for summer                                                  | `Numeric`                              |        | `≥0`  |     | Often used to account for interior shading such as drapes.                        |
| `solar_transmittance_multiplier_winter` | Solar transmittance multiplier for summer                                                  | `Numeric`                              |        | `≥0`  |     | Often used to account for interior shading such as drapes.                        |
| `has_automatic_shades`                  | Are there automatic interior shading such as blinds, curtains or shades                    | `Boolean`                              |        |       |     |                                                                                   |

# InteriorLighting
|                Name                 |                                Description                                 |              Data Type               | Units | Range | Req |                                Notes                                |
|-------------------------------------|----------------------------------------------------------------------------|--------------------------------------|-------|-------|-----|---------------------------------------------------------------------|
| `id`                                | Unique ID assigned to each interior lighting fixture(s) reported in an RMR | `Numeric`                            |       | `>0`  |     |                                                                     |
| `name`                              | Interior lighting fixture name                                             | `String`                             |       |       |     |                                                                     |
| `purpose_type`                      | Lighting space type classification                                         | `<LightingPurposeType2019ASHRAE901>` |       |       |     | The enumeration is based on the standard used.                      |
| `power_per_area`                    | Total power for lights divided by the area of the space.                   | `Numeric`                            | W/m2  |       |     | When computing the power per area use the area of the entire space. |
| `lighting_multiplier_schedule_name` | Lighting multiplier schedule name                                          | `String`                             |       |       |     |                                                                     |
| `has_occupancy_control`             | Indicates that the lighting has occupancy controls                         | `Boolean`                            |       |       |     |                                                                     |
| `has_daylighting_control`           | Includes daylighting controls                                              | `Boolean`                            |       |       |     |                                                                     |

# MiscellaneousEquipment
|              Name              |                              Description                              |           Data Type            | Units |  Range   | Req |                         Notes                          |
|--------------------------------|-----------------------------------------------------------------------|--------------------------------|-------|----------|-----|--------------------------------------------------------|
| `id`                           | Unique ID assigned to each interior miscellaneous equipment in an RMR | `Numeric`                      |       | `>0`     |     |                                                        |
| `name`                         | Miscellaneous equipment name                                          | `String`                       |       |          |     |                                                        |
| `energy_type`                  | Source of energy for the miscelleous equipment in the space           | `<FuelTypeOptions>`            |       |          |     |                                                        |
| `peak_usage`                   | Peak energy usage per hour by the miscelleous equipment in the space. | `Numeric`                      | W     |          |     |                                                        |
| `multiplier_schedule_name`     | miscelleous equipment in the space multiplier schedule name           | `String`                       |       |          |     |                                                        |
| `sensible_fraction`            | Fraction of energy that is a sensible load on the space.              | `Numeric`                      |       | `≥0, ≤1` |     | Sensible plus latent do not necessarily add up to 1.0. |
| `latent_fraction`              | Fraction of energy that is a latent load on the space.                | `Numeric`                      |       | `≥0, ≤1` |     | Sensible plus latent do not necessarily add up to 1.0. |
| `miscellaneous_equipment_type` | Type of miscellaneous equipment                                       | `<MiscellaneousEquipmentType>` |       |          |     |                                                        |
| `has_automatic_control`        | Indicates that the receptacles have automatic controls                | `Boolean`                      |       |          |     |                                                        |

# Transformer
|     Name     |                 Description                  |      Data Type      | Units |  Range   | Req |                                                      Notes                                                      |
|--------------|----------------------------------------------|---------------------|-------|----------|-----|-----------------------------------------------------------------------------------------------------------------|
| `id`         | Unique Identification Number                 | `Numeric`           |       |          | ✓   |                                                                                                                 |
| `name`       | Transformer Name                             | `String`            |       |          | ✓   |                                                                                                                 |
| `type`       | The type of transformer                      | `<TransformerType>` |       |          |     |                                                                                                                 |
| `phase`      | The number of electrical phases              | `<ElectricalPhase>` |       |          |     |                                                                                                                 |
| `efficiency` | Transformer efficiency                       | `Numeric`           |       | `≥0, ≤1` |     | Expresses the efficiency of the transformer as a fraction from 0 to 1, where 1 would represent 100% efficiency. |
| `capacity`   | Rated Capacity of the Transformer            | `Numeric`           | V-A   | `≥0`     |     |                                                                                                                 |
| `peak_load`  | Annual Peak electric load on the transformer | `Numeric`           | W     | `≥0`     |     | Peak electric load on the transfomer based on an annual simulation with typical weather file.                   |

# Schedule
|                 Name                  |                                    Description                                     |              Data Type               | Units | Range | Req |                                                                                                                                 Notes                                                                                                                                 |
|---------------------------------------|------------------------------------------------------------------------------------|--------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `id`                                  | Unique Identification Number                                                       | `Numeric`                            |       |       | ✓   |                                                                                                                                                                                                                                                                       |
| `name`                                | Name of the Schedule                                                               | `String`                             |       |       | ✓   |                                                                                                                                                                                                                                                                       |
| `purpose`                             | The purpose of schedule                                                            | `String`                             |       |       |     | Describe the purpose of the schedule and how it can be used. Not an enumerations. The purpose assigned by BEM tool should match across RMRs. Examples include thermostat, multiplier for lighting, availability for equipment.                                        |
| `schedule_sequence_type`              | Schedule sequence type                                                             | `<ScheduleSequenceTypeOptions>`      |       |       |     |                                                                                                                                                                                                                                                                       |
| `hourly_values`                       | Hourly Values of Schedule                                                          | `[Numeric][8760]`                    |       |       |     | Used when schedule_sequence_type is HOURLY. Can also use functions like EFLH(), MAX(), MIN() to determine overall characteristics for the list of schedule values.                                                                                                    |
| `event_times`                         | Event times when the schedule changes                                              | `[Numeric]`                          | s     |       |     | Used when schedule_sequence_type is EVENT to describe the time of the year in seconds that the schedule changes value.                                                                                                                                                |
| `event_values`                        | Event value at corresponding event time.                                           | `[Numeric]`                          |       |       |     | Used when schedule_sequence_type is EVENT. New values starting at corresponding to the event time until following event time minus one second. Can also use functions like EFLH(), MAX(), MIN() to determine overall characteristics for the list of schedule values. |
| `type`                                | The type of schedule                                                               | `<ScheduleTypeOptions>`              |       |       |     | Primarily indicates if the values may be represented by units such as C for temperature or W for power or m3/s for flow rate or are dimensionless multipliers.                                                                                                        |
| `prescribed_schedule`                 | True if any schedule values have changed from what appears in the schedule library | `<PrescribedSchedules2019ASHRAE901>` |       |       |     |                                                                                                                                                                                                                                                                       |
| `is_schedule_modified_for_workaround` | True if any schedule has been modified for a workaround                            | `Boolean`                            |       |       |     |                                                                                                                                                                                                                                                                       |

# Calendar
|            Name             |                  Description                   |   Data Type   | Units | Range | Req | Notes |
|-----------------------------|------------------------------------------------|---------------|-------|-------|-----|-------|
| `id`                        | Unique Identification Number                   | `Numeric`     |       |       | ✓   |       |
| `name`                      | Name of the calendar                           | `String`      |       |       | ✓   |       |
| `day_of_week_for_january_1` | Day of the week for January 1                  | `<DayOfWeek>` |       |       |     |       |
| `is_leap_year`              | The schedules assume it is a leap year         | `Boolean`     |       |       |     |       |
| `is_daylight_savings_time`  | The schedules adjust for daylight Savings Time | `Boolean`     |       |       |     |       |

# Weather
|             Name             |                            Description                            |          Data Type           | Units | Range | Req |                     Notes                      |
|------------------------------|-------------------------------------------------------------------|------------------------------|-------|-------|-----|------------------------------------------------|
| `id`                         | Unique Identification Number                                      | `Numeric`                    |       |       | ✓   |                                                |
| `name`                       | Name of the Weather data group                                    | `String`                     |       |       | ✓   |                                                |
| `monthly_ground_temperature` | Modeled monthly ground temperatures                               | `[Numeric][1..12]`           | C     |       |     |                                                |
| `climate_zone`               | The designation of the climate zone where the building is located | `<ClimateZone2019ASHRAE901>` |       |       | ✓   | The enumeration is based on the standard used. |

# Elevator
|                   Name                    |                         Description                         | Data Type | Units | Range | Req | Notes |
|-------------------------------------------|-------------------------------------------------------------|-----------|-------|-------|-----|-------|
| `id`                                      | Unique Identification Number                                | `Numeric` |       |       | ✓   |       |
| `name`                                    | Name of the elevator                                        | `String`  |       |       | ✓   |       |
| `motor_power`                             | Elevator peak motor power                                   | `Numeric` | W     |       |     |       |
| `cab_counterweight`                       | Elevator car counterweight                                  | `Numeric` | kg    |       |     |       |
| `cab_weight`                              | Weight of elevator car                                      | `Numeric` | kg    |       |     |       |
| `design_elevator_load`                    | Elevator load at which to operate                           | `Numeric` | kg    |       |     |       |
| `speed`                                   | Design speed of the elevator                                | `Numeric` | m/s   |       |     |       |
| `cab_area`                                | Floor area of elevator cab                                  | `Numeric` | m2    |       |     |       |
| `cab_lighting_power`                      | Lighitng power of cab                                       | `Numeric` | W     |       |     |       |
| `cab_ventilation_fan_power`               | Ventilation fan power of cab                                | `Numeric` | W     |       |     |       |
| `cab_ventilation_fan_flow`                | Airflow of cab ventfan                                      | `Numeric` | L/s   |       |     |       |
| `cab_motor_multiplier_schedule`           | Elevator motor operation multiplier schedule name           | `String`  |       |       |     |       |
| `cab_ventilation_fan_multiplier_schedule` | Elevator ventilation fan operation mulitplier schedule name | `String`  |       |       |     |       |
| `cab_lighting_multiplier_schedule`        | Elevator lighting multiplier schedule name                  | `String`  |       |       |     |       |

# HeatingVentilationAirConditioningSystem
|            Name             |                 Description                 |  Data Type  | Units | Range | Req |                                                                Notes                                                                 |
|-----------------------------|---------------------------------------------|-------------|-------|-------|-----|--------------------------------------------------------------------------------------------------------------------------------------|
| `id`                        | Unique Identification Number                | `Numeric`   |       |       | ✓   |                                                                                                                                      |
| `name`                      | Name of the HVAC system                     | `String`    |       |       | ✓   |                                                                                                                                      |
| `zones_served`              | List of the zones served by the HVAC system | `[{Zone}]`  |       |       |     |                                                                                                                                      |
| `hot_water_loop_name`       | Hot water fluid loop name                   | `String`    |       |       |     |                                                                                                                                      |
| `chilled_water_loop_name`   | Chilled water fluid loop name               | `String`    |       |       |     |                                                                                                                                      |
| `condenser_water_loop_name` | Condenser water fluid loop name             | `String`    |       |       |     |                                                                                                                                      |
| `preheat_loop_name`         | Preheat fluid loop name                     | `String`    |       |       |     |                                                                                                                                      |
| `reheat_loop_name`          | Reheat fluid loop name                      | `String`    |       |       |     |                                                                                                                                      |
| `sensible_cool_capacity`    | Sensible cooling capacity                   | `[Numeric]` | W/m2  | `≥0`  |     | May be design value or result from the simulation. If multiple values are provided, they correspond to rotated building orientations |
| `heat_capacity`             | Heating capacity                            | `[Numeric]` | W/m2  | `≥0`  |     | May be design value or result from the simulation. If multiple values are provided, they correspond to rotated building orientations |

# FluidLoop
|                    Name                    |                                  Description                                   |           Data Type           | Units | Range | Req | Notes |
|--------------------------------------------|--------------------------------------------------------------------------------|-------------------------------|-------|-------|-----|-------|
| `id`                                       | Unique Identification Number                                                   | `Numeric`                     |       |       | ✓   |       |
| `name`                                     | Name of the fluid loop connecting primary and secondary equipment in the plant | `String`                      |       |       | ✓   |       |
| `type`                                     | Type of loop                                                                   | `<FluidLoopTypeOptions>`      |       |       |     |       |
| `child_loops`                              | Other fluid loops connected to this one as children.                           | `[{FluidLoop}]`               |       |       |     |       |
| `cooling_or_condensing_design_and_control` |                                                                                | `{FluidLoopDesignAndControl}` |       |       |     |       |
| `heating_design_and_control`               |                                                                                | `{FluidLoopDesignAndControl}` |       |       |     |       |

# FluidLoopDesignAndControl
|                       Name                       |                     Description                     |            Data Type            | Units | Range | Req | Notes |
|--------------------------------------------------|-----------------------------------------------------|---------------------------------|-------|-------|-----|-------|
| `id`                                             | Unique Identification Number                        | `Numeric`                       |       |       | ✓   |       |
| `name`                                           | Name of the fluid loop design and control.          | `String`                        |       |       | ✓   |       |
| `design_supply_temperature`                      | Design Supply Temperature                           | `Numeric`                       | C     |       |     |       |
| `design_return_temperature`                      | Design Return Temperature                           | `Numeric`                       | C     |       |     |       |
| `is_sized_using_coincident_load`                 | True if the loop is sized based on coincident load  | `Boolean`                       |       |       |     |       |
| `minimum_flow_fraction`                          | Minimum fraction of full flow allowed               | `Numeric`                       |       |       |     |       |
| `operation`                                      | Type of operation used by loop                      | `<FluidLoopOperationOptions>`   |       |       |     |       |
| `temperature_reset_type`                         | Type of temperature reset used by loop              | `<TemperatureResetTypeOptions>` |       |       |     |       |
| `outdoor_high_for_loop_supply_temperature_reset` | Outdoor high for loop supply temp reset             | `Numeric`                       | C     |       |     |       |
| `outdoor_low_for_loop_supply_temperature_reset`  | Outdoor low for loop supply temp reset              | `Numeric`                       | C     |       |     |       |
| `loop_supply_temperature_at_outdoor_high`        | Loop supply temperature at outdoor high temperature | `Numeric`                       | C     |       |     |       |
| `loop_supply_temperature_at_outdoor_low`         | Loop supply temperature at outdoor low temperature  | `Numeric`                       | C     |       |     |       |

# Pump
|          Name           |                Description                 |             Data Type              | Units |  Range   | Req |                                             Notes                                              |
|-------------------------|--------------------------------------------|------------------------------------|-------|----------|-----|------------------------------------------------------------------------------------------------|
| `id`                    | Unique Identification Number               | `Numeric`                          |       |          | ✓   |                                                                                                |
| `name`                  | Name identifying pump                      | `String`                           |       |          | ✓   |                                                                                                |
| `loop_name`             | Fluid loop name                            | `String`                           |       |          |     |                                                                                                |
| `specification_method`  | Options for how the pump is specified      | `<PumpSpecificationMethodOptions>` |       |          |     |                                                                                                |
| `design_electric_power` | Pump design electric power                 | `Numeric`                          | W     |          |     | Pump electric power at design conditions. Only used when specification_method is set to Simple |
| `motor_nameplate_power` | Pump motor nameplate power                 | `Numeric`                          | W     |          |     | Only used when specification_method is set to Detailed                                         |
| `design_head`           | Head of the pump at design flow conditions | `Numeric`                          | m     |          |     | Only used when specification_method is set to Detailed                                         |
| `impeller_efficiency`   | Full load efficiency of the impeller       | `Numeric`                          |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed                                         |
| `motor_efficiency`      | Full load efficiency of the pump motor     | `Numeric`                          |       | `≥0, ≤1` |     | Only used when specification_method is set to Detailed                                         |
| `speed_control`         | Options for pump speed control             | `<PumpSpeedControlOptions>`        |       |          |     |                                                                                                |
| `flow_control`          | Flow control options                       | `<PumpFlowControlOptions>`         |       |          |     |                                                                                                |
| `design_flow`           | Design Pump Flowrate                       | `Numeric`                          | L/s   |          |     |                                                                                                |
| `is_variable_speed`     | True if variable speed drive such a VFD    | `Boolean`                          |       |          |     |                                                                                                |

# Boiler
|            Name            |                       Description                        |               Data Type                | Units |  Range   | Req |                                             Notes                                             |
|----------------------------|----------------------------------------------------------|----------------------------------------|-------|----------|-----|-----------------------------------------------------------------------------------------------|
| `id`                       | Unique Identification Number                             | `Numeric`                              |       |          | ✓   |                                                                                               |
| `name`                     | Name identifying boiler                                  | `String`                               |       |          | ✓   |                                                                                               |
| `loop_name`                | Fluid loop name                                          | `String`                               |       |          |     |                                                                                               |
| `design_capacity`          | Heating capacity                                         | `Numeric`                              | W     |          |     |                                                                                               |
| `rated_capacity`           | Heating capacity                                         | `Numeric`                              | W     |          |     | At rating conditions.                                                                         |
| `minimum_load_ratio`       | Minimum fraction of full load allowed                    | `Numeric`                              |       |          |     |                                                                                               |
| `draft_type`               | Combustion option                                        | `<BoilerCombustionOptions>`            |       |          |     |                                                                                               |
| `efficiency_metric_type`   | The type of efficiency metric used                       | `<BoilerEfficiencyMetricTypeOptions>`  |       |          |     |                                                                                               |
| `efficiency_metric`        | Annual fuel utilization efficiency (AFUE)                | `Numeric`                              |       | `≥0, ≤1` |     | Enter the efficiency value based on the selected efficiency_metric_type                       |
| `detailed_performance`     | Detailed performance as specified in ASHRAE Standard 205 | `UUID`                                 |       |          |     | Reserved for referencing after ASHRAE Standard 205 is published.                              |
| `energy_validation_points` | Energy validation points                                 | `[{BoilerPerformanceValidationPoint}]` |       |          |     | Load is input to each validation point and energy output is the result.                       |
| `auxiliary_power`          | Auxiliary power                                          | `Numeric`                              | W     |          |     | Power for boiler pump, combustion fan, or other auxiliary that operates when boiler operates. |
| `operation_lower_limit`    | Heating load range operation, lower limit                | `Numeric`                              | W     |          |     |                                                                                               |
| `operation_upper_limit`    | Heating load range operation, upper limit                | `Numeric`                              | W     |          |     |                                                                                               |

# BoilerPerformanceValidationPoint
|   Name   | Description | Data Type | Units | Range | Req |                               Notes                               |
|----------|-------------|-----------|-------|-------|-----|-------------------------------------------------------------------|
| `load`   | Load        | `Numeric` | W     |       |     | No name and id is needed since typically used as one of a series. |
| `result` | Result      | `Numeric` | W     |       |     |                                                                   |

# Chiller
|                  Name                   |                                      Description                                      |                Data Type                | Units | Range | Req |                              Notes                               |
|-----------------------------------------|---------------------------------------------------------------------------------------|-----------------------------------------|-------|-------|-----|------------------------------------------------------------------|
| `id`                                    | Unique Identification Number                                                          | `Numeric`                               |       |       | ✓   |                                                                  |
| `name`                                  | Name identifying chiller                                                              | `String`                                |       |       | ✓   |                                                                  |
| `cooling_loop_name`                     | Cooling fluid loop name                                                               | `String`                                |       |       |     |                                                                  |
| `condensing_loop_name`                  | Condensing fluid loop name                                                            | `String`                                |       |       |     | No condensing loop name implies air-cooled chiller.              |
| `compressor_type`                       | Compressor Type                                                                       | `<ChillerCompressorTypeOptions>`        |       |       |     |                                                                  |
| `design_capacity`                       | Chiller Design Cooling Capacity                                                       | `Numeric`                               | W     |       |     |                                                                  |
| `rated_capacity`                        | Chiller Design Cooling Capacity                                                       | `Numeric`                               | W     |       |     | At rating conditions.                                            |
| `minimum_load_ratio`                    | Minimum fraction of full load allowed                                                 | `Numeric`                               |       |       |     |                                                                  |
| `design_flow_evaporator`                | Chiller evaporator design flow                                                        | `Numeric`                               | L/s   |       |     |                                                                  |
| `design_flow_condenser`                 | Chiller condenser design flow                                                         | `Numeric`                               | L/s   |       |     |                                                                  |
| `full_load_efficiency`                  | Full Low Efficiency expressed as a coefficient of performance (COP)                   | `Numeric`                               | W/W   |       |     |                                                                  |
| `integrated_part_load_value_efficiency` | Integrated part load value efficiency expressed as a coefficient of performance (COP) | `Numeric`                               | W/W   |       |     | Can be input by user or computed.                                |
| `capacity_validation_points`            | Capacity validation points                                                            | `[{ChillerPerformanceValidationPoint}]` |       |       |     |                                                                  |
| `energy_validation_points`              | Energy validation points                                                              | `[{ChillerPerformanceValidationPoint}]` |       |       |     |                                                                  |
| `detailed_performance`                  | Detailed performance as specified in ASHRAE Standard 205                              | `UUID`                                  |       |       |     | Reserved for referencing after ASHRAE Standard 205 is published. |

# ChillerPerformanceValidationPoint
|                Name                |           Description            | Data Type | Units | Range | Req |                                                       Notes                                                        |
|------------------------------------|----------------------------------|-----------|-------|-------|-----|--------------------------------------------------------------------------------------------------------------------|
| `chilled_water_supply_temperature` | Chilled water supply temperature | `Numeric` | C     |       |     | No name and id is needed since used as one of a series.                                                            |
| `second_temperature`               | Second temperature               | `Numeric` | C     |       |     | Outside air dry-bulb temperature for air cooled chillers and condenser water temperature for water cooled chillers |
| `load`                             | Load                             | `Numeric` | W     |       |     |                                                                                                                    |
| `result`                           | Result                           | `Numeric` | W     |       |     |                                                                                                                    |

# HeatRejection
|             Name             |                Description                |                Data Type                | Units | Range | Req |         Notes         |
|------------------------------|-------------------------------------------|-----------------------------------------|-------|-------|-----|-----------------------|
| `id`                         | Unique Identification Number              | `Numeric`                               |       |       | ✓   |                       |
| `name`                       | Name identifying heat rejection equipment | `String`                                |       |       | ✓   |                       |
| `loop_name`                  | Fluid loop name                           | `String`                                |       |       |     |                       |
| `type`                       | Heat Rejection Type                       | `<HeatRejectionTypeOptions>`            |       |       |     |                       |
| `fan_type`                   | Heat Rejection Fan Type                   | `<HeatRejectionFanTypeOptions>`         |       |       |     |                       |
| `fluid`                      | Fluid Cooled by Heat Rejection            | `<HeatRejectionFluidOptions>`           |       |       |     |                       |
| `range`                      | Heat rejection Range                      | `Numeric`                               | C     |       |     |                       |
| `approach`                   | Heat rejection Approach                   | `Numeric`                               | C     |       |     |                       |
| `reset_type`                 | Leaving Temperature reset strategy        | `<HeatRejectionResetOptions>`           |       |       |     |                       |
| `minimum_reset_temperature`  | Minimum leaving temperature setpoint      | `Numeric`                               | C     |       |     |                       |
| `fan_power`                  | Fan Power                                 | `Numeric`                               | W     |       |     |                       |
| `fan_speed_control`          | Fan Speed Control Type                    | `<HeatRejectionFanSpeedControlOptions>` |       |       |     |                       |
| `design_supply_temperature`  | Design leaving water temperature          | `Numeric`                               | C     |       |     |                       |
| `design_wetbulb_temperature` | Design wetbulb temperature                | `Numeric`                               | C     |       |     | 0.4% ASHRAE MCWB      |
| `design_water_flowrate`      | Design condenser water flow rate          | `Numeric`                               | L/s   |       |     |                       |
| `rated_water_flowrate`       | Rated condenser water flow rate           | `Numeric`                               | L/s   |       |     | At rating conditions. |

# ExternalFluidSource
|    Name     |              Description               |             Data Type              | Units | Range | Req |                                                            Notes                                                            |
|-------------|----------------------------------------|------------------------------------|-------|-------|-----|-----------------------------------------------------------------------------------------------------------------------------|
| `id`        | Unique Identification Number           | `Numeric`                          |       |       | ✓   |                                                                                                                             |
| `name`      | Name identifying external fluid source | `String`                           |       |       | ✓   | External fluid source is a method to indicate that it is connected to a district or campus system external to the building. |
| `loop_name` | Fluid loop name                        | `String`                           |       |       |     |                                                                                                                             |
| `type`      | Type of external fluid source          | `<ExternalFluidSourceTypeOptions>` |       |       |     |                                                                                                                             |

# ServiceWaterHeatingSystem
|                 Name                 |                                                           Description                                                            |                          Data Type                          | Units | Range | Req |                                 Notes                                  |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|-------|-------|-----|------------------------------------------------------------------------|
| `id`                                 | Unique Identification Number                                                                                                     | `Numeric`                                                   |       |       | ✓   |                                                                        |
| `name`                               | Name of service water heating system loop                                                                                        | `String`                                                    |       |       |     |                                                                        |
| `area_type`                          | Service Water Heating Loop Area Type                                                                                             | `<ServiceWaterHeatingSpaceType2019ASHRAE901>`               |       |       |     | The enumeration is based on the standard used.                         |
| `design_flow`                        | Design Flowrate of service water heating loop                                                                                    | `Numeric`                                                   | L/s   |       |     |                                                                        |
| `supply_temperature`                 | Design supply temperature setpoint of service water heating loop                                                                 | `Numeric`                                                   | C     |       |     |                                                                        |
| `flow_multiplier_schedule`           | service water heating Loop flow muliplier schedule name                                                                          | `String`                                                    |       |       |     |                                                                        |
| `annual_entering_water_temperature`  | Annual service main or annual ground temperature used for service water heating calculations entering water temperature  degrees | `Numeric`                                                   | C     |       |     |                                                                        |
| `monthly_entering_water_temperature` | Monthly service main or ground temperatures used for service water heating entering water temperature  degrees                   | `[Numeric][1..12]`                                          | C     |       |     | Arrayed variable with 12 values for monthly entering water temperature |
| `entering_water_temperature_type`    | Method of determining service water heating entering water temperature                                                           | `<ServiceWaterHeatingEnteringWaterTemperatureInputOptions>` |       |       |     |                                                                        |
| `heater_name`                        | Service water heating heater name                                                                                                | `String`                                                    |       |       |     |                                                                        |
| `heater_fuel_type`                   | Service water heating heater fuel type                                                                                           | `<FuelTypeOptions>`                                         |       |       |     |                                                                        |
| `heater_efficiency`                  | Service water heating heater efficiency                                                                                          | `Numeric`                                                   |       | `≥0`  |     |                                                                        |

# ExteriorLighting
|               Name                |                                     Description                                      |                   Data Type                    | Units | Range | Req | Notes |
|-----------------------------------|--------------------------------------------------------------------------------------|------------------------------------------------|-------|-------|-----|-------|
| `id`                              | Unique ID assigned to each exterior lighting fixture(s) reported in an RMR           | `Numeric`                                      |       | `>0`  |     |       |
| `name`                            | Exterior lighting fixture name                                                       | `String`                                       |       |       |     |       |
| `type`                            | The type of exterior lighting fixture  none                                          | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |       |       |     |       |
| `area`                            | Area of the exterior functional space.                                               | `Numeric`                                      | m2    | `>0`  |     |       |
| `norminal_wattage`                | Nominal capacity of exterior lighting fixtures                                       | `Numeric`                                      | W     | `>0`  |     |       |
| `fixture_height`                  | Installation height of exterior fixture                                              | `Numeric`                                      | m     | `>0`  |     |       |
| `power`                           | Total exterior lighting power of all fixtures in a specific functional area          | `Numeric`                                      | W     | `>0`  |     |       |
| `designed_power`                  | Total designed exterior lighting power of all fixtures in a specific functional area | `Numeric`                                      | W     | `>0`  |     |       |
| `trade_light_power`               | Exterior Lighting power for tradable surface                                         | `Numeric`                                      | W     | `≥0`  |     |       |
| `non_trade_light_power`           | Exterior Lighting power for non-tradable surface                                     | `Numeric`                                      | W     | `≥0`  |     |       |
| `site_zone_type`                  | Site zone type for Sec 9.4.2                                                         | `<ExteriorLightingZones2019ASHRAE901>`         |       |       |     |       |
| `parking_area`                    | Area of exterior parking space                                                       | `Numeric`                                      | m2    | `≥0`  |     |       |
| `tradable_surface_type`           | Type of tradable surfaces for exterior lighting                                      | `<ExteriorLightingAreas2019ASHRAE901TableG36>` |       |       |     |       |
| `tradable_surface_area`           | Area of tradable surface                                                             | `Numeric`                                      | m2    | `≥0`  |     |       |
| `tradable_surface_linear_footage` | Linear feet of tradable surface                                                      | `Numeric`                                      | m     | `≥0`  |     |       |
| `has_walkway`                     | If the building has an exterior walkway                                              | `Boolean`                                      |       |       |     |       |
| `tradable_walkway_width_footage`  | Width of the exterior walkway                                                        | `Numeric`                                      | m     | `≥0`  |     |       |
| `tradable_opening_width_footage`  | Width of an exterior opening                                                         | `Numeric`                                      | m     | `≥0`  |     |       |
| `multiplier`                      | Multiplier for exterior lighting specifications                                      | `Numeric`                                      |       | `>0`  |     |       |

# Refrigeration
|         Name         |                     Description                      |              Data Type              | Units | Range | Req | Notes |
|----------------------|------------------------------------------------------|-------------------------------------|-------|-------|-----|-------|
| `id`                 | Unique Identification Number                         | `Numeric`                           |       |       | ✓   |       |
| `name`               | Name of the refrigeration component                  | `String`                            |       |       | ✓   |       |
| `type`               | Refrigeration equipment type                         | `<RefrigerationType2019ASHRAE901>`  |       |       |     |       |
| `equipment_class`    | Equipment Class from referenced standard             | `<RefrigerationClass2019ASHRAE901>` |       |       |     |       |
| `energy_per_day`     | Rated electrical energy use per day                  | `Numeric`                           | kWh   |       |     |       |
| `case_volume`        | volume of a refrigerated case in cubic meters        | `Numeric`                           | m3    |       |     |       |
| `total_display_area` | display area of a refrigerated case in square meters | `Numeric`                           | m2    |       |     |       |

# OverallSimulationOutputs
|                       Name                        |                        Description                         | Data Type | Units | Range | Req | Notes |
|---------------------------------------------------|------------------------------------------------------------|-----------|-------|-------|-----|-------|
| `id`                                              | Unique Identification Number                               | `Numeric` |       |       | ✓   |       |
| `name`                                            | Name of the overall simulation output                      | `String`  |       |       | ✓   |       |
| `refrigeration_energy_enduse`                     | Annual refrigeration energy end use from simulation output | `Numeric` | kWh   |       |     |       |
| `service_water_heating_annual_enduse_electricity` | Annual electricity energy end_use for SWH loops            | `Numeric` | kWh   | `≥0`  |     |       |
| `service_water_heating_annual_enduse_fossilfuel`  | Annual fossil fuel energy end_use for SWH loops            | `Numeric` | J     | `≥0`  |     |       |

