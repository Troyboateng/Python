# Listbox = is a listing of selectable text items within it's own container

def submit():

                                                            #creates a list that will hold multiple selection
    food = []
                                                            #recursively stores in the empty list created above
    for index in listbox.curselection():
        food.insert(index,listbox.get(index))

    print("You have ordered: ")
    
                                                                #This prints the items in the list food created above    
    for index in food:
        print(index)
    
    
    #print(listbox.get(listbox.curselection())) # gets the current submission

def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())  #Change the size of listbox dynamically

def delete():
                                                            #Multiple deletion of items
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

   # listbox.delete(listbox.curselection())  #when you have to delete one item only at a time
    listbox.config(height=listbox.size())


from tkinter import *

window = Tk()

listbox=Listbox(window,
                bg='#f7ffde',
                font=("constantia", 24),
                width=12,
                selectmode=MULTIPLE, #select multiple
                )
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()



window.mainloop()