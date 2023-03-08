# Import the random module
import random

# now we can use the module in the code
# generate a random whole number between 100 and 200 including these two numbers.
random_integer = random.randint(100, 200)
print(random_integer)

random_float = random.uniform(1, 5)
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")