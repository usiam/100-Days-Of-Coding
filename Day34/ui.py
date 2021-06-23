from tkinter import *
from quiz_brain import QuizBrain

QFONT = ('Arial', 16, 'italic')
SFONT = ('Ariel', 11)
THEME_COLOR = "#375362"


class QuizInterface():
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.ques_txt = self.canvas.create_text(150, 125, text="", font=QFONT, fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.scoreLabel = Label(text=f"score: {self.quiz.score}", font=SFONT, bg=THEME_COLOR, fg='white')
        self.scoreLabel.grid(row=0, column=1)

        self.trueImg, self.falseImg = PhotoImage(file='./images/true.png'), PhotoImage(file='./images/false.png')
        self.trueButton, self.falseButton = Button(image=self.trueImg, highlightthickness=0, borderwidth=0, command=self.trueCmd), Button(
            image=self.falseImg, highlightthickness=0, borderwidth=0, command=self.falseCmd)
        self.trueButton.grid(row=2, column=0)
        self.falseButton.grid(row=2, column=1)
        self.getNextQ()

        self.window.mainloop()

    def getNextQ(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoreLabel.config(text=f"score: {self.quiz.score}")
            qTxt = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_txt, text=qTxt)
        else:
            self.canvas.itemconfig(self.ques_txt, text="End of quiz!")
            self.trueButton.config(state='disabled')
            self.falseButton.config(state='disabled')


    def trueCmd(self):
        isRight = self.quiz.check_answer("True")
        self.feedback(isRight)

    def falseCmd(self):
        isRight = self.quiz.check_answer("False")
        self.feedback(isRight)

    def feedback(self, isRight):
        if isRight:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, func=self.getNextQ)
