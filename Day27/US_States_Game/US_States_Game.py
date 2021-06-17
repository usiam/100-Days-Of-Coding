import turtle, pandas, time

screen = turtle.Screen()
screen.title('US States Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

screen.tracer(0)

def writeGuess(guess):
    state = data[data.state == guess]
    corr = (int(state.x), int(state.y))
    turtle.penup()
    turtle.goto(corr)
    turtle.write(answerState)
    turtle.goto(0, 0)


data = pandas.read_csv('50_states.csv')

totalStates = len(data.state)
corrStates = 0
guessedStates = []

while len(guessedStates) < totalStates:
    screen.update()
    answerState = screen.textinput(title=f"{corrStates}/{totalStates} States Correct",
                                   prompt="What's another state's name?").title()
    if answerState in data.state.to_list():
        corrStates += 1
        guessedStates.append(answerState)
        writeGuess(answerState)
    elif answerState == 'Exit':
        missingStates = [state for state in data.state.to_list() if state not in guessedStates]
        newData = pandas.DataFrame(missingStates)
        newData.to_csv("statesToLearn.csv")
        break

screen.mainloop()
