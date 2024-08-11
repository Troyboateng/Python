from tkinter import *
from tkinter import messagebox

def click():
    #messagebox.showinfo(title='This is an info message box', message='You are a person')
    #messagebox.showwarning(title='WARNING', message='You have a VIRUS!')
    #messagebox.showerror(title='ERROR!', message='something went wrong')

    #if messagebox.askyesno(title='ask yes or no', message='Do you like cake'):
     #  print('I like cake too')
    #else:
    #   print('Why not ?')
    
   # answer = messagebox.askquestion(title='ask question', message='Do you like pie?')
    #if (answer=='yes'): # type: ignore
      # print('I like pie too')
   print(messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code', icon='info'))
   



window = Tk()

button = Button(window, 
                command=click,
                 text='click me' )

button.pack()

window.mainloop()