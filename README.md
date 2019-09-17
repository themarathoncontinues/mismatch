# mismatch

Identifying retail arbitrage opportunities.


## craigslist.org

| tag  | argument    | description                        | default      | choices | required |
|------|---------------|------------------------------------|--------------|---------|----------|
| `-m` | `--metroarea`| `Metropolitan area to search caigslist.org for` | `None`        | `None`  | `True`   |
| `-p` | `--product` | `Product to find prices for` | `None`       | `None`  | `True`  |

### Sample Input
```bash
python src/craigslist -m newyork -p "macbook pro touchbar"
```

### Sample Output
```bash
INFO:__main__:Url constructed: https://newyork.craigslist.org/search/sss?query=macbook+pro+touchbar&sort=rel

[
    {
    "listingUrl": "https://newjersey.craigslist.org/sys/d/north-bergen-2018-macbook-pro-13-inch/6969179978.html",
    "createdAt": "2019-09-01 11:59",
    "salePrice": 1300
    },
    {
    "listingUrl": "https://newjersey.craigslist.org/sys/d/stamford-13-macbook-pro-touch-bar-16gb/6972176677.html",
    "createdAt": "2019-09-13 15:54",
    "salePrice": 975
    },
    {
    "listingUrl": "https://newjersey.craigslist.org/sys/d/ridgewood-new-macbook-pro-pro-13-inch/6968906872.html",
    "createdAt": "2019-08-31 19:08",
    "salePrice": 1300
    }
]

INFO:__main__:107 listings for MACBOOK PRO TOUCHBAR found.
```