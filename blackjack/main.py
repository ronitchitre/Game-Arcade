import random


class Card:
    def __init__(self,value,section):
        self.value=value
        self.section=section

    def show_card(self):
        if self.value != 11 and self.value != 12 and self.value != 13:
            return (self.value,self.section)
        if self.value == 11:
            return ("jack",self.section)
        if self.value == 12:
            return ("queen",self.section)
        if self.value == 13:
            return ("king",self.section)


class Player:
    def __init__(self,name,cards = [],chips = 5):
        self.name = name
        self.chips = chips
        self.cards = cards

    def tell_name(self):
        return f"my name is {self.name}"

    def see_cards(self):
        list_of_cards=[]
        for i in self.cards:
            list_of_cards.append(i.show_card())
        return list_of_cards

    def add_chips(self,chips_added):
        self.chips = self.chips+chips_added

    def remove_chips(self,chips_removed):
        self.chips = self.chips+chips_removed


def lister(value,section):
    deck=[]
    for i in range(1,value+1):
        deck.append(Card(i,section))
    return deck


my_deck=lister(13,"hea") + lister(13,"dia") + lister(13,"spa") + lister(13,"clu")
random.shuffle(my_deck)
player = Player("ronit" )



def hit(deck):
    return my_deck.pop( )

def adder(list):
    total = 0
    for i in list:
        total = total + i
    return total


def value_adder(deck):
    adding_list=[]
    for i in deck:
        adding_list.append(i.value)
    for i in range(len(adding_list)):
        if adding_list[i] == 11 or adding_list[i] == 12 or adding_list[i] == 13:
            adding_list[i] = 10
    while adder(adding_list) <=21:
        if adder(adding_list)-1+11>21:
            break
        try:
            adding_list[adding_list.index(1)] = 11
        except:
            break
    return adder(adding_list)

def game_rule(deck):
    total = value_adder(deck)
    return total


def display():
    player.cards = []
    player.cards.append(hit(my_deck))
    player.cards.append(hit(my_deck))
    dealer_cards = []
    dealer_cards.append(hit(my_deck))
    dealer_cards.append(hit(my_deck))
    print(f"{player.name} has got ")
    print("your cards are")
    for i in player.cards:
        print(i.show_card())
    print("dealers cards are")
    print(dealer_cards[0].show_card())
    chips_beted = "wrong"
    while chips_beted.isdigit() is False:
        chips_beted = input("How many chips do you want to bet")
        if str(chips_beted).isdigit() is False:
            print("enter a valid number")
    while int(chips_beted) > player.chips:
        print(f"you have {player.chips} chips left")
        chips_beted = input("how many chips do you want to bet")
    answer = "wrong"
    while answer != "hit" and answer != "stay":
        answer = input("What do you want to do")
        if answer == "quit":
            display()
        if answer != "hit" or answer != "stay":
            print("hit or stay")
    while game_rule(player.cards) < 21:
        while answer == "hit":
            player.cards.append(hit(my_deck))
            print(player.see_cards())
            if game_rule(player.cards) >=21:
                break
            while True:
                answer = input("What do you want to do")
                if answer == "quit":
                    quit()
                if answer == "hit" or answer == "stay":
                    break
                else:
                    print("hit or stay")
        if answer == "stay":
            break
    if game_rule(player.cards) > 21:
        print(f"{player.name} bounced. {player.name} loses \n")
        player.chips = player.chips - int(chips_beted)
        print(f"you have {player.chips} chips left")
        if player.chips <= 0:
            quit()
        elif player.chips > 0:
            display()
    elif game_rule(player.cards) == 21:
        print(f"blackjack!! {player.name} wins \n")
        player.chips = round(player.chips + ((1.5)*int(chips_beted)))
        print(f"you have {player.chips} chips left")
        if player.chips <= 0:
            quit()
        elif player.chips > 0:
            display()
    print("now its dealers turn")
    while abs(game_rule(dealer_cards)-21) >= abs(game_rule(player.cards)-21) and game_rule(dealer_cards)<21:
        print("dealers cards are")
        dealer_cards.append(hit(my_deck))
        for i in dealer_cards:
            print(i.show_card())
        if game_rule(dealer_cards) > 21:
            print(f"dealer bounced {player.name} wins \n")
            player.chips = player.chips + int(chips_beted)
            print(f"you have {player.chips} chips left")
            if player.chips <= 0:
                quit()
            elif player.chips > 0:
                display()
    if abs(game_rule(dealer_cards)-21) < abs(game_rule(player.cards)):
        for i in dealer_cards:
            print(i.show_card())
        print("dealer is closer to 21 dealer wins \n")
        player.chips = player.chips - int(chips_beted)
        print(f"you have {player.chips} chips left")
        if player.chips <= 0:
            quit()
        elif player.chips > 0:
            display()

print(f"You start with {player.chips} chips")
display()


















