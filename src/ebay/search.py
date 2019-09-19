import argparse
import json
import logging
import os
import pickle
import random
import requests

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

from bs4 import BeautifulSoup
from datetime import datetime

from src.constants import (
    EBAY_BASE,
    EBAY_BASE_SEARCH,
    EBAY_COMPLETE_FILTER,
    EBAY_US_ONLY_FILTER
)


def _get_product_price(soup):

    price_soup = soup.find('span', {'class': 's-item__price'})
    price = price_soup.text if price_soup else 'ERROR'

    if price.startswith('$'):
        if 'to' in price:
            price_raw = price.split('to')
            price_clean = [price.replace('$', '') for price in price_raw]
            price = (float(price_clean[0].strip()), float(price_clean[1].strip()))
        else:
            price = float(price.replace('$', ''))

    return price


def _get_product_shipping(soup):

    shipping_soup = soup.find('span', {'class': 's-item__shipping'})
    shipping = shipping_soup.text if shipping_soup else 'ERROR'

    return shipping


def _get_product_status(soup):

    status_soup = soup.find('div', {'class': 's-item__title--tag'})
    status_raw = status_soup.text.split(' ', 1)

    result = status_raw[0]
    datestamp = datetime.strptime(status_raw[1].strip(), '%b %d, %Y')

    status = {
        'result': result,
        'datestamp': datestamp
    }

    return status


def _get_product_name(soup):

    name_soup = soup.find('h3', {'class': 's-item__title'})
    name = name_soup.text if name_soup else 'ERROR'

    if name.startswith('New Listing'):
        name = name.replace('New Listing', '')

    return name


def get_product_info(soup):

    product_info = {
        'name': _get_product_name(soup),
        'status': _get_product_status(soup),
        'price': _get_product_price(soup),
        'shipping': _get_product_shipping(soup)
    }

    print(product_info)

    return product_info


def get_products(soup):

    products = soup.find_all('div', {'class': 's-item__wrapper'})

    return products


def run(args_dict):

    query = args_dict['query']
    logger.info(f'RUNNING ON QUERY: {query}')

    if args_dict['sold']:
        url = '{}{}{}{}'.format(
            EBAY_BASE,
            EBAY_BASE_SEARCH,
            query,
            EBAY_COMPLETE_FILTER,
            EBAY_US_ONLY_FILTER
        )
    else:
        # here is where other search filters would come in
        pass

    logger.info(f'BUILD EBAY URL: {url}')
    resp = requests.get(url)
    logger.info(f'EBAY REQUEST STATUS: {resp.status_code}')

    soup = BeautifulSoup(resp.content, 'html.parser')

    products = get_products(soup)
    logger.info(f'FOUND PRODUCTS: {len(products)}')

    product_info = []
    for product in products:
        info = get_product_info(product)
        product_info.append(info)
        logger.info(f'ADDED PRODUCT: {info["name"]}')

    return product_info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find prices for products products on eBay'
    )
    parser.add_argument(
        '-q', '--query',
        required=True,
        type=str,
        help='Product query to find prices for.'
    )
    parser.add_argument(
        '--sold',
        action='store_true'
    )

    args_dict = vars(parser.parse_args())

    run(args_dict)
