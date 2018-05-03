#!Python 3

import csv

with open("test.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    test = len(list(reader))
