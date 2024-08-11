""" name = "bro code" """
#print(name.find("o"))
##print(name.capitalize())
#print(name.upper())
#print(name.count("o"))
#print(name*3)

""" x=0
y=1
z='2'
z=int(z)
print(z*3) """

""" ame = input("Enter your name: ")
age = int(input("What is your age ? "))
height= float(input(("How tall are you?")))


print("Hello " + name)
print("Your age is: " + str(age))
print("You are " + str(height) + "cm tall")
 """

""" import math
pi = 3.14
print(round(pi))
print(math.ceil(pi)) #roundup
print(math.floor(pi)) #round down

 """

#Slicing
#create a substring by extracting elements from another string
# indexing[] or slice[]
# [start:stop:step]
""" name = "Bro code"
first_name = name[:3]
last_name = name[4:]
print(first_name)
print(last_name)
funky_name=name[::3]
print(funky_name)
reversed_name=name[::-1]
print(reversed_name) """

#String Slicing
""" website1="https://google.com"
website2="https://wikipedia.com"
slice = slice(8, -4) #Beginning point and endpoint
print(website1[slice])
print(website2[slice]) """

#If statement
""" 
age = int(input("How old are you? "))
if age>=18:
    print("You are an adult")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are a child") """

""" 
#While Loop, unlimited time execution
name = None
while not name:
    name=input("Enter your name ")
print("Hello, " + name)
 """


#For loops a limited time execution

""" for i in range(10+1):
    print(i+i) """

""" for i in range(50,100, 2):
    print(i) """

""" for i in "Bro code":
    print(i) """

""" import time


for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) """

#Nexted loops
""" 
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol= input("Enter a symbol ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
 """

#Loop control statements

""" while True:
    name = input("Enter name ")
    if name !="":
        break """

""" phone_number = '123-456-789'
for i in phone_number:
    if i == "-":
        continue
    print(i, end="") """

""" for i in range(1,21):
    if i==13:
        pass      #Passes skips
    else:
        print(i) """

#List in python

""" food = ["pizza","hamburger","spaghetti", "hotdog"]
food[0] = "sushi"

food.insert(0, "cake")
food.reverse()
food.sort()
print(food[0:4])

for x in food:
    print(x) """

""" #2D Lists = a list of lists

drinks = ["coffee","soda", "tea"]
dinner = ["pizza","hamburger", "hotdog"]
dessert = ["cake","ice cream"]

food = [drinks, dinner, dessert]
print(food[0][2]) #This prints from drinks
print(food[1][2]) #This prints from dinner
 """

#Tuples  collection  of ordered and unchangeable used to group together related date
""" student =("Bro", 21, "male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here") """

#Set = collection which is unordered, uninedxed. No duplicate value

""" utensils = {"fork", "spoon", "knife"}
dishes = {"ball", "plate", "cup"}
utensils.add("napkin")
utensils.update(dishes)
dinner_table = utensils.union(dishes)

for x in utensils:
    print(x)

for x in dinner_table:
    print(x) 

print(utensils.difference(dishes))
print(utensils.intersection(dishes)) """

#Dictionary = A changeable, unordered collection of unique key:value pairs
#Fast because they use hashing, allow us to access a value quickly

""" capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijin',
            'Russia': 'Moscow'}

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key, value in capitals.items():
    print(key,value) """

# Index operator [] = gives access to a sequence's element(str,list,tuples)

""" name = "bro Code"

#if(name[0].islower()):
    #name = name.capitalize()

first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character) """

#function = a block of code which is executed only when its called

""" def hello(firstname, lastname):
    print("Hello " + firstname + " " + lastname)
hello("bro", "code") """

#Return Statement 

""" def mult (num1, num2):
    result = num1 * num2
    return result
x = mult(6,8)
print(x)

def mult (num1, num2):
    return num1 * num2
x = mult(6,8)
print(x) """

#Arguments parameters that will pack all arguments into a tuple
#useful so that a function can accept a very amount of arguments

""" def add(*stuff):
    sum = 0
    stuff = list(stuff)
    stuff[0]=0
    for i in stuff:
        sum += i
    return sum
print(add(1,2,3,4,5,6)) """


#Kwargs, parameter that will pack all arguments into a dictionary
#Useful so that a function can accept a varying amount of keyword argument
# ...into a dictionary
""" 
def hello(**kwargs):
    print("Hello ", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")
hello(title="Mr.", first="Bro", middle="Dude", last="Code")
 """

# Format method available to strings

""" animal = "cow"
item = "moon"
#print("The " + animal + " jumped over the " + item)

#print("The {} jumped over the {}".format(animal, item))
#print("The {0} jumped over the {1}".format(animal, item)) #positional argument
#print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Bro"
print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:<10} Nice to meet you".format(name)) #left align
print("Hello, my name is {:>10} Nice to meet you".format(name)) #right align
print("Hello, my name is {:^10} Nice to meet you".format(name)) #centre align

number = 3.14159
print("The number pi is {:.2f}".format(number))

number = 1000
print("The number is {:,}".format(number)) #Puts a comma
print("The number is {:b}".format(number)) #Displays as a binary
print("The number is {:o}".format(number)) #Displays as octo
 """

# generate random numbers
""" import random

x = random.randint(1,6)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,'J','Q','K','A']
random.shuffle(cards)

print(cards) """

#Exception = events detected during execution that interrupt the flow of a program
# Exception handling prevents the program from being interrupted
#Good practice to catch the specific exceptions to let the user know what specifically 
#went wrong using the TRY and EXCEPT Blocks
""" 
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)
except ZeroDivisionError:
    print("You can't divide by 0")
except ValueError:
    print("Enter only numbers please")
except Exception:
    print("Something went wrong")

#You can also catch exceptions properly using the below
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0")
except ValueError as e:
    print(e)
    print("Enter only numbers please")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")

 """

# File and folder detection in python

""" import os

path = "C:\\Users\\dasiedu\\Desktop\\MUN"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("That location doesn't exist")
 """

#Open and read a file
""" 
try:
    with open('text.txt') as file:
         print(file.read())
         print(file.closed)
except FileNotFoundError as e:
     print(e)
     print("file was not found") """




""" text = "uh oh, this text has been overwritten"
with open('text.txt', 'w') as file:
    file.write(text) """

""" text1 = "uh oh, this text has been added to the text"
with open('text.txt', 'a') as file:
    file.write(text1)
 """


#Copy a file 
#copyfile() - copies content of a file
#copy() - copyfile()+permission mode + destination can be a dir
#copy2() - copy() + copies metadata
""" 
import shutil

shutil.copyfile('text.txt', 'copy.txt') #src, destination
 """

#Move files using python
""" 
import os

source = 'text.txt'
destination = 'C:\\Users\\dasiedu\\Desktop\\text.txt'

#This can be used to move a Dir
try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+"was moved")
except FileNotFoundError:
    print(source + "was not found") """

#delete a file or dir

""" import os, shutil
path = 'text.txt'

try:
    os.remove(path) #deletes a file
    os.rmdir(path) #deletes an empty dir
    shutil.rmtree(path) #deletes a dir containing files
except FileNotFoundError as e:
    print(e)
except PermissionError as e:
    print(e)
except OSError as e:
    print(e)
else:
    print(path+" was deleted") """

#Modules

#Modules a file containing python code, may contain functions
#classes, etc used with modular programming which is to separate a program into parts

#To use the module you need to import it

""" import messages as msg
from messages import hello, bye #this imports a selected modules
from messages import * # this imports all modules

msg.hello()
msg.bye()
 """

say = print
say("Whoa! I cant believe this works!")

