from tkinter import *

WIDTH = 350
HEIGHT = 50


def convertMilesToKm():
    # convert miles to km
    miles = toConvertEntry.get()
    km = round(float(miles) * 1.609,2)
    zeroLabel.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx = 20, pady = 20)

# Entry box
toConvertEntry = Entry(width=10)
toConvertEntry.insert(END, string="0")
toConvertEntry.grid(row=0, column=1)

# Button
button = Button(text="Calculate", command=convertMilesToKm)
button.grid(row=2, column=1)

# Labels

toConvertLabel = Label(text="Miles")
toConvertLabel.grid(row=0, column=2)
convertedLabel = Label(text="Km")
convertedLabel.grid(row=1, column=2)
zeroLabel = Label(text="0")
zeroLabel.grid(row=1, column=1)
equalToLabel = Label(text="is equal to")
equalToLabel.grid(row=1, column=0)


window.mainloop()
