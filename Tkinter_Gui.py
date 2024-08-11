#First Gui using Python

from tkinter import *

#widgets = GUI elements: buttons, textboxes, labels, images
#windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
#window.geometry("420x420") #adding a specific dimensions
window.title("Dom first GUI program")

icon = PhotoImage(file='sdgs.png')
window.iconphoto(True, icon)
window.config(background="#5dbad4")

# LABELS
photo = PhotoImage(file='cim.png')
label = Label(window,
              text="Hello Bro", 
              font=('Arial', 20, 'bold'), 
              fg='#7a3bed', 
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')
label.pack() # Automatically places it in the top middle
#label.place(x=100, y=100) # using coordinates

# BUTTON = ypu click it, then it does stuff

count = 0

def click():
    global count
    count += 1

    print(count)

button = Button(window,
                text="click me",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activebackground='#00ff00',
                state=ACTIVE,

                )
#You can add image in the button

button.pack()






window.mainloop() #place a window on computer screen, listen for for events
