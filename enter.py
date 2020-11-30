# AMBER ADONIS
# CLASS 1
# PYTHOM EOMP
# DUE DATE: 30/11/2020

# Creating a window
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('LOTTO GAME')
window.geometry("600x500")
window.configure(background="aquamarine")

# Label for header
heading = Label(text="WELCOME !!!", bg="grey", fg="white")
heading.pack()


# FUNCTION FOR Age
def check():
    age = int(age_entry.get())
    if age >= 18:
        messagebox.showinfo("Allowed!!", "You're old enough to play the lottery!!!")
        import lotterychallenge
        lotterychallenge.mainloop()
    elif age < 18:
        messagebox.showerror("Not Allowed!!", "You're too young to play the lottery.")


# Creating entry and label for Age
agelabel = Label(window, text="Enter age: \n")
agelabel.pack(side=TOP)
age_entry = Entry(window)
age_entry.pack(side=TOP)

#Button for age
openbutton1 = Button(window, text="Check age to play", command=check)
openbutton1.place(x=180, y=220)
openbutton1.pack()

window.mainloop()
