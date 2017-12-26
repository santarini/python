import csv
import random

with open('mktsimdata.csv', 'w') as csvfile:
    fieldnames = ['Trial', 'Count', 'Value']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

    def marketsimulation( maxloss, maxgain, price=100, days=250):

    #set the number of days (there are 260 weekdays in a year)
        j = days
        i = 1
        writer.writerow({'Count': str(0), 'Value': str(price) })
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
        writer.writerow({'Trial': "Trial " + str(m), 'Count': "Count", 'Value': "Value"})
        marketsimulation(10, 10, 100, 250)
        m += 1
