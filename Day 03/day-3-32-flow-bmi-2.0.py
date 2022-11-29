# Write your code below this line 👇

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# print(type(height))

# Write your code below this line 👇
bmi = round(float(weight) / (float(height) ** 2))



if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.") 