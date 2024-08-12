from tkinter import *

def doSomething(event):
    print("Mouse coordinates: " + str(event.x) + "," + str(event.y))

window = Tk()

#window.bind("<Button-1>", doSomething) #Left mouse click
#window.bind("<Button-2>", doSomething) #Pressing on Scroll wheel
#window.bind("<Button-3>", doSomething) # Right mouse click
window.bind("<ButtonRelease>", doSomething)
window.bind("<Enter>", doSomething)
window.bind("<Leave>", doSomething)
window.bind("<Motion>", doSomething) #where the mouse moved

window.mainloop()

