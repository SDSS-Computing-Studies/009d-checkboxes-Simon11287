#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""
import tkinter as tk 
from tkinter import *
from tkinter import ttk



def binary_to_decimal(binary):
    decimal = binary[0]*128+binary[1]*64+binary[2]*32+binary[3]*16+binary[4]*8+binary[5]*4+binary[6]*2+binary[7]
    return decimal 

    

def decimal_to_binary(decimal):


    num=int(decimal)
    
    binary=[]
    for i in range(0,8):
        newnum=128/(2**i)
        remaining=num-newnum
        
        if remaining>=0:
            binary.insert(i,1)
            num=remaining
        elif remaining<0:
            binary.insert(i,0)
            num=remaining+newnum
        
    return binary

def get_binary():
    decimal = e1.get()
    binary = decimal_to_binary(decimal)
    state1.set(binary[0])
    state2.set(binary[1])
    state3.set(binary[2])
    state4.set(binary[3])
    state5.set(binary[4])
    state6.set(binary[5])
    state7.set(binary[6])
    state8.set(binary[7])
def get_decimal():

    binary = []
    
    a=int(state1.get())
    b=int(state2.get())
    c=int(state3.get())
    d=int(state4.get())
    e=int(state5.get())
    f=int(state6.get())
    g=int(state7.get())
    h=int(state8.get())
    binary.insert(0,a)
    binary.insert(1,b)
    binary.insert(2,c)
    binary.insert(3,d)
    binary.insert(4,e)
    binary.insert(5,f)
    binary.insert(6,g)
    binary.insert(7,h)
    decimal = binary_to_decimal(binary)
    eoutput.set(decimal)
win = tk.Tk() 
state1=IntVar()
state1.set(0)
state2=IntVar()
state2.set(0)
state3=IntVar()
state3.set(0)
state4=IntVar()
state4.set(0)
state5=IntVar()
state5.set(0)
state6=IntVar()
state6.set(0)
state7=IntVar()
state7.set(0)
state8=IntVar()
state8.set(0)
eoutput=StringVar()
win.title("Task1")
l1=Label(win,text="Binary/Decimal Converter")


cb1=Checkbutton(win,variable=state1)
cb2=Checkbutton(win,variable=state2)
cb3=Checkbutton(win,variable=state3)
cb4=Checkbutton(win,variable=state4)
cb5=Checkbutton(win,variable=state5)
cb6=Checkbutton(win,variable=state6)
cb7=Checkbutton(win,variable=state7)
cb8=Checkbutton(win,variable=state8)
b1 = Button(win, text="Convert to Binary",command=get_binary)
b2 = Button(win, text="Convert to Decimal",command=get_decimal)
e1=Entry(win,textvariable=eoutput)
win.geometry("230x120")


l1.place(x=30,y=10)
cb1.place(x=10,y=30)
cb2.place(x=30,y=30)
cb3.place(x=50,y=30)
cb4.place(x=70,y=30)
cb5.place(x=90,y=30)
cb6.place(x=110,y=30)
cb7.place(x=130,y=30)
cb8.place(x=150,y=30)
b1.place(x=1,y=55)
b2.place(x=105,y=55)
e1.place(x=40,y=90)
win.mainloop()
