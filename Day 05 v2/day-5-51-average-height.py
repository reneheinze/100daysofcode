# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# 156 178 165 171 187

#Write your code below this row 👇
# How many list objects?
print(len(student_heights))
# Sum up my values of my list
print(sum(student_heights))

sum_height = 0
count_heights = 0

for height in student_heights:
  sum_height += height
  count_heights += 1

print(count_heights)
print(sum_height)
print(round(sum_height/count_heights))