# Write your code below this line 👇
print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm? "))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is you age? "))
    if age >= 45 and age <= 55:
        print("Midlife crisis tickets are free")
        bill = 0
    elif age > 18:
        print("Adult tickets are 12.")
        bill += 12
    elif age < 12:
        print("Child tickets are $5. ")
        bill += 5
    elif age < 18 and age > 12:
        print("Youth tickets are 7.")
        bill += 7
    
    if not (age >= 45 and age <= 55):
        wants_photo = input("Do you want a photo taken? Y or N.")
        if wants_photo == "Y":
            bill +=3
    
    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride")