from tkinter import *

def openFile():
    print('File has been opened')
def saveFile():
    print('File has been saved')
def cut():
    print('You cut some text')
def copy():
    print('You copy some text')
def paste():
    print('You pasted some text')


window = Tk()

openImage=PhotoImage(file='open.png')
openResize_img=openImage.subsample((60))

saveImage=PhotoImage(file='save.png')
saveResize_img=saveImage.subsample((60))

exitImage=PhotoImage(file='exit.png')
exitResize_img=exitImage.subsample((60))

#openLabel= Label(image=openResize_img)


menubar = Menu(window)
window.config(menu=menubar)

#File Menu
fileMenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='File', menu=fileMenu)
fileMenu.add_command(label='Open', command=openFile, image=openResize_img, compound='left')
fileMenu.add_command(label='Save', command=saveFile, image=saveResize_img, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit, image=exitResize_img, compound='left')

#Edit Menu

editMenu = Menu(menubar, tearoff=0, font=('MV Boli', 15))
menubar.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label='Copy', command=copy)
editMenu.add_command(label='Paste', command=paste)




window.mainloop()