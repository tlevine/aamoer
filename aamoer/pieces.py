from io import StringIO
from logging import getLogger
from collections import Counter, defaultdict

logger = getLogger(__name__)

def count(functions:dict, table:iter) -> list:
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

def load(table):
    if isinstance(table, str):
        fp = open(table, 'r')
        result = csv.reader(fp, dialect = _guess_dialect(fp))
    elif isinstance(table, StringIO):
        fp = table
        result = csv.reader(fp, dialect = _guess_dialect(fp))
    else:
        result = table
    return result
        
def _guess_dialect(fp):
    'Guess the dialect of a CSV file.'
    pos = fp.tell()
    try:
        dialect = csv.Sniffer().sniff(fp.read(1024))
    except csv.Error:
        dialect = 'excel' # the default
    fp.seek(pos)
    return dialect