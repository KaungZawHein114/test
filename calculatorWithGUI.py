import tkinter as tk
from tkinter import *
hafsaklgfkagfjshgfkegyiaer

root = tk.Tk()
root.title("Calculator")

box = Entry(root, width=50, borderwidth=5)
box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def numberAdd(number):
    current = box.get()
    box.delete(0, END)
    box.insert(0, str(current) + str(number))
    
def clear():
    box.delete(0, END)

def add():
    firstNumber = box.get()
    global f_num
    global math
    math = "addition"
    f_num = int(firstNumber)
    box.delete(0, END)
    
def subtract():
    firstNumber = box.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(firstNumber)
    box.delete(0, END)

def multiply():
    firstNumber = box.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(firstNumber)
    box.delete(0, END)

def divide():
    firstNumber = box.get()
    global f_num
    global math
    math = "division"
    f_num = int(firstNumber)
    box.delete(0, END)

def equal():
    secondNumber = box.get()
    box.delete(0, END)
    if math == "addition":
        box.insert(0, f_num + int(secondNumber))
    elif math == "subtraction":
        box.insert(0, f_num - int(secondNumber))
    elif math == "multiplication":
        box.insert(0, f_num * int(secondNumber))
    elif math == "division":
        box.insert(0, f_num / int(secondNumber))

button2 = Button(root, text="1",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(1)).grid(row=3, column=1)
button1 = Button(root, text="2",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(2)).grid(row=3, column=0)
button3 = Button(root, text="3",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(3)).grid(row=3, column=2)
button4 = Button(root, text="4",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(4)).grid(row=2, column=0)
button5 = Button(root, text="5",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(5)).grid(row=2, column=1)
button6 = Button(root, text="6",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(6)).grid(row=2, column=2)
button7 = Button(root, text="7",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(7)).grid(row=1, column=0)
button8 = Button(root, text="8",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(8)).grid(row=1, column=1)
button9 = Button(root, text="9",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(9)).grid(row=1, column=2)
button0 = Button(root, text="0",padx= 40, pady=20, borderwidth=1, command=lambda: numberAdd(0)).grid(row=4, column=0)

buttonAdd = Button(root, text="+", padx= 40, pady= 20, borderwidth= 1, command= add).grid(row=4, column=1)
buttonSubtract = Button(root, text="-", padx = 40, pady = 20, borderwidth=1, command= subtract).grid(row=4, column=2 )
buttonMultiply = Button(root, text="×", padx = 40, pady = 20, borderwidth=1, command= multiply).grid(row=5, column=1 )
buttonDivide = Button(root, text="÷", padx = 40, pady = 20, borderwidth=1, command= divide).grid(row=5, column=2 )
buttonClear = Button(root, text="Clear", padx= 30, pady= 60, borderwidth=1, command= clear).grid(row=5, column=0, rowspan=2)
buttonEqual = Button(root, text="=", padx= 95, pady=20, borderwidth=1, command= equal).grid(row=6, column=1, columnspan= 2)

root.mainloop()