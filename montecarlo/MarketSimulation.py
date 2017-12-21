import random

#set the starting price
price = 100

#set the number of days (there are 260 weekdays in a year)
j = 250

print(price)

i = 0
while i <= j:
    change = random.uniform(-10,10)
    result = price + change
    print(result)
    price = result
    i+=1
