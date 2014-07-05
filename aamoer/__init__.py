from aamoer.pieces import count, load

def aamoer(functions:dict, table) -> list:
    '''
    Specify some function and an iterable of iterables
    (like a list of lists), where the inner iterable is
    a row in a data table.
    
    Receive histograms of the results of those functions.
    You receive one histogram per function per column.
    That is, if each row is eight long and you pass two
    functions, you'll get 16 histograms.
    '''
    return count(functions, load(table))
