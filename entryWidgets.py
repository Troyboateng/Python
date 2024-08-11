from tkinter import *

# Entry Widge creation, textboz that accepts a single line of user input

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED) #This will disable after the submit is pressed

def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)




window = Tk()

#Entry Widget 
entry = Entry(window,
              font=('Arial', 20),
              fg ="#00FF00",
              bg ='black',
              
              )
entry.config(show="*") #This hashe's whatever is being inputted in the entry widget good for passwords
entry.insert(0, 'type here')   #This gives an indication to the user as to where to type
entry.pack(side=LEFT)

#Submit Widget
submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack(side=TOP)

#Delete Widget
delete_button = Button(window,
                       text="Delete",
                       command=delete)
delete_button.pack(side=TOP)

#Backspace Widget
backspace_button = Button(window,
                       text="Backspace",
                       command=backspace)
backspace_button.pack(side=TOP)



window.mainloop() #place a window on computer screen, listen for for events
