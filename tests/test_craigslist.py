import codecs
import mock
import unittest

from bs4 import BeautifulSoup

from src.craigslist.craigslist import (
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


def test_get_soup():
    IN_URL = 'https://newyork.craigslist.org/search/sss?query=macbook+pro+touchbar&sort=rel'

    result = get_soup(IN_URL)

    assert type(result) == BeautifulSoup


def test_parse_soup():
    IN_HTML = codecs.open('tests/testData/test_soup.html', 'r')
    mock_soup = BeautifulSoup(IN_HTML.read(), features='html.parser')

    result = parse_soup(mock_soup)

    assert len(result) == 120
