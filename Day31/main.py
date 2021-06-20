from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timerText, text="00:00")
    timerLabel.config(text="Timer", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
    checkLabel.config(font=(FONT_NAME, 10, 'bold'), bg=YELLOW, fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global reps
    reps += 1
    print(reps)
    workInSec = WORK_MIN * 60
    shortBreakInSec = SHORT_BREAK_MIN * 60
    longBreakInSec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        countdown(longBreakInSec)
        timerLabel.config(text="Break", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=RED)
    elif reps % 2 == 0:
        countdown(shortBreakInSec)
        timerLabel.config(text="Break", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=PINK)
    else:
        countdown(workInSec)
        timerLabel.config(text="Work", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    minute, sec = count // 60, count % 60,
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfigure(timerText, text=f"{minute}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    elif count == 0:
        startTimer()
        marks = ""
        for _ in range(reps // 2):
            marks += "✓"
        checkLabel.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# MAIN WINDOW
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# CANVAS
#############
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
imageFile = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=imageFile)
timerText = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

# LABELS
##############
# Timer
timerLabel = Label(text="Timer", font=(FONT_NAME, 35, 'bold'), bg=YELLOW, fg=GREEN)
timerLabel.grid(row=0, column=1)

# CheckMark
checkLabel = Label(font=(FONT_NAME, 10, 'bold'), bg=YELLOW, fg=GREEN)
checkLabel.grid(row=3, column=1)

# BUTTONS
##############
# Start button
startButton = Button(text="Start", highlightthickness=0, command=startTimer)
startButton.grid(row=2, column=0)

# Reset Button
resetButton = Button(text="Reset", highlightthickness=0, command=resetTimer)
resetButton.grid(row=2, column=2)

window.mainloop()
