student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇

#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

for student in student_scores:
    score = student_scores[student]
    if score > 90 and score < 101:
        student_grades[student] = "Outstanding"
    elif score > 80 and score < 91:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 and score < 81:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"






    

# 🚨 Don't change the code below 👇
print(student_grades)





