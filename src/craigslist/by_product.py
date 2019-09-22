import argparse
import json
import logging
import re
import requests

from src.utils.json_util import set_nested

from bs4 import BeautifulSoup

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


def get_product_soup(url):
    req = requests.get(url)
    req_content = req.content

    soup = BeautifulSoup(req_content, 'html.parser')

    return soup


def extract_product_meta(soup):
    product_meta = {
        'productName': soup.find('span', id='titletextonly').text,
        'listingDate': (soup.find('time', {'class': 'date timeago'}).text).strip(),
        'salePrice': {
            'price': _parse_pricing(soup.find('span', {'class': 'price'}).text),
            'currency': _derive_currency(soup.find('span', {'class': 'price'}).text)
        },
        'region': (soup.find_all(attrs={'name': re.compile('geo.region', re.I)}))[0]['content'],
        'shippingPrice': 0,
        'imageUrl': (soup.find_all(attrs={'property': re.compile('og:image', re.I)}))[0]['content'],
        'description': (soup.find_all(attrs={'name': re.compile('description', re.I)}))[0]['content']
    }

    print(json.dumps(product_meta, indent=4))
    return product_meta


def _parse_pricing(price):
    if '$' in price.strip():
        usd_price = price.replace('$', '')
        price = usd_price

    return float(price)


def _derive_currency(price):
    if '$' in price:
        return 'USD'


def run(args_dict):
    product = args_dict['url']
    soup = get_product_soup(product)
    metadata = extract_product_meta(soup)

    logger.info(f'Data extracted for {metadata["productName"].upper()}')

    return metadata



if __name__ == '__main__': # pragma: no cover
    parser = argparse.ArgumentParser(
        description='Find metadata for product url'
    )
    parser.add_argument(
        '-u', '--url',
        required=True,
        type=str,
        help='Url for metadata fetching'
    )

    args_dict = vars(parser.parse_args())

    run(args_dict)