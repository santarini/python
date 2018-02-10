import random

HeadsCount = 0
TailsCount = 0

#set the number of trials
j = 100

i = 0
while i < j:
    result = random.randint(0,1)
    if result == 0:
        print("Heads")
        HeadsCount+=1
    if result == 1:
        print("Tails")
        TailsCount+=1
    i+=1
print("\nTotal Trials " + str(j))
print("Total Heads " + str(HeadsCount))
print(str(round((HeadsCount/j)*100)) + "%")
print("Total Tails " + str(TailsCount))
print(str(round((TailsCount/j)*100)) + "%")
