import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

	def __init__(self, suit, rank):

		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):

		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):

		self.all_cards = []

		for suit in suits:
			for rank in ranks:
				created_card = Card(suit, rank)
				self.all_cards.append(created_card)

	def __str__(self):
		deck_comp = ''
		for card in self.all_cards:
			deck_comp += '\n ' + card.__str__()
		return 'The deck has:' + deck_comp

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal(self):
		single_card = self.all_cards.pop()
		return single_card

class Hand:

	def __init__(self):

		self.cards = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):

		self.cards.append(card)
		self.value += values[card.rank]

class Player:

	def __init__(self,name):

		self.name = name
		self.all_cards = []

	def remove_one(self):

		return self.all_cards.pop(0)

	def add_cards(self, new_cards):

		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):

		return f'Player {self.name} has {len(self.all_cards)} cards.'

def hit(deck, hand):

	hand.add_card(deck.deal())

def show_all(player1,player2):
    print("\nPlayer 1 Hand:", *player1.all_cards, sep='\n ')
    #print("Dealer's Hand =",dealer.value)
    print("\nPlayer 2 Hand:", *player2.all_cards, sep='\n ')
    #print("Player's Hand =",player.value)

# GAME SETUP

player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for x in range(5):
	player_one.add_cards(new_deck.deal())
	player_two.add_cards(new_deck.deal())

game_on = True

show_all(player_one, player_two)