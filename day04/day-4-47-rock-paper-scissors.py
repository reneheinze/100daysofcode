from operator import truediv
import random

wrong_input = False

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

#Simpel rules
#- Rock wins against scissors
#- Scissors win against paper
#- Paper wins against rock


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if user_choice == 0:
    print(rock)

elif user_choice == 1:
    print(paper)

elif user_choice == 2:
    print(scissors)

else:
    wrong_input = True
    print("Falsche Eingabe")


if wrong_input == False:

    computer_choice = random.randint(0, 2)

    if computer_choice == 0:
        print(rock)

    elif computer_choice == 1:
        print(paper)

    elif computer_choice == 2:
        print(scissors)

    #Simpel rules
    #- Rock wins against scissors
    #- Scissors win against paper
    #- Paper wins against rock

    # Unentschieden
    if user_choice == computer_choice:
        print("Unentschieden")

    #- Rock 0 wins against Scissors 2 
    if user_choice == 0 and computer_choice == 2 or user_choice == 2 and computer_choice == 1 or user_choice == 1 and computer_choice == 0:
        print("You win")

    #- Scissors 2 win against Paper 1
    if user_choice == 2 and computer_choice == 0 or user_choice == 1 and computer_choice == 2 or user_choice == 0 and computer_choice == 1:
        print("You lose")

else:
    print("Exit Program")


