""" x = 5
y = 10
c = "Hello"
print(x + y)


Radius = eval (input("Enter a value as input: "))
print(Radius)
 """

"""a = 6
b = 2

c = (a % b)
print(c)
"""

'''
x=y=z=u = 0
n=eval(input("The total number to be inputted : "))

for index in range(n):
    B = eval(input("Enter a number : "))
    if (B > 0):
        x += 1
    if(B<0):
        y += 1
    if(B==0):
        z+= 1
    
print("positive ", x, "negative", y, "zeros", z)

'''
"""
adj=['a', 'b', 'c']
for i, x in enumerate(adj):
    print(i, x)
"""
"""
for i in range(1, 20):
    if i % 2 == 0:
        print(i)


for i in range(19):
    if i == 0: continue
    if i % 2 == 0:
        print(i)
"""

#Factorial 

# number = 100
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(factorial)
    
#Fibonnaci

#0,1,1,2,3

#Start
# set a =b = 1, set Fib-c = 0
#  print a, b
# add a to b and set to Fib-c
# set a = b
# set b = Fib-c
#print Fib-c
# if Fib-c is less than 100
# Repeat step

#code for fibonacci

# a = b = 1
# while( a <= 100):
#     print(a)
#     fib = a + b
#     a = b
#     b = fib

1
#Code for GCD

# a = int(input("Enter num1:"))
# b = int(input("Enter num2: "))
# while b != 0:
#     a, b = b, a % b
# print(a)


# # Input two numbers
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# # Using the Euclidean algorithm to find GCD
# while b != 0:
#     a, b = b, a % b

# # The GCD is now in 'a'
# print("The greatest common divisor is:", a)



#Count number of digits in a number

# A= eval(input("Enter anumber: "))
# count = 0

# while (A != 0):
#     A = A // 10
#     count = count + 1
# print(count)


#Question: Write a program that gets and prints the reverse of the number:

#Count number of digits in a number

# A= eval(input("Enter a number: "))
# ReversedA = 0

# while (A != 0):
#     C = A % 10
#     ReversedA = (ReversedA * 10) + C
#     A = A // 10
# print(ReversedA)

# Question: write an algorithm and program to calculate the sum of the numbers from 1 to 10
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print(sum)

"""
y = eval(input("Enter num: "))
prime = True

for i in range(y):
    if y % i == 0:
        prime = False
        break


# Question: Write a program that gets a number and prompts whether it is prime or not.
A = eval(input("Enter num: "))
count = 0

for i in range(2, A):
    if(A % i == 0):
        count = count + 1

if (count == 0) and (A != 1):
    print("The number is prime")
else:
    print("Not prime")

"""

# Write a Python program to find 
# and print numbers between 401 and 470 
# where each digit of a number is an even number 
# (For example 426 is one of these numbers).

# for number in range(401,471):
#         if int(number) % 2 == 0:
#             even_number = number
#             print(even_number)
#         else:
#             ("not even number")

#Write a program that takes n numbers and shows the average of these numbers

# N = eval(input('How many numbers: '))
# sum = 0

# for i in range(1, N+1):
#     A = eval(input("Enter a number: "))
#     sum = sum + A

# average = sum / N
# print(average)


#Question: Write a program that prints a multiplication table

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i * j, end =" ")
#     print()

#Code to print even numbers from 401 to 471

# Write a Python program to find and
#  print numbers between 401 and 470 where each digit 
#  of a number is an even number (For example 426 is one of these numbers).

# for number in range(401, 470):
#     hundreds = number // 100
#     tens = (number // 10) % 10
#     zeros = number % 10

#     if (hundreds % 2 == 0) and (tens % 2 == 0) and (zeros % 2 == 0):
#         print(number, end = " ")
    
#Python Classes (Super class)

# class Emp():
#     def __init__(self, id, name, Add):
#         self.id = id
#         self.name = name
#         self.Add = Add

# #Class freelancer inherits EMP
# class Freelance(Emp):
#     def __init__(self,id,name,Add,Emails):
#         super().__init__(id,name,Add)
#         self.Emails = Emails

# Emp_1 = Freelance(103, "Arash", "AR2020", "KKK@gmails")
# print("The ID is: ", Emp_1.id)
# print("The name is: ",Emp_1.name)
# print("The Address is :", Emp_1.Add)
# print("The email is :", Emp_1.Emails)

# #This includes whitespaces
# x = "hello world"
# print(len(x))

# #Tuples
# mytuple = ('apple', 'banana', 'cherry')
# print(len(mytuple))

