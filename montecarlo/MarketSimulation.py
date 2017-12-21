import random

#set the starting price
price = 100
i = 0
#set the number of days
j = 250

print(price)

while i <= j:
    change = random.uniform(-10,10)
    result = price + change
    print(result)
    price = result
    i+=1
