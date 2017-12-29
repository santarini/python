x = int(input("How many bottles of beer on the wall are there? \n"))
y = 1

while x >= y:
    z = x - 1
    print(str(x)," bottles of beer on the wall, ", str(x), " bottles of beer. \n Take one down and pass it around, ", str(z)," bottles of beer on the wall. \n \n")
    x -= 1

print("No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall.")
