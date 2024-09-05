import random

def play():
    user = input("What's your choice? rock(r), paper(p) or scissor(s)\n")
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "You won!"
    return "You Lost!"
    
def is_win(player, computer):
    if (player == "r" and computer == "s") or (player == "p" and computer == "r") or (player == "s" and computer == "p"):
        return True

print(play())        