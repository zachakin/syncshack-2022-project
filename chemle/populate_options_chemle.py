import csv
from wsgiref.headers import tspecials

class periodic_table:
    def __init__(self, id_: int, name: str, atomic_number: int, period: int, group: int, classification: str):
        self.id = id_
        self.name = name
        self.atomic_number = atomic_number
        self.period = period
        self.group = group
        self.classification = classification
    
    def __str__(self):
        return f'Name: {self.name}\nAtomic Number: {self.atomic_number}\nPeriod: {self.period}\nGroup: {self.group}\nClassification: {self.classification}'


def populate_options(filename):
    j = 0
    output = dict()
    with open(filename,'r') as f:
        reader = csv.reader(f)
        next(reader,None)
        for i in reader:
            a = periodic_table(j,i[0],i[1],i[2],i[3],i[4])
            output[j] = a
            j += 1
    return output

periodic_table = populate_options('./periodic_table.csv')