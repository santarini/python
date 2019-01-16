import random

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
        elif (comeOutRoll == 7) or (comeOutRoll == 11):
            print("Natural")
            #pass line bets win
            #no pass bets lose
            playerBank = playerBank - bet
            print(playerBank)
        elif (comeOutRoll == 12):
            print("Push")
            #no pass bets push
            print(playerBank)
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
            elif subsequentRoll == point:
                #no pass bets lose
                print("Craps")
                playerBank = playerBank - bet
                print(playerBank)
            elif subsequentRoll == 12:
                #no pass bets lose
                print("Push")
                print(playerBank)
        gameCount += 1
