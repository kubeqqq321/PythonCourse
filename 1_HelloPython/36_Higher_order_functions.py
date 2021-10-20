#  Higher Order Function - a function that either:
#                          1. accepts a function as an argument
#                             or
#                          2. returns a function
#                             (In python, functions are also treated as an objects)

def loud(text):
    return text.upper()

def quite(text):
    return text.lower()

def hello(func):
    txt = func("Hello")
    print(txt)
    
    
hello(loud)
hello(quite)


def divisor(x):
    def dividend(y):
        return y/x
    return dividend


divide = divisor(2)
print(divide(10))
print(divisor(2)(10))   #skrócona wersja

def dodawanie_1(x):
    def dodawanie_2(y):
        return x + y
    return dodawanie_2

sum = dodawanie_1(1)
print(sum(2))

print(dodawanie_1(1)(2))