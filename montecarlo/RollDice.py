import random

TwoCount = 0
ThreeCount = 0
FourCount = 0
FiveCount = 0
SixCount = 0
SevenCount = 0
EightCount = 0
NineCount = 0
TenCount = 0
ElevenCount = 0
TwelveCount = 0


#set the number of trials
j = 100

i = 0
while i < j:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2
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
    if result == 7:
        print(result)
        SevenCount+=1
    if result == 8:
        print(result)
        EightCount+=1
    if result == 9:
        print(result)
        NineCount+=1
    if result == 10:
        print(result)
        TenCount+=1
    if result == 11:
        print(result)
        ElevenCount+=1
    if result == 12:
        print(result)
        TwelveCount+=1
    i+=1
    
print("\nTotal Trials " + str(j))

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
print("Total 7: " + str(SevenCount))
print(str(round((SevenCount/j)*100)) + "%")
print("Total 8: " + str(EightCount))
print(str(round((EightCount/j)*100)) + "%")
print("Total 9: " + str(NineCount))
print(str(round((NineCount/j)*100)) + "%")
print("Total 10: " + str(TenCount))
print(str(round((TenCount/j)*100)) + "%")
print("Total 11: " + str(ElevenCount))
print(str(round((ElevenCount/j)*100)) + "%")
print("Total 12: " + str(TwelveCount))
print(str(round((TwelveCount/j)*100)) + "%")
