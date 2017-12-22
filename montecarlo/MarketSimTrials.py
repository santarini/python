import random

def marketsimulation(p, dec, inc, days):

#set the starting price
    price = p

#set the number of days (there are 260 weekdays in a year)
    j = days

    print(price)

    i = 0
    while i <= j:
        change = random.uniform(-dec,inc)
        result = price + change
        print(result)
        price = result
        i+=1

m = 1
#set the number of trials (n)
n = 10

while m <= n:
    print("\n" + "Trial " + str(m))
    marketsimulation(100, 10, 10, 10)
    m += 1
