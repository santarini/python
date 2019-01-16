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
        
def multipleSimulations(totalTrials):
    j = 1
    while j < totalTrials:
        payoutResult = startCraps(1000, 100, 10)
        with open('nopassdata.csv', mode='a') as csv_file:
            fieldnames = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, lineterminator = '\n')
            writer.writerow({'0': 1000,
                             '1': payoutResult[0],
                             '2': payoutResult[1],
                             '3': payoutResult[2],
                             '4': payoutResult[3],
                             '5': payoutResult[4],
                             '6': payoutResult[5],
                             '7': payoutResult[6],
                             '8': payoutResult[7],
                             '9': payoutResult[8],
                             '10': payoutResult[9]
                             })
        j+=1
