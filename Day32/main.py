from tkinter import *
from tkinter import messagebox
import genpass
import pyperclip
import json


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

    userpassDict = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        confirmation = messagebox.askokcancel(title=website,
                                              message=f"These are the details entered: "
                                                      f"\nEmail: {email}"
                                                      f"\nPassword: {password}"
                                                      f"\nIs it okay to save?")
        if confirmation == True:
            try:
                with open('data.json', mode='r') as file:
                    # reads old data
                    info = json.load(file)  # loads the info in the json file and saves it into variable info
                    # updating the old info with new info

            except FileNotFoundError:
                with open('data.json', mode='w') as file:
                    # writing the updated info into the file
                    json.dump(userpassDict, file, indent=4)  # writes the first parameter to the 2nd parameter

            else:
                info.update(userpassDict)  # writes new info from userpassDict into the info
                with open('data.json', mode='w') as file:
                    # writing the updated info into the file
                    json.dump(info, file, indent=4)  # writes the first parameter to the 2nd parameter

            finally:
                websiteEntry.delete(0, END)
                passEntry.delete(0, END)
                messagebox.showinfo(title="Done", message="Your details have been saved.")


# ----------------------------  SEARCH  ------------------------------- #

def searchInfo():
    try:
        with open('data.json') as file:
            infoDict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR", message="No Data File Found")
    else:
        if websiteEntry.get() in infoDict:
            messagebox.showinfo(title=f"{websiteEntry.get()}",
                                message=f"Email: {infoDict[websiteEntry.get()]['email']}"
                                        f"\nPassword: {infoDict[websiteEntry.get()]['password']}")
        else:
            messagebox.showinfo(title="ERROR", message=f"No details for {websiteEntry.get()} exists.")


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
websiteEntry = Entry(width=23)
websiteEntry.focus()
websiteEntry.grid(row=1, column=1, sticky=W)

userEntry = Entry(width=40)
userEntry.insert(END, 'email@emailProvider.com')
userEntry.grid(row=2, column=1)

passEntry = Entry(width=23)
passEntry.grid(row=3, column=1, sticky=W)

# BUTTONS

genpassButton = Button(text="Generate Password", width=14, command=writePass)
genpassButton.grid(row=3, column=1, sticky=E)

addButton = Button(text="Add", width=34, command=writeInfo)
addButton.grid(row=4, column=1)

searchButton = Button(text="Search", width=14, command=searchInfo)
searchButton.grid(row=1, column=1, sticky=E)

window.mainloop()
