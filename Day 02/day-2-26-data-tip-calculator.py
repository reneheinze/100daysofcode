# Write your code below this line 👇

print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 1, 12, or 15? ")
people_bill = input("How many people to split the bill? ")

total_bill_float = float(total_bill)
percentage_tip_int = int(percentage_tip)
people_bill_int = int(people_bill)

#Prozentrechnng 
total_bill_tip = (total_bill_float * (percentage_tip_int+100))/100

#Runden auf zwei Nachkommestellen
bill_per_person = total_bill_tip / people_bill_int

# Ich formatiere das Python zwei Nachkommastellen ausgibt. 
# Auch wenn die letzte Stelle eine 0 ist. Diese wird nochmalerweise nicht ausgegeben.
# https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python
formatted_bill_per_person = "{:.2f}".format(bill_per_person)

#Fstring bauen uns ausgeben
message = f"Each person should pay: {formatted_bill_per_person}"
print(message)
