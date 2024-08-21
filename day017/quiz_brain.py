class QuizBrain:

    def __init__(self, question_list) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {q.text} [T]rue or [F]alse? "
        ).lower()
        self.check_answer(user_answer, q.answer)

    def is_next_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, correct_answer):
        if u_answer == correct_answer[0].lower():
            self.score += 1
            print("You're right!")
        else:
            print("That is wrong.")
        print(f"The correct answer is: {correct_answer}.")
        print(f"Current score is {self.score}/{self.question_number}.\n")
