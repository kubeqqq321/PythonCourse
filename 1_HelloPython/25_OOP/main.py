from car import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford" , "Mustang" , 2020, "Red")

print("car_1-------------------")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("car_2-------------------")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()

print("--------------------------")

car_1.wheels = 2

print("Car.wheels: "+str(Car.wheels))
print("car_1.wheels: "+str(car_1.wheels))
print("car_2.wheels: "+str(car_2.wheels))
