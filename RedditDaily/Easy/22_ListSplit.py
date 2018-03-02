#recieve input
startStr = input("Please enter your strings: ")
#create array
strArray = [str(i) for i in startStr.split()]
print(strArray)
#count number of items in list
n = len(strArray)
#divide that number in half
m = int(n/2)
#create array with first half of items
a = []
b = []
x = 0
print (n)
while x < m:
    a.append(strArray[x])
    x +=1
while m < n:
    b.append(strArray[m])
    m +=1
print(a)
print(b)
