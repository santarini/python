#recieve input
startNumber = input("Please enter your number: ")
#create array
numberArray = [int(i) for i in startNumber]
#sort the array
sortedArray = sorted(numberArray)
#define the smallest and largest value in the array
x = min(int(i) for i in startNumber)
y = max(int(i) for i in startNumber)

#
