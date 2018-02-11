import random

def coinTrial(NumOfFlips, Trials):
    TotalTrialHeads = 0
    TotalTrialTails = 0
    TotalFlipCount = 0
    m = 1
    n = Trials
    while m <= n:
        HeadsCount = 0
        TailsCount = 0
        #set the number of flips in a trial
        i = 0
        j = NumOfFlips
        while i < j:
            result = random.randint(0,1)
            if result == 0:
                print("Heads")
                HeadsCount+=1
            if result == 1:
                print("Tails")
                TailsCount+=1
            TotalFlipCount += 1
            i+=1
        print("\nTRIAL NUMBER " + str(m) + " RESULTS")
        print("Total Flips in Trial: " + str(j))
        print("Total Heads: " + str(HeadsCount))
        print(str(round((HeadsCount/j)*100)) + "%")
        print("Total Tails: " + str(TailsCount))
        print(str(round((TailsCount/j)*100)) + "%")
        TotalTrialHeads = TotalTrialHeads + HeadsCount
        TotalTrialTails = TotalTrialTails + TailsCount
        m += 1
    print("\nSIMULATION RESULTS")
    print("Total TrialS Count: " + str(m-1))
    print("Total Flip Count: " + str(TotalFlipCount))
    print("Total Heads in Trials: " + str(TotalTrialHeads))
    print(str(round((TotalTrialHeads/TotalFlipCount)*100)) + "%")
    print("Total Tails in Trials: " + str(TotalTrialTails))
    print(str(round((TotalTrialTails/TotalFlipCount)*100)) + "%")
coinTrial(100, 10)
