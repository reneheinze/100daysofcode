class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.question_score = 0

    def still_has_questions(self):
        # long version
        #if self.question_number < len(self.question_list):
        #    return True
        #else:
        #    return False

        # short version
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

        self.check_answer(user_answer,current_question.answer)
        # print(current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Checks the answer, increases the question score if right and prints the right answer."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.question_score += 1
        else:
            print("That's wrong.")
        print(f"The current answer was: {correct_answer}.")
        print(f"You current score is: {self.question_score}/{self.question_number}.")
        print("\n")

    def finish(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.question_score}/{self.question_number}.")

    def test(self):
        print("hallo")


