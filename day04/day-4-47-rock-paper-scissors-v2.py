import random

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
#- Rock 0 wins against scissors 2
#- Scissors 2 win against paper 1
#- Paper 1 wins against rock 0


game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))



if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")

else:
    print("I chose: ")
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")

    elif user_choice == 2 and computer_choice == 0:
        print("You loose!")

    elif user_choice == computer_choice:
        print("It's a draw")

    elif computer_choice > user_choice:
        print("You loose!")

    elif computer_choice < user_choice:
        print("You win!")


