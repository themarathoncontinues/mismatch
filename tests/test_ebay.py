import mock
import pickle

from bs4 import BeautifulSoup

from src.ebay.search import (
    get_products
)


def test_get_products():

    fp = open('tests/ebay_search_results.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()
    soupified = BeautifulSoup(tmp, 'html.parser')
    result = get_products(soupified)

    assert isinstance(result, list)
    assert len(result) > 0
