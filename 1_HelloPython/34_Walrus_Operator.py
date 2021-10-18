# Walrus Operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression


# happy = True
# print(happy)

# print(happy=True) #źle
print(happy := True)


# foods = list()
# while True:
#     food = input("Enter food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while food := input("Enter food do you like?: ") != "quit":
    foods.append(food)
