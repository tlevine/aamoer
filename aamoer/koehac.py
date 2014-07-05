from collections import Counter, defaultdict

def count(table, functions):
    histograms = defaultdict(lambda: defaultdict(Counter))
    for row in table:
        for i, value in row:
            for function in functions:
                histograms[i][function.__name__] = function(value)
    for i in range(max(histograms.keys()) + 1):
        yield histograms[i]
