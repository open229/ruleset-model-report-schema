import schema229
import os

'''
Unit tests
'''

def test_resolve_ref():
    schema = schema229.A229Schema(os.path.join(os.path.dirname(__file__),'..','build',"schema","ASHRAE229.schema.json"))

    node = schema.resolve_ref("ASHRAE229.schema.json#/definitions/ASHRAE229")
    assert('title' not in node)

def test_get_schema_node():
    schema = schema229.A229Schema(os.path.join(os.path.dirname(__file__),'..','build',"schema","ASHRAE229.schema.json"))

    # Root node
    node = schema.get_schema_node([])
    assert('version' in node)
