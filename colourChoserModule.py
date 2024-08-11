from tkinter import *
from tkinter import colorchooser  #submodule


def click():
    color=colorchooser.askcolor()
    print(color)
    window.config(bg=color[1]) #change background color

window =Tk()
window.geometry('420x420')
button = Button(text='click me', command=click)
button.pack()
window.mainloop()