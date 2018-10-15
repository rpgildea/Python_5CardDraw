import random
from collections import namedtuple
import os
import time

Couple = namedtuple("Couple", ("first", "second"))


class Player(object):
    def __init__(self, name):
        self.DECK_OF_CARDS = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
                              '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                              '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                              '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD']
        self.RANKS_IN_DECK = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.SUIT_IN_DECK = ('S', 'C', 'H', 'D')
        self.name = name
        self.credits = 0
        self.bet = 0
        self.firstHand = []
        self.secondHand = []
        self.powerOfHand = [Couple("Pair", False), Couple("Two Pair", False), Couple("Three of a Kind", False),
                            Couple("Straight", False), Couple("Flush", False), Couple("Full House", False),
                            Couple("Four of a Kind", False), Couple("Straight Flush", False),
                            Couple("Royal Flush", False)]
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0
        self.numJ = 0
        self.numQ = 0
        self.numK = 0
        self.numA = 0
        self.numSpades = 0
        self.numClubs = 0
        self.numHearts = 0
        self.numDiamonds = 0
        self.values = {'2': self.num2, '3': self.num3, '4': self.num4, '5': self.num5, '6': self.num6,
                       '7': self.num7, '8': self.num8, '9': self.num9, '10': self.num10, 'J': self.numJ,
                       'Q': self.numQ, 'K': self.numK, 'A': self.numA}

    def display(self):
        print("Name: ", self.name)
        time.sleep(1)
        print("Credits: ", self.credits)
        time.sleep(1)
        print("Ranks: ", self.values)
        time.sleep(4)
        print("Suits: ")
        print("Spades:", self.numSpades)
        print("Clubs:", self.numClubs)
        print("Hearts:", self.numHearts)
        print("Diamonds:", self.numDiamonds)
        time.sleep(4)
        # for first, second in self.powerOfHand:
        #     print(first, ":", second)
        # time.sleep(6)
        print("\n" * 50)

    def reset_hand_and_stats(self):
        self.DECK_OF_CARDS = ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS',
                              '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
                              '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
                              '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD']
        self.firstHand = []
        self.secondHand = []
        self.powerOfHand = [Couple("Pair", False), Couple("Two Pair", False), Couple("Three of a Kind", False),
                            Couple("Straight", False), Couple("Flush", False), Couple("Full House", False),
                            Couple("Four of a Kind", False), Couple("Straight Flush", False),
                            Couple("Royal Flush", False)]
        self.num2 = 0
        self.num3 = 0
        self.num4 = 0
        self.num5 = 0
        self.num6 = 0
        self.num7 = 0
        self.num8 = 0
        self.num9 = 0
        self.num10 = 0
        self.numJ = 0
        self.numQ = 0
        self.numK = 0
        self.numA = 0
        self.numSpades = 0
        self.numClubs = 0
        self.numHearts = 0
        self.numDiamonds = 0
        self.values = {'2': self.num2, '3': self.num3, '4': self.num4, '5': self.num5, '6': self.num6,
                       '7': self.num7, '8': self.num8, '9': self.num9, '10': self.num10, 'J': self.numJ,
                       'Q': self.numQ, 'K': self.numK, 'A': self.numA}

    def increment_rank(self):
        rank = []
        for j in range(0, 5):
            rank.append(self.secondHand[j][0])
            if rank[j] == '2':
                self.num2 += 1
            elif rank[j] == '3':
                self.num3 += 1
            elif rank[j] == '4':
                self.num4 += 1
            elif rank[j] == '5':
                self.num5 += 1
            elif rank[j] == '6':
                self.num6 += 1
            elif rank[j] == '7':
                self.num7 += 1
            elif rank[j] == '8':
                self.num8 += 1
            elif rank[j] == '9':
                self.num9 += 1
            elif rank[j] == '1':
                self.num10 += 1
            elif rank[j] == 'J':
                self.numJ += 1
            elif rank[j] == 'Q':
                self.numQ += 1
            elif rank[j] == 'K':
                self.numK += 1
            elif rank[j] == 'A':
                self.numA += 1

    def increment_suit(self):
        # Manages the number of each suit for the player
        suit = []
        for j in range(0, 5):
            if self.secondHand[j][1] == '0':
                suit.append(self.secondHand[j][2])
            else:
                suit.append(self.secondHand[j][1])
            if suit[j] == 'S':
                self.numSpades += 1
            elif suit[j] == 'C':
                self.numClubs += 1
            elif suit[j] == 'H':
                self.numHearts += 1
            elif suit[j] == 'D':
                self.numDiamonds += 1

    def update_values(self):
        # Updates ranks to help when calculating a hand
        self.values = {'2': self.num2, '3': self.num3, '4': self.num4, '5': self.num5, '6': self.num6,
                       '7': self.num7, '8': self.num8, '9': self.num9, '10': self.num10, 'J': self.numJ,
                       'Q': self.numQ, 'K': self.numK, 'A': self.numA}

    def calculate_hand(self):
        # calculates what hand the player has(Royal Flush displays true for both flush and royal flush)
        # this function also manages the winnings based on the hand
        index = -1
        for i in range(0, len(self.powerOfHand)):
            if self.powerOfHand[i][1]:
                index = i
        if index == -1:
            print("YOU RECEIVED NOTHING :(\n")
        if index == 0:
            print("YOU RECEIVED A PAIR\n")
            self.credits = self.credits + 1 * self.bet
        if index == 1:
            print("YOU RECEIVED A TWO PAIR\n")
            self.credits = self.credits + 2 * self.bet
        if index == 2:
            print("YOU RECEIVED A THREE OF A KIND\n")
            self.credits = self.credits + 3 * self.bet
        if index == 3:
            print("YOU RECEIVED A STRAIGHT\n")
            self.credits = self.credits + 4 * self.bet
        if index == 4:
            print("YOU RECEIVED A FLUSH\n")
            self.credits = self.credits + 6 * self.bet
        if index == 5:
            print("YOU RECEIVED A FULL HOUSE\n")
            self.credits = self.credits + 9 * self.bet
        if index == 6:
            print("YOU RECEIVED A FOUR OF A KIND\n")
            self.credits = self.credits + 25 * self.bet
        if index == 7:
            print("YOU RECEIVED A STRAIGHT FLUSH\n")
            self.credits = self.credits + 50 * self.bet
        if index == 8:
            print("YOU RECEIVED A ROYAL FLUSH\n")
            self.credits = self.credits + 250 * self.bet

    def update_power_of_hand(self):
        self.powerOfHand = [Couple("Pair", self.calculate_pair()), Couple("Two Pair", self.calculate_two_pair()),
                            Couple("Three of a Kind", self.calculate_three_of_a_kind()),
                            Couple("Straight", self.calculate_straight()),
                            Couple("Flush", self.calculate_flush()), ("Full House", self.calculate_full_house()),
                            Couple("Four of a Kind", self.calculate_four_of_a_kind()),
                            Couple("Straight Flush", self.calculate_straight_flush()),
                            Couple("Royal Flush", self.calculate_royal_flush())]

    def calculate_pair(self):
        # Checks if hand consists of ONE pair
        combination = {self.secondHand[0][0], self.secondHand[1][0], self.secondHand[2][0],
                       self.secondHand[3][0], self.secondHand[4][0]}
        return len(combination) == 4

    def calculate_two_pair(self):
        # Checks if hand consists of two pairs
        values = {}
        combination = {self.secondHand[0][0], self.secondHand[1][0],
                       self.secondHand[2][0],
                       self.secondHand[3][0], self.secondHand[4][0]}
        result = 1
        # This for-loop updates the dictionary, 'values', based off the secondHand
        for i in range(0, 5):
            if values.get(self.secondHand[i][0]) is not None:
                values[self.secondHand[i][0]] = 1 + values.get(self.secondHand[i][0])
            else:
                values[self.secondHand[i][0]] = 1
        for key in values:
            if result < values[key]:
                result = values[key]
        return result == 2 and len(combination) == 3

    def calculate_three_of_a_kind(self):
        # Checks if hand consists of a three of a kind
        values = {}
        result = 1
        # This for-loop updates the dictionary, 'values', based off the secondHand
        for i in range(0, 5):
            if values.get(self.secondHand[i][0]) is not None:
                values[self.secondHand[i][0]] = 1 + values.get(self.secondHand[i][0])
            else:
                values[self.secondHand[i][0]] = 1
        for key in values:
            if result < values[key]:
                result = values[key]
        return result == 3

    def calculate_straight(self):
        # Checks if a hand consists of a Straight
        if self.values[self.RANKS_IN_DECK[len(self.RANKS_IN_DECK)-1]] == 1:
            count = 1
        else:
            count = 0
        for i in range(0, len(self.values)):
            if count == 5:
                return True
            if self.values[self.RANKS_IN_DECK[i]] == 1:
                count = count + 1
            else:
                count = 0
        return False

    def calculate_flush(self):
        # Checks if cards are same suit aka a Flush
        return (self.numClubs == 5 or self.numSpades == 5 or self.numHearts == 5
                or self.numDiamonds == 5)

    def calculate_full_house(self):
        # Checks if hand consists of Full House
        values = {}
        combination = {self.secondHand[0][0], self.secondHand[1][0],
                       self.secondHand[2][0], self.secondHand[3][0], self.secondHand[4][0]}
        result = 1
        # This for-loop updates the dictionary, 'values', based of the secondHand
        for i in range(0, 5):
            if values.get(self.secondHand[i][0]) is not None:
                values[self.secondHand[i][0]] = 1 + values.get(self.secondHand[i][0])
            else:
                values[self.secondHand[i][0]] = 1
        for key in values:
            if result < values[key]:
                result = values[key]
        return result == 3 and len(combination) == 2

    def calculate_four_of_a_kind(self):
        # Checks if hand consists of four of a kind
        combination = {self.secondHand[0][0], self.secondHand[1][0],
                       self.secondHand[2][0], self.secondHand[3][0], self.secondHand[4][0]}
        return len(combination) == 2

    def calculate_straight_flush(self):
        # Checks is a hand consists of a Straight Flush
        return self.calculate_straight() and self.calculate_flush()

    def calculate_royal_flush(self):
        # Checks if hand is a Royal Flush
        return (self.calculate_flush() and
                (self.values['10'] == 1 and self.values['J'] == 1 and self.values['Q'] == 1 and self.values['K'] == 1
                 and self.values['A'] == 1))
