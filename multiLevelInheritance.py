""" class Organism:
    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")
class Dog(Animal):

    def bark(self):
        print("This dog is barking")

dog=Dog()
print(dog.alive)
dog.eat()
dog.bark()
 """
#Multiple inheritance = when a child class is derived from more than one parent class

""" class Prey:
    def flee(self):
        print("This animal flees")
class Predator:
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt() """


# Method Changing or overriding

""" class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    def eat(self):
        print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()
 """

# Method Chaining - calling multiple methods sequentially
# each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("you start the engine")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on the brake")
        return self
    def turn_off(self):
        print("you turn off the engine")
        return self

car = Car()
car.turn_on().drive() #Method chaining

car.brake().turn_off()

#Nicer way to do method chaining
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()




