"""
My attempt to code a game of blackjack, insprired by my annoyance of seeing ads every two seconds while playing blackjack on my phone.
"""

import random, copy

class Card:
    """
    A card class that stores the value and suit of a card.
    """

    def __init__(self, value, color):
        """
        Parameter value: the value of the card
        Precondition: value is a string representing the value of a card

        Parameter color: the suit of the card
        Precondition: color is a string respresenting the suit of a card
        """
        self.value = value
        self.color = color
    
    def show_card(self):
        """
        Prints out the card of the user (player/dealer)
        """
        print(str(self.value) + " of " + str(self.color))

    def return_string(self):
        """
        Returns a string of the cards the user currently has (player/dealer)
        """
        return (str(self.value) + " of " + str(self.color))

suit = ['heart', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = [Card(value, color) for value in values for color in suit]

def game():
    print("Welcome to Blackjack! Enter 'play' to begin:")
    input() # what player inputs doesn't matter for right now
    local_deck = copy.deepcopy(deck)
    random.shuffle(local_deck)

    player_deck = [] # Initializng player deck
    dealer_deck = [] # Initializing dealer deck

    for x in range(2): # Give card to player/dealer, then remove it from deck
        player_deck.append(local_deck[0])
        local_deck = local_deck[1:]

        dealer_deck.append(local_deck[0])
        local_deck = local_deck[1:]

    win = winner(player_deck, dealer_deck)

    if win == -1:
        pass
    elif win == 0:
        pass
    elif win == 1:
        pass
    else:
        pass

def winner(player, dealer):
    """
    Function that determines who won the game of Blackjack. Returns -1 if no one has won yet, 
    1 if the player has won, 2 if the dealer has won, and 0 if there is a tie
    """
    pass





if __name__ == "__main__":
    game()