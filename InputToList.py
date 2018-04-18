##########Space seperate number to lists

#recieve input
startNumber = input("Please enter your number: ")
#create array
numberArray = [int(i) for i in startNumber.split()]
print(numberArray)


##########Characters to array

#recieve input
startStr = input("Please enter your string: ")
#create array
charArray = [str(i) for i in startStr]
print(charArray)


##########Space seperated words to array

#recieve input
startStr = input("Please enter your string: ")
#create array
strArray = [str(i) for i in startStr.split()]
print(strArray)

##########String to list
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
