import random

OneCount = 0
TwoCount = 0
ThreeCount = 0
FourCount = 0
FiveCount = 0
SixCount = 0

#set the number of trials
j = 100

i = 0
while i < j:
    result = random.randint(1,6)
    if result == 1:
        print(result)
        OneCount+=1
    if result == 2:
        print(result)
        TwoCount+=1
    if result == 3:
        print(result)
        ThreeCount+=1
    if result == 4:
        print(result)
        FourCount+=1
    if result == 5:
        print(result)
        FiveCount+=1
    if result == 6:
        print(result)
        SixCount+=1
    i+=1
    
print("\nTotal Trials " + str(j))
print("Total 1: " + str(OneCount))
print(str(round((OneCount/j)*100)) + "%")
print("Total 2: " + str(TwoCount))
print(str(round((TwoCount/j)*100)) + "%")
print("Total 3: " + str(ThreeCount))
print(str(round((ThreeCount/j)*100)) + "%")
print("Total 4: " + str(FourCount))
print(str(round((FourCount/j)*100)) + "%")
print("Total 5: " + str(FiveCount))
print(str(round((FiveCount/j)*100)) + "%")
print("Total 6: " + str(SixCount))
print(str(round((SixCount/j)*100)) + "%")
