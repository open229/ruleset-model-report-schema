# EvaluationCriteriaOptions
| Enumerator  |                                                                     Description                                                                     | Notes |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `VALUE`     | Data elements whose values are required to match the corresponding value in the test case specification                                             |       |
| `PRESENT`   | Data elements that are required to be present, but whose values cannot be checked                                                                   |       |
| `REFERENCE` | Data elements whose values are required to match the name of the object that corresponds to the object that is named in the test case specification |       |

# TestOutcomeOptions
|    Enumerator     |                                                                                                                      Description                                                                                                                      | Notes |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| `MATCH`           | the required type of alignment (value, present, or reference) between the expected ruleset project description file and the ruleset project description file created by the candidate ruleset project description generation software is achieved     |       |
| `DIFFER`          | the required type of alignment (value, present, or reference) between the expected ruleset project description file and the ruleset project description file created by the candidate ruleset project description generation software is not achieved |       |
| `NOT_IMPLEMENTED` | the data element is not supported by the ruleset project description generation software                                                                                                                                                              |       |

# RulesetProjectDescriptionGenerationSoftwareTestReport
|                 Name                  |                                   Description                                   |      Data Type       | Units | Range | Req |                                  Notes                                  |
| ------------------------------------- | ------------------------------------------------------------------------------- | -------------------- | ----- | ----- | --- | ----------------------------------------------------------------------- |
| `generation_software_name`            | Name of the ruleset project description generation software                     | `String`             |       |       |     |                                                                         |
| `generation_software_version`         | Version of the ruleset project description generation software                  | `String`             |       |       |     | Version naming/numbering convention is not defined                      |
| `modeling_software_name`              | Name of the building performance modeling software used in testing              | `String`             |       |       |     |                                                                         |
| `modeling_software_version`           | Version of the building performance modeling software used in testing           | `String`             |       |       |     | Version naming/numbering convention as defined by the modeling software |
| `schema_version`                      | Version of the ruleset evaluation schema used in testing                        | `String`             |       |       |     | Version naming/numbering convention as defined by the schema            |
| `ruleset_name`                        | Name of the ruleset for which compliance is demonstrated                        | `String`             |       |       |     |                                                                         |
| `ruleset_checking_specification_name` | Name of the ruleset checking specification for which compliance is demonstrated | `String`             |       |       |     |                                                                         |
| `test_case_reports`                   | Results of the test cases                                                       | `[{TestCaseReport}]` |       |       |     |                                                                         |

# TestCaseReport
|         Name          |                                                                                          Description                                                                                           |        Data Type        | Units | Range | Req | Notes |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----- | ----- | --- | ----- |
| `test_id`             | ID corresponding to the ruleset checking specification test ID                                                                                                                                 | `String`                |       |       |     |       |
| `generated_file_name` | Name of the ruleset project description file generated by the ruleset project description generation software                                                                                  | `String`                |       |       |     |       |
| `files_utilized`      | Names of all user and software created files utilized by the ruleset project description generation software to produce the values used in creating the associated ruleset project description | `[String]`              |       |       |     |       |
| `specification_tests` | Specification tests of the test case                                                                                                                                                           | `[{SpecificationTest}]` |       |       |     |       |

# SpecificationTest
|         Name          |                                    Description                                    |           Data Type           | Units | Range | Req | Notes |
| --------------------- | --------------------------------------------------------------------------------- | ----------------------------- | ----- | ----- | --- | ----- |
| `data_path`           | Data path to locate instances of the test specification within the test case      | `String`                      |       |       |     |       |
| `evaluation_criteria` | Evaluation criteria used for the test specification                               | `<EvaluationCriteriaOptions>` |       |       |     |       |
| `test_results`        | Test results for various instances of the test specification within the test case | `[{TestResult}]`              |       |       |     |       |
| `notes`               | Notes on the test results for the test specification                              | `String`                      |       |       |     |       |

# TestResult
|      Name      |                                               Description                                               |       Data Type        | Units | Range | Req | Notes |
| -------------- | ------------------------------------------------------------------------------------------------------- | ---------------------- | ----- | ----- | --- | ----- |
| `instance_id`  | ID corresponding to the instance of the data group to which the test specification data element belongs | `String`               |       |       |     |       |
| `data_element` | Data element name corresponding to the test specification                                               | `String`               |       |       |     |       |
| `test_outcome` | Outcome of the test                                                                                     | `<TestOutcomeOptions>` |       |       |     |       |

