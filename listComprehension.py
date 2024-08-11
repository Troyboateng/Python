# list comprehension, a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]

squares = []
for i in range(1,11):
    squares.append(i*i)
print(squares)

#Above code can be rewritten with fewer lines using list comp
squares = [i * i for i in range(1,11)]
print(squares)

students = [100,90,80,70,60,50,40,30,20,10]
passed_students = list(filter(lambda x: x>=60, students))
print(passed_students)

passed = [k for k in students if k >=60]
print(passed)

passed1 = [i if i >=60 else "Failed" for i in students]
print(passed1)

