x = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
month = int(input("What is the month? \n"))
day = int(input("What is the day? \n"))
base = x[month-1]
y = base + day
print(y)
