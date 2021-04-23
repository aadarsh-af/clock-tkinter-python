from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime("%I:%M:%S %p") #"%H:%M:%S: %p" for 24 hour format
    label.config(text=string)
    label.after(1000,time)


label = Label(root, font=("quicksand",50,'normal'),background = "black", foreground = "yellow")
label.pack(anchor='center')
time()

mainloop()