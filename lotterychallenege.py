# AMBER ADONIS
# CLASS 1
# PYTHOM EOMP
# DUE DATE: 30/11/2020
#Creating a window
from tkinter import *
from tkinter import messagebox
from random import sample
from _datetime import datetime
import unittest

# Printing date and time
date = datetime.now()
date1  = date.strftime("%d %b %Y")
time = date.strftime("%H:%M%p")
print(date1)
print(time)



# Creat a GHUI that confirms users age
window = Tk()
window.title("Play Now, Laugh Forever.")
window.geometry("600x500")
window.configure(background="yellow")

numbers = sample(range(1,49),6)
print(numbers)

age_label = Label(window, text="Please enter your age: ")
age_label.place(x=0, y=0)

age_entry = Entry(window, width=10)
age_entry.place(x=150,y=0)

def age():
    try:
        if int(age_entry.get())<18:
            messagebox.showinfo("Error","Not allowed to play !!")
    except ValueError :
        messagebox.showinfo("Error","Please enter a number")
        raise ValueError

    else:
        if int(age_entry.get())>=18:
            window.withdraw()
            lotto=Tk()
            lotto.geometry("900x600")
            lotto.title("Lottery Game")
            lotto.configure(background="red")


            enter_label=Label(lotto,text="Enter your numbers")
            enter_label.place(x=200, y=0)
            # Creating the entries for the user to enter their numbers
            num1 = Entry(lotto, width=5)
            num1.place(x=120, y=80)
            num2 = Entry(lotto, width=5)
            num2.place(x=180, y=80)
            num3 = Entry(lotto, width=5)
            num3.place(x=240, y=80)
            num4 = Entry(lotto, width=5)
            num4.place(x=300, y=80)
            num5 = Entry(lotto, width=5)
            num5.place(x=360, y=80)
            num6 = Entry(lotto, width=5)
            num6.place(x=420, y=80)
            winnings = Label(lotto, text="results")
            winnings.place(x=500, y=100)

            def generate():
                try:
                    user_entries=[int(num1.get()) ,int(num2.get()),int(num3.get()),int(num4.get()),int(num5.get()),int(num6.get())]
                    print(user_entries)

                    x=set(user_entries).intersection(numbers)
                    print(len(x))

                    # putting the results over into a text file

                    if len(x) ==0:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn nothing"+"\n"+str(date1+"\n"+str(time)))
                    if len(x) ==1:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn nothing"+"\n"+str(date1+"\n"+str(time)))
                    if len(x)==2:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn R20.00"+"\n"+str(date1+"\n"+str(time)))
                    if len(x)==3:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn R100.50"+"\n"+str(date1+"\n"+str(time)))
                    if len(x)==4:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn R2384.00"+"\n"+str(date1+"\n"+str(time)))
                    if len(x)==5:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn R8584.00"+"\n"+str(date1+"\n"+str(time)))
                    if len(x)==6:
                        winnings.config(text="Your numbers were:"+str(user_entries)+"\n"+
                                    "the winnings numbers are:"+
                                     str(numbers)+"\n"+"You earn R10 000 000.00"+"\n"+str(date1+"\n"+str(time)))
                except ValueError:
                    messagebox.showinfo("error", "Enter a number")











                f=open("winning.txt", "w+")
                f.close()
                f = open("winning.txt", "a")
                f.write(winnings.cget("text"))



            draw_button=Button(lotto,text="Play" , command=generate)
            draw_button.place(x=0,y=150)















age_button=Button(window,text="Enter",command=age)
age_button.place(x=50,y=150)




window.mainloop()


