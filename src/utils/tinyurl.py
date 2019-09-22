import requests


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