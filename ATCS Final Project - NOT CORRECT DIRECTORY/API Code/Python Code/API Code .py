class card:
	def __init__(card, card_string):
		card.suit = card_string[0]
		card.value = card_string[1]

class hand:
	def __init__(hand, hand_string):
		hand.card_one = card(hand_string[:2])
		hand.card_two = card(hand_string[1:4])
		hand.stats = {}
	def fill(hand):
		hand.stats[hand.card_one.value] = 




if __name__ == "__main__":
	card_one = card("HK")
	print (card_one.value)
	hand = hand("H3HT")
	print (hand.card_one.suit)
	print(hand.stats["H"])

