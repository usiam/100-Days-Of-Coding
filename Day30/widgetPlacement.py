from tkinter import *
WIDTH = 500
HEIGHT = 300

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=WIDTH, height=HEIGHT)
#window.config(padx = 50, pady = 100)

# Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.grid(row=0, column=0)
label.config(padx = 100, pady = 100)
# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(row=1, column=1)

button2 = Button(text="Button 2")
button2.grid(row=0, column=2)

# Entries
entry = Entry(width=30)
# Add some text to begin with
entry.insert(END, string="Some text to begin with.")
# Gets text in entry
print(entry.get())
entry.grid(row=2, column=3)


window.mainloop()

# Positioning the widgets: pack(), place(), and grid()