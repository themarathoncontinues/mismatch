import mock

from src.craigslist import (
    construct_url,
    get_soup,
    parse_soup
)


def test_construct_url():
    METRO = 'newyork'
    PRODUCT='macbook pro touchbar'
    expected_result = 'https://newyork.craigslist.org/search/sss?query=macbook+pro+touchbar&sort=rel'

    result = construct_url(metro=METRO, product=PRODUCT)

    assert result == expected_result