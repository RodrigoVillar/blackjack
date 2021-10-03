"""
My attempt to code a game of blackjack, insprired by my annoyance of seeing ads 
every two seconds while playing blackjack on my phone.
"""

import random
import copy


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

    def print_card(self):
        """
        Prints out the card of the user (player/dealer)

        Example: '4 of spades'
        """
        print(str(self.value) + " of " + str(self.color))

    def return_string(self):
        """
        Returns a string of the card the user currently has (player/dealer)

        Example: '4 of spades'
        """
        return (str(self.value) + " of " + str(self.color))


class Score:
    """
    Because a player's/dealer's hand can be worth two scores at the same time
    (as a result of an Ace), this class stores the player's/dealer's hand
    as a numerical value
    """

    def __init__(self):
        """
        Initializer for Score; player/dealer by default ends up with 0 score for
        their two possible hands and an ace_present attribute of False.
        """
        self.score = [0, 0]
        self.ace_present = False

    def add_card(self, card):
        """
        Function that adds to the user's score whenever a card is given

        Preconditions: card must be a valid Card object
        """
        nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        medival = ['jack', 'queen', 'king']
        if self.ace_present:
            if card.value in nums:
                self.score[0] += int(card.value)
                self.score[1] += int(card.value)
            elif card.value in medival:
                self.score[0] += 10
                self.score[1] += 10
            else:  # Ace Present
                self.score[0] += 1
                self.score[1] += 11
        else:
            if card.value in nums:
                self.score[0] += int(card.value)
            elif card.value in medival:
                self.score[0]
            else:  # Ace Present
                self.ace_present = True
                self.score[1] = self.score[0]  # Set scores equal
                self.score[0] += 1
                self.score[1] += 11

    def has_winning_hand(self):
        """
        Function that checks if either one of the player's/dealer's two possible
        scores is equal to 21. Returns true if the player/dealer has a winning
        hand, false otherwise
        """
        return self.score[0] == 21 or self.score[1] == 21


suit = ['heart', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack',
          'queen', 'king']
deck = [Card(value, color) for value in values for color in suit]


def game():
    print("Welcome to Blackjack! Enter 'play' to begin:")
    input()  # what player inputs doesn't matter for right now
    local_deck = copy.deepcopy(deck)
    random.shuffle(local_deck)

    player_deck = []  # Initializng player deck
    dealer_deck = []  # Initializing dealer deck

    player_score = Score()
    dealer_score = Score()

    for x in range(2):  # Give card to player/dealer, then remove it from deck
        player_deck.append(local_deck[0])
        local_deck = local_deck[1:]

        dealer_deck.append(local_deck[0])
        local_deck = local_deck[1:]

    for card in player_deck:  # Calculate player score
        player_score.add_card(card)

    for card in dealer_deck:  # Calculate dealer score
        dealer_score.add_card(card)

    win = winner(player_score, dealer_score)

    if win == -1:
        while True:
            print("You have the following cards: ")
            for card in player_deck:
                card.print_card()
            print("The dealer has the following card: " + card.return_string())
            choice = input(
                "Would you like to hit or stand? Enter 'hit' to hit and 'stand' to stand: ")
            if choice == 'hit':
                pass
            else:  # Implicitly stand
                pass
                break  # Once stand is called, player cannot go back

    elif win == 0:
        print("Both you and the dealer have 21 and the same cards, PUSH!")
    elif win == 1:
        print("Congrats, you have blackjack!")
    else:
        print("Sorry, you lost!")


def winner(player, dealer):
    """
    Function that determines who won the game of Blackjack. Returns -1 if no one
    has won yet, 1 if the player has won, 2 if the dealer has won, and 0 if 
    there is a tie (push)

    Precondition: player, dealer must be valid Score objects
    """
    player_won = player.has_winning_hand()
    dealer_won = dealer.has_winning_hand()
    # If just player has 21 or if just dealer has 21, return either 1 or 2
    if player_won and dealer_won == False:
        return 1
    elif dealer_won and player_won == False:
        return 2
    # If player/dealer have same value AND both of them won, return 0 (push)
    elif player_won and dealer_won:
        return 0

    # Otherwise, return -1
    return -1


def hit_helper():
    pass


def stand_helper():
    pass


if __name__ == "__main__":
    game()
