# AdditionalSurfaceAdjacencyOptions2019ASHRAE901
|   Enumerator    |                                                                   Description                                                                   | Notes |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `UNENCLOSED`    | The space on the other side of the surface is assumed to be unenclosed. The space on the other side of the surface is not explicity modeled.    |       |
| `UNCONDITIONED` | The space on the other side of the surface is assumed to be unconditioned. The space on the other side of the surface is not explicity modeled. |       |
| `UNHEATED`      | Surface adjacent to a environment that is not heated but enclosed.                                                                              |       |
| `SEMIHEATED`    | Surface adjacent to a environment that is semi-heated.                                                                                          |       |

# ClimateZoneOptions2019ASHRAE901
| Enumerator |      Description      | Notes |
| ---------- | --------------------- | ----- |
| `CZ0A`     | Extremely Hot - Humid |       |
| `CZ0B`     | Extremely Hot - Dry   |       |
| `CZ1A`     | Very Hot - Humid      |       |
| `CZ1B`     | Very Hot - Dry        |       |
| `CZ2A`     | Hot - Humid           |       |
| `CZ2B`     | Hot - Dry             |       |
| `CZ3A`     | Warm - Humid          |       |
| `CZ3B`     | Warm - Dry            |       |
| `CZ3C`     | Warm - Marine         |       |
| `CZ4A`     | Mixed - Humid         |       |
| `CZ4B`     | Mixed - Dry           |       |
| `CZ4C`     | Mixed - Marine        |       |
| `CZ5A`     | Cool - Humid          |       |
| `CZ5B`     | Cool - Dry            |       |
| `CZ5C`     | Cool - Marine         |       |
| `CZ6A`     | Cold - Humid          |       |
| `CZ6B`     | Cold - Dry            |       |
| `CZ7`      | Very cold             |       |
| `CZ8`      | Subarctic/arctic      |       |

# CompliancePathOptions2019ASHRAE901
|    Enumerator    |   Description   | Notes |
| ---------------- | --------------- | ----- |
| `CODE_COMPLIANT` | Code Compliance |       |
| `BEYOND_CODE`    | Beyond Code     |       |

# ConstructionClassificationOptions2019ASHRAE901
|   Enumerator   | Description  | Notes |
| -------------- | ------------ | ----- |
| `STEEL_FRAMED` | Steel-framed |       |

# EnvelopeSpaceOptions2019ASHRAE901
|          Enumerator          |        Description         | Notes |
| ---------------------------- | -------------------------- | ----- |
| `NONRESIDENTIAL_CONDITIONED` | Nonresidential conditioned |       |
| `RESIDENTIAL_CONDITIONED`    | Residential conditioned    |       |
| `SEMIHEATED`                 | Semiheated                 |       |
| `UNCONDITIONED`              | Unconditioned              |       |

# ExteriorLightingAreaOptions2019ASHRAE901TableG36
|              Enumerator              |                Description                |                                                                                        Notes                                                                                         |
| ------------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `UNCOVERED_PARKING_LOTS_AND_DRIVES`  | Uncovered parking lots and drives         |                                                                                                                                                                                      |
| `WALKWAY_NARROW`                     | Walkway - narrow                          | Less than 10 ft wide                                                                                                                                                                 |
| `WALKWAY_WIDE`                       | Walkway - wide                            | 10 ft wide or greater                                                                                                                                                                |
| `PLAZA_AREAS`                        | Plaza Areas                               |                                                                                                                                                                                      |
| `SPECIAL_FEATURE_AREAS`              | Special Feature Areas                     |                                                                                                                                                                                      |
| `STAIRWAYS`                          | Stairways                                 |                                                                                                                                                                                      |
| `MAIN_ENTRANCE_DOOR`                 | Main entrance door                        |                                                                                                                                                                                      |
| `OTHER_ENTRANCE_OR_EXIT_DOORS`       | Other entrance or exit doors              |                                                                                                                                                                                      |
| `EXTERIOR_CANOPIES`                  | Exterior canopies                         |                                                                                                                                                                                      |
| `OUTDOOR_SALES_OPEN_AREAS`           | Outdoor sales - open areas                |                                                                                                                                                                                      |
| `STREET_FRONTAGE`                    | Street frontage                           |                                                                                                                                                                                      |
| `BUILDING_FACADE`                    | Building facade                           |                                                                                                                                                                                      |
| `AUTOMATED_TELLER_MACHINES`          | Automated teller machines                 |                                                                                                                                                                                      |
| `NIGHT_DEPOSITORIES`                 | Night depositories                        |                                                                                                                                                                                      |
| `ENTRANCE_AND_GATEHOUSE`             | Entrance and gatehouses                   | Entrances and gatehouse inspection stations at guarded facilities.                                                                                                                   |
| `EMERGENCY_VEHICLE_LOADING_AREA`     | Emergency vehicle loading area            | Loading areas for law enforcement, fire, ambulance and other emergency service vehicles                                                                                              |
| `DRIVE_UP_WINDOWS_FAST_FOOD`         | Drive-up windows at fast-food restaurants |                                                                                                                                                                                      |
| `PARKING_NEAR_24HR_RETAIL_ENTRANCES` | Parking near 24-hour retail entrances     |                                                                                                                                                                                      |
| `MISCELLANEOUS_TRADABLE`             | Miscellaneous tradable                    | This option would most often be used by software that does not support entire schema and doesn't know if exterior lighting is in a specific type but does know if it is tradable     |
| `MISCELLANEOUS_NON_TRADABLE`         | Miscellaneous non-tradable                | This option would most often be used by software that does not support entire schema and doesn't know if exterior lighting is in a specific type but does know if it is non-tradable |

