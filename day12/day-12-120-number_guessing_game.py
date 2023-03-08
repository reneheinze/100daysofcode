# Import the random module
import random

#Logo
from art import logo

#Set Global Const for Turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def welcome():
  print("Welcome to the Number Guessing Game!")
  print("I´m thinking of a number between 1 and 100.")

def difficulty():
  diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if diff_level == "easy":
    return EASY_LEVEL_TURNS
  elif diff_level == "hard":
    return HARD_LEVEL_TURNS

def create_number():
  random_number = random.randint(1, 100)
  return (random_number)

# Check my Answer
def check_answer(guess, answer, guesses):
  """" Returns the number of turns remaining"""
  if guess > answer:
    print("Too high.")
    return guesses - 1
  elif guess < answer:
    print("Too low.")
    return guesses - 1
  elif guess == answer:
    print(f"You got it! The answer was {answer}")
    return guesses

# Main Function for Game
def game():
  print(logo)
  welcome()
  guesses = difficulty()
  random_number = create_number()

  guess_input = 0
  
  while guess_input != random_number:
    print(f"You have {guesses} attempts remaining to guess the number.")
  # Let the user guess a number.
    guess_input = int(input("Make a guess: "))
  # Check the Users guess against the actual answer
    guesses = check_answer(guess_input, random_number, guesses)
    
    if guesses == 0:
      print("You have run out of guesses, you lose.")
      # I can exit my main program with return, as it is inside the function game :)
      return


game()