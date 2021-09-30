import random
import sys
import time
import pickle


suit = ["Spades","Diamonds","Hearts","Clubs"]
number = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
color = ["Red","Black"]

card = [suit[random.randint(0,3)],number[random.randint(0,12)],color[random.randint(0,1)]]
#For later additional values, face, suit etc
print("\n"*10)


while True:
    playerCardValue = 0
    aiCardValue = 0
    move = "hit"
    player = "W"
    print("-"*10,"\tWelcome to BlackJack!\t","-"*10,"\n")
    while True:
        play=input("Play? (y/n)\t")
        play.lower()
        if play == "y":
            break
        if play == "n":
            sys.exit(0)

    while move == "hit":
        drawCard = number[random.randint(0,12)]
        cardName = drawCard
        
        if drawCard == number[9] or drawCard == number[10] or drawCard == number[11]:
            drawCard = 10
        if drawCard == number[12]:
            if playerCardValue > 10:
                drawCard = 1
            else:
                drawCard = 10

        

        playerCardValue = int(drawCard) + playerCardValue
        print("\nCard drawn:",cardName,"\nTotal:",playerCardValue,"\n")
        if playerCardValue > 21:
            print("\n","="*5,"Bust","="*5,"\n")
            player = "L"
            break
        if playerCardValue == 21:
            print("BlackJack!")
            player = "L"
            break
        move = input("Hit or stay?\t")
        move.lower()
    if player == "W":
        print("\nAI's turn...\n")

    while player == "W":
        time.sleep(1.5)
        drawCard = number[random.randint(0,12)]    
        cardName = drawCard
        if drawCard == number[9] or drawCard == number[10] or drawCard == number[11]:
            drawCard = 10
        if drawCard == number[12]:
            if aiCardValue > 10:
                drawCard = 1
            else:
                drawCard = 10
        
        aiCardValue = int(drawCard) + aiCardValue
        print("Card:",cardName,"\nTotal:",aiCardValue,"\n")
        if aiCardValue > 21:
            print("Ai card value:\t\t", aiCardValue, "\nPlayer card value:\t", playerCardValue,"\n","*"*5,"You win!","*"*5,"\n")
            break
        if playerCardValue < aiCardValue:
            print("Ai card value:\t", aiCardValue, "Player card value:\t", playerCardValue,"\n\n","-"*5,"You win!","-"*5,"\n")
            break
        
