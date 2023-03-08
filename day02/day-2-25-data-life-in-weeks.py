# Write your code below this line 👇

# maximum age = 90
# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

age = input("What is you current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left."
print(message)
