import csv

with open('simData.csv', 'w') as csvfile:
    fieldnames = ['Count', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

    writer.writeheader()
    writer.writerow({'Count': 'cheese', 'Value': 'pickles'})
    writer.writerow({'Count': 'cheese', 'Value': 'pickles'})
    writer.writerow({'Count': 'cheese', 'Value': 'pickles'})
