from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

Bgimage = PhotoImage(file='space.png')
Bg_photo = canvas.create_image(0,0, image=Bgimage)

myimage = PhotoImage(file='sdgs.png')
myimage = myimage.subsample(10)
my_image = canvas.create_image(0,0, image=myimage, anchor=NW)

image_width = myimage.width()
image_height = myimage.height()

while True:
    coordinates =canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= (WIDTH-image_width) or coordinates[0] < 0 ):
        xVelocity = - xVelocity

    if (coordinates[1] >= (HEIGHT-image_height) or coordinates[1] < 0 ):
        yVelocity = - yVelocity

    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()