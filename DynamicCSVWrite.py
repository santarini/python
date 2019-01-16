import csv

fieldNameList = []

for t in range(0,10):
    fieldNameList.append(str(t))

testDictionary = {}
for t in range(0,10):
    testDictionary[fieldNameList[t]] = str(t)

with open('csvTest.csv', mode='a') as csv_file:
    fieldnames = fieldNameList
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
    writer.writerow(testDictionary)
