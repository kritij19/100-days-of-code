class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list #List of questions
        self.question_number = 0
        self.score = 0
    
    # Prints the question corresponding to that question number
    # By adding check_answer also evaluates the guess.
    def next_question(self):
        question = self.question_list[self.question_number] 
        question_text = question.question # Attribute in question_model
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {question_text} (True/False): ") 
        self.check_answer(user_answer, question.answer) # Attribute in question_model
    
    # Checks if the quiz still has question remaining
    # Returns False if there are no questions left
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    

    # If the answer entered by the user matches the actual answer, score is increased by 1.  
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You're answer is correct")
            self.score += 1
        else:
            print("You have got it wrong")
        print(f"Your current score: {self.score}/ {self.question_number}\n")
