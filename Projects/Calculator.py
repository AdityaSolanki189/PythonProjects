import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


def clicked_1():
    global val
    val = val + "1"
    data.set(val)

def clicked_2():
    global val
    val = val + "2"
    data.set(val)

def clicked_3():
    global val
    val = val + "3"
    data.set(val)

def clicked_4():
    global val
    val = val + "4"
    data.set(val)

def clicked_5():
    global val
    val = val + "5"
    data.set(val)

def clicked_6():
    global val
    val = val + "6"
    data.set(val)

def clicked_7():
    global val
    val = val + "7"
    data.set(val)

def clicked_8():
    global val
    val = val + "8"
    data.set(val)

def clicked_9():
    global val
    val = val + "9"
    data.set(val)

def clicked_0():
    global val
    val = val + "0"
    data.set(val)

def clicked_plus():
    global A
    global val
    global operator
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def clicked_minus():
    global A
    global val
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def clicked_multiply():
    global A
    global val
    global operator
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def clicked_divide():
    global A
    global val
    global operator
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def clear_screen():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val_2 = val
    if operator == "+":
        x = int((val_2.split("+")[1]))
        C = A + x
        data.set(C)
        val = str(C)
    elif operator == "-":
        x = int((val_2.split("-")[1]))
        C = A - x
        data.set(C)
        val = str(C)
    elif operator == "*":
        x = int((val_2.split("*")[1]))
        C = A * x
        data.set(C)
        val = str(C)
    elif operator == "/":
        x = int((val_2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error","NOT POSSIBLE")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)
            val = str(C)

root = tkinter.Tk()
root.geometry("350x500+450+450")
root.resizable(0,0)
root.title("My Calculator")

data = StringVar()
lbl = Label(
    root,
    text = "Label",
    anchor = SE,
    font = ("Verana",22),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both",)

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btn1 = Button(
    btnrow1,
    text = "1",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_1,
)
btn1.pack(side = LEFT,expand = True,fill = "both")

btn2 = Button(
    btnrow1,
    text = "2",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_2,
)
btn2.pack(side = LEFT,expand = True,fill = "both")

btn3 = Button(
    btnrow1,
    text = "3",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_3,
)
btn3.pack(side = LEFT,expand = True,fill = "both")

btnplus = Button(
    btnrow1,
    text = "+",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_plus,
)
btnplus.pack(side = LEFT,expand = True,fill = "both")

btn4 = Button(
    btnrow2,
    text = "4",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_4,

)
btn4.pack(side = LEFT,expand = True,fill = "both")

btn5 = Button(
    btnrow2,
    text = "5",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_5,
)
btn5.pack(side = LEFT,expand = True,fill = "both")

btn6 = Button(
    btnrow2,
    text = "6",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_6,
)
btn6.pack(side = LEFT,expand = True,fill = "both")

btnminus = Button(
    btnrow2,
    text = "-",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_minus,
)
btnminus.pack(side = LEFT,expand = True,fill = "both")

btn7 = Button(
    btnrow3,
    text = "7",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_7,
)
btn7.pack(side = LEFT,expand = True,fill = "both")

btn8 = Button(
    btnrow3,
    text = "8",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_8,
)
btn8.pack(side = LEFT,expand = True,fill = "both")

btn9 = Button(
    btnrow3,
    text = "9",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_9,
)
btn9.pack(side = LEFT,expand = True,fill = "both")

btnmultiply = Button(
    btnrow3,
    text = "*",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_multiply,
)
btnmultiply.pack(side = LEFT,expand = True,fill = "both")

btnclear = Button(
    btnrow4,
    text = "C",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clear_screen,
)
btnclear.pack(side = LEFT,expand = True,fill = "both")

btn0 = Button(
    btnrow4,
    text = "0",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_0,
)
btn0.pack(side = LEFT,expand = True,fill = "both")

btnequal = Button(
    btnrow4,
    text = "=",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT,expand = True,fill = "both")

btndivide = Button(
    btnrow4,
    text = "/",
    font = ("Verana",22),
    relief = GROOVE,
    border = 0,
    command = clicked_divide,
)
btndivide.pack(side = LEFT,expand = True,fill = "both")

root.mainloop()
