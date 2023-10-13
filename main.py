from data import question_data
from question import Question
from quiz import Quiz

question_bank = []

for i in range(len(question_data)):
    que = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(que)

quiz = Quiz(question_bank)

while quiz.still_questions():
    quiz.next_question()

print("you have completed the Quiz")
print(f"your final score is: {quiz.score}/{quiz.question_number}")
