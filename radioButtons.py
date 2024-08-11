#Radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get()==0):
        print("You ordered a pizza")
    elif(x.get()==1):
        print("You ordered a hamburger")
    elif(x.get()==2):
        print("You ordered a hotdog")
    else:
        print("Huh")


window =Tk()

pizzaImage=PhotoImage(file='pizza.png')
burgerImage=PhotoImage(file='burger.png')
hotdogImage=PhotoImage(file='hotdog.png')

#smallerPizza=pizzaImage.subsample(2,2)
#smallerBurger=burgerImage.subsample(2,2)
#smallerHotdog=hotdogImage.subsample(2,2)

#foodImages=[smallerBurger,smallerHotdog,smallerPizza]
foodImages=[pizzaImage,burgerImage,hotdogImage]


x=IntVar()

for index in range(len(food)):
    radiobuttuon=Radiobutton(window,
                             text=food[index], #adds text to radio buttons
                             variable=X, #groups radiobuttons together if they share the same variable 
                             value=index, #assigns each radBut a diff value
                             padx = 25,
                             font=("impact", 20),
                             image=foodImages[index], #This adds image to RadButton
                             compound='left', #adds image and text
                             indicatoron=0, #eliminate circle indicators
                             width= 100, #sets width of radio buttons
                            height=100,
                            command=order #set command of radiobutton to function


                             )
    radiobuttuon.pack(anchor=W)



window.mainloop()

