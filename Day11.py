# -*- coding: utf-8 -*-
"""
Created on Sun May 30 03:13:19 2021

@author: Tahamid
"""

# =============================================================================
# Day 11: TTY Blackjack Project 
# =============================================================================

import random
from os import system, name


def intro():
    logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
    print(logo)

def rules():
    rule = '''
    Basic Blackjack Rules:

        The goal of blackjack is to beat the dealer's hand without going over 21.
        Face cards are worth 10. Aces are worth 1 or 11, whichever makes a better hand.
        Each player starts with two cards, one of the dealer's cards is hidden until the end.
        To 'Hit' is to ask for another card. To 'Stand' is to hold your total and end your turn.
        If you go over 21 you bust, and the dealer wins regardless of the dealer's hand.
        If you are dealt 21 from the start (Ace & 10), you got a blackjack.
        Blackjack usually means you win 1.5 the amount of your bet. Depends on the casino.
        Dealer will hit until his/her cards total 17 or higher.
        Doubling is like a hit, only the bet is doubled and you only get one more card.
        Split can be done when you have two of the same card - the pair is split into two hands.
        Splitting also doubles the bet, because each new hand is worth the original bet.
        You can only double/split on the first move, or first move of a hand created by a split.
        You cannot play on two aces after they are split.
        You can double on a hand resulting from a split, tripling or quadrupling you bet.
    '''
    print(rule)

                   
clear = lambda: system('cls' if name=='nt' else 'clear')
    
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
 
def dealCards(cardsInHand):
    cardsInHand.append(random.choice(cards)) 

def score(cardsList):
    if sum(cardsList) == 21 and len(cardsList) == 2:
        return 0 #represents a blackjack
    
    if 11 in cardsList and sum(cardsList) > 21:
        cardsList.remove(11)
        cardsList.append(1)
   
    return sum(cardsList)


def compare(playerScore, comScore):
    #the and condition is because if playerScore > 21 player loses all the time
    if playerScore == comScore and playerScore < 21: 
        print("    It's a draw!")
    elif comScore == 0:
        print("    Dealer has a blackjack! You lose.")
    elif playerScore == 0:
         print("    Blackjack! You win.")
    elif playerScore > 21:
        print("    You went over! You lose.")
    elif comScore > 21:
        print("    Dealer went over! You win!")
    elif playerScore > comScore:    
        print("    Player wins!")
    else:
        print("    Player loses.")


def playGame():    
    intro()
    endGame = False
    playerCards = [random.choice(cards) for _ in range(2)]
    comCards = [random.choice(cards) for _ in range(2)]
    
    while not endGame:
        playerScore = score(playerCards)
        comScore = score(comCards)   
           
        print(f"\n    Your cards: {playerCards}, current score: {playerScore}")
        print(f"    Computer's first card: {comCards[0]}")
  
        if comScore == 0 or playerScore == 0 or playerScore > 21:
            endGame = True
        else:
            draw = input("\nType 'y' to get another card and 'n' to pass: ")
            if draw == 'y':
                dealCards(playerCards)
            else:
                print("\n")
                endGame = True
    
    while comScore < 17 and comScore != 0:
        dealCards(comCards)
        comScore = score(comCards)
    
    print(f"    Your final hand: {playerCards}, final score: {playerScore}")
    print(f"    Computer's final hand: {comCards}, final score: {comScore}")
    print("\n")
        
    compare(playerScore, comScore)

clear()

intro()
print("Welcome to Blackjack!")
rulePrompt = input("\nDo you want to see the rules? Type 'y' or 'n': ")
if rulePrompt == 'y':
    rules()

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    playGame()
  
print("\nThanks for playing~")

# =============================================================================
# End of Day 11
# =============================================================================
