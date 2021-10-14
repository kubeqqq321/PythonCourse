# str.format - optional method that gives users
#              more  control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {0} jumped over the {1}".format(animal, item))  # positional argument
print("The {1} jumped over the {0}".format(animal, item))
print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword arguments

print("")

text = "The {animal} jumped over the {item}"
print(text.format(animal="lion", item="fence"))

print("")

name = "Jakub"
print("Hello, my name is {}".format(name))
print("Hello, my name is {name:10}. Nice to meet you.".format(name = "JAKUB"))
print("Hello, my name is {:>10}. Nice to meet you.".format(name))
print("Hello, my name is {:<10}. Nice to meet you.".format(name))
print("Hello, my name is {:^10}. Nice to meet you.".format(name))

print("")

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))


