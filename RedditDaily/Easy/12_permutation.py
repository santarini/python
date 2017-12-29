import itertools
import csv
x = input("What string would you like to permute? \n")
x = x.replace(" ","")
y = list(x)
print(y)
print(list(itertools.permutations(y)))
