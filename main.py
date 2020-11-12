#imported repl.it clear function
from replit import clear
from art import logo
print(logo)
print("２０２０ ｜ ＠Ｃｍｌｏｈｒ")
print("-------------------")

user_bids = {}
bidding_end = False

def the_high_bidder(bidding_log):
    high_bid = 0
    won = ""
    for bidder in bidding_log:
        user_bids = bidding_log[bidder]
        if user_bids > high_bid:
            high_bid = user_bids
            won = bidder
    print("------------------------------------------------------")        
    print(f"The highest bidder is {won} with a bid of ${high_bid}!")

while not bidding_end:
    name = input("What is your name?\n>> ")
    bid = int(input("How much would you like to bid?\n>> $"))
    user_bids[name] = bid
    add_bidders = input("Any other bidders, Y or N?\n>> ").lower()
    if add_bidders == "n":
        bidding_finished = True
        the_high_bidder(user_bids)
        break
    elif add_bidders == "y":
        clear() #imported repl.it clear


