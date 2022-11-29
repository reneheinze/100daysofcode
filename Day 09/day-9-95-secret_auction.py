import os
from art import logo
#HINT: You can call clear() to clear the output in the console.

# Define Empty Dictionary
bid_dictionary = {}

# Define While Variable
bit_loop = True

# Print the hammer logo
print(logo)

def highest_bidder(high_bid_dict):
  highest_bidder = {
    "id": "highest_bidder",
    "name": "high_name",
    "bid": 0
  }

  for item in high_bid_dict:
    print(high_bid_dict[item])
    print(highest_bidder["bid"])

    if high_bid_dict[item] > highest_bidder["bid"]:
      highest_bidder["name"] = item
      highest_bidder["bid"] = high_bid_dict[item]

# I cannot access a dictionary in a fstring. Therfore i use vars 
  highest_bidder_name = highest_bidder["name"]
  highest_bid = highest_bidder["bid"]
  print(f"The winnder is {highest_bidder_name} with a bid of ${highest_bid}")
  



while bit_loop == True:
  bid_name = input("Please input your Name: ")
  #Convert to int. Otherwise String.
  bid_price = int(input("Please input Bid Price: "))
  bid_dictionary[bid_name]=bid_price
  
  another_bit = input("Another user wants to bid (yes/no)?")
  if another_bit == "no":
    bit_loop = False

  os.system('clear')

print(bid_dictionary)
highest_bidder(bid_dictionary)

