import schema229.validate
import schema229.markdown
import schema229.json_translate
import schema229.util_229
import os
from doit.tools import create_folder

BUILD_PATH = "build"
SOURCE_PATH = 'schema-source'
DOCS_PATH = os.path.join(BUILD_PATH, "docs")
SCHEMA_PATH = os.path.join(BUILD_PATH, "schema")


def collect_source_files():
    file_list = []
    for file_name in sorted(os.listdir('schema-source')):
        if '.schema.yaml' in file_name:
            file_list.append(os.path.join(SOURCE_PATH, file_name))
    return file_list


def collect_target_files(target_dir, extension):
    file_list = []
    for file_name in sorted(os.listdir('schema-source')):
        if '.schema.yaml' in file_name:
            file_name_root = os.path.splitext(os.path.splitext(file_name)[0])[0]
            file_list.append(os.path.join(target_dir, f'{file_name_root}.schema.{extension}'))
    return file_list


# Start 229-specific code ------------------------------------


def task_strip_extra_data_element_fields():
    """Strips specified data element fields"""
    return {
        'actions': [
            (
                schema229.util_229.strip_extra_data_element_fields_from_yaml,
                [
                    [
                        "RMD Test",
                        "AppG Used By TCDs",
                        "AppG P_RMD Equals U_RMD",
                        "AppG B_RMD Equals P_RMD"
                    ],
                    os.path.join(SOURCE_PATH, 'ASHRAE229_extra.schema.yaml'),
                    os.path.join(SOURCE_PATH, 'ASHRAE229.schema.yaml')
                ]
            )
        ],
        # Run this task only if either ASHRAE229_extra.schema.yaml has changed or
        # ASHRAE229.schema.yaml does not exist
        'file_dep': [os.path.join(SOURCE_PATH, 'ASHRAE229_extra.schema.yaml')],
        'targets': [os.path.join(SOURCE_PATH, 'ASHRAE229.schema.yaml')]
    }


# ------------------------------- End 229-specific code

def task_validate():
    """Validates source-schema against meta-schema"""
    return {
        'file_dep': [os.path.join("meta-schema", "meta.schema.json")] + collect_source_files(),
        'actions': [(schema229.validate.validate_dir, [SOURCE_PATH])]
    }


def task_doc():
    """Generates Markdown tables from source-schema"""
    return {
        'file_dep': collect_source_files() + [os.path.join('schema229', 'markdown.py')],
        'targets': collect_target_files(DOCS_PATH, 'md'),
        'task_dep': ['validate'],
        'actions': [
            (create_folder, [DOCS_PATH]),
            (schema229.markdown.write_dir, [SOURCE_PATH, DOCS_PATH])
        ],
        'clean': True
    }


def task_schema():
    """Generates JSON schema from source-schema"""
    return {
        'file_dep': collect_source_files(),
        'targets': collect_target_files(SCHEMA_PATH, 'json'),
        'task_dep': ['validate'],
        'actions': [
            (create_folder, [SCHEMA_PATH]),
            (schema229.json_translate.translate_dir, [SOURCE_PATH, SCHEMA_PATH])
        ],
        'clean': True
    }


# Start 229-Specific Code --------------------------------------
def task_remove_ashrae229_schema_yaml():
    """Removes schema-source/ASHRAE229.schema.yaml"""
    return {
        'actions': [
            (
                # There is no harm in running this task every time
                schema229.util_229.remove_file,
                [os.path.join('schema-source', 'ASHRAE229.schema.yaml')]
            )
        ]
    }
# ----------------------------- End 229-Specific Code


def task_test():
    """Performs unit tests and example file validation tests"""
    return {
        'task_dep': ['schema'],
        'actions': ['pytest -v test']
    }
