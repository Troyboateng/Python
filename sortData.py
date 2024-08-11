#sort() method = used with lists
#sort() function = used with iterables

#NB: Tuples - () , List - [] , Set - { },  Dictionary {key:value} 

""" 
students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

#students.sort()

sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)
 """

students = [("Squidward","F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr. Krabs", "C", 78)]

grade = lambda grades:grades[1] #This will pick column [1]
students.sort(key=grade) #This will will sort students by the grade in alphabetical order

for i in students:
    print(i)

student = [("Squidward","F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr. Krabs", "C", 78)]

age = lambda ages:ages[2] #This will pick column 3 [2]
student.sort(key=age) #This will will sort students by the age in alphabetical order

for k in student:
    print(k)