# ----------------- END OF CLASS (Player) -----------------


# ----------------- HELPER FUNCTIONS (START) -----------------
def deal_first_hand(player):
    # This function deals the first hand
    for i in range(0, 5):
        card = player.DECK_OF_CARDS.pop(random.randint(0, len(player.DECK_OF_CARDS)-1))
        player.firstHand.append(card)


def deal_second_hand_with_keep(player, answer):
    # This function deals the second hand when player wants to keep certain cards
    try:
        answer = answer.split(",")
        answer.sort(reverse=True)
        for i in range(0, len(answer)):
            kept_card = player.firstHand.pop(int(answer[i]))
            # print(keptCard)
            player.secondHand.append(kept_card)
            # print(newHand)
        for i in range(0, 5 - len(answer)):
            card = player.DECK_OF_CARDS.pop(random.randint(0, len(player.DECK_OF_CARDS)-1))
            player.secondHand.append(card)
    except IndexError:
        print("You've entered a number outside of the range 0-4.\n"
              "Please enter an answer within the range: ")
        answer_handling(player)
    except ValueError:
        print("You've entered an answer of the wrong value.\n"
              "Please enter an answer with the correct values(numbers): ")
        answer_handling(player)


def deal_second_hand_without_keep(player):
    # Deals the second hand when player chooses not to keep any of the cards
    for i in range(0, 5):
        card = player.DECK_OF_CARDS.pop(random.randint(0, len(player.DECK_OF_CARDS)-1))
        player.secondHand.append(card)


def answer_handling(player):
    # checks if input is correct for choosing cards the player would like to keep
    answer = input("Which cards would you like to keep?(Choose 0-4 separating numbers with a comma or\n"
                   "simply press 'Enter' if you don't want to keep any.)")
    if answer is not '':  # Keep kept cards and deal remaining hand from deck
        deal_second_hand_with_keep(player, answer)
    else:  # Deal a completely new hand
        deal_second_hand_without_keep(player)


def credit_handling(player):
    # Checks if the credit are numbers only
    player.credits = input("How much credit would you like to start with?(Default is 10. Range[10-1,000,000])\n")
    try:
        player.credits = int(player.credits)
    except ValueError:
        print("You have entered a value that is not a number. Please try again.\n")
        credit_handling(player)
    if player.credits is '' or player.credits < 10:
        player.credits = 10
    if player.credits > 1000000:
        player.credits = 1000000


def bet_handling(player):
    print("Here is the amount of credits", player.name, "has:", player.credits)
    bet = input("How much credit would you like to bet?(Default is 1. Range[1-10])\n")
    try:
        bet = int(bet)
    except ValueError:
        print("You have entered a value that is not a number. Please try again.\n")
        bet_handling(player)
    if player.credits is '' or player.credits < 1:
        bet = 1
    if bet > 10:
        bet = 10
    if bet > player.credits:
        print("You have entered a bet greater than your current credit(", player.bet, ">", player.credits, ")")
        print("Please enter another amount.\n")
        bet = bet_handling(player)
    # print(player.name, "has bet", player.bet, "credits")
    # player.credits = player.credits - player.bet
    return bet


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def run():
    # Initialize 'hand' with 5 cards and remove them from the 'deck_of_cards'
    name = input("Please enter a name: ")
    player1 = Player(name)
    # clear_screen()
    credit_handling(player1)
    while player1.credits != 0:
        player1.bet = bet_handling(player1)
        print(player1.name, "has bet", player1.bet, "credits")
        player1.credits = player1.credits - player1.bet
        deal_first_hand(player1)
        print(player1.firstHand)
        answer_handling(player1)
        # player1.secondHand = ['2S', '2H', '4D', '5S', 'AS'] #(TESTING: PAIR)
        # player1.secondHand = ['2S', '2D', '4S', '4H', 'AS'] #(TESTING: TWO PAIR)
        # player1.secondHand = ['2S', '2H', '2D', '5S', 'AS'] #(TESTING: THREE OF A KIND)
        # player1.secondHand = ['2S', '3D', '4C', '5S', 'AH'] #(TESTING: STRAIGHT)
        # player1.secondHand = ['10S', '3S', '4S', '5S', 'AS'] #(TESTING: FLUSH)
        # player1.secondHand = ['2S', '2D', '2H', 'AS', 'AC'] #(TESTING: FULL HOUSE)
        # player1.secondHand = ['2S', '2C', '2H', '2D', 'AS'] #(TESTING: FOUR OF A KIND)
        # player1.secondHand = ['2S', '3S', '4S', '5S', 'AS'] #(TESTING: STRAIGHT FLUSH)
        # player1.secondHand = ['10S', 'JS', 'QS', 'KS', 'AS'] # (TESTING: ROYAL FLUSH)
        print(player1.secondHand)
        player1.increment_rank()
        player1.increment_suit()
        player1.update_values()
        player1.update_power_of_hand()
        player1.calculate_hand()
        time.sleep(4)
        player1.display()
        player1.reset_hand_and_stats()
        # print("Pair: ", player1.calculate_pair())
        # print("Two Pair: ", player1.calculate_two_pair())
        # print("Three of a kind: ", player1.calculate_three_of_a_kind())
        # print("Straight: ", player1.calculate_straight())
        # print("Flush: ", player1.calculate_flush())
        # print("Full House: ", player1.calculate_full_house())
        # print("Four of a kind: ", player1.calculate_four_of_a_kind())
        # print("Straight Flush: ", player1.calculate_straight_flush())
        # print("Royal Flush: ", player1.calculate_royal_flush())
# ----------------- HELPER FUNCTIONS (END) -----------------


# ----------------- HERE IS WHERE WE RUN THE GAME -----------------
run()
