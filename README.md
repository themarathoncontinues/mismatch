# mismatch

[![Build Status](https://travis-ci.com/leonkozlowski/mismatch.svg?branch=master)](https://travis-ci.com/leonkozlowski/mismatch)
[![codecov](https://codecov.io/gh/leonkozlowski/mismatch/branch/master/graph/badge.svg)](https://codecov.io/gh/leonkozlowski/mismatch)

Identifying retail arbitrage opportunities.


## argparse

| tag  | argument    | description                        | default      | choices | required |
|------|---------------|------------------------------------|--------------|---------|----------|
| `-m` | `--metroarea`| `Metropolitan area to search for` | `None`        | `None`  | `True`   |
| `-q` | `--query` | `Product to find prices for` | `None`       | `None`  | `True`  |

### Sample Input
```bash
>> NOTE: Will run all websites

python src/main -m newyork -q "macbook pro touchbar" --sold
```
