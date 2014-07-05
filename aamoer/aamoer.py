from collections import Counter, defaultdict

def count(functions:dict, table:iter):
    histograms = defaultdict(lambda: defaultdict(Counter))
    for row in table:
        for i, value in row:
            for name, function in functions.items():
                histograms[i][name] = function(value)
    return [histograms[i] for i in range(max(histograms.keys()) + 1)]
