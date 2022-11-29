# 🚨 Don't change the code below 👇

from select import select


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal -1] = "X"

print(selected_row)
print(row1)

#Write your code above this row 👆
print("fertig")
# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
print(map)