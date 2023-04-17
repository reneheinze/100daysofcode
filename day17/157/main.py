from question_model import Question
from data import question_data
from data2 import question_data2
from quiz_brain import QuizBrain

# Create a empty list
question_bank = []
question_bank2 = []

# Loop through the questions
# Short Version
# for data in question_data:
#     question_bank.append(Question(data['text'],data['answer']))


# Loop through the questions from question_data (data.py) and create a question object for each directory
# Then append each question object in the question_bank list
# Long Version
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


for question in question_data2:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question2 = Question(question_text, question_answer)
    question_bank2.append(new_question2)




# print(question_bank[0].answer)

start = input("Start Quiz 1.0?")

if (start.lower()== "yes"):
    new_quiz = QuizBrain(question_bank)
    while new_quiz.still_has_questions():
        new_quiz.next_question()
    new_quiz.finish()

if (start.lower()== "no"):
    new_quiz = QuizBrain(question_bank2)
    while new_quiz.still_has_questions():
        new_quiz.next_question()
    new_quiz.finish()




#print(new_quiz.question_list[0].answer)

#new_quiz.next_question()



# print(question_data)
# print(question_data[0])
# print(question_data[0]['text'])
# print(question_data[0]['answer'])




