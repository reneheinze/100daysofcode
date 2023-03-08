# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def my_function(check_name, check_char):
    lower_check_name = check_name.lower()
    counter = (lower_check_name.count(check_char))
    return counter

name = name1 + name2

check_true1 = 0
check_true1 += (my_function(name, "t"))
check_true1 += (my_function(name, "r"))
check_true1 += (my_function(name, "u"))
check_true1 += (my_function(name, "e"))

check_true2 = 0
check_true2 += (my_function(name, "l"))
check_true2 += (my_function(name, "o"))
check_true2 += (my_function(name, "v"))
check_true2 += (my_function(name, "e"))

check_true_total = str(check_true1) + str(check_true2)
#print(check_true_total)
#optional da dem FString das egal ist, dass dies ein Integer ist.
check_true_total = int(check_true_total)

if (check_true_total < 10) or (check_true_total > 90):
    print(f"Your score is {check_true_total}, you go together like coke and mentos.")
elif (check_true_total > 40) and (check_true_total < 50):
    print(f"Your score is {check_true_total}, you are alright together.")
else:
    print(f"Your score is {check_true_total}.")



