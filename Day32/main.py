from tkinter import *
from tkinter import messagebox
import genpass
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def writePass():
    passEntry.delete(0, END)
    password = genpass.makePassword()
    passEntry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def writeInfo():
    website = websiteEntry.get()
    email = userEntry.get()
    password = passEntry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        confirmation = messagebox.askokcancel(title=website,
                                              message=f"These are the details entered: "
                                                      f"\nEmail: {email}"
                                                      f"\nPassword: {password}"
                                                      f"\nIs it okay to save?")
        if confirmation == True:
            with open('data.txt', mode='a') as file:
                text = f"{website} | {email} | {password}\n"
                file.write(text)
                websiteEntry.delete(0, END)
                passEntry.delete(0, END)
                messagebox.showinfo(title="Done", message="Your details have been saved.")


# ---------------------------- UI SETUP ------------------------------- #

# WINDOW
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# CANVAS
canvas = Canvas(width=200, height=200)
imageFile = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=imageFile)
canvas.grid(row=0, column=1, sticky=W)

# LABELS

websiteLabel = Label(text="Website:")
websiteLabel.grid(row=1, column=0)

userLabel = Label(text="Email/Username:")
userLabel.grid(row=2, column=0)

passLabel = Label(text="Password:")
passLabel.grid(row=3, column=0)

# ENTRIES
websiteEntry = Entry(width=40)
websiteEntry.focus()
websiteEntry.grid(row=1, column=1)

userEntry = Entry(width=40)
userEntry.insert(END, 'usiam@u.rochester.edu')
userEntry.grid(row=2, column=1)

passEntry = Entry(width=34)
passEntry.grid(row=3, column=1, sticky=W)

# BUTTONS

genpassButton = Button(text="Generate Password", command=writePass)
genpassButton.grid(row=3, column=1, sticky=E)

addButton = Button(text="Add", width=34, command=writeInfo)
addButton.grid(row=4, column=1)

window.mainloop()
