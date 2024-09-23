from replit import clear

bids = {}
biding_finished = False

def highest_biding(bid_rec):
    highest_bid = 0
    winner = ""
    for bidder in bid_rec:
        bid_amount =  bid_rec[bidder]
        if highest_bid > bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with bid ${highest_bid}')            

while not biding_finished :
    name = input("What's your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    con = input("Are there any other bidders? yes or no ").lower()
    
    if con == "no":
        biding_finished = True
        highest_biding(bids)
    elif con == "yes":
        clear()