from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for data in question_data:
    questionText = data['question']
    answerText = data['correct_answer']
    question = Question(questionText, answerText)
    questionBank.append(question)
    
quiz = QuizBrain(questionBank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.quesNum}")