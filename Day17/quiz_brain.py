class QuizBrain:
    def __init__(self, quesList):
        self.quesNum = 0
        self.quesList = quesList
        self.score = 0
        
    def nextQuestion(self):
        currQues = self.quesList[self.quesNum]
        self.quesNum += 1
        userAns = input(f"Q.{self.quesNum}: {currQues.question}. (True/False)? ").lower()
        correctAns = currQues.answer.lower()
        self.answerIsRight(userAns, correctAns)
        
    def stillHasQuestion(self):
        return self.quesNum < len(self.quesList) 
    
    def answerIsRight(self, userAns, correctAns):
        if userAns == correctAns:
            self.score += 1
            print("You got it right.")
        else: 
            print("That's wrong.")
        print(f"The correct answer is {correctAns}.")
        print(f"Your current score is: {self.score}/{self.quesNum}\n")
