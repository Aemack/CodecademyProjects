import random

money = 100

#Write your game of chance functions here

def headsOrTails(bet, playerCall):
    print("\nYou have £{money}\n".format(money=money))
    if (bet > money) or (bet <= 0) or (type(bet) != int ):
        print ("Invalid bet! You must bet a positive number and make sure you have the money to back it up!")
        return 0
    print("\nLet's play Coin-Flip!\nYou choose {call}".format(call=playerCall))
    randomNum = random.randint(0,1)
    if (randomNum):
        outcome = "Heads"
    else: 
        outcome = "Tails"
    print("It's {outcome}".format(outcome = outcome))
    if (outcome == playerCall.lower().capitalize()):
        print("You win!\n")
        return bet
    else:
        
        print("You loose!\n")
        return bet * -1

def choHan(bet,playerCall):
    print("\nYou have £{money}\n".format(money=money))
    if (bet > money) or (bet <= 0) or (type(bet) != int ):
        print ("Invalid bet! You must bet a positive number and make sure you have the money to back it up!")
        return 0
    print("\nLet's play Cho-Han!\nYou choose {call}".format(call=playerCall))
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    total = die1+die2
    if (total % 2 == 0):
        outcome = "Even"
    else: 
        outcome = "Odd"
    print("Die 1: {die1}\nDie 2: {die2}".format(die1=die1, die2=die2))
    print("Total: {total} \nOutcome: {outcome}".format(total=total, outcome=outcome))
    if (outcome == playerCall.lower().capitalize()):
        print("You win!\n")
        return bet
    else:
        print("You loose!\n")
        return bet*-1.
    
def pickACard(bet):
    print("\nYou have £{money}\n".format(money=money))
    if (bet > money) or (bet <= 0) or (type(bet) != int ):
        print ("Invalid bet! You must bet a positive number and make sure you have the money to back it up!")
        return 0
    
    print("\nLet's play Pick the High Card!")
    cards =["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    suits = ["Hearts","Clubs","Diamonds","Spades"]
    player1CardValue = random.randint(0,12)
    player1Suit = random.randint(0,3)
    player2CardValue = random.randint(0,12)
    player2Suit = random.randint(0,3)
    print("Player One drew the {card} of {suits}.".format(card=cards[player1CardValue],suits=suits[player1Suit]))
    print("Player Two drew the {card} of {suits}.".format(card=cards[player2CardValue],suits=suits[player2Suit]))
    if (player1CardValue == player2CardValue):
        print("It's a tie!\n")
        return 0
    elif (player1CardValue > player2CardValue):
        print("You win!\n")
        return bet
    else:
        print("You loose\n")
        return bet*-1


def roulette(bet, playerCall):
    print("\nYou have £{money}\n".format(money=money))

    if (bet > money) or (bet <= 0) or (type(bet) != int ):
        print ("Invalid bet! You must bet a positive number and make sure you have the money to back it up!")
        return 0




    print("\nLet's play Roullete!")
    print("You choose {call}.".format(call =playerCall))

    wheel = ["00"]
    for i in range(37):
        wheel.append(i)
    ball = random.randint(0,37)
    if (ball == 0) or (ball == 1):
        outcome = "Green"
    elif (ball % 2 != 0):
        outcome = "Black"
    else:
        outcome = "Red"    
    print("The ball lands on {number} {color}".format(number=wheel[ball], color=outcome))
    if (playerCall == outcome):
        print("Correct!")
        return bet
    elif (playerCall == wheel[ball]):
        print("Correct!")
        return bet *36
    else:
        print("Wrong!")
        return bet*-1

    




#Call your game of chance functions here
money += headsOrTails(10, "taIls")
money += choHan(20,"eVeN")
money += pickACard(50)
money += roulette(20, "Black")
money += roulette(20, 23)

