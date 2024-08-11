from tkinter import *
from tkinter import filedialog


def saveFile():
    file=filedialog.asksaveasfile(initialdir='C:\\Users\\dasiedu\\Desktop\\Codes',
                                    defaultextension='.txt',
                                  filetypes=[
                                      ("Text file", ".txt"),
                                      ("HTML file", ".html"),
                                      ("All files", ".*")
                                  ])
    
    if file is None:   #Exception to handle error
        return
    
    filetext=str(text.get(1.0,END)) # This allows you to text in a text area
    #filetext=input('Enter some text I guess: ')  # Takes text from the console area
    file.write(filetext)
    file.close()

window=Tk()

button = Button(text='save',
                command=saveFile)
button.pack()

text = Text(window)

text.pack()

window.mainloop()