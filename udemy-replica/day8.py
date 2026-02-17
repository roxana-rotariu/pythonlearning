import os

# --- ASCII LOGO ---
logo = """
   ____                     _       _   _             
  / ___|  ___  ___ _ __ ___(_) __ _| |_(_) ___  _ __  
  \___ \ / _ \/ __| '__/ _ \ |/ _` | __| |/ _ \| '_ \ 
   ___) |  __/ (__| | |  __/ | (_| | |_| | (_) | | | |
  |____/ \___|\___|_|  \___|_|\__,_|\__|_|\___/|_| |_|
"""

print(logo)
print("Welcome to the Secret Auction Program!\n")

# --- DATA STORAGE ---
bids = {}
bidding_finished = False


# --- FUNCTIONS ---
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"\n🏆 The winner is **{winner}** with a bid of **${highest_bid}**! 🏆")


# --- MAIN PROGRAM LOOP ---
while not bidding_finished:
    name = input("What is your name?: ")

    # Validate bid input
    while True:
        try:
            price = int(input("What is your bid? $"))
            break
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    bids[name] = price

    # Ask if more bidders want to join
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    while should_continue not in ["yes", "no"]:
        should_continue = input("Invalid input. Please type 'yes' or 'no': ").lower()

    if should_continue == "no":
        bidding_finished = True
        clear_screen()
        find_highest_bidder(bids)
    else:
        clear_screen()
        print(logo)
        print("Current bidders will be hidden.\n")