import json
import mock
import datetime

from bs4 import BeautifulSoup

from src.aliexpress.aliexpress import (
    construct_url,
    get_soup,
    find_items_element,
    parse_javascript,
    extract_metadata,
    _parse_prices
)

DT_CLASS = datetime.datetime

def mock_datetime_now(target, dt):
    class DatetimeSubclass(type):
        @classmethod
        def __instancecheck__(mcs, obj):
            return isinstance(obj, DT_CLASS)

    class MockedDatetime(DT_CLASS):
        @classmethod
        def now(cls):
            return target.replace(tzinfo=None)

        @classmethod
        def utc(cls):
            return target

    mock_dt_now = DatetimeSubclass('datetime', (MockedDatetime,), {})

    return mock.patch.object(dt, 'datetime', mock_dt_now)


def test_construct_aliexpress_url():
    TARGET = datetime.datetime(2019, 8, 9)
    with mock_datetime_now(TARGET, datetime):

        PRODUCT = 'macbook pro touchbar'
        expected_result = \
            'https://aliexpress.com/wholesale?catId=0&initiative_id=SB_20190009000000&SearchText=' \
            'macbook+pro+touchbar&&switch_new_app=y'

        result = construct_url(product=PRODUCT)

        assert result == expected_result


def test_get_aliexpress_soup():
    IN_URL = \
        'https://aliexpress.com/wholesale?catId=0&initiative_id=SB_20190009000000&SearchText=' \
        'macbook+pro+touchbar&&switch_new_app=y'

    result = get_soup(IN_URL)

    assert type(result) == BeautifulSoup


def test_parse_prices():
    in_item = {
        'price': 'US $22 - 25.50'
    }
    expected_result = (22.0, 25.50)
    result = _parse_prices(in_item)

    assert result == expected_result
