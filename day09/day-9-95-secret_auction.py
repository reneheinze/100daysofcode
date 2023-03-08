import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

# Define Empty Dictionary
bid_dictionary = {}

# Define While Variable
bidding_finished = False

# Print the hammer logo
print(logo)

def highest_bidder(bidding_record):
# create new dictionary for the highest bidder
  highest_bidder = {
    "id": "highest_bidder",
    "name": "high_name",
    "bid": 0
  }
# It helps to make the dictionary visible :)
# bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    print(bidder)
# Iteration through the dictionary 
    if bidding_record[bidder] > highest_bidder["bid"]:
      highest_bidder["name"] = bidder
      highest_bidder["bid"] = bidding_record[bidder]

# I cannot access a dictionary in a fstring. Therfore i use vars 
  highest_bidder_name = highest_bidder["name"]
  highest_bid = highest_bidder["bid"]
  print(f"The winner is {highest_bidder_name} with a bid of ${highest_bid}")
  

while not bidding_finished == True:
  bid_name = input("Please input your Name: ")
  #Convert to int. Otherwise String.
  bid_price = int(input("Please input Bid Price: "))
  #Add entry to the dictionary
  bid_dictionary[bid_name]=bid_price
  
  should_continue = input("Another user wants to bid (yes/no)?")
  if should_continue == "no":
    bidding_finished = True
#only clear the screen when I add another user
  elif should_continue == "yes":
    os.system('clear')

highest_bidder(bid_dictionary)

