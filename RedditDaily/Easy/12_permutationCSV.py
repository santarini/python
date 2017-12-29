import itertools
import csv

x = input("What string would you like to permute? \n")
x = x.replace(" ","")
y = list(x)
z = list(itertools.permutations(y))
i =1
with open('cheese.csv', 'w') as csvfile:
        fieldnames = ['Count', 'Value']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for n in z:
            writer.writerow({'Count': str(i), 'Value': n})
            i += 1
