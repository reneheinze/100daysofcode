# Write your code below this line 👇
print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is you age? "))
    if age > 18:
        print("Please pay $12.")
    elif age < 12:
        print("Please pay $5. ")
    else:
        print("Please pay $7.")

else:
    print("Sorry, you have to grow taller before yxou can ride")

