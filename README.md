# Ruleset Model Report Schema

A schema development package consistent with ASHRAE Standard 229P.

The public review version of the schema is contained in the [main](https://github.com/open229/ruleset-model-description-schema/tree/main) branch. The [develop](https://github.com/open229/ruleset-model-description-schema) branch is the branch where work is continuing and will contain changes that are not part of the public review draft. The develop branch is also the default branch for all new changes.

See [the resources page](https://github.com/open229/ruleset-model-description-schema/blob/develop/RESOURCES.md) containing a collection of resources for developers of RMD generation tools. 

**Warning!**  As the proposed ASHRAE Standard 229P has not yet been published, the content in this repository is subject to change and should be considered unstable for application development.

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