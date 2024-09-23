from art import logo
from art import vs
from game_data import data
import random
from replit import clear

print(logo)
score = 0
game = True
is_correct = False

def format_data(account):
    acc_name = account["name"]
    acc_descrp = account["description"]
    acc_country = account["country"]
    return f"{acc_name}, a {acc_descrp}, from {acc_country}"

def check_answer(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"

while game:
    if is_correct and guess == "a":
        account_a = account_a
    else:        
        account_a = random.choice(data)
    if is_correct and guess == "b":
        account_a = account_b
    else:
        account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]
    is_correct = check_answer(guess, followers_a, followers_b)
    clear()
    if is_correct:
        score += 1
        print(f"You're right! Your score is {score}.")
        
    else:
        print(f"You're Wrong! Total score is {score}.")
        game = False                 