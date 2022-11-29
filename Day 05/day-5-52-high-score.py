# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# print(max(student_scores)) -> darf ich hier nicht nutzen.
# print(min(student_scores)) -> darf ich hier nicht nutzen.


#input 78 65 89 86 55 91 64 89
score_high=0


for score in student_scores:
  if score_high < score:
    score_high = score

print(f"The highest score in the class is: {score_high}")
