# frame = a rectangular container to group and hold widgets

from tkinter import *

window = Tk()

frame = Frame(window, bg="Pink", bd=5, relief=SUNKEN)  #bd - border, relief = font
#frame.place(x=20, y=25) #Adjust the position of the fram
frame.pack(side=BOTTOM)

button = Button(frame, text="W", font=("Consolas", 25), width = 3).pack(side=TOP)
button = Button(frame, text="A", font=("Consolas", 25), width = 3).pack(side=LEFT)
button = Button(frame, text="S", font=("Consolas", 25), width = 3).pack(side=LEFT)
button = Button(frame, text="D", font=("Consolas", 25), width = 3).pack(side=LEFT)


window.mainloop()