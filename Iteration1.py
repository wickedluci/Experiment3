# Creating A Calculator
from tkinter import *

def button_click(number):
    e.insert(END, number)

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num, math
    f_num = float(e.get())
    math = "addition"
    e.delete(0, END)

def button_equal():
    second_number = float(e.get())
    e.delete(0, END)
    
    if math == "addition":
        e.insert(0, f_num + second_number)
    elif math == "subtraction":
        e.insert(0, f_num - second_number)
    elif math == "multiplication":
        e.insert(0, f_num * second_number)
    elif math == "division":
        e.insert(0, f_num / second_number)

def button_subtract():
    global f_num, math
    f_num = float(e.get())
    math = "subtraction"
    e.delete(0, END)

def button_multiply():
    global f_num, math
    f_num = float(e.get())
    math = "multiplication"
    e.delete(0, END)

def button_divide():
    global f_num, math
    f_num = float(e.get())
    math = "division"
    e.delete(0, END)

root = Tk()
root.title("Calculator")
root.configure(bg="black")


e = Entry(root, width=35, borderwidth=5, fg="white", bg="black", font=("Arial", 14))
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button properties
btn_config = {"padx": 20, "pady": 10, "fg": "cyan", "bg": "black", "font": ("Arial", 12)}

# Create buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text.isdigit():
        Button(root, text=text, command=lambda t=text: button_click(t), **btn_config).grid(row=row, column=col)
    elif text == "C":
        Button(root, text=text, command=button_clear, **btn_config).grid(row=row, column=col)
    elif text == "=":
        Button(root, text=text, command=button_equal, **btn_config).grid(row=row, column=col)
    elif text == "+":
        Button(root, text=text, command=button_add, **btn_config).grid(row=row, column=col)
    elif text == "-":
        Button(root, text=text, command=button_subtract, **btn_config).grid(row=row, column=col)
    elif text == "*":
        Button(root, text=text, command=button_multiply, **btn_config).grid(row=row, column=col)
    elif text == "/":
        Button(root, text=text, command=button_divide, **btn_config).grid(row=row, column=col)

root.mainloop()
