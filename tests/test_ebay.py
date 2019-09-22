import datetime
import mock
import pickle

from bs4 import BeautifulSoup

from src.ebay.search import (
    get_products,
    get_product_info,
    _get_product_name,
    _get_product_status,
    _get_product_shipping,
    _get_product_price,
    _get_product_url
)


def test_get_products():

    fp = open('tests/testData/ebay_get_products.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = get_products(soupified)

    assert isinstance(result, list)
    assert len(result) > 0


def test_get_product_info():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = get_product_info(soupified)


    assert isinstance(result, dict)
    assert {'name', 'status', 'price', 'shipping', 'url'} == set(result.keys())


def test_get_product_name():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = _get_product_name(soupified)

    assert isinstance(result, str)
    assert result == 'Fenwick HMG Spinning Rod 1pcs 7\'0" Medium Heavy'

def test_get_product_status():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = _get_product_status(soupified)

    assert isinstance(result, dict)
    assert {'result', 'datestamp'} == set(result.keys())
    assert isinstance(result['datestamp'], datetime.datetime)

def test_get_product_shipping():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = _get_product_shipping(soupified)

    # this needs more test cases
    assert result == 0.0

def test_get_product_price():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = _get_product_price(soupified)

    assert isinstance(result, float)

def test_get_product_url():

    fp = open('tests/testData/ebay_get_product_info.pkl', 'rb')
    tmp = pickle.load(fp)
    fp.close()

    soupified = BeautifulSoup(tmp, 'html.parser')
    result = _get_product_url(soupified)

    assert isinstance(result, str)

