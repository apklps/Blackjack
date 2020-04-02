# Blackjack

import random

def makeCardDeck(cardList):

    deck = [] # deck used by dealer
    deck.append(cardList * 16) # adding four decks to the dealer deck
    return deck

def main():

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
    split = random.randint(0, len(deck) - 1)

main()