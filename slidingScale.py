#Sliding Scale GUI

from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + " degrees C")

window =Tk()

hotImage=PhotoImage(file='fire.png')
hotResize_img=hotImage.subsample((60))
hotLabel= Label(image=hotResize_img)
hotLabel.pack()



scale = Scale(window, 
              from_ = 100, 
              to=0,
              length = 400,
              orient=VERTICAL, #Orientation of scale
              font=('Consolas', 15),
              tickinterval= 10, #adds numric indicators for value
              showvalue=0, #hide current value
              resolution=5, #increment of slider
              troughcolor='#69EAFF',
              fg='#FF1C00',
              bg='#111111'



              )

scale.set(((scale['from']-scale['to'])/2)+scale['to'])  #set current value of slider
scale.pack()


coldImage=PhotoImage(file='cold.png')
coldResize_img=coldImage.subsample((50))
coldLabel= Label(image=coldResize_img)
coldLabel.pack()


button = Button(window, text='submit', command=submit)
button.pack()


window.mainloop()