class Quiz:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        quest = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number}: {quest.text} (True/False)?: ")
        self.check_answer(ans, quest.answer)

    def still_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, u_answer, c_answer):
        if u_answer.lower() == c_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("you got it wrong!")
        print(f"the correct answer is {c_answer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
