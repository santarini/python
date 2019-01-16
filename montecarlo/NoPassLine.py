import random
import csv

playerBank = 1000

craps = [2,3,12]
naturals = [7,11]


    
def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2
    print(str(dice1) + " " + str(dice2) + ": " + str(result))
    return result

#set up for no pass

def startCraps(playerBank, bet, trials):
    payout = []
    gameCount = 1
    while gameCount <= trials:
        print("Game #" + str(gameCount))
        comeOutRoll = rolldice()
        if (comeOutRoll == 2) or (comeOutRoll == 3):
            print("Craps")
            #pass line bets lose
            #no pass bets win
            playerBank = playerBank + bet
            print(playerBank)
            payout.append(playerBank)
        elif (comeOutRoll == 7) or (comeOutRoll == 11):
            print("Natural")
            #pass line bets win
            #no pass bets lose
            playerBank = playerBank - bet
            print(playerBank)
            payout.append(playerBank)
        elif (comeOutRoll == 12):
            print("Push")
            #no pass bets push
            print(playerBank)
            payout.append(playerBank)
        else:
            point = comeOutRoll
            print("Point:" + str(point))
            subsequentRoll = 0
            while not (subsequentRoll == 7 or subsequentRoll == point):
                subsequentRoll = rolldice()
            if subsequentRoll == 7:
                #no pass bets win
                print("Natural")
                playerBank = playerBank + bet
                print(playerBank)
                payout.append(playerBank)
            elif subsequentRoll == point:
                #no pass bets lose
                print("Craps")
                playerBank = playerBank - bet
                print(playerBank)
                payout.append(playerBank)
            elif subsequentRoll == 12:
                #no pass bets lose
                print("Push")
                print(playerBank)
                payout.append(playerBank)
        gameCount += 1
    return payout
        
def multipleSimulations(totalTrials, playerBank, bet, trials):
    j = 1
    while j <= totalTrials:
        payoutResult = startCraps(playerBank, bet, trials)

        fieldNameList = []
        for t in range(0,trials+1):
            fieldNameList.append(str(t))

        testDictionary = {'0': playerBank}
        for t in range(1,trials):
            testDictionary[fieldNameList[t]] = payoutResult[t]
        
        with open('nopassdata.csv', mode='a') as csv_file:
            fieldnames = fieldNameList
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
            writer.writerow(testDictionary)
        j+=1
