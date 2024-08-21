from data import Data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

db = Data()
db.get_data()

for question_dict in db.questions:
    question_bank.append(
        Question(question_dict["question"], question_dict["correct_answer"])
    )

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.is_next_question():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
