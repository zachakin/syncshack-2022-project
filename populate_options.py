import csv
from wsgiref.headers import tspecials

class algo:
    def __init__(self, id_, name, ds, tc):
        self.id = id_
        self.name = name
        self.data_structure = ds
        self.time_complexity = tc
        # self.space_complexity = sc


def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            output[j] = algo(j,i[0],i[1],i[2])
            j += 1
    return output

algos = populate_options('./algos.csv')