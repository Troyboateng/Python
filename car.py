class Car:

    wheels = 4     #class variables


    def __init__(self, make, model, year, color):  #Constructor
            self.make = make  #Instance variable
            self.model = model  #Instance variable
            self.year = year  #Instance variable
            self.color = color  #Instance variable

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")



