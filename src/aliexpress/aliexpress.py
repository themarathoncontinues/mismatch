import argparse
import bs4
import datetime
import json
import logging
import requests

from bs4 import BeautifulSoup

from src.constants import (
    ALI_BASE,
    ALI_BASE_SEARCH,
    ALI_BASE_TAIL
)

from src.utils.json_util import get_nested
from src.utils.url_util import (
    partition_product,
    shorten
)


logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)



def construct_url(product):
    """
    Construct a craigslist compliant URL for a given metro and product
    :param metro:
    :param product:
    :return:
    """
    current_date = datetime.datetime.now().strftime('%Y%M%d%H%M%S')
    serialize_product = partition_product(product)
    out_url = f'https://{ALI_BASE}{current_date}{ALI_BASE_SEARCH}{serialize_product}&{ALI_BASE_TAIL}'

    return out_url


def get_soup(request_url):
    """
    Using Url constructed, get top level html from aliexpress
    :param request_url:
    :return:
    """
    req = requests.get(request_url)
    req_content = req.content

    soup = BeautifulSoup(req_content, 'html.parser')

    return soup


def find_items_element(soup_html):
    """
    Create data structure of craiglist.org data from product request
    :param cl_soup:
    :return:
    """
    stringized = None
    products = soup_html.find_all('script', type='text/javascript')

    for product in products:
        if 'breadCrumb' in str(product):
            assert isinstance(product, bs4.element.Tag)
            stringized = str(product)
            logger.info('Items detected in <script>')

        else:
            logger.error('No items to extract')

    return stringized


def parse_javascript(string_js):
    """
    Hacky parser for javascript unique to aliexpress soup
    :param string_js:
    :return:
    """
    # Need to write a parser for these javascript components
    head, *parts = string_js.split(';')

    for part in parts:
        if 'window.runParams = ' in part:
            target = part.replace('window.runParams = ', '')
            items_string = target.split('"items"', 1)[1]
            stitch_strings = '{'+'"items"'+items_string

            items_dict = json.loads(stitch_strings)

            return items_dict


def extract_metadata(ali_items):
    """
    Parse items on aliexpress for metadata
    :param ali_items:
    :return:
    """
    all_items = []
    items = ali_items.get('items')

    current = {}
    for item in items:
        current['productName'] = get_nested(item, 'title')
        current['salePrice'] = _parse_prices(item)
        current['listingUrl'] = shorten(get_nested(item, 'productDetailUrl'))

        print(json.dumps(current, indent=4))
        all_items.append(current)


    return all_items


def _parse_prices(item):
    price = get_nested(item, 'price')
    if 'US $' in price:
        price = price.replace('US $', '').replace(',', '')

    if ' - ' in price:
        price = price.replace(' - ', ',')
        price_list = price.split(',')
        float_list = [float(x.replace(',','')) for x in price_list]
        price = tuple(float_list)

    if type(price) == str:
        price = float(price)

    return price


def run(args_dict): # pragma: no cover
    """
    Pseudo handler for aliexpress scraping from given args
    :param args_dict:
    :return:
    """
    product = args_dict['query']
    fout = construct_url(product)

    # Get URL constructed
    logger.info(f'Url constructed: {fout}')

    soup = get_soup(fout)
    items_string = find_items_element(soup)

    if items_string is None:
        logger.info(f'No items found for {product.upper()}')
    else:
        rule_based = parse_javascript(items_string)
        out_items = extract_metadata(rule_based)

        logger.info(f'{len(out_items)} listings for {product.upper()} found.')

        return out_items


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(
        description='Find prices for product based on metropolitan area'
    )
    parser.add_argument(
        '-q', '--query',
        required=True,
        type=str,
        help='Product to find prices for'
    )

    args_dict = vars(parser.parse_args())

    if args_dict['query'] is None:
        logger.error(' Please enter a product for search')

    run(args_dict)
