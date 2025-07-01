Computer Software Fundamentals

Developing an Algorithm

Practice:
An algorithm to calculate the area of a rectangle

Answer: 
Start
Input A # as the length of the rectangle
Input B # as the width of the rectangle
Multiply A and B and store the area in C
Return C
End

Program:
length = 3
width = 4
area = length * width
print(area)

An algorithm to calculate the factorial of a number

Answer:
Start
Input A # desired number 
Calculate the factorial of A! by A * (A-1) * (A-2) * … * 1 saving as B
Return B
End

Types of Algorithm

Brute Force Algo
Benefits
Simple but not suitable for complex problems
Recursive Algo 
the function used will recursively call itself directly or indirectly
Benefits
Can solve certain problems quite easily
Backtracking Algo  
They are like problem-solving strategies that help explore different options for the best solution. They work by trying out different paths; if one doesn't work, they backtrack and try another until they find the right one. It's like solving a puzzle by testing different pieces until they fit together perfectly.

Searching Algo
		They are used to locate specific items within a collection of data.

Sorting Algo
They are used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of elements in the respective data structure.
NB: Indexes return “- 1” if what is indexed does not exist.

Divide and Conquer Algo
		This algo breaks a problem into sub-problems, solves a single sub-problem 
		and merge the solutions to get the final solutions.
	Benefits:
		It's used to break the complexity of a problem
Greedy Algorithm
	In this type of algorithm, the solution is built part by part. The solution for the next part is built based on immediate benefit of the next part. The one solution …
Dynamic Programming Algorithm
	This algo uses the concept of using existing solutions to avoid repetitive calculation of the same part of the problem. It divides the problem into smaller overlapping subproblems and solves them. NB: This uses/needs memory to function.

How to design an Algorithm

The problem that is to be solved by this algo i.e. clearly defined.
The constraints of the problem must be considered while solving the problem
The input to be taken to solve the problem - You have to know the input
The output to be expected when the problem is solved.
The solution to this problem is within the given constraints - Consider the given constraints in solving the problem.
Example
Consider the example to add three numbers and print the sum.
Answer:
Option A
Start
InputA the first number
InputB the second number
InputC the third number
Add the three numbers in Input(A, B, C) and save the result in D
Print D
End

Option B
Start
InputA the three numbers as num1, num2, num3
Add the three numbers saving result in B
Print D
End


Testing the Algorithm by implementing it

Develop the algorithm
Convert  the algorithm into a program
Run the code to test - Testing the Algorithm

Problem

Consider 10 numbers. Find the maximum value among these numbers and print it. Write an algorithm for this problem

Solution:
Start
Set i to 1
Set max to 0
Input a number as B
If B is greater than max then set max as the number
Increase i by one
If i <= 10 then goto step 4
Print max
End 


Chapter 2

My First python program - Hello world

Topic: Python Variables, Casting, Get the type, Case sensitive, Python Variable naming rules,legal and illegal variable names.

Variables
X = 5
Y = “John”
print(x)
print(y)

Exercise:
Write an algorithm and a program that changes the values of two variables.

Algorithm:

Start
Start
Input A
Input B
Set A to X
Set B to A
Set X to B
End

Converting to a Program

A = 5
B = 7
X = A
B = A
X = B
print(A)
print(B)

Assignment 1

Algorithm to print Fibonacci

Start
Set initial values of a = 0, b = 1 and c = 0
Print  a and b
Update the value of c  = a + b
Set the current value of  a = b
Set the current value of b = c
Print c
If c  < 100 repeat step 4
End

Second Option
Start
Set initial values of a = 1, b = 1 and set fib (c = 0)
Print values in a and b
Calculate c by adding a and b, store the result in c (as the next fibonacci number)
If  c is less than 100
Print c
Set the current value of  a = b
Set the current value of b = c
Recalculate the next c = a + b
Repeat step 5
End

Start
Set initial values: x = 1, y = 1
Print x, print y
Calculate n by adding x and y and store the result in n as the fib
While  n is less than 100, print n   
Update x = y
Update y = n
Update n by adding x and y.
End

#code for fibonacci


a = b = 1
while( a <= 100):
    print(a)
    fib = a + b
    a = b
    b = fib

Write an algorithm and a program that shows whether A is divisible by B or not.
Start
Initialize A and B
A modulo (%) B and store the remainder in C
If C = 0, output A is divisible by B.
End
Write an algorithm and a program that takes n numbers from the input and prints the number of positive, negative, and zero numbers.
Start
Input N as the number of n
Initialize x = 0, y = 0, z = 0, u = 0
Input B as the value
If B >0 add 1 to x
If B is < 0 add 1 to y
If B = 0 add 1 to z
Increase u by 1
If u < n repeat step 4
Print the value of x - number of positives, y number of negatives and z - number of zeros
Stop
Converting to Program
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

Write a program that shows the even numbers between 1 and 20
Start
Set n = 1
Find the modulo of n and set to x
If x equal 0 print  n
Increase n by 1
If n <= 20 repeat setp c
Stop
Code
for i in range(1, 20):
    if i % 2 == 0:
        print(i)

Code 2:

for i in range(19):
    if i == 0: continue
    if i % 2 == 0:
        print(i)



Algorithm for GCD
Start
Input two positive integers, num1 and num2
Set num1 = num2
Set num2 = num1 % num2
If num2 is not equal to 0 repeat step 2
Print num1 as the GCD
Code;

a = int(input("Enter num1:"))
b = int(input("Enter num2: "))
while b != 0:
    a, b = b, a % b
print(a)





Compound Interest

Start
Set initial value 10,00 to x
Set rate 7% to y
Set target amount z = 10,000 x 2
Set current amount a = x
Set years b = 0
Current amount a = a*(1+y)
Increase b by 1
If a < z repeat step 7
