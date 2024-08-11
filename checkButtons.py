from tkinter import *

# Check buttons or Check boxes

def display():
    if(x.get()==1):
        print("You agree!")

    else:
        print("You dont agree :(")

window = Tk()

x = IntVar()   #If it were to return a string then StrVar, BooleanVar if True/False

used_Picture=PhotoImage(file='cim.png')

check_button=Checkbutton(window,
                         text="I agree to something",
                         variable=x,
                         onvalue=1,
                         offvalue=0,
                         command=display,
                         font=('Arial', 20),
                         fg='#00ff00',
                         bg = 'black',
                         activeforeground='#00ff00',
                         activebackground='black',
                         padx=25,
                         pady=10,
                         image=used_Picture,
                         compound='left'
                         )

check_button.pack()
window.mainloop()
