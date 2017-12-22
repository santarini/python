import csv
import random

with open('simdata.csv', 'w') as csvfile:
    fieldnames = ['Trial','Count', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

    def marketsimulation(price, maxloss, maxgain, days):

    #set the number of days (there are 260 weekdays in a year)
        j = days
        i = 1
        while i <= j:
            change = random.uniform(-maxloss,maxgain)
            result = price + change
            writer.writerow({'Count': str(i), 'Value': str(result)})
            price = result
            i+=1

    m = 1
    #set the number of trials (n)
    n = 10

    while m <= n:
        writer.writerow({'Trial': "Trial " + str(m)})
        marketsimulation(100, 10, 10, 10)
        m += 1
