import nose.tools as n

from aamoer.aamoer import count

def test_count():
    functions = {
        'koehac': lambda x: x + 3,
        'no': lambda _: False,
        'mod': lambda x: x % 88,
        'err': lamda x: x.lower() + 'aoeu',
    }
    data = [
        [3, 3, 4],
        [4, 1, 114],
        [5, 3, 9],
        [1, 3, 8],
    ]
    observed = aamoer.count(functions, data)
    expected = []
    n.assert_list_equal(observed, expected)