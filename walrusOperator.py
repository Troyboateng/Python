#walrus operator :=
#assignment expression aka walrus operator
#assigns values to variables as part of a larger expression

#happy = True
#print(happy)

 #above code can be done using walrus

#print(happy := True)

""" foods = list()
while True:
    food = input("What food do you like? : ")
    if food == "quit":
        break
    foods.append(food) """

#using walrus for the above code

foods = list()
while food := input("What food do you like? : ") != "quit":
    foods.append(food)

