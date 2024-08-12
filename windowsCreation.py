# New ways of creating windows

from tkinter import *

def create_window():
    #new_window = Toplevel() # new window on top of other windows
    new_window = Tk()   # new independ window

    old_window.destroy() #This close out of old window

old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()
old_window.mainloop()