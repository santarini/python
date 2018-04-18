#append(item) 
#add to the end of a list
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.append('bacon')
print(mylist)

#insert(index, item) 
#add item to a specific index in the list
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.insert(1, 'bacon')
print(mylist)

#remove(item) 
#remove item from a list 
#note: if the item appears multiple times in the list remove() deletes the first instance
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.remove('cheese')
print(mylist)

#del statement 
#remove item at a specific index from list 
#note: del myList[:] can be used to delete entire list
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
del myList[0]
print(mylist)

#sort() 
#arranges list in ascending alphabetical OR numerical order 
#note: cannot sort lists that have bost strings and numbers
#note: uses "ASCIIbetical order", caps before lowercase (eg. AaBbCcDdEd....)
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.sort()
print(mylist)

#sort(reverse=True) 
#arranges list in descending alphabetical OR numerical order 
#note: cannot sort lists that have bost strings and numbers
#note: uses "ASCIIbetical order", caps before lowercase (eg. AaBbCcDdEd....)
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.sort(reverse=True) 
print(mylist)

#sort(key=str.lower)
#arranges list in descending alphabetical OR numerical order 
#note: cannot sort lists that have bost strings and numbers
#note: allows case insensitive alphabetical sort
myList = ['cheese', 'pickles', 'cucumbers', 'bananas']
mylist.sort(key=str.lower)
print(mylist)
