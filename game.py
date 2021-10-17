"""
My attempt to code a game of blackjack, insprired by my annoyance of seeing ads 
every two seconds while playing blackjack on my phone.

- Rodrigo Villar
"""

import random
import copy
from resources import *

suit = ['heart', 'diamonds', 'spades', 'clubs']
values = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack',
          'queen', 'king']
deck = [Card(value, color) for value in values for color in suit]


def game():

    # Welcome Screen
    print("Welcome to Blackjack! Enter 'play' to begin:")
    input()  # what player inputs doesn't matter for right now
    print("\n--------\n")

    # Setting up deck
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

    win = winner(player_score, dealer_score)  # Check to see if there is an
    # immediate winner

    dealer_shown_card = dealer_deck[0]

    game_on = True

    if win == -1:
        while game_on:
            
            # Showing cards
            print("You have the following cards: ")
            for card in player_deck:
                card.print_card()
            print("The dealer has the following card shown: " +
                  dealer_shown_card.return_string())
            print("\n--------\n")

            # Player either hits or stands
            choice = input(
                "Would you like to hit or stand? Enter 'hit' to hit and 'stand' to stand: ")
            print("\n--------\n")
                
            # If player hits:
            if choice == 'hit':
                # Deal card to user
                player_deck.append(local_deck[0])
                local_deck = local_deck[1:]
                player_score.add_card(player_deck[-1])
                # Tell player what card they got
                print("You got: " + player_deck[-1].return_string())
                # Check if user has busted or not
                if player_score.general_bust():
                    print("Sorry, but you've went over 21. You lose!")
                    break
                # Check if user has won
                win = winner(player_score, dealer_score)
                if win == 1:
                    print("Congratulations, you have blackjack!")
                    break

            # If player stands
            else: 
                while True:
                    # Dealer is hitting until he has a soft 17
                    # Already assumed that dealer does not have a winning hand
                    # prior to this while loop beginning
                    print("The dealer currently has the following cards: ")
                    for card in dealer_deck:
                        card.print_card()

                    # Give dealer card
                    dealer_deck.append(local_deck[0])
                    local_deck = local_deck[1:]
                    dealer_score.add_card(dealer_deck[-1])

                    # Tell player what the dealer got
                    print("The dealer got a: " +
                          dealer_deck[-1].return_string())
                    print("\n--------\n")
                    # Check win status
                    win = winner(player_score, dealer_score)
                    if win == 0:
                        print("You and the dealer both have the same score, tie!")
                        game_on = False
                        break
                    # Check if there if the dealer won
                    elif win == 2:
                        print("The dealer has won, you lose!")
                        game_on = False
                        break
                    # Check if dealer has greater score than player
                    elif win == 1:
                        print("Congrats, you win!")
                        game_on = False
                        break
                    else:
                        continue



    elif win == 0:
        print("Both you and the dealer have 21 and the same cards, PUSH!")
    elif win == 1:
        print("Congrats, you have blackjack!")
    else:
        print("Sorry, you lost!")


def winner(player, dealer):
    """
    Function that determines who has won the current game of Blackjack. Returns
    -1 if no one has won yet, 1 if the player has won, 2 if the dealer has won,
    and 0 if there is a tie (push)

    Rules for blackjack: After the player/dealer are given their cards, winner
    is called(). There is a winner at this point in time ONLY IF either the
    player or dealer has a soft or hard score of 21. If both the player and
    dealer have blackjack, then there is a push.

    If there is no immediate winner, the next time winner is called is when the
    player decides to stand. Here, the outcome of the game is in the hands of
    the dealer. This method is abiding by the principle that most casinos
    do, which is that the dealer must continue hitting until they get at least a
    soft 17 (if they do not have an Ace or their soft hand is over 21, then the 
    dealer's hard score must be atleast a 17). winner() starts by checking if
    the player OR the dealer hasblackjack. If the player AND the dealer have 
    blackjack, there is a push.Otherwise, it checks for the following
    conditions: if the dealer's hard score is over 21, the player wins. If the 
    dealer has at least a soft 17 and has a greater score than the player, the 
    dealer wins. If the dealer has at least a soft 17 and the player has a 
    greater score, the player wins. If the dealer and player both have a score 
    over a soft 17 and are both tied, the game ends in a push. Otherwise, there
    is no winner yet.

    Precondition: player, dealer must be valid Score objects
    """
    player_won = player.has_blackjack()
    dealer_won = dealer.has_blackjack()
    # If just player has 21 and dealer doesn't
    if player_won and (dealer_won == False):
        return 1
    # If just dealer has 21 and dealer doesn't
    elif dealer_won and (player_won == False):
        return 2
    # If player/dealer both have blackjack, return 0 (push)
    elif player_won and dealer_won:
        return 0
    else:
        # If dealer has no ace or their soft_score is a bust
        if dealer.soft_score == None or type(dealer.soft_score) == Bust:
            # If dealer does not have 17, continue game
            if dealer.hard_score < 17:
                return -1
            
            # If dealer is over 21, player wins
            if dealer.hard_score > 21: return 1

            # Split between soft/hard score path

            # Case of player only has hard score
            if player.soft_score == None or type(player.soft_score) == Bust:
                # If dealer has higher score
                if dealer.hard_score > player.hard_score:
                    return 2
                # If there is a push
                elif dealer.hard_score == player.hard_score:
                    return 0
                # If player has higher score
                else:
                    return 1
            # Case of player having a soft score
            else:
                # If dealer has higher score
                if dealer.hard_score > player.soft_score:
                    return 2
                # If there is a push
                elif dealer.hard_score == player.hard_score:
                    return 0
                # If player has a higher score
                else:
                    return 1
        # If dealer has a soft score    
        else:
            if dealer.soft_score < 17:
                return -1

            # Split betwen soft/hard score path
            if player.soft_score == None or type(player.soft_score) == Bust:
                # If dealer has higher score
                if dealer.soft_score > player.hard_score:
                    return 2
                # If there is a push
                elif dealer.soft_score == player.hard_score:
                    return 0
                # If player has higher score
                else:
                    return 1
            # Case of player having a soft score
            else:
                # If dealer has higher score
                if dealer.soft_score > player.soft_score:
                    return 2
                # If there is a push
                elif dealer.soft_score == player.hard_score:
                    return 0
                # If player has a higher score
                else:
                    return 1


if __name__ == "__main__":
    game()
