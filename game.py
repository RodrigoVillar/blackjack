"""
My attempt to code a game of blackjack, insprired by my annoyance of seeing ads every two seconds while playing blackjack on my phone.


"""

import random, copy

class Card:

    def __init__(self, value, color):
        self.value = value
        self.color = color
    
    def show(self):
        print(str(self.value) + " of " + str(self.color))

    def show_string(self):
        return (str(self.value) + " of " + str(self.color))

colors = ['heart', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = [Card(value, color) for value in values for color in colors]

def process():
    print("Welcome to Blackjack! Enter c to continue:")

    while True:
        letter = input()
        if letter == 'c':
            break

    round()

def round():
    # Creates set of cards
    current_deck = copy.deepcopy(deck)
    random.shuffle(current_deck)

    # Creating player, dealer set
    player_deck = []
    dealer_deck = []

    # Gives out two cards to both player and dealer (in that order)
    for x in range(2):
        # Gives card to player, removes it from current_deck
        player_deck.append(current_deck[0])
        current_deck = current_deck[1:]

        # Gives card to dealer, removes it from current_deck
        dealer_deck.append(current_deck[0])
        current_deck = current_deck[1:]

    print("You current cards are the following: " + str(show_player(player_deck)))
    print("The dealer's shown card is the following: " + str(dealer_deck[0].show_string()))

    initial_result = winner(player_deck, dealer_deck)
    if initial_result ==

    while True:
        break

def show_player(deck):
    result = []
    for card in deck:
        name = (str(card.value) + " of " + str(card.color))
        result.append(name)

    return result

def get_card_value(card):
    value = card.value
    if value == 'ace':
        return [1, 11]
    elif value == 'jack':
        return 10
    elif value == 'queen':
        return 10
    elif value == 'king':
        return 10
    else:
        return int(value)

def winner(player, dealer):
    result = None




if __name__ == "__main__":
    process()