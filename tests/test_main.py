import mock

from src.main import GetProducts


@mock.patch('src.ebay.search.run')
@mock.patch('src.craigslist.craigslist.run')
@mock.patch('src.aliexpress.aliexpress.run')
def test_GetProducts_constructor(mock_ali, mock_craigs, mock_ebay):
    mock_ali.return_value = 'some values'
    mock_craigs.return_value = 'some values'
    mock_ebay.return_value = 'some values'

    obj = GetProducts(
        args_dict={
            'query': 'macbook',
            'metroarea': 'newyork',
            'sold': '',
            'n': 1
        }
    )

    assert obj.aliexpress == 'some values'
    assert obj.craigslist == 'some values'
    assert obj.ebay == 'some values'
