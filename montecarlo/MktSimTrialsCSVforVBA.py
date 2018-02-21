import csv
import random
import pathlib



def marketsimulation(maxloss, maxgain, price=100, days=250 , trialsCount=1):
    folderPath = 'C:/Users/m4k04/Desktop/vb_files/'
    x = 1
    while x <= trialsCount:
        with open(folderPath + str(x) + '.csv', 'w') as csvfile:
            fieldnames = ['Price']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, lineterminator = '\n')

            #set the number of days (there are 260 weekdays in a year)
            j = days
            i = 1
            while i <= j:
                change = random.uniform(-maxloss,maxgain)
                result = price + change
                writer.writerow({'Price': str(result)})
                price = result
                i+=1
        x +=1

marketsimulation(10, 10, 100, 260, 10)
