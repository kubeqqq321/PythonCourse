# while loop - a statement that will execute is's block of code,
#               as long as it's condition remains true

print("----------------------------")

x = 0
y = 10
while x<y:
    x+=1
    name= print(str(x)+". Hello I'm stuck in a loop!")

print("----------------------------")

name = ""
while len(name) == 0:
#while not name:
    name=input("Enter your name: ")

print("Hello " + name)

print("----------------------------")


import time
#for loop - a statement that will execute it's block of code 
#           a limited amount of times
#
#           while loop = unlimited
#           for loop = limited

for i in range(10):
    print(i+1)

print("----------------------------")

for i in range(50 , 100,2 ): #start , koniec , przesuniecie
    print(i+1)

print("----------------------------")

for i in "Jakub Marciniak":
    print(i)

print("----------------------------")

for seconds in range(10,0, -1):
    print(seconds)
    time.sleep(1)

print("Happy New Year")

print("----------------------------")



#nested loops - the "inner loop" will finish all of it's iterations before
#               finishing one iteration of "outer loop"

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter the symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print()



