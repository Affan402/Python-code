import random
from replit import clear
from art import logo
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

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "game Draw!"
    elif user_score == 0 :
        return "Win with a Blackjack"
    elif comp_score == 0 :
        return "Loose, opponent has Blackjack"
    elif comp_score > 21 :
        return "You win, opponent went over!"
    elif  user_score > 21 : 
        return "You Loose, you went over!"
    elif user_score > comp_score:
        return "You win!"
    elif comp_score > user_score:
        return "You loose!" 

def play_game():
    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not game_over:
        user_score = calc_score(user_card)
        comp_score = calc_score(computer_card)
        print(f'user card {user_card} and user score {user_score}')
        print(f'computer card is {computer_card[0]}')

        if user_score == 0 or user_score >21 or comp_score == 0:
            game_over = True
        else:
            user_deal = input("Type 'y' to enter card, type 'p' to pass: ").lower()  
            if user_deal == "y":
                user_card.append(deal_card())
            elif user_deal == "p":
                game_over = True
    while comp_score != 0 and comp_score < 17:
        computer_card.append(deal_card())
        comp_score = calc_score(computer_card)
    print(f"computer card {computer_card} and score is {comp_score}")
    print(compare(user_score, comp_score))                       

while input("Do you want to play a game of BlackJack? Type 'y' or 'n'. ") == "y":
    clear()
    play_game()