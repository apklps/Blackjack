# Blackjack

import random

def makeCardDeck(cardList):

    deck = [] # deck used by dealer
    deck.append(cardList * 16) # adding four decks to the dealer deck
    return deck

def blackjack(deck, money):
    
    playAgain = False # won't play game again unless otherwise specified later
    while money > 0:
        bet = getBet(money) # gets player bet for round
        dealtCards = deal(deck)
        displayHand(dealtCards)

    return playAgain

def getBet(money):

    try:
        print('Current balance:', money) # informs player how much money they have to bet
        bet = input('How much would you like to wager?') # gets player bet
        if not type(bet) is int:
            raise TypeError # maybe this isn't the best error to raise? who knows.
        if bet > money:
            raise Exception # catch this mistake too please
    except TypeError: # input was not a number
        print('Error: Invalid Input.')
        bet = getBet(money)
    except Exception: # bet was higher than money available, or something else is broken
        print('Error: Bet is higher than money available.')
        bet = getBet(money)

    return bet

def deal(deck):
    
    dealtCards = []
    dealtCards.append('P1') # player first card
    dealtCards.append('DH') # dealer hidden card
    dealtCards.append('P2') # player second card
    dealtCards.append('DV') # dealer visible card

    return dealtCards

def displayHand(dealtCards):
    pass

def main():

    # Variables needed for game

    continueGame = True
    money = 10000

    # Card Dictionary

    cardDict = {
        'A': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 11,
        'K': 12
    }

    # Make card bank
    cardList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = makeCardDeck(cardList) # creates deck for dealer to use
    split = random.randint(0, len(deck) - 1) # finds an index for a split in the deck (like Vegas apparently)
    deck.insert(split, 'SHUFFLE') # inserts a split in the deck

    # Game loop
    while continueGame == True:
        continueGame = blackjack(deck, money)

    print('Thanks for playing Blackjack!')

main()