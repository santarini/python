import csv

with open("sandp500.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ticker = (row['ticker'])
        print(ticker)
