import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    global cards
    return random.choice(cards)

def calc_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

user_card = []
computer_card = []

for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

user_sc = user_card[0] + user_card[1]
comp_sc = computer_card[0] + computer_card[1]

score = calc_score(user_card)
if score == 0 or score >21:
    