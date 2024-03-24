from tkinter import *
import random

import tkinter as tk

#Button
count = 0

def click():
    global count
    count+=1
    print("You clicked me")
    print(count)

#Open Window
window = tk.Tk()

w_width, w_height = 1000, 650
s_width, s_height = window.winfo_screenwidth(), window.winfo_screenheight()
x, y = (s_width/2)-(w_width/2), (s_height/2)-(w_height/2)
window.geometry('%dx%d+%d+%d' % (w_width,w_height,x,y-30))
window.configure(bg='white')

def destroy_button():
    button.destroy()

button = tk.Button(window, 
    text="Button", 
    font=("Comic Sans", 30), 
    fg = "green", 
    bg = "black", 
    activeforeground="green", 
    activebackground="black", 
    command=destroy_button,
    )

#Button End
button.pack(side=TOP, padx=15, pady=275)

button.pack()

#Start input box
"""def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp)"""
  
# TextBox Creation 
inputtxt = tk.Text(window, 
    height = 1, 
    width = 25)
inputtxt.pack(side=TOP, padx=15, pady=275)
  
inputtxt.pack() 

  
# Button Creation 
printButton = tk.Button(window, 
    text = "Confirm",
    font=("Comic Sans", 10), 
    fg = "green", 
    bg = "black", 
    activeforeground="green", 
    activebackground="black", 
    #command = printInput,
    )
printButton.pack(side=TOP, padx=0, pady=0)
printButton.pack() 
  
# Label Creation 
"""lbl = tk.Label(window, text = "") 
lbl.pack() """

#End
window.mainloop()