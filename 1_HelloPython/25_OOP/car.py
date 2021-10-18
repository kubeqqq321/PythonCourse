
class Car:

    wheels = 4  #class variable

    def __init__(self, fmake, fmodel, fyear, fcolor): #konstruktor
        self.make = fmake       #instance variable
        self.model = fmodel     #instance variable
        self.year = fyear       #instance variable
        self.color = fcolor     #instance variable

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


