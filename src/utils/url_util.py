import re
import requests


def partition_product(product_arg):
    """
    Serialize input 'product' for craigslist.org search
    :param product_arg:
    :return:
    """
    word_list = re.sub("[^\w]", " ", product_arg.lower()).split()
    cl_url_product = '+'.join(str(w) for w in word_list)

    return cl_url_product


def shorten(url):

    endpoint = "http://tinyurl.com/api-create.php"

    params = {
    	'url': url
    }

    try:
        res = requests.get(endpoint, params=params)
    except Exception as e:
        raise

    return res.text