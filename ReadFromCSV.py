import csv

with open("sandp500.csv") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        ticker = (row['ticker'])
