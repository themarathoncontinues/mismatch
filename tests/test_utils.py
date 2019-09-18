from src.utils.url_util import cl_product

def test_cl_product():
    in_arg = "MY UNIT TEST"
    expected_out = 'my+unit+test'

    result = cl_product(in_arg)

    assert result == expected_out