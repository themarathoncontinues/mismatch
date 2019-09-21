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

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

from src.utils.url_util import cl_product


def construct_url(product):
    """
    Construct a craigslist compliant URL for a given metro and product
    :param metro:
    :param product:
    :return:
    """
    current_date = datetime.datetime.now().strftime('%Y%M%d%H%M%S')
    serialize_product = cl_product(product)
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
    # Need to write a parser for these javascript components
    partitions = []
    first, *parts = string_js.split(';')

    print(first)



def run(args_dict):
    """
    Pseudo handler for aliexpress scraping from given args
    :param args_dict:
    :return:
    """
    product = args_dict['product']
    fout = construct_url(product)

    # Get URL constructed
    logger.info(f'Url constructed: {fout}')

    soup = get_soup(fout)
    items_string = find_items_element(soup)

    if items_string is None:
        logger.info(f'No items found for {product.upper()}')
    else:
        rule_based = parse_javascript(items_string)


if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(
        description='Find prices for product based on metropolitan area'
    )
    parser.add_argument(
        '-p', '--product',
        required=True,
        type=str,
        help='Product to find prices for'
    )

    args_dict = vars(parser.parse_args())

    if args_dict['product'] is None:
        logger.error(' Please enter a product for search')

    run(args_dict)
