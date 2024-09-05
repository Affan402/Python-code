import random
def guess(x):
    random_num = random.randint(1,x)
    guess = 0
    while random_num != guess:
        guess = int(input(f"Guess the num b/w 1 to {x}: "))
        if guess > random_num:
            print("Pls guess again, guess to too high!") 
        elif guess < random_num:
            print("Pls guess again, guess to too low") 
    print("You have guessed the num correctly")

def computer_guess(x):
    lower =1 
    high = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(lower, high)
        feedback = input(f"Is {guess} too high(h), low(c) or correct? ").lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            lower = guess -1               
    print(f"computer guessed you number, {guess} correctly!")
    
computer_guess(10)    
