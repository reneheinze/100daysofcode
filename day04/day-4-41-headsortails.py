#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

# Import the random module
import random

# now we can use the module in the code
# generate a random whole number between 100 and 200 including these two numbers.
random_integer = random.randint(0, 1)
if random_integer == 1:
    print("Heads")
else:
    print("Tails")