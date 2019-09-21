import os

##############
# CRAIGSLIST #
##############

CL_BASE = 'craigslist.org'

CL_BASE_SEARCH = '/search/sss?query='
CL_BASE_TAIL = 'sort=rel'

CL_CITIES = [
    'atlanta',
    'austin',
    'boston',
    'chicago',
    'dallas',
    'denver',
    'detroit',
    'houston',
    'lasvegas',
    'losangeles',
    'miami',
    'minneapolis',
    'newyork',
    'orangecounty',
    'philadelphia',
    'phoenix',
    'portland',
    'raleigh',
    'sacramento',
    'sandiego',
    'seattle',
    'sfbay',
    'washingtondc'
]


##############
# EBAY #######
##############

EBAY_BASE = 'http://ebay.com'
EBAY_BASE_SEARCH = '/sch/i.html?_from=R40&_nkw='
EBAY_COMPLETE_FILTER = '&_sacat=0&rt=nc&LH_Complete=1'
EBAY_US_ONLY_FILTER = '&rt=nc&LH_PrefLoc=1'
EBAY_PAGE_NUMBER = '&_pgn={}'