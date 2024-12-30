# Ruleset Evaluation Schema and Related Schemas

ASHRAE Standard 229P includes several schemas being developed in this repository:

- Ruleset Evaluation Schema 
- Ruleset Checking Tool Software Testing Report Schema
- Ruleset Checking Tool Project Evaluation Report Schema
- Ruleset Project Description Generation Software Test Report Schema
- Simulation Output of Results for ASHRAE 901-2019 Schema

The public review version of the schemas are contained in the [main](https://github.com/open229/ruleset-model-description-schema/tree/main) branch. The [develop](https://github.com/open229/ruleset-model-description-schema) branch is the branch where work is continuing and will contain changes that are not part of the public review draft. The develop branch is also the default branch for all new changes.

See [the resources page](https://github.com/open229/ruleset-model-description-schema/blob/develop/RESOURCES.md) containing a collection of resources for developers of RPD generation tools. 

**Warning!**  As the proposed ASHRAE Standard 229P has not yet been published, the content in this repository is subject to change and should be considered unstable for application development.

More information on each schema is shown below.

### Ruleset Evaluation Schema 

The draft standard describes Ruleset Evaluation Schema (RES) as "schema that describes elements of building performance models that are relevant to rulesets" and is the primary schema of draft Standard 229P. An instance of the RES schema is called a Ruleset Project Description (RPD) and is a JSON file. This is the most detailed and extensive schema defined as part of draft 229P and consists of data elements organized into data groups that represent specific or summarized inputs and outputs typically found in building energy performance models. In addition, it contains compliance parameters which are "user inputs that used by the ruleset checking tool but are not directly used by the simulation engine". Compliance parameters include categorization of spaces or zones and many other types of information typically known by the energy modeler but not directly needed for a simulation. 

- [YAML](schema-source/ASHRAE229_extra.schema.yaml)
- [JSON schema file](docs229/ASHRAE229.schema.json)
- [markdown](docs229/ASHRAE229.schema.md)
- [PDF](docs229/ASHRAE229.schema.pdf)

The YAML source file includes some extra attributes for each data element that do not appear in the other formats. 

Also available is a [diagram](docs229/ASHRAE229_connect.pdf) that shows the relationship between the data groups.


### Ruleset Checking Tool Software Testing Report Schema

The Ruleset Checking Tool Software Testing Report Schema, often shortened to RCT Software Testing Report Schema, is the format of a JSON output file from the Ruleset Checking Tool (RCT) that shows the results of running a suite of tests through the RCT tool. These tests provide validation for the proper operation of the Ruleset Checking Tool. This schema is described in Normative Appendix B of draft Standard 229P. The JSON file following this schema would be produced whenever a Ruleset Checking Tool software was updated or when support of a new ruleset was added to a Ruleset Checking Tool.

- [YAML](schema-source/RCT_software_output_test_report.schema.yaml)
- [JSON schema file](docs229/RCT_software_output_test_report.schema.json)
- [markdown](docs229/RCT_software_output_test_report.schema.md)
- [PDF](docs229/RCT_software_output_test_report.schema.pdf)
- [Diagram](docs229/RCT_software_output_test_report_connect.pdf)

### Ruleset Checking Tool Project Evaluation Report Schema

The Ruleset Checking Tool Project Evaluation Report Schema, often shortened to RCT Project Evaluation Report Schema, is the format of a JSON output file from the Ruleset Checking Tool (RCT) that shows the resutls of a specific building project being run through a Ruleset Checking Tool software. These results are typically based on comparing the user, proposed and baseline mdoels represented in the Ruleset Project Description file(s). These are specific for 90.1 and other rulesets would have other terms for these different models. The Ruleset Checking Tool has a long list of rules that must be followed for each ruleset and this output file describes if individual models have followed the rules correctly. This schema is described in Normative Appendix C of draft Standard 229P. The JSON file following this schema would be produced by Ruleset Checking Tool each time a project is provided as a Ruleset Poject Description file(s) following the format described in the Ruleset Evaluation Schema.

- [YAML](schema-source/RCT_project_output_test_report.schema.yaml)
- [JSON schema file](docs229/RCT_project_output_test_report.schema.json)
- [markdown](docs229/RCT_project_output_test_report.schema.md)
- [PDF](docs229/RCT_project_output_test_report.schema.pdf)
- [Diagram](docs229/RCT_project_output_test_report_connect.pdf)

### Ruleset Project Description Generation Software Test Report Schema

The draft standard describes Ruleset Project Description Generation Software as "software used to create a ruleset project description based on one or more building performance models.  Informative note: Ruleset project description generation software may be part of the building performance modeling software or a separate software tool." The Ruleset Project Description Generation Software needs to follow certain tests described in draft Standard 229P in order to show that is creating the Ruleset Project Descriptions properly. The format for the results of this series of test are desribed in the Ruleset Project Description Generation Software Test Report Schema. The draft Standard 229P provides a description of the tests in Section 6.5 and then provides additional detail in Appendix E1.7 and Informative Appendix F.

- [YAML](schema-source/RPD_generation_software_test_report.schema.yaml)
- [JSON schema file](docs229/RPD_generation_software_test_report.schema.json)
- [markdown](docs229/RPD_generation_software_test_report.schema.md)
- [PDF](docs229/RPD_generation_software_test_report.schema.pdf)
- [Diagram](docs229/RPD_generation_software_test_report_connect.pdf)


### Simulation Output of Results for ASHRAE 90.1-2019 Schema

This is a sub-schema that may be referenced in the Ruleset Evaluation Schema which describes the outputs from a building energy simulation program that is needed to assess the rules in the ASHRAE Standard 90.1-2019 Performance Rating Method (Appendix G) ruleset. It is ruleset specific but may include outputs sufficient for rulesets besides 90.1-2019 Appendix G. Other outputs schemas for other rulesets may be developed in the future. It is not documented in the draft ASHRAE Standard 229P but is desribed below. Because it is referenced as part of the Ruleset Evaluation Schema, an instance of it would normally appear in a Ruleset Project Description file.

- [YAML](schema-source/Output2019ASHRAE901.schema.yaml)
- [JSON schema file](docs229/Output2019ASHRAE901.schema.json)
- [markdown](docs229/Output2019ASHRAE901.schema.md)
- [PDF](docs229/Output2019ASHRAE901.schema.pdf)
- [Diagram](docs229/Output2019ASHRAE901_connect.pdf)


Development Workflow
--------------------

### Setting Up Schema 229 for Development

For those who wish to develop the Schema229 repository directly, we are using the [Pipenv](https://github.com/pypa/pipenv) python package management and dependency tool.

Following are some considerations you should go through to configure your environment correctly for development and exploration.

1. **Install Pipenv**

    Be sure to install [Pipenv](https://github.com/pypa/pipenv) per the instructions from the website.

2. **Install Python and support multiple Python versions on one machine**

    If you don't desire to support multiple versions of Python, then you need only ensure that you have at least one version of Python installed. This project requires Python 3.6 or higher. Please see the [Python Website](https://www.python.org/) for installation instructions for your operating system.

    If you wish to support multiple versions of Python during development, there are several options. One simple option is to just ensure you start up your command prompt (i.e., shell) with the Python version you wish to develop with. However, for something more sophisticated, we recommend [mini-conda](https://docs.conda.io/en/latest/miniconda.html), a free minimal installer for Conda. Conda is an open-source package and environment management system that runs on Windows, macOS, and Linux.

    First [install mini-conda](https://docs.conda.io/en/latest/miniconda.html).
    Next [start conda](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html#starting-conda). After that, create an environment for the version of Python you would like to use with Pipenv and this project by typing the following at the shell:

    > conda create -n py36 python=3.6

    Note: these environments persist between usage so you only need to create the environment once.

    This will create a conda environment named "py36" that only has Python 3.6 (and its dependencies) installed.
    If you want to use Python 3.9, you could type `conda create -n py39 python=3.9`, for example.
    The `-n` flag is short for the `--name` of the new conda environment.
    You have a lot of freedom for the names provided there are no spaces or exotic characters.
    The `python=3.6` part specifies that the new conda environment will use Python version 3.6.
    You can create as many environments with differing versions of Python as you desire.

    Once the desired environments are created, you can activate an environment by typing:

    > conda activate py36

    When you are done with the environment, type:

    > conda deactivate

    ... or simply close your command shell when done.

    Once you've created the environment you desire, on subsequent use, you just need to start conda and activate the environment you want.

    Select the desired Python environment and activate it before proceeding to the next step.

3. **Install dependencies**

    To install dependencies, go to the root folder of this repository and type:

    > pipenv install --dev -e .

    This will install all of the normal and developer dependencies.
    If you have done this previously and there are no changes to the library versions being used, nothing will happen.

4. **Use the project**

    To run the various scripts and commands of the project, you can use the [DoIt!](https://pydoit.org/) file as follows:

    > pipenv run doit

    The first part of the command, `pipenv run`, uses Pipenv to place the remaining part of the command within a Python virtual environment with all dependencies setup.
    The second part of the command, `doit`, runs all of the tasks available in the `dodo.py` file.

5. **Using an editor**

    Of course, you can use any editor you desire to edit or explore the Python code and schema documents in our repository.
    However, we recommend [Visual Studio Code](https://code.visualstudio.com/) because of its strong Python integration.
    To get Visual Studio Code to work with Pipenv, first follow steps 1-3 above.
    Next, if you are on macOS and do not have command-line integration, [follow these instructions](https://code.visualstudio.com/docs/setup/mac#_launching-from-the-command-line), restart your shell, perform steps 1-3 and return here.
    If you are on Windows, the `code` command is already integrated into your shell.

    From within your running Python environment, type:

    > pipenv shell

    This activates the virtual environment for Pipenv.

    > code .

    This launches Visual Studio Code from within your Pipenv environment.
    At the bottom left, choose the Python version you wish to use with the given environment.
    You're now ready to develop using Visual Studio Code!