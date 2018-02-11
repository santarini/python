import random

def diceTrial(NumOfRolls, Trials):
    TotalTwoCount = 0
    TotalThreeCount = 0
    TotalFourCount = 0
    TotalFiveCount = 0
    TotalSixCount = 0
    TotalSevenCount = 0
    TotalEightCount = 0
    TotalNineCount = 0
    TotalTenCount = 0
    TotalElevenCount = 0
    TotalTwelveCount = 0
    TotalRolls = 0
    m = 1
    n = Trials
    while m <= n:
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
        #set the number of rolls
        j = NumOfRolls
        i = 0
        print("\nTRIAL " + str(m))
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
            TotalRolls+=1
        print("\nTRIAL " + str(m) + " RESULTS")
        print("Total Rolls this Trial: " + str(j))
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
        TotalTwoCount = TotalTwoCount + TwoCount
        TotalThreeCount = TotalThreeCount + ThreeCount
        TotalFourCount = TotalFourCount + FourCount
        TotalFiveCount = TotalFiveCount + FiveCount
        TotalSixCount = TotalSixCount + SixCount
        TotalSevenCount = TotalSevenCount + SevenCount
        TotalEightCount = TotalEightCount + EightCount
        TotalNineCount = TotalNineCount + NineCount
        TotalTenCount = TotalTenCount + TenCount
        TotalElevenCount = TotalElevenCount + ElevenCount
        TotalTwelveCount = TotalTwelveCount + TwelveCount
        m += 1
    print("\nSIMULATION RESULTS")
    print("Total Rolls: " + str(TotalRolls))
    print("Total 2: " + str(TotalTwoCount))
    print(str(round((TotalTwoCount/TotalRolls)*100)) + "%")
    print("Total 3: " + str(TotalThreeCount))
    print(str(round((TotalThreeCount/TotalRolls)*100)) + "%")
    print("Total 4: " + str(TotalFourCount))
    print(str(round((TotalFourCount/TotalRolls)*100)) + "%")
    print("Total 5: " + str(TotalFiveCount))
    print(str(round((TotalFiveCount/TotalRolls)*100)) + "%")
    print("Total 6: " + str(TotalSixCount))
    print(str(round((TotalSixCount/TotalRolls)*100)) + "%")
    print("Total 7: " + str(TotalSevenCount))
    print(str(round((TotalSevenCount/TotalRolls)*100)) + "%")
    print("Total 8: " + str(TotalEightCount))
    print(str(round((TotalEightCount/TotalRolls)*100)) + "%")
    print("Total 9: " + str(TotalNineCount))
    print(str(round((TotalNineCount/TotalRolls)*100)) + "%")
    print("Total 10: " + str(TotalTenCount))
    print(str(round((TotalTenCount/TotalRolls)*100)) + "%")
    print("Total 11: " + str(TotalElevenCount))
    print(str(round((TotalElevenCount/TotalRolls)*100)) + "%")
    print("Total 12: " + str(TotalTwelveCount))
    print(str(round((TotalTwelveCount/TotalRolls)*100)) + "%")

diceTrial(100, 10)
