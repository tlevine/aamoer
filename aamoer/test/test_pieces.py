from collections import Counter
import nose.tools as n

import aamoer.pieces as aamoer

def test_count():
    functions = {
        'koehac': lambda x: x + 3,
        'no': lambda _: False,
        'mod': lambda x: x % 88,
        'err': lambda x: x.lower() + 'aoeu',
    }
    data = [
        [3, 3, 4],
        [4, 1, 114],
        [5, 3, 9],
        [1, 3, 8],
    ]
    observed = aamoer.count(functions, data)
    expected = [
        {'err': Counter({None:4}),
         'koehac': Counter({8: 1, 4: 1, 6: 1, 7: 1}),
         'mod': Counter({1: 1, 3: 1, 4: 1, 5: 1}),
         'no': Counter({False: 4})},
        {'err': Counter({None:4}),
         'koehac': Counter({6: 3, 4: 1}),
         'mod': Counter({3: 3, 1: 1}),
         'no': Counter({False: 4})},
        {'err': Counter({None:4}),
         'koehac': Counter({11: 1, 12: 1, 117: 1, 7: 1}),
         'mod': Counter({8: 1, 9: 1, 26: 1, 4: 1}),
         'no': Counter({False: 4})},
    ]
    n.assert_list_equal(observed, expected)
