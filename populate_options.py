import csv

def populate_options(filename):
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        return list(reader)

algos = populate_options('./algos.csv')