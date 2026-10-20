# Auction Program - Blind Bidding System
 
print("===================================")
print("       AUCTION PROGRAM")
print(" Blind Bidding & Winner Selection")
print("===================================")

bids = {}

print("\nWelcome to the Auction Program!")

while True:
    name = input("\nEnter participant name: ")

    bid_amount = int(input("Enter your bid amount: $"))
     
    bids[name] = bid_amount

    another = input("Is there another bidder? (yes/no): ").lower()

    if another != "yes":
        break

if len(bids) > 0:

    highest_bid = 0
    winner = ""

    # Find the participant with the highest bid
    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name

    # Display all participants and their bids
    print("\n========== AUCTION RESULTS ==========")
    print("Participant\tBid Amount\tStatus")

    for name in bids:
        if name == winner:
            print(name, "\t\t$", bids[name], "\t\tWinner Declared")
        else:
            print(name, "\t\t$", bids[name], "\t\tParticipant")

    # Display the final winner
    print("\n===================================")
    print("WINNER IS:", winner.upper())
    print("Winning Bid: $", highest_bid)
    print("===================================")

else:
    print("No bids were submitted.")

