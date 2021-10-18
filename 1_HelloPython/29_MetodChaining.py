# method chaining - calling multiple methods sequentially
#                  each call performs an action on the same object and return self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the break")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car() #tworzymy obiekt Car

car.turn_on()
car.drive()
print("--------------------------")
car.turn_on().drive()
print("--------------------------")
car.turn_on().drive().brake().turn_off()
print("--------------------------")
car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()

