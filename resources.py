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

class Bust:
    """
    Bust is a type to represent whether if the score of the player's/dealer's 
    hand is greater than 21
    """
    pass


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
        self.soft_score = None
        self.hard_score = 0

    def add_card(self, card):
        """
        Function that adds to the user's score whenever a card is given

        Preconditions: card must be a valid Card object
        """
        nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
        medival = ['jack', 'queen', 'king']
    
        # If hard_score == None:
            # If card is not ace, add to just soft score.
            # If card is ace, add to both soft and hard score
                # Check if hard_score over 21. If it is, set hard_score equal to
                # bust object
        # If hard_score != None:
        if self.soft_score == None: # Player hasn't had an ace before this
            if card.value == 'ace': # Ace
                self.soft_score = 11 + self.hard_score
                self.hard_score += 1
                if self.check_soft_bust():
                    self.soft_score = Bust()
            elif card.value in nums: # Integer card
                self.hard_score += int(card.value)
            else: # Either a jack, king or queen
                self.hard_score += 10
        elif type(self.soft_score) == Bust: # Player's soft score already over 21
            if card.value == 'ace':
                self.hard_score += 1
            elif card.value in nums:
                self.hard_score += int(card.value)
            else:
                self.hard_score += 10
        else: # Player already has an ace in their hand
            if card.value == 'ace': # Ace
                self.hard_score += 1
                self.soft_score += 11
            elif card.value in nums: # Integer Card
                self.hard_score += int(card.value)
                self.soft_score += int(card.value)
            else: # Either a jack, king, or queen
                self.hard_score += 10
                self.soft_score += 10
            # Check for bust
            if self.check_soft_bust():
                self.soft_score = Bust()


    def has_blackjack(self):
        """
        Function that checks if either one of the player's/dealer's two possible
        scores is equal to 21. Returns true if the player/dealer has a winning
        hand, false otherwise
        """
        if type(self.soft_score) == Bust:
            return self.hard_score == 21
        else:
            return self.soft_score == 21 or self.hard_score == 21

    def check_soft_bust(self):
        """
        Function that checks if the player's hard score is over 21.

        Precondition: the player MUST already have an ace in their hand. In
        other words, self.hard_score must be of type int, NOT 'None' or 'Bust'
        """
        return self.soft_score > 21
    
    def general_bust(self):
        """
        Function that checks if the player has completely busted. In this case,
        checks if the player's hard score is greater than 21. Returns true if
        hard_score is greater than 21, false otherwise
        """
        return self.hard_score > 21
