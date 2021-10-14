# *args - parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(num1 ,num2):
    sum = num1 + num2
    return sum


def add_arguments(*stuff):
    sum = 0
    stuff = list(stuff)     #jeżeli chcemy zmienic wartości w krotce musimy
    stuff[0] = 0            #musimy zrobić rzutownaie na inny typ np list
    for i in stuff:
        sum += i
    return sum


print(add(4, 5))
print(add_arguments(1, 2, 3, 4, 5, 6, 7, 8))
print("")



# **kwargs - parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amoutnt of keyword arguments

def hello(first , last):
    print("Hello "+first+" "+ last+ " :)")


def helloKwargs(**kwargs):
    print("Hello " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'] + " :)")
    print("Hello" , end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Jakub", last="Marciniak")
print("")
helloKwargs(title="Mr.", first="Jakub", last="Marciniak", middle="Pawel")
