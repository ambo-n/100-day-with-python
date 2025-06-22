bidders ={}
bidding = True

print("Welcome to the secret auction program.")
while bidding:
    name = input("What is your name?: ")
    amount = int(input("What's your bid?: $"))
    bidders[name]=amount
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if continue_bidding == 'no':
        bidding = False
        # consider putting this into a function
        max_bid = 0
        for key, value in bidders.items():
            if value > max_bid:
                max_bid=value
                winner = key
        print(f"The winner is {winner} with a bid of ${max_bid}")
    else:
        print("\n"*100)