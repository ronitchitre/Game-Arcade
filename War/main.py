# Game called war
# simulated by 2 computers
# card class
# deck class
# player with higher card wins and takes the lower card with him
# player with 0 cards loses

import random

class Card:
    def __init__(self, section, value):
        self.section = section
        self.value = value

    def show_card(self):
        if self.value <= 10:
            return (self.section, self.value)
        elif self.value == 11:
            return (self.section, "Jack")
        elif self.value == 12:
            return (self.section, "Queen")
        elif self.value == 13:
            return (self.section, "King")
class Player:
    def __init__(self,name,player_cards=0):
        self.name = name
        self.player_cards=player_cards

    def say_name(self):
        return f"my name is {self.name}"

def lister(value, section):
    deck_list = []
    for value in range(1, value + 1):
        deck_list.append(Card(section, value))
    return deck_list

def make_a_deck():
    hearts = lister(13, "hea")
    diamonds = lister(13, "diam")
    spades = lister(13, "spa")
    clubs = lister(13, "clu")
    return hearts + diamonds + spades + clubs


def game_round(player_set,name):
    card1=random.randint(0,len(player_set)-1)
    player_got=player_set[card1].show_card()
    print(f"{name} got {player_got}")
    return player_set[card1]


def card_judger(card1,card2):
    if card1.value>card2.value:
        return ("player1won",card1,card2)
    elif card1.value<card2.value:
        return ("player2won",card2,card1)
    else:
        return ("war",card1,card2)


def display():
    print(player1.say_name())
    print(player2.say_name())
    deck = make_a_deck()
    random.shuffle(deck)
    player1.player_cards = deck[0:26]
    player2.player_cards = deck[26:52]
    while True:
        print(f"{player1.name} has {len(player1.player_cards)} cards")
        print(f"{player2.name} has {len(player2.player_cards)} cards")
        if len(player1.player_cards)==0 or len(player2.player_cards)==0:
            if len(player1.player_cards)==0:
                print(f"{player2.name} won")
            elif len(player2.player_cards)==0:
                print(f"{player1.name} won")
            quit()
        card_on_table = []
        while True:
            player1_card = game_round(player1.player_cards, player1.name)
            player2_card = game_round(player2.player_cards, player2.name)
            player1.player_cards.remove(player1_card)
            player2.player_cards.remove(player2_card)
            result = card_judger(player1_card, player2_card)
            card_on_table.append(result[1])
            card_on_table.append(result[2])
            if result[0] == "player1won":
                player1.player_cards = player1.player_cards + card_on_table
                print(f"{player1.name} won")
                break
            elif result[0] == "player2won":
                player2.player_cards = player2.player_cards + card_on_table
                print(f"{player2.name} won")
                break
            elif result[0] == "war":
                print("its war")
                pass


player1=Player(input("Enter your name"))
player2=Player(input(("Enter your name")))
display()