# ExteriorLightingZoneOptions2019ASHRAE901
|            Enumerator             |            Description            |                                                                               Notes                                                                                |
| --------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ZONE_0_UNDEVELOPED`              | Zone 0 - undeveloped              | Undeveloped areas within national parks, state parks, forest land, rural areas, and other undeveloped areas as defined by the authority having jurisdiction        |
| `ZONE_1_DEVELOPED_RURAL_AND_PARK` | Zone 1 - developed rural and park | Developed areas of national parks, state parks, forest land, and rural areas                                                                                       |
| `ZONE_2_RESIDENTIAL_NEIGHBORHOOD` | Zone 2 - residential neighborhood | Areas predominantly consisting of residential zoning, neighborhood business districts, light industrial with limited nighttime use and residential mixed use areas |
| `ZONE_3_ALL_OTHER_AREAS`          | Zone 3 - all other areas          |                                                                                                                                                                    |
| `ZONE_4_HIGH_ACTIVITY_COMMERCIAL` | Zone 4 - high-activity commercial | High-activity commercial districts in major metropolitan areas as designated by the local jurisdiction                                                             |

# HeatingVentilatingAirConditioningBuildingAreaOptions2019ASHRAE901
|       Enumerator        |      Description      | Notes |
| ----------------------- | --------------------- | ----- |
| `RESIDENTIAL`           | Residential           |       |
| `PUBLIC_ASSEMBLY`       | Public assembly       |       |
| `RETAIL`                | Retail                |       |
| `HOSPITAL`              | Hospital              |       |
| `HEATED_ONLY_STORAGE`   | Heated only storage   |       |
| `OTHER_NON_RESIDENTIAL` | Other non-residential |       |

# LightingBuildingAreaOptions2019ASHRAE901T951TG38
|          Enumerator          |         Description         |                                             Notes                                              |
| ---------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------- |
| `AUTOMOTIVE_FACILITY`        | Automotive facility         |                                                                                                |
| `CONVENTION_CENTER`          | Convention center           |                                                                                                |
| `COURTHOUSE`                 | Courthouse                  |                                                                                                |
| `DINING_BAR_LOUNGE_LEISURE`  | Dining: Bar lounge/leisure  |                                                                                                |
| `DINING_CAFETERIA_FAST_FOOD` | Dining: Cafeteria/fast food |                                                                                                |
| `DINING_FAMILY`              | Dining: Family              |                                                                                                |
| `DORMITORY`                  | Dormitory                   |                                                                                                |
| `EXERCISE_CENTER`            | Exercise center             |                                                                                                |
| `FIRE_STATION`               | Fire station                |                                                                                                |
| `GYMNASIUM`                  | Gymnasium                   |                                                                                                |
| `HEALTH_CARE_CLINIC`         | Health-care clinic          |                                                                                                |
| `HOSPITAL`                   | Hospital                    |                                                                                                |
| `HOTEL_MOTEL`                | Hotel/motel                 |                                                                                                |
| `LIBRARY`                    | Library                     |                                                                                                |
| `MANUFACTURING_FACILITY`     | Manufacturing facility      |                                                                                                |
| `MOTION_PICTURE_THEATER`     | Motion picture theater      |                                                                                                |
| `MULTIFAMILY`                | Multifamily                 |                                                                                                |
| `MUSEUM`                     | Museum                      |                                                                                                |
| `OFFICE`                     | Office                      |                                                                                                |
| `PARKING_GARAGE`             | Parking garage              |                                                                                                |
| `PENITENTIARY`               | Penitentiary                |                                                                                                |
| `PERFORMING_ARTS_THEATER`    | Performing arts theater     |                                                                                                |
| `POLICE_STATION`             | Police station              |                                                                                                |
| `POST_OFFICE`                | Post office                 |                                                                                                |
| `RELIGIOUS_FACILITY`         | Religious facility          |                                                                                                |
| `RETAIL`                     | Retail                      |                                                                                                |
| `SCHOOL_UNIVERSITY`          | School/university           |                                                                                                |
| `SPORTS_ARENA`               | Sports arena                |                                                                                                |
| `TOWN_HALL`                  | Town hall                   |                                                                                                |
| `TRANSPORTATION`             | Transportation              |                                                                                                |
| `WAREHOUSE`                  | Warehouse                   |                                                                                                |
| `WORKSHOP`                   | Workshop                    |                                                                                                |
| `NONE`                       | None                        | Indicates that building area method is not used and instead the space-by-space method is used. |

# LightingPurposeOptions2019ASHRAE901
|    Enumerator    |  Description   | Notes |
| ---------------- | -------------- | ----- |
| `GENERAL`        | General        |       |
| `TASK`           | Task           |       |
| `DECORATIVE`     | Decorative     |       |
| `RETAIL_DISPLAY` | Retail display |       |
| `UNREGULATED`    | Unregulated    |       |

# LightingSpaceOptions2019ASHRAE901TG37
|                          Enumerator                           |                                           Description                                           |                             Notes                             |
| ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `ATRIUM_LOW_MEDIUM`                                           | Atrium - Low/Medium                                                                             |                                                               |
| `ATRIUM_HIGH`                                                 | Atrium - High                                                                                   |                                                               |
| `AUDIENCE_SEATING_AREA_AUDITORIUM`                            | Audience Seating Area - Auditorium                                                              |                                                               |
| `AUDIENCE_SEATING_AREA_CONVENTION_CENTER`                     | Audience Seating Area - Convention center                                                       |                                                               |
| `AUDIENCE_SEATING_AREA_EXERCISE_CENTER`                       | Audience Seating Area - Excercise center                                                        |                                                               |
| `AUDIENCE_SEATING_AREA_GYMNASIUM`                             | Audience Seating Area - Gymnasium                                                               |                                                               |
| `AUDIENCE_SEATING_AREA_MOTION_PICTURE_THEATER`                | Audience Seating Area - Motion picture theater                                                  |                                                               |
| `AUDIENCE_SEATING_AREA_PENITENTIARY`                          | Audience Seating Area - Penitentiary                                                            |                                                               |
| `AUDIENCE_SEATING_AREA_PERFORMING_ARTS_THEATER`               | Audience Seating Area - Performing arts theater                                                 |                                                               |
| `AUDIENCE_SEATING_AREA_RELIGIOUS_FACILITY`                    | Audience Seating Area - Religious facility                                                      |                                                               |
| `AUDIENCE_SEATING_AREA_SPORTS_ARENA`                          | Audience Seating Area - Sports arena                                                            |                                                               |
| `AUDIENCE_SEATING_AREA_TRANSPORTATION_FACILITY`               | Audience Seating Area - Transportation facility                                                 |                                                               |
| `AUDIENCE_SEATING_AREA_ALL_OTHER`                             | Audience Seating Area - All other                                                               |                                                               |
| `BANKING_ACTIVITY_AREA`                                       | Banking Activity Area                                                                           |                                                               |
| `CLASSROOM_LECTURE_HALL_TRAINING_ROOM_PENITENTIARY`           | Classroom/Lecture Hall/Training Room - Penitentiary                                             |                                                               |
| `CLASSROOM_LECTURE_HALL_TRAINING_ROOM_SCHOOL`                 | Classroom/Lecture Hall/Training Room - School                                                   | Preschool through 12th grade, laboratory, and shop classrooms |
| `CLASSROOM_LECTURE_HALL_TRAINING_ROOM_ALL_OTHER`              | Classroom/Lecture Hall/Training Room - All other                                                |                                                               |
| `CONFERENCE_MEETING_MULTIPURPOSE_ROOM`                        | Conference/Meeting/Multipurpose Room                                                            |                                                               |
| `CONFINEMENT_CELLS`                                           | Confinement Cells                                                                               |                                                               |
| `COPY_PRINT_ROOM`                                             | Copy/Print Room                                                                                 |                                                               |
| `CORRIDOR_FACILITY_FOR_THE_VISUALLY_IMPAIRED`                 | Corridor - Facility for the visually impaired (and not used primarily by the staff)             |                                                               |
| `CORRIDOR_HOSPITAL`                                           | Corridor - Hospital                                                                             |                                                               |
| `CORRIDOR_MANUFACTURING_FACILITY`                             | Corridor - Manufacturing facility                                                               |                                                               |
| `CORRIDOR_ALL_OTHERS`                                         | Corridor - All others                                                                           |                                                               |
| `COURT_ROOM`                                                  | Court room                                                                                      |                                                               |
| `COMPUTER_ROOM`                                               | Computer Room                                                                                   |                                                               |
| `DINING_AREA_PENITENTIARY`                                    | Dining Area - Penitentiary                                                                      |                                                               |
| `DINING_AREA_FACILITY_FOR_THE_VISUALLY_IMPAIRED`              | Dining Area - Facility for the visually impaired (and not used primarily by the staff)          |                                                               |
| `DINING_AREA_BAR_LOUNGE_OR_LEISURE_DINING`                    | Dining Area - Bar/lounge or leisure dining                                                      |                                                               |
| `DINING_AREA_CAFETERIA_OR_FAST_FOOD_DINING`                   | Dining Area - Cafeteria or fast food dining                                                     |                                                               |
| `DINING_AREA_FAMILY_DINING`                                   | Dining Area - Family dining                                                                     |                                                               |
| `DINING_AREA_ALL_OTHERS`                                      | Dining Area - All others                                                                        |                                                               |
| `ELECTRICAL_MECHANICAL_ROOM`                                  | Electrical/Mechanical Room                                                                      |                                                               |
| `EMERGENCY_VEHICLE_GARAGE`                                    | Emergency Vehicle Garage                                                                        |                                                               |
| `FOOD_PREPARATION_AREA`                                       | Food Preparation Area                                                                           |                                                               |
| `GUEST_ROOM`                                                  | Guest Room                                                                                      |                                                               |
| `JUDGES_CHAMBERS`                                             | Judges Chambers                                                                                 |                                                               |
| `DWELLING_UNIT`                                               | Dwelling Unit                                                                                   |                                                               |
| `LABORATORY_EXCEPT_IN_OR_AS_A_CLASSROOM`                      | Laboratory - Except in or as a classroom                                                        |                                                               |
| `LAUNDRY_WASHING_AREA`                                        | Laundry/Washing Area                                                                            |                                                               |
| `LOADING_DOCK_INTERIOR`                                       | Loading Dock, Interior                                                                          |                                                               |
| `LOBBY_FACILITY_FOR_THE_VISUALLY_IMPAIRED`                    | Lobby - Facility for the visually impaired (and not used primarily by the staff)                |                                                               |
| `LOBBY_ELEVATOR`                                              | Lobby - Elevator                                                                                |                                                               |
| `LOBBY_HOTEL`                                                 | Lobby - Hotel                                                                                   |                                                               |
| `LOBBY_MOTION_PICTURE_THEATER`                                | Lobby - Motion picture theater                                                                  |                                                               |
| `LOBBY_PERFORMING_ARTS_THEATER`                               | Lobby - Performing arts theater                                                                 |                                                               |
| `LOBBY_ALL_OTHERS`                                            | Lobby - All others                                                                              |                                                               |
| `LOCKER_ROOM`                                                 | Locker Room                                                                                     |                                                               |
| `LOUNGE_BREAKROOM_HEALTH_CARE_FACILITY`                       | Lounge/Breakroom - Health care facility                                                         |                                                               |
| `LOUNGE_BREAKROOM_ALL_OTHERS`                                 | Lounge/Breakroom - All others                                                                   |                                                               |
| `OFFICE_ENCLOSED`                                             | Office - Enclosed                                                                               |                                                               |
| `OFFICE_OPEN_PLAN`                                            | Office - Open plan                                                                              |                                                               |
| `PARKING_AREA_INTERIOR`                                       | Parking Area, Interior                                                                          |                                                               |
| `PHARMACY_AREA`                                               | Pharmacy Area                                                                                   |                                                               |
| `RESTROOM_FACILITY_FOR_THE_VISUALLY_IMPAIRED`                 | Restroom - Facility for the visually impaired (and not used primarily by the staff)             |                                                               |
| `RESTROOM_ALL_OTHERS`                                         | Restroom - All others                                                                           |                                                               |
| `SALES_AREA`                                                  | Sales Area                                                                                      |                                                               |
| `SEATING_AREA_GENERAL`                                        | Seating Area, General                                                                           |                                                               |
| `STAIRWELL`                                                   | Stairwell                                                                                       |                                                               |
| `STORAGE_ROOM_HOSPITAL`                                       | Storage Room - Hospital                                                                         |                                                               |
| `STORAGE_ROOM_SMALL`                                          | Storage Room - Small                                                                            |                                                               |
| `STORAGE_ROOM_LARGE`                                          | Storage Room - Large                                                                            |                                                               |
| `VEHICULAR_MAINTENANCE_AREA`                                  | Vehicular Maintenance Area                                                                      |                                                               |
| `WORKSHOP`                                                    | Workshop                                                                                        |                                                               |
| `ASSISTED_LIVING_FACILITY_CHAPEL`                             | Assisted Living Facility - Chapel (used primarily by residents)                                 |                                                               |
| `ASSISTED_LIVING_FACILITY_RECREATION_ROOM_COMMON_LIVING_ROOM` | Assisted Living Facility - Recreation room/common living room (and not used primarily by staff) |                                                               |
| `CONVENTION_CENTER_EXHIBIT_SPACE`                             | Convention Center â€” Exhibit Space                                                             |                                                               |
| `DORMITORY_LIVING_QUARTERS`                                   | Dormitory â€” Living Quarters                                                                   |                                                               |
| `FIRE_STATION_SLEEPING_QUARTERS`                              | Fire Station â€” Sleeping Quarters                                                              |                                                               |
| `GYMNASIUM_FITNESS_CENTER_EXERCISE_AREA`                      | Gymnasium/Fitness Center - Exercise area                                                        |                                                               |
| `GYMNASIUM_FITNESS_CENTER_PLAYING_AREA`                       | Gymnasium/Fitness Center - Playing area                                                         |                                                               |
| `HEALTHCARE_FACILITY_EMERGENCY_ROOM`                          | Healthcare Facility - Emergency Room                                                            |                                                               |
| `HEALTHCARE_FACILITY_EXAM_TREATMENT_ROOM`                     | Healthcare Facility - Exam/treatment room                                                       |                                                               |
| `HEALTHCARE_FACILITY_MEDICAL_SUPPLY_ROOM`                     | Healthcare Facility - Medical supply room                                                       |                                                               |
| `HEALTHCARE_FACILITY_NURSERY`                                 | Healthcare Facility - Nursery                                                                   |                                                               |
| `HEALTHCARE_FACILITY_NURSES_STATION`                          | Healthcare Facility - Nurseâ€™s station                                                         |                                                               |
| `HEALTHCARE_FACILITY_OPERATING_ROOM`                          | Healthcare Facility - Operating room                                                            |                                                               |
| `HEALTHCARE_FACILITY_PATIENT_ROOM`                            | Healthcare Facility - Patient room                                                              |                                                               |
| `HEALTHCARE_FACILITY_PHYSICAL_THERAPY_ROOM`                   | Healthcare Facility - Physical therapy room                                                     |                                                               |
| `HEALTHCARE_FACILITY_RECOVERY_ROOM`                           | Healthcare Facility - Recovery room                                                             |                                                               |
| `LIBRARY_READING_AREA`                                        | Library - Reading area                                                                          |                                                               |
| `LIBRARY_STACKS`                                              | Library - Stacks                                                                                |                                                               |
| `MANUFACTURING_FACILITY_DETAILED_MANUFACTURING_AREA`          | Manufacturing Facility - Detailed manufacturing area                                            |                                                               |
| `MANUFACTURING_FACILITY_EQUIPMENTROOM`                        | Manufacturing Facility - Equipment room                                                         |                                                               |
| `MANUFACTURING_FACILITY_EXTRA_HIGH_BAY_AREA`                  | Manufacturing Facility - Extra high bay area                                                    |                                                               |
| `MANUFACTURING_FACILITY_HIGH_BAY_AREA`                        | Manufacturing Facility - High bay area                                                          |                                                               |
| `MANUFACTURING_FACILITY_LOW_BAY_AREA`                         | Manufacturing Facility - Low bay area                                                           |                                                               |
| `MUSEUM_GENERAL_EXHIBITION_AREA`                              | Museum - General exhibition area                                                                |                                                               |
| `MUSEUM_RESTORATION_ROOM`                                     | Museum - Restoration room                                                                       |                                                               |
| `POST_OFFICE_SORTING_AREA`                                    | Post Office â€” Sorting Area                                                                    |                                                               |
| `RELIGIOUS_FACILITY_FELLOWSHIP_HALL`                          | Religious Facility - Fellowship hall                                                            |                                                               |
| `RELIGIOUS_FACILITY_WORSHIP_PULPIT_CHOIR_AREA`                | Religious Facility - Worship/pulpit/choir area                                                  |                                                               |
| `RETAIL_FACILITIES_DRESSING_FITTING_ROOM`                     | Retail Facilities - Dressing/fitting room                                                       |                                                               |
| `RETAIL_FACILITIES_MALL_CONCOURSE`                            | Retail Facilities - Mall concourse                                                              |                                                               |
| `SPORTS_ARENA_PLAYING_AREA_CLASS_I_FACILITY`                  | Sports Arena â€” Playing Area - Class I facility                                                |                                                               |
| `SPORTS_ARENA_PLAYING_AREA_CLASS_II_FACILITY`                 | Sports Arena â€” Playing Area - Class II facility                                               |                                                               |
| `SPORTS_ARENA_PLAYING_AREA_CLASS_III_FACILITY`                | Sports Arena â€” Playing Area - Class III facility                                              |                                                               |
| `SPORTS_ARENA_PLAYING_AREA_CLASS_IV_FACILITY`                 | Sports Arena â€” Playing Area - Class IV facility                                               |                                                               |
| `TRANSPORTATION_FACILITY_BAGGAGE_CAROUSEL_AREA`               | Transportation Facility - Baggage/carousel area                                                 |                                                               |
| `TRANSPORTATION_FACILITY_AIRPORT_CONCOURSE`                   | Transportation Facility - Airport concourse                                                     |                                                               |
| `TRANSPORTATION_FACILITY_TICKET_COUNTER`                      | Transportation Facility - Ticket counter                                                        |                                                               |
| `WAREHOUSE_STORAGE_AREA_MEDIUM_TO_BULKY_PALLETIZED_ITEMS`     | Warehouse â€” Storage Area - Medium to bulky, palletized items                                  |                                                               |
| `WAREHOUSE_STORAGE_AREA_SMALLER_HAND_CARRIED_ITEMS`           | Warehouse â€” Storage Area - Smaller, hand-carried items                                        |                                                               |

# OutputSchemaOptions2019ASHRAE901
|           Enumerator           |            Description             | Notes |
| ------------------------------ | ---------------------------------- | ----- |
| `OUTPUT_SCHEMA_ASHRAE901_2019` | Output schema for ASHRAE 90.1 2019 |       |

# PrescribedScheduleOptions2019ASHRAE901
|    Enumerator    |                                                     Description                                                     | Notes |
| ---------------- | ------------------------------------------------------------------------------------------------------------------- | ----- |
| `NOT_APPLICABLE` | No prescribed schedules for Appendix G of ASHRAE Standard 90.1-2019. This field may be relavent for other rulesets. |       |

# RulesetModelOptions2019ASHRAE901
|   Enumerator   |                                                             Description                                                              | Notes |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ----- |
| `BASELINE_0`   | The building model that corresponds with the Baseline Buildings Performance column of Appendix G Table G3.1 with no rotation         |       |
| `BASELINE_90`  | The building model that corresponds with the Baseline Buildings Performance column of Appendix G Table G3.1 with 90 degree rotation  |       |
| `BASELINE_180` | The building model that corresponds with the Baseline Buildings Performance column of Appendix G Table G3.1 with 180 degree rotation |       |
| `BASELINE_270` | The building model that corresponds with the Baseline Buildings Performance column of Appendix G Table G3.1 with 270 degree rotation |       |

# ServiceWaterHeatingSpaceOptions2019ASHRAE901
|            Enumerator             |              Description               | Notes |
| --------------------------------- | -------------------------------------- | ----- |
| `AUTOMOTIVE_FACILITY`             | Automotive facility                    |       |
| `CONVENIENCE_STORE`               | Convenience store                      |       |
| `CONVENTION_CENTER`               | Convention center                      |       |
| `COURTHOUSE`                      | Courthouse                             |       |
| `DINING_BAR_LOUNGE_LEISURE`       | Dining: Bar lounge/leisure             |       |
| `DINING_CAFETERIA_FAST_FOOD`      | Dining: Cafeteria/fast food            |       |
| `DINING_FAMILY`                   | Dining: Family                         |       |
| `DORMITORY`                       | Dormitory                              |       |
| `EXERCISE_CENTER`                 | Exercise center                        |       |
| `FIRE_STATION`                    | Fire station                           |       |
| `GROCERY_STORE`                   | Grocery store                          |       |
| `GYMNASIUM`                       | Gymnasium                              |       |
| `HEALTH_CARE_CLINIC`              | Health-care clinic                     |       |
| `HOSPITAL_AND_OUTPATIENT_SURGERY` | Hospital and outpatient surgery center |       |
| `HOTEL`                           | Hotel                                  |       |
| `LIBRARY`                         | Library                                |       |
| `MANUFACTURING_FACILITY`          | Manufacturing facility                 |       |
| `MOTEL`                           | Motel                                  |       |
| `MOTION_PICTURE_THEATER`          | Motion picture theater                 |       |
| `MULTIFAMILY`                     | Multifamily                            |       |
| `MUSEUM`                          | Museum                                 |       |
| `OFFICE`                          | Office                                 |       |
| `PARKING_GARAGE`                  | Parking garage                         |       |
| `PENITENTIARY`                    | Penitentiary                           |       |
| `PERFORMING_ARTS_THEATER`         | Performing arts theater                |       |
| `POLICE_STATION`                  | Police station                         |       |
| `POST_OFFICE`                     | Post office                            |       |
| `RELIGIOUS_FACILITY`              | Religious facility                     |       |
| `RETAIL`                          | Retail                                 |       |
| `SCHOOL_UNIVERSITY`               | School/university                      |       |
| `SPORTS_ARENA`                    | Sports arena                           |       |
| `TOWN_HALL`                       | Town hall                              |       |
| `TRANSPORTATION`                  | Transportation                         |       |
| `WAREHOUSE`                       | Warehouse                              |       |
| `WORKSHOP`                        | Workshop                               |       |
| `ALL_OTHERS`                      | All others                             |       |

# SubsurfaceFrameOptions2019ASHRAE901
|        Enumerator        |          Description           | Notes |
| ------------------------ | ------------------------------ | ----- |
| `ALUMINUM_WITHOUT_BREAK` | Aluminum without Thermal Break |       |
| `ALUMINUM_WITH_BREAK`    | Aluminum with Thermal Break    |       |
| `REINFORCED_VINYL`       | Reninforced Vinyl              |       |
| `ALUMINUM_CLAD_WOOD`     | Aluminum Clad Wood             |       |
| `WOOD`                   | Wood                           |       |
| `VINYL`                  | Vinyl                          |       |
| `STRUCTURAL_GLAZING`     | Structural Glazing             |       |
| `METAL_WITHOUT_BREAK`    | Metal without Thermal Break    |       |
| `METAL_WITH_BREAK`       | Metal with Thermal Break       |       |
| `FIBERGLASS`             | Fiberglass                     |       |
| `OTHER`                  | Other                          |       |

# SubsurfaceSubclassificationOptions2019ASHRAE901
|       Enumerator        |                                                                                        Description                                                                                        | Notes |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `METAL_COILING_DOOR`    | an upward-acting, nonswinging door assembly consisting of interlocking horizontal slats or sheets that, upon opening the door, roll up around a horizontal barrel above the door opening. |       |
| `NONSWINGING_DOOR`      | roll-up, metal coiling, sliding, and any other door that is not a swinging door.                                                                                                          |       |
| `SECTIONAL_GARAGE_DOOR` | an upward-acting, nonswinging door assembly made of two or more horizontal panels hinged together vertically.                                                                             |       |
| `SWINGING_DOOR`         | a door having an operable opaque panel with hinges or pivots on one side.                                                                                                                 |       |
| `SPANDREL_GLASS`        | opaque glass that conceals structural building components from being visible from the exterior of the building                                                                            |       |
| `GLASS_BLOCK`           | a translucent, hollow or solid block of glass for glazing openings or constructing partitions                                                                                             |       |
| `OTHER`                 | other subclassifications                                                                                                                                                                  |       |

# VentilationSpaceOptions2019ASHRAE901
|                                                        Enumerator                                                        |                                                        Description                                                         | Notes |
| ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| `ANIMAL_FACILITIES_ANIMAL_EXAM_ROOM_VETERINARY_OFFICE`                                                                   | Animal Facilities - Animal exam room (veterinary office)                                                                   |       |
| `ANIMAL_FACILITIES_ANIMAL_IMAGING_MRI_CT_PET`                                                                            | Animal Facilities - Animal imaging (MRI/CT/PET)                                                                            |       |
| `ANIMAL_FACILITIES_ANIMAL_OPERATING_ROOMS`                                                                               | Animal Facilities - Animal operating rooms                                                                                 |       |
| `ANIMAL_FACILITIES_ANIMAL_POSTOPERATIVE_RECOVERY_ROOM`                                                                   | Animal Facilities - Animal postoperative recovery room                                                                     |       |
| `ANIMAL_FACILITIES_ANIMAL_PREPARATION_ROOMS`                                                                             | Animal Facilities - Animal preparation rooms                                                                               |       |
| `ANIMAL_FACILITIES_ANIMAL_PROCEDURE_ROOM`                                                                                | Animal Facilities - Animal procedure room                                                                                  |       |
| `ANIMAL_FACILITIES_ANIMAL_SURGERY_SCRUB`                                                                                 | Animal Facilities - Animal surgery scrub                                                                                   |       |
| `ANIMAL_FACILITIES_LARGE_ANIMAL_HOLDING_ROOM`                                                                            | Animal Facilities - Large-animal holding room                                                                              |       |
| `ANIMAL_FACILITIES_NECROPSY`                                                                                             | Animal Facilities - Necropsy                                                                                               |       |
| `ANIMAL_FACILITIES_SMALL_ANIMAL_CAGE_ROOM_STATIC_CAGES`                                                                  | Animal Facilities - Small-animal-cage room (static cages)                                                                  |       |
| `ANIMAL_FACILITIES_SMALL_ANIMAL_CAGE_ROOM_VENTILATED_CAGES`                                                              | Animal Facilities - Small-animal-cage room (ventilated cages)                                                              |       |
| `CORRECTIONAL_FACILITIES_BOOKING_WAITING`                                                                                | Correctional Facilities - Booking/waiting                                                                                  |       |
| `CORRECTIONAL_FACILITIES_CELL`                                                                                           | Correctional Facilities - Cell                                                                                             |       |
| `CORRECTIONAL_FACILITIES_DAYROOM`                                                                                        | Correctional Facilities - Dayroom                                                                                          |       |
| `CORRECTIONAL_FACILITIES_GUARD_STATIONS`                                                                                 | Correctional Facilities - Guard stations                                                                                   |       |
| `EDUCATIONAL_FACILITIES_ART_CLASSROOM`                                                                                   | Educational Facilities - Art classroom                                                                                     |       |
| `EDUCATIONAL_FACILITIES_CLASSROOMS_AGES_5_TO_8`                                                                          | Educational Facilities - Classrooms (ages 5 to 8)                                                                          |       |
| `EDUCATIONAL_FACILITIES_CLASSROOMS_AGE_9_PLUS`                                                                           | Educational Facilities - Classrooms (age 9 plus)                                                                           |       |
| `EDUCATIONAL_FACILITIES_COMPUTER_LAB`                                                                                    | Educational Facilities - Computer lab                                                                                      |       |
| `EDUCATIONAL_FACILITIES_DAYCARE_SICKROOM`                                                                                | Educational Facilities - Daycare sickroom                                                                                  |       |
| `EDUCATIONAL_FACILITIES_DAYCARE_THROUGH_AGE_4`                                                                           | Educational Facilities - Daycare (through age 4)                                                                           |       |
| `EDUCATIONAL_FACILITIES_LECTURE_CLASSROOM`                                                                               | Educational Facilities - Lecture classroom                                                                                 |       |
| `EDUCATIONAL_FACILITIES_LECTURE_HALL_FIXED_SEATS`                                                                        | Educational Facilities - Lecture hall (fixed seats)                                                                        |       |
| `EDUCATIONAL_FACILITIES_LIBRARIES`                                                                                       | Educational Facilities - Libraries                                                                                         |       |
| `EDUCATIONAL_FACILITIES_MEDIA_CENTER`                                                                                    | Educational Facilities - Media center                                                                                      |       |
| `EDUCATIONAL_FACILITIES_MULTIUSE_ASSEMBLY`                                                                               | Educational Facilities - Multiuse assembly                                                                                 |       |
| `EDUCATIONAL_FACILITIES_MUSIC_THEATER_DANCE`                                                                             | Educational Facilities - Music/theater/dance                                                                               |       |
| `EDUCATIONAL_FACILITIES_SCIENCE_LABORATORIES`                                                                            | Educational Facilities - Science laboratories                                                                              |       |
| `EDUCATIONAL_FACILITIES_UNIVERSITY_COLLEGE_LABORATORIES`                                                                 | Educational Facilities - University/college laboratories                                                                   |       |
| `EDUCATIONAL_FACILITIES_WOOD_METAL_SHOP`                                                                                 | Educational Facilities - Wood/metal shop                                                                                   |       |
| `FOOD_AND_BEVERAGE_SERVICE_BARS_COCKTAIL_LOUNGES`                                                                        | Food and Beverage Service - Bars, cocktail lounges                                                                         |       |
| `FOOD_AND_BEVERAGE_SERVICE_CAFETERIA_FAST_FOOD_DINING`                                                                   | Food and Beverage Service - Cafeteria/fast-food dining                                                                     |       |
| `FOOD_AND_BEVERAGE_SERVICE_KITCHEN_COOKING`                                                                              | Food and Beverage Service - Kitchen (cooking)                                                                              |       |
| `FOOD_AND_BEVERAGE_SERVICE_RESTAURANT_DINING_ROOMS`                                                                      | Food and Beverage Service - Restaurant dining rooms                                                                        |       |
| `FOOD_AND_BEVERAGE_SERVICE_GENERAL_BREAK_ROOMS`                                                                          | Food and Beverage Service, General - Break rooms                                                                           |       |
| `FOOD_AND_BEVERAGE_SERVICE_GENERAL_COFFEE_STATIONS`                                                                      | Food and Beverage Service, General - Coffee stations                                                                       |       |
| `FOOD_AND_BEVERAGE_SERVICE_GENERAL_CONFERENCE_MEETING`                                                                   | Food and Beverage Service, General - Conference/meeting                                                                    |       |
| `FOOD_AND_BEVERAGE_SERVICE_GENERAL_CORRIDORS`                                                                            | Food and Beverage Service, General - Corridors                                                                             |       |
| `FOOD_AND_BEVERAGE_SERVICE_GENERAL_OCCUPIABLE_STORAGE_ROOMS_FOR_LIQUIDS_OR_GELS`                                         | Food and Beverage Service, General - Occupiable storage rooms for liquids or gels                                          |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_BARRACKS_SLEEPING_AREAS`                                                              | Hotels, Motels, Resorts, Dormitories - Barracks sleeping areas                                                             |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_BEDROOM_LIVING_ROOM`                                                                  | Hotels, Motels, Resorts, Dormitories - Bedroom/living room                                                                 |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_LAUNDRY_ROOMS_CENTRAL`                                                                | Hotels, Motels, Resorts, Dormitories - Laundry rooms, central                                                              |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_LAUNDRY_ROOMS_WITHIN_DWELLING_UNITS`                                                  | Hotels, Motels, Resorts, Dormitories - Laundry rooms within dwelling units                                                 |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_LOBBIES_PREFUNCTION`                                                                  | Hotels, Motels, Resorts, Dormitories - Lobbies/prefunction                                                                 |       |
| `HOTELS_MOTELS_RESORTS_DORMITORIES_MULTIPURPOSE_ASSEMBLY`                                                                | Hotels, Motels, Resorts, Dormitories - Multipurpose assembly                                                               |       |
| `MISCELLANEOUS_SPACES_BANKS_OR_BANK_LOBBIES`                                                                             | Miscellaneous Spaces - Banks or bank lobbies                                                                               |       |
| `MISCELLANEOUS_SPACES_BANK_VAULTS_SAFE_DEPOSIT`                                                                          | Miscellaneous Spaces - Bank vaults/safe deposit                                                                            |       |
| `MISCELLANEOUS_SPACES_COMPUTER_NOT_PRINTING`                                                                             | Miscellaneous Spaces - Computer (not printing)                                                                             |       |
| `MISCELLANEOUS_SPACES_FREEZER_AND_REFRIGERATED_SPACES`                                                                   | Miscellaneous Spaces - Freezer and refrigerated spaces (<50Â°F [10Â°C])                                                    |       |
| `MISCELLANEOUS_SPACES_MANUFACTURING_WHERE_HAZARDOUS_MATERIALS_ARE_NOT_USED`                                              | Miscellaneous Spaces - Manufacturing where hazardous materials are not used                                                |       |
| `MISCELLANEOUS_SPACES_MANUFACTURING_WHERE_HAZARDOUS_MATERIALS_ARE_USED_EXCLUDES_HEAVY_INDUSTRIAL_AND_CHEMICAL_PROCESSES` | Miscellaneous Spaces - Manufacturing where hazardous materials are used (excludes heavy industrial and chemical processes) |       |
| `MISCELLANEOUS_SPACES_PHARMACY_PREP_AREA`                                                                                | Miscellaneous Spaces - Pharmacy (prep. area)                                                                               |       |
| `MISCELLANEOUS_SPACES_PHOTO_STUDIOS`                                                                                     | Miscellaneous Spaces - Photo studios                                                                                       |       |
| `MISCELLANEOUS_SPACES_SHIPPING_RECEIVING`                                                                                | Miscellaneous Spaces - Shipping/receiving                                                                                  |       |
| `MISCELLANEOUS_SPACES_SORTING_PACKING_LIGHT_ASSEMBLY`                                                                    | Miscellaneous Spaces - Sorting, packing, light assembly                                                                    |       |
| `MISCELLANEOUS_SPACES_TELEPHONE_CLOSETS`                                                                                 | Miscellaneous Spaces - Telephone closets                                                                                   |       |
| `MISCELLANEOUS_SPACES_TRANSPORTATION_WAITING`                                                                            | Miscellaneous Spaces - Transportation waiting                                                                              |       |
| `MISCELLANEOUS_SPACES_WAREHOUSES`                                                                                        | Miscellaneous Spaces - Warehouses                                                                                          |       |
| `OFFICE_BUILDINGS_BREAKROOMS`                                                                                            | Office Buildings - Breakrooms                                                                                              |       |
| `OFFICE_BUILDINGS_MAIN_ENTRY_LOBBIES`                                                                                    | Office Buildings - Main entry lobbies                                                                                      |       |
| `OFFICE_BUILDINGS_OCCUPIABLE_STORAGE_ROOMS_FOR_DRY_MATERIALS`                                                            | Office Buildings - Occupiable storage rooms for dry materials                                                              |       |
| `OFFICE_BUILDINGS_OFFICE_SPACE`                                                                                          | Office Buildings - Office space                                                                                            |       |
| `OFFICE_BUILDINGS_RECEPTION_AREAS`                                                                                       | Office Buildings - Reception areas                                                                                         |       |
| `OFFICE_BUILDINGS_TELEPHONE_DATA_ENTRY`                                                                                  | Office Buildings - Telephone/data entry                                                                                    |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_BIRTHING_ROOM`                                                                        | Outpatient Health Care Facilities - Birthing room                                                                          |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_CLASS_1_IMAGING_ROOMS`                                                                | Outpatient Health Care Facilities - Class 1 imaging rooms                                                                  |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_DENTAL_OPERATORY`                                                                     | Outpatient Health Care Facilities - Dental operatory                                                                       |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_GENERAL_EXAMINATION_ROOM`                                                             | Outpatient Health Care Facilities - General examination room                                                               |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_OTHER_DENTAL_TREATMENT_AREAS`                                                         | Outpatient Health Care Facilities - Other dental treatment areas                                                           |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PHYSICAL_THERAPY_EXERCISE_AREA`                                                       | Outpatient Health Care Facilities - Physical therapy exercise area                                                         |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PHYSICAL_THERAPY_INDIVIDUAL_ROOM`                                                     | Outpatient Health Care Facilities - Physical therapy individual room                                                       |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PHYSICAL_THERAPEUTIC_POOL_AREA`                                                       | Outpatient Health Care Facilities - Physical therapeutic pool area                                                         |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PROSTHETICS_AND_ORTHOTICS_ROOM`                                                       | Outpatient Health Care Facilities - Prosthetics and orthotics room                                                         |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PSYCHIATRIC_CONSULTATION_ROOM`                                                        | Outpatient Health Care Facilities - Psychiatric consultation room                                                          |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PSYCHIATRIC_EXAMINATION_ROOM`                                                         | Outpatient Health Care Facilities - Psychiatric examination room                                                           |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PSYCHIATRIC_GROUP_ROOM`                                                               | Outpatient Health Care Facilities - Psychiatric group room                                                                 |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_PSYCHIATRIC_SECLUSION_ROOM`                                                           | Outpatient Health Care Facilities - Psychiatric seclusion room                                                             |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_SPEECH_THERAPY_ROOM`                                                                  | Outpatient Health Care Facilities - Speech therapy room                                                                    |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_URGENT_CARE_EXAMINATION_ROOM`                                                         | Outpatient Health Care Facilities - Urgent care examination room                                                           |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_URGENT_CARE_OBSERVATION_ROOM`                                                         | Outpatient Health Care Facilities - Urgent care observation room                                                           |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_URGENT_CARE_TREATMENT_ROOM`                                                           | Outpatient Health Care Facilities - Urgent care treatment room                                                             |       |
| `OUTPATIENT_HEALTH_CARE_FACILITIES_URGENT_CARE_TRIAGE_ROOM`                                                              | Outpatient Health Care Facilities - Urgent care triage room                                                                |       |
| `PUBLIC_ASSEMBLY_SPACES_AUDITORIUM_SEATING_AREA`                                                                         | Public Assembly Spaces - Auditorium seating area                                                                           |       |
| `PUBLIC_ASSEMBLY_SPACES_COURTROOMS`                                                                                      | Public Assembly Spaces - Courtrooms                                                                                        |       |
| `PUBLIC_ASSEMBLY_SPACES_LEGISLATIVE_CHAMBERS`                                                                            | Public Assembly Spaces - Legislative chambers                                                                              |       |
| `PUBLIC_ASSEMBLY_SPACES_LIBRARIES`                                                                                       | Public Assembly Spaces - Libraries                                                                                         |       |
| `PUBLIC_ASSEMBLY_SPACES_LOBBIES`                                                                                         | Public Assembly Spaces - Lobbies                                                                                           |       |
| `PUBLIC_ASSEMBLY_SPACES_MUSEUMS_CHILDRENS`                                                                               | Public Assembly Spaces - Museums (children's)                                                                              |       |
| `PUBLIC_ASSEMBLY_SPACES_MUSEUMS_GALLERIES`                                                                               | Public Assembly Spaces - Museums/galleries                                                                                 |       |
| `PUBLIC_ASSEMBLY_SPACES_PLACES_OF_RELIGIOUS_WORSHIP`                                                                     | Public Assembly Spaces - Places of religious worship                                                                       |       |
| `RETAIL_SALES_EXCEPT_OTHER_SPECIFIC_RETAIL`                                                                              | Retail - Sales (except other specific retail)                                                                              |       |
| `RETAIL_BARBERSHOP`                                                                                                      | Retail - Barbershop                                                                                                        |       |
| `RETAIL_BEAUTY_AND_NAIL_SALONS`                                                                                          | Retail - Beauty and nail salons                                                                                            |       |
| `RETAIL_COIN_OPERATED_LAUNDRIES`                                                                                         | Retail - Coin-operated laundries                                                                                           |       |
| `RETAIL_MALL_COMMON_AREAS`                                                                                               | Retail - Mall common areas                                                                                                 |       |
| `RETAIL_PET_SHOPS_ANIMAL_AREAS`                                                                                          | Retail - Pet shops (animal areas)                                                                                          |       |
| `RETAIL_SUPERMARKET`                                                                                                     | Retail - Supermarket                                                                                                       |       |
| `SPORTS_AND_ENTERTAINMENT_BOWLING_ALLEY_SEATING`                                                                         | Sports and Entertainment - Bowling alley (seating)                                                                         |       |
| `SPORTS_AND_ENTERTAINMENT_DISCO_DANCE_FLOORS`                                                                            | Sports and Entertainment - Disco/dance floors                                                                              |       |
| `SPORTS_AND_ENTERTAINMENT_GAMBLING_CASINOS`                                                                              | Sports and Entertainment - Gambling casinos                                                                                |       |
| `SPORTS_AND_ENTERTAINMENT_GAME_ARCADES`                                                                                  | Sports and Entertainment - Game arcades                                                                                    |       |
| `SPORTS_AND_ENTERTAINMENT_GYM_SPORTS_ARENA_PLAY_AREA`                                                                    | Sports and Entertainment - Gym, sports arena (play area)                                                                   |       |
| `SPORTS_AND_ENTERTAINMENT_HEALTH_CLUB_AEROBICS_ROOM`                                                                     | Sports and Entertainment - Health club/aerobics room                                                                       |       |
| `SPORTS_AND_ENTERTAINMENT_HEALTH_CLUB_WEIGHT_ROOMS`                                                                      | Sports and Entertainment - Health club/weight rooms                                                                        |       |
| `SPORTS_AND_ENTERTAINMENT_SPECTATOR_AREAS`                                                                               | Sports and Entertainment - Spectator areas                                                                                 |       |
| `SPORTS_AND_ENTERTAINMENT_STAGES_STUDIOS`                                                                                | Sports and Entertainment - Stages, studios                                                                                 |       |
| `SPORTS_AND_ENTERTAINMENT_SWIMMING_POOL_AND_DECK`                                                                        | Sports and Entertainment - Swimming (pool and deck)                                                                        |       |
| `TRANSIENT_RESIDENTIAL_COMMON_CORRIDORS`                                                                                 | Transient Residential - Common corridors                                                                                   |       |
| `TRANSIENT_RESIDENTIAL_DWELLING_UNIT`                                                                                    | Transient Residential - Dwelling unit                                                                                      |       |

# VerticalFenestrationBuildingAreaOptions2019ASHRAE901
|            Enumerator             |            Description            | Notes |
| --------------------------------- | --------------------------------- | ----- |
| `GROCERY_STORE`                   | Grocery store                     |       |
| `HEALTHCARE_OUTPATIENT`           | Healthcare (outpatient)           |       |
| `HOSPITAL`                        | Hospital                          |       |
| `HOTEL_MOTEL_SMALL`               | Hotel/motel - Small               |       |
| `HOTEL_MOTEL_LARGE`               | Hotel/motel - Large               |       |
| `OFFICE_SMALL`                    | Office - Small                    |       |
| `OFFICE_MEDIUM`                   | Office - Medium                   |       |
| `OFFICE_LARGE`                    | Office - Large                    |       |
| `RESTAURANT_QUICK_SERVICE`        | Restaurant (quick service)        |       |
| `RESTAURANT_FULL_SERVICE`         | Restaurant (full service)         |       |
| `RETAIL_STAND_ALONE`              | Retail (stand alone)              |       |
| `RETAIL_STRIP_MALL`               | Retail (strip mall)               |       |
| `SCHOOL_PRIMARY`                  | School (primary)                  |       |
| `SCHOOL_SECONDARY_AND_UNIVERSITY` | School (secondary and university) |       |
| `WAREHOUSE_NONREFRIGERATED`       | Warehouse (nonrefrigerated)       |       |
| `OTHER`                           | Other                             |       |