# #Dictionary

# thisdict = {
#     'brand': 'Toyota',
#     'country': 'Canada'

# }

# x = -1
# if x < 0:
#     raise Exception("X should be greater than 0")

# Questions:

# Write a program that gets two numbers, divide them and prints the results. (Tip: Use exception)

# x = int(eval(input("Enter first number: ")))
# y = int(eval(input("Enter first number: ")))


# try:
#     z = x /y
#     print(z)
# except:
#     print("Error")


# # Regular expression
# import re
# y = "The rain in the country spain"
# m = re.search("rain?", y, re.IGNORECASE)
# print(m)

# # Reading a file

# f = open("C:\\Users\\dasiedu\\Desktop\\Codes\\text.txt", "r")
# x = f.read()  #This will read only 10 characters from X
# print(x)


# f =open("demofile3.txt","w")
# f.write("Woops! I have deleted the content!")
# f.close()

# f = open("myfile.txt", "x") # create
# f = open("myfile.txt", "a") # append
# f = open("myfile.txt", "w") # write

# # OS Manipulation

# # delete a file
# import os
# os.remove("demofile.txt")

# #check if file exist:
# if os.path.exists("demofile.txt"):
#     os.remove("demofile.txt")
# else:
#     print("The file does not exist")


# # Delete folder

# os.remdir("myfolder")

#Write a program that gets an array with length of 10, and calculates its reversed array

# array = []

# for i in range(10):
#     x = int(eval(input(f"Enter numbers {i+1} : ")))
#     array.append(x)
# reversed_array = array[::-1]

# print(reversed_array)

#Write a program that calculates the sum of two arrays with length of 8

# array1 = [1,2,3,4,5,6,7,8]
# array2 = [2,3,4,5,6,7,8,9]


# sum_array = [array1[i] + array2[i] for i in range(8)]
# print(sum_array)

# #Write a program which finds and prints majority element (with the most repetition) in an array with a length of 10.


# # Create a dictionary to store the frequency of each number
# frequency = {}

# # Calculate the frequency of each number
# for num in array:
#     if num in frequency:
#         frequency[num] += 1
#     else:
#         frequency[num] = 1

# # Find the most repeated number
# most_repeated = None
# max_count = 0
# for num in frequency:
#     if frequency[num] > max_count:
#         most_repeated = num
#         max_count = frequency[num]

# # Output the most repeated number
# print("Most repeated number:", most_repeated)


# Get 5 numbers from the user
# Write a program that gets 5 numbers (using loop) and only ptints a message for each one if ir is a 3 - digit number. 

# for i in range(5):
#     num = int(eval(input(f"Enter number {i + 1}: ")))
#     if 100 <= num <= 999:
#         print(f"{num} is a three digit number")


# Write a program that adds to a LinkedList.

class Node:

   def __init__(self, data=None):

         self.data = data

         self.next = None

class LinkedList:
     def __init__(self):
          self.head = None
          self.tail = None
          self.count = 0
          def append(self, data):
                new_node = Node(data)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self.count += 1
                print(f"Added {data} to the list")
                return self.count
          def print_list(self):
                node = self.head
                while node:
                    print(node.data, end=" ")
                    node = node.next
                print()
                return self.count
          def reverse_list(self):
                prev = None
                current = self.head
                while current:
                    next_node = current.next
                    current.next = prev
                    prev = current
                    current = next_node
                self.head = prev
                return self.count
          def find_middle(self):
                slow_ptr = self.head
                fast_ptr = self.head
                while fast_ptr and fast_ptr.next:
                    slow_ptr = slow_ptr.next
                    fast_ptr = fast_ptr.next.next
                return slow_ptr.data
          def delete_node(self, key):
                if self.head is None:
                    return
                if self.head.data == key:
                    self.head = self.head.next
                    self.count -= 1
                    return
                prev = None
                current = self.head
                while current and current.data!= key:
                    prev = current
                    current = current.next
                if current is None:
                    return
                prev.next = current.next
                self.count -= 1
                return self.count
          def delete_duplicates(self):
                if self.head is None:
                    return
                current = self.head
                while current:
                    next_node = current.next
                    while next_node and next_node.data == current.data:
                        next_node = next_node.next
                    current.next = next_node
                    current = next_node
                return self.count
          def merge_lists(self, other_list):
                if self.head is None:
                    self.head = other_list.head
                    self.tail = other_list.tail
                    self.count += other_list.count
                    return
                self.tail.next = other_list.head
                self.tail = other_list.tail
                self.count += other_list.count
                return self.count


