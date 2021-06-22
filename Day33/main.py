from tkinter import *
import random, pandas as pd

WORDFONT = ('Ariel', 60, 'bold')
LANGFONT = ('Ariel', 40, 'italic')

BACKGROUND_COLOR = "#B1DDC6"

# ------------------ Data reading ---------------- #

currCard = {}
try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv('./data/french_words.csv')
wordsDict = data.to_dict(orient="records")


# -------------------- Flipping ------------------ #

def flipCard():
    canvas.itemconfig(cardFront, image=backImage)
    canvas.itemconfig(langText, text='English', fill='white')
    canvas.itemconfig(wordText, text=currCard["English"], fill='white')


# -------------- Right button -------------- #

def wordKnown():
    wordsDict.remove(currCard)
    data = pd.DataFrame(wordsDict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    nextWord()


# -------------- Wrong button -------------- #

def nextWord():
    global currCard, flipTimer
    window.after_cancel(flipTimer)  # cancels the timer when a new card is generated
    currCard = random.choice(wordsDict)
    canvas.itemconfig(langText, text='French', fill='black')
    canvas.itemconfigure(wordText, text=currCard["French"], fill='black')
    canvas.itemconfigure(cardFront, image=frontImage)
    flipTimer = window.after(3000, func=flipCard)  # restarts the timer


# -------------- UI SETUP ---------------- #

# WINDOW
window = Tk()
window.title("FlashCard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=flipCard)  # calls the function flipCard every 3 s

# CANVAS
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
frontImage = PhotoImage(file='./images/card_front.png')
backImage = PhotoImage(file='./images/card_back.png')
cardFront = canvas.create_image(400, 263, image=frontImage)
langText = canvas.create_text(400, 150, text="", font=LANGFONT)
wordText = canvas.create_text(400, 263, text="", font=WORDFONT)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrongButtonImg = PhotoImage(file='./images/wrong.png')
wrongButton = Button(image=wrongButtonImg, highlightthickness=0, borderwidth=0, command=nextWord)
wrongButton.grid(row=1, column=0)

rightButtonImg = PhotoImage(file='./images/right.png')
rightButton = Button(image=rightButtonImg, highlightthickness=0, borderwidth=0, command=wordKnown)
rightButton.grid(row=1, column=1)

nextWord()  # gives the first word since langText and wordText are empty initially

window.mainloop()
