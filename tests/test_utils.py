from src.utils.json_util import (
    get_nested,
    set_nested
)

from src.utils.url_util import partition_product


# json_util unit tests
def test_get_nested():
    in_structure = {
        'get': {
            'nested': 'structure'
        }
    }

    expected_result = 'structure'
    result = get_nested(in_structure, 'get.nested')

    assert result == expected_result


def test_set_nested():
    in_structure = {
        'get': {
            'nested': 'structure'
        }
    }

    expected_result = {
        'get': {
            'nested': 'structure',
            'new': 'structure'
        }
    }
    result = set_nested(in_structure, 'get.new', 'structure')

    assert result == expected_result


# url_util unit tests
def test_cl_product():
    in_arg = "MY UNIT TEST"
    expected_out = 'my+unit+test'

    result = partition_product(in_arg)

    assert result == expected_out
