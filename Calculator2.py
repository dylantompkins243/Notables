from tkinter import *
import random

import tkinter as tk
gui = Tk()

#Button
count = 0

def click():
    global count
    count+=1
    print("You clicked me")
    print(count)

#Open Window
gui = tk.Tk()

w_width, w_height = 650, 300
s_width, s_height = gui.winfo_screenwidth(), gui.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
gui.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
gui.configure(bg='light grey')

if __name__ == "__main__": 
 
    gui.configure(background="light green") 
  
    gui.title("Simple Calculator") 
  
    gui.geometry("270x150") 

equation = StringVar() 
expression_field = Entry(gui, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
 
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
button1 = Button(gui, text=' 1 ', fg='black', bg='red', 
    command=lambda: press(1), height=1, width=7)

"""def destroy_button():
    button.destroy()"""
  
# TextBox Creation 
inputtxt = tk.Text(gui, 
    height = 1, 
    width = 100,
    font=("Comic Sans", 20),
    )
#inputtxt.pack(side=TOP, padx=15, pady=15)
  
#inputtxt.pack() 

#Number 0 BUtton
button0 = tk.Button(gui, 
    text = "0",
    height = 1,
    width = 8,
    font=("Comic Sans", 10), 
    fg = "black", 
    bg = "white", 
    activeforeground="black", 
    activebackground="white", 
    #command = printInput,
    )
#button0.pack(side=LEFT, anchor=SW, padx=10, pady=10)
#button0.pack() 
  
#Number 1 Button
button1 = tk.Button(gui, 
    text = "1",
    height = 1,
    width = 8,
    font=("Comic Sans", 10), 
    fg = "black", 
    bg = "white", 
    activeforeground="black", 
    activebackground="white", 
    #command = printInput,
    )
#button1.pack(side=LEFT, anchor=SW, padx=0, pady=45)
#button1.pack() 

#Number 2 Button
button2 = tk.Button(gui, 
    text = "2",
    height = 1,
    width = 8,
    font=("Comic Sans", 10), 
    fg = "black", 
    bg = "white", 
    activeforeground="black", 
    activebackground="white", 
    #command = printInput,
    )
#button2.pack(side=TOP, padx=0, pady=0)
#button2.pack() 

#End
gui.mainloop()