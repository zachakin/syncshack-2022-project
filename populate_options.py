import csv
from wsgiref.headers import tspecials

class algo:
    def __init__(self, id_: int, name: str, ds: str, tc: str, sc: str):
        self.id = id_
        self.name = name
        self.data_structure = ds
        self.time_complexity = tc
        self.space_complexity = sc
    
    def __str__(self):
        return f'Name: {self.name}\nData Structure: {self.data_structure}\nTime Complexity: {self.time_complexity}\nSpace Complexity: {self.space_complexity}'


def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = algo(j,i[0],i[1],i[2],i[3])
            output[j] = a
            j += 1
    return output

algos = populate_options('./algos.csv')