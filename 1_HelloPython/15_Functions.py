#function - a block of code which is executed only when it is called

def hello(ffirst_name,flast_name, fage):
    print("Hello " + ffirst_name + " " + flast_name)
    print("You are " + str(fage) + " years old")
    print("Have a nice day! ")

first_name = input("What is your name?: ")
last_name = input("What is your surname?:")
age = int(input("How old are you?:"))

hello(first_name, last_name, age)


#return statement - Functions send Python values/objects back to the caller.
#                   These values/objects are known as the function's return value

def multiply(number1 , number2):
    # result = number1*number2
    # return result
    return number1*number2


x = multiply(6,8)
print(x)

print(multiply(6, 8))



#keyword arguments - arguments preceded by an identifiler when we pass them to a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    Python knows the names of the arguments that our function receives


def FML(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)


FML(middle="Jakub", last="Marciniak", first=" Dude")


# nested function calls - function calls inside other function calls innermost
#                         function calls are resolved first returned value is used as
#                         argument for the next other function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num round(num)
# print(num)

#  ||

print(round(abs(float(input("Enter a whole number: ")))))






