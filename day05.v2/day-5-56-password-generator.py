
import random
from tokenize import String
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# create empty list
password = []

letter = 0

my_password = ""

# Letters
for number in range(0,nr_letters):
  # 0 - 2 bei eingabe von 3
  letter = letter +1
  print(letter)
  password.append(letters[random.randint(0, len(letters)-1)])

# Numbers
for number in range(0,nr_numbers):
  password.append(numbers[random.randint(0, len(numbers)-1)])

# Symbols
for number in range(0,nr_symbols):
  password.append(symbols[random.randint(0, len(symbols)-1)])

# Convert List to String #1st Version
#my_password = ''.join(password)

# Convert List to String #2nd Version
for char in password:
  my_password += char

# Output 
print(f"Here is your password: {my_password}" )