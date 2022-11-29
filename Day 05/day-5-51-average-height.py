# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# 156 178 165 171 187

#Write your code below this row 👇
#damit nicht :)
#sum(liste)
#len(liste)

sum_height = 0
sum_student = 0
average_height = 0

#Summe der Größen rausbekommen
for student in student_heights:
    sum_height = student + sum_height
#print(sum_height)

#Anzahl der Elemente in der Liste rausbekommen
for student in student_heights:
    sum_student = sum_student + 1
#print(sum_student)

print(round(sum_height / sum_student))




