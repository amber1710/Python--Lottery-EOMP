# AMBER ADONIS
# CLASS 1
# PYTHOM EOMP
# DUE DATE: 30/11/2020
#Creating a window
from tkinter import *
import random
from _datetime import datetime
import unittest



#function to reset generated numbers
def die():
    num1.configure(text=str(0))
    num2.configure(text=str(0))
    num3.configure(text=str(0))
    num4.configure(text=str(0))
    num5.configure(text=str(0))
    num6.configure(text=str(0))

#function for delete entry numbers
def delete():
    digit1.delete(0,END)
    digit2.delete(0,END)
    digit3.delete(0,END)
    digit4.delete(0,END)
    digit5.delete(0,END)
    digit6.delete(0,END)

def player_numbers():
    players_numbers=set()

    playernum1= int(digit1.get())
    players_numbers.add(playernum1)

    playernum2= int(digit2.get())
    players_numbers.add(playernum2)

    playernum3= int(digit3.get())
    players_numbers.add(playernum3)

    playernum4= int(digit4.get())
    players_numbers.add(playernum4)

    playernum5= int(digit5.get())
    players_numbers.add(playernum5)

    playernum6= int(digit6.get())
    players_numbers.add(playernum6)

#function for generated numbers

def response():
    lottery_nums=set()

    num1.configure(text=str(random.sample(range(1, 6),1)))
    lottery_nums.add(num1)

    num2.configure(text=str(random.sample(range(1, 6), 1)))
    lottery_nums.add(num2)
    num3.configure(text=str(random.sample(range(1, 6), 1)))
    lottery_nums.add(num3)
    num4.configure(text=str(random.sample(range(1, 6), 1)))
    lottery_nums.add(num4)
    num5.configure(text=str(random.sample(range(1, 6), 1)))
    lottery_nums.add(num5)
    num6.configure(text=str(random.sample(range(1, 6), 1)))
    lottery_nums.add(num6)







#Creating a window
window = Tk()
window.title("Lottery Game!!!")
window.geometry("700x500")
window.config(background="teal")

#creating the labels
num1 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num1.grid(row = 2, column = 1, padx = 5, pady = 7)
num2 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num2.grid(row = 2, column = 2, padx = 5, pady = 7)
num3 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num3.grid(row = 2, column = 3, padx = 5, pady = 7)
num4 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num4.grid(row = 2, column = 4, padx = 5, pady = 7)
num5 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num5.grid(row = 2, column = 5, padx = 5, pady = 7)
num6 = Label(window, relief='groove', width = 5, bd=4, text="0", fg='black', bg='beige')
num6.grid(row = 2, column = 6, padx = 5, pady = 7)


#entries for the players numbers
digit1=Entry(window,relief='groove',width=5,bd=4,fg='black',bg='light blue')
digit1.grid(row=1,column=1,padx=5,pady=7)
digit2=Entry(window,relief='groove',width=5,bd=4, fg='black',bg='light blue')
digit2.grid(row=1,column=2,padx=5,pady=7)
digit3=Entry(window,relief='groove',width=5,bd=4,fg='black',bg='light blue')
digit3.grid(row=1,column=3,padx=5,pady=7)
digit4=Entry(window,relief='groove',width=5,bd=4, fg='black',bg='light blue')
digit4.grid(row=1,column=4,padx=5,pady=7)
digit5=Entry(window,relief='groove',width=5,bd=4,fg='black',bg='light blue')
digit5.grid(row=1,column=5,padx=5,pady=7)
digit6=Entry(window,relief='groove',width=5,bd=4, fg='black',bg='light blue')
digit6.grid(row=1,column=6,padx=5,pady=7)

#function to check the results
def create():
    file=open('/home/user/Desktop/lotto_results.txt','w+'+ "\n")
    file.write("6 correct numbers:10,000 000.00"+ "\n")
    file.write("5 correct numbers:8,584.00"+ "\n")
    file.write("4 correct numbers:2,384.00"+ "\n")
    file.write("3 correct numbers:100.50"+ "\n")
    file.write("2 correct numbers:20.00"+ "\n")
    file.write("1 correct number:0")
    file.close()

#function for date
def date():
    today = datetime.today().strftime('%Y-%m-%d')
    tlabel.config(text=str(today))
    print(today)


#Creating button for close
#Close
closeButton = Button(window)
closeButton.configure(text = "CLOSE", fg = 'black', bg = 'pink')
closeButton.grid(row =8, column = 1, columnspan = 6, pady = 7)

#Generate Numbers
numberGen = Button(window, width=20, text="Generate Numbers", command=response)
numberGen.configure(fg = "black" ,bg = "light blue")
numberGen.grid(row = 5, column = 1, padx = 5, pady = 7)

#Creating a reset button
reset = Button(window, width=10, text="Reset", command =die)
reset.configure(fg = "black" ,bg = "coral")
reset.grid(row = 5, column = 2, padx = 5, pady = 7)

#Creating a clear button
clearButton=Button(window)
clearButton.configure(text="Delete entry numbers",command=delete)
clearButton.grid(row=8,column=6,columnspan=6,pady=7)

#Creating a check button
checkButton=Button(window)
checkButton.configure(text="Check results", command=response)
checkButton.grid(row=9,column=6,columnspan=6,pady=7)

#Button for my date and time
tbutton = Button(window, text="Date/Time", command=date)
tbutton.grid(row=10,column=6,columnspan=6,pady=7)

#Label for my date
tlabel = Label(window)
tlabel.grid(row=11,column=6,columnspan=6,pady=7)


yourresults = Label(window)
yourresults.grid(row=12, column=6, columnspan=6, pady=7)
#function to close the program
def close():
    quit()


#Attached the close function to the button
closeButton.configure(command = close)

window.mainloop()
