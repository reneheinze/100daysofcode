import random
from art import logo, vs
from game_data import data

# Define Global Variables
score = 0
data_choice_high = 111111

# Example Dictionary for visualisation.
# {
#     'name': 'Instagram',
#     'follower_count': 346,
#     'description': 'Social media platform',
#     'country': 'United States'
# }

# Print High Candidate

def gen_choice_high(score, name, description, country):
    """Takes parts of the dictionary and display it for high candidate"""
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    print(f"Compare A: {name}, a {description}, from {country}.")

# Print Low Candidate
def gen_choice_low(name, description, country):
    """Takes parts of the dictionary and display it for low candidate"""
    print(vs)
    print(f"Compare B: {name}, a {description}, from {country}.")

# Generate random number from the list with the length of the data list in mind
def random_number(data,data_choice_high):
    """Takes the dictionary and high choice and returns an unique choice for lower choice"""
    # Catch the inital data_choice_high creation
    if data_choice_high == 111111:
        return random.randint(0, len(data)-1)

    # random.choice is better as it is for lists
    # Generate Random Integer
    data_choice = random.randint(0, len(data)-1)
    # Check for the same value of high and low
    if data_choice_high == data_choice:
        random_number(data,data_choice_high)
        # return is important he because after random_number is called here. He jumps right back in here.
        return data_choice
    else:
        return data_choice




# Generate the winner
def generate_winner(data, data_choice_high, data_choice_low, guess_followers):
    """Takes parts of the dictionary, user input and high and low and returns True or False for the winner"""
    # Check who has more follower - candidate A or candidate B
    if data[data_choice_high]["follower_count"] > data[data_choice_low]["follower_count"]:
        more_follower = "a"
    else:
        more_follower = "b"
    if guess_followers == more_follower:
        return True
    else:
        return False

    # Much shorter Version would be
    #if data[data_choice_high]["follower_count"] > data[data_choice_low]["follower_count"]:
    #    return guess_followers == "a"
    #else:
    #    return guess == "b"



# Main Code
def main(score,data_choice_high):
    #score_text = ""
    #game_finished = False

    # Create a random number for data choice
    data_choice_low = random_number(data,data_choice_high)

    # Another aproach would be. That runs as long as the number are the same.
    while data_choice_low == data_choice_high:
        data_choice_high = random.randint(0, len(data)-1)

    # Print High vs Low 
    gen_choice_high(score, data[data_choice_high]["name"],data[data_choice_high]["description"],data[data_choice_high]["country"])
    print(data_choice_low)
    gen_choice_low(data[data_choice_low]["name"],data[data_choice_low]["description"],data[data_choice_low]["country"])

    # For Debugging print data
    #print(data[data_choice_high]["follower_count"])
    #print(data[data_choice_low]["follower_count"])

    # Ask who has more followers (data_choice_high or data_choice_low)
    guess_followers = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check who has more followers 
    answer_winner = generate_winner(data, data_choice_high, data_choice_low, guess_followers)

    # You Loose
    if answer_winner == False:
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return

    # You Win and Next Round
    else:
        score = score + 1
        data_choice_high = data_choice_low
        main(score,data_choice_high)

#call main()
# Create initial data_choice_high
data_choice_high = random_number(data,data_choice_high)
main(score,data_choice_high)