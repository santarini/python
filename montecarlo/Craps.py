import random
import csv

playerBank = 1000

craps = [2,3,12]
naturals = [7,11]

#1 : 1 Snake eyes (Aces)
#2 : 1 Ace Deuce
#2 : 2 Hard Four
#3 : 1 Easy Four
#6 : 6 Box Cars

def quickGame(gameType):
    playerBank = 1000
    betType = gameType
    bet = 100
    trials = 10
    startCraps(playerBank, betType, bet, trials)

def createGame():
    playerBank = int(input("How much money would you like to start with? "))
    betType = input("What type of bet would you like to make? ")
    bet = int(input("How much would like to bet per game? "))
    trials = int(input("How many games would you like to play? "))
    startCraps(playerBank, betType, bet, trials)

def rolldice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2
    print(str(dice1) + " " + str(dice2) + ": " + str(result))
    return result

#set up for no pass

def startCraps(playerBank, betType, bet, trials):
    payout = []
    gameCount = 1
    while gameCount <= trials:
        print("-----------")
        print("Game #" + str(gameCount))
        print("-----------")
        comeOutRoll = rolldice()
        if (comeOutRoll == 2) or (comeOutRoll == 3):
            print("Craps!")
            if betType == "Pass":
                #pass line bets lose
                playerBank = playerBank - bet
                print(playerBank)
                payout.append(playerBank)
            if betType == "No Pass":
                #no pass bets win
                playerBank = playerBank + bet
                print(playerBank)
                payout.append(playerBank)
        elif (comeOutRoll == 7) or (comeOutRoll == 11):
            print("Natural!")
            if betType == "Pass":
                #pass line bets win
                playerBank = playerBank + bet
                print(playerBank)
                payout.append(playerBank)
            if betType == "No Pass":   
                #no pass bets lose
                playerBank = playerBank - bet
                print(playerBank)
                payout.append(playerBank)
        elif (comeOutRoll == 12):
            if betType == "Pass":
                #pass line bets lose
                print("Craps!")
                playerBank = playerBank - bet
                print(playerBank)
                payout.append(playerBank)
            if betType == "No Pass":  
                #no pass bets push
                print("Push")
                print(playerBank)
                payout.append(playerBank)
        else:
            point = comeOutRoll
            print("Point:" + str(point))
            subsequentRoll = 0
            while not (subsequentRoll == 7 or subsequentRoll == point):
                subsequentRoll = rolldice()
            if subsequentRoll == 7:
                if betType == "Pass":
                    print("Seven Out!")
                    #pass line bets lose
                    playerBank = playerBank - bet
                    print(playerBank)
                    payout.append(playerBank)
                if betType == "No Pass": 
                #no pass bets win
                    playerBank = playerBank + bet
                    print(playerBank)
                    payout.append(playerBank)
            elif subsequentRoll == point:
                if betType == "Pass":
                    #pass line bets win
                    print("Point!")
                    playerBank = playerBank + bet
                    print(playerBank)
                    payout.append(playerBank)
                if betType == "No Pass":
                    #no pass bets lose
                    print("Craps")
                    playerBank = playerBank - bet
                    print(playerBank)
                    payout.append(playerBank)
##            elif subsequentRoll == 12:
##                if betType == "Pass":
##                    #pass line bets lose
##                    playerBank = playerBank + bet
##                    print(playerBank)
##                    payout.append(playerBank)
##                if betType == "No Pass":
##                    #no pass bets push
##                    print("Push")
##                    print(playerBank)
##                    payout.append(playerBank)
        gameCount += 1
    return payout


def multipleSimulations(totalTrials, playerBank, betType, bet, trials):
    j = 1
    while j <= totalTrials:
        payoutResult = startCraps(playerBank, betType, bet, trials)
        fieldNameList = []
        for t in range(0,trials+1):
            fieldNameList.append(str(t))

        testDictionary = {'0': playerBank}
        for t in range(1,trials):
            testDictionary[fieldNameList[t]] = payoutResult[t]
        
        with open(betType + '.csv', mode='a') as csv_file:
            fieldnames = fieldNameList
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
            writer.writerow(testDictionary)
        j+=1
