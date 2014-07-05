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

def cli(functions:dict):
    import sys, argparse, csv
    p = argparse.ArgumentParser(description = 'Find risk-related features in CSV files.')
    p.add_argument('csv', metavar = '[csv file]', nargs = '+', help = 'csv files to look at')
    def main():
        writer = csv.writer(sys.stdout)
        writer.writerow(['filename','column.index','feature','value','count'])
        for filename in p.parse_args().csv:
            for column_number, column in enumerate(aamoer(functions, filename)):
                for feature_name, counter in column.items():
                    for value, value_count in counter.items():
                        writer.writerow([filename,column_number,feature_name,value,value_count])
    return main
