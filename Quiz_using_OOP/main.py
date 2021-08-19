from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# The list holds Question objects.
question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = QuizBrain(question_bank) 

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have finished the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
