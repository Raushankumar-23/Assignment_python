# step-1 importing

import tkinter as tk
from tkinter import *

window = Tk()
window.geometry("320x450")
window.title("Calculator",)
window.configure(bg="#1E1E1E")   # Dark background

e = Entry(window, width=56,borderwidth=5,bg="#2D2D2D", fg="white", insertbackground="white")
e.place(x=0,y=0)


def click(num):
    resut = e.get()
    e.delete(0,END)
    e.insert(0, str(resut) + str(num))


# Button
b = Button(window,text="1",width=12,command=lambda:click(1) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=10,y=60)

b = Button(window,text="2",width=12,command=lambda:click(2),bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3 )
b.place(x=80,y=60)

b = Button(window,text="3",width=12, command=lambda:click(3) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=170,y=60)

b = Button(window,text="4",width=12, command=lambda:click(4) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=10,y=120)

b = Button(window,text="5",width=12,command=lambda:click(5) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=80,y=120)

b = Button(window,text="6",width=12,command=lambda:click(6),bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3 )
b.place(x=170,y=120)

b = Button(window,text="7",width=12,command=lambda:click(7),bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3 )
b.place(x=10,y=180)

b = Button(window,text="8",width=12 ,command=lambda:click(8),bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3 )
b.place(x=80,y=180)

b = Button(window,text="9",width=12,command=lambda:click(9) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=170,y=180)

b= Button(window,text="0",width=12,command=lambda:click(0) ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=10,y=240)

# operator

def add():
    n1 = e.get()
    global  i
    global math
    math = "addition"
    i = int(n1)
    e.delete(0,END)


b = Button(window,text="+",width=12, command=add,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=80,y=240)


def sub():
    n1 = e.get()
    global  i
    global math
    math = "subtraction"
    i = int(n1)
    e.delete(0,END)

b= Button(window,text="-",width=12,command=sub,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=170,y=240)

def mul():
    n1 = e.get()
    global  i
    global math
    math = "multiplication"
    i = int(n1)
    e.delete(0,END)

b= Button(window,text="*",width=12,command=mul ,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=10,y=300)

def div():
    n1 = e.get()
    global  i
    global math
    math = "divide"
    i = int(n1)
    e.delete(0,END)

b = Button(window,text="/",width=12,command=div , bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=80,y=300)


def equal():
    n2 = e.get()
    e.delete(0,END)
    if   math == "addition":
        e.insert(0,i + int(n2))
    elif math == "subtraction":
        e.insert(0,i - int(n2))
    elif math == "multiplication":
        e.insert(0,i * int(n2))
    elif math == "divide":
        e.insert(0,i / int(n2))



b= Button(window,text="=",width=12,command=equal, bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=170,y=300)

def clear():
    e.delete(0,END)

b= Button(window,text="clear",width=12,command=clear,bg="#2A2A2A",fg="#EAEAEA",relief="raised",bd=3)
b.place(x=10,y=360)




# step-4 mainloop

mainloop()

