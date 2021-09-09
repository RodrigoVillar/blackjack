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
    
    def show_print(self):
        """
        Prints out the cards of the user (player/dealer)
        """
        print(str(self.value) + " of " + str(self.color))

    def show_string(self):
        """
        Returns a string of the cards the user currently has (player/dealer)
        """
        return (str(self.value) + " of " + str(self.color))

colors = ['heart', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king']
deck = [Card(value, color) for value in values for color in colors]

def process():
    """
    Function called when game.py is run

    Begins by telling the user to hit 'c' to begin playing. Once the user proceeds, process() call round(), which
    effectively begins the game.
    """
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

    # Creating player, dealer scores
    player_score = []
    dealer_score = []

    # Gives out two cards to both player and dealer (in that order)
    for x in range(2):
        # Gives card to player, removes it from current_deck
        player_deck.append(current_deck[0])
        current_deck = current_deck[1:]

        # Gives card to dealer, removes it from current_deck
        dealer_deck.append(current_deck[0])
        current_deck = current_deck[1:]

    result = winner(player_deck, dealer_deck)

    if result is not 0:
        # Announce winner, return to main menu
        if result == 1:
            pass
        elif result == 2:
            pass

    print("You current cards are the following: " + str(show_player(player_deck)))
    print("The dealer's shown card is the following: " + str(dealer_deck[0].show_string()))

    initial_result = winner(player_deck, dealer_deck)

def show_player(deck):
    result = []
    for card in deck:
        name = (str(card.value) + " of " + str(card.color))
        result.append(name)

    return result

def get_card_value(card):
    """
    Precondition: card is a card object
    """
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
    result = 0
    # First convert cards to number value
    player_nums = []
    dealer_nums = []
    # Create list of player/dealer scores
    player_result = [0, 0]
    dealer_result = [0]
    for card in player:
        val = get_card_value(card)
        player_nums.append(val)
    for card in dealer:
        val = get_card_value(card)
        dealer_nums.append(val)
    # For undecided ace, create two variables, use as a 1 and other as 11. Then compare at the end.
    for val in player_nums:
        if type(val) == list:
            player_result[0]+= 1
            player_result[1] += 11
        else:
            player_result[0] += val
            player_result[1] += val

    # Since we're playing with dealer soft 17, no need to check 1 or 11 Ace
    dealer_result[0] += val

    # Check for blackjack
    for val in player_result:
        if val == 21:
            result = 1
    for val in dealer_result:
        if val == 21:
            if result == 1:
                result = 3
                break
            else:
                result = 2

    return result



if __name__ == "__main__":
    process()