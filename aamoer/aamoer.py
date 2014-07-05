from logging import getLogger
from collections import Counter, defaultdict

logger = getLogger(__name__)

def count(functions:dict, table:iter):
    histograms = defaultdict(lambda: defaultdict(Counter))
    for row in table:
        for i, value in enumerate(row):
            for name, function in functions.items():
                try:
                    histograms[i][name][function(value)] += 1
                except Exception as e:
                    logger.error(e)
                    histograms[i][name][None] += 1
    return [histograms[i] for i in range(max(histograms.keys()) + 1)]
