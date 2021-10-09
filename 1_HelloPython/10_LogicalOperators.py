#logical operators (and ,or , not) -used to check if two or more conditional statements is true

temp = float(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside")
elif temp <0 or temp>30:
    print("the temperature is bad today")
    print("stay inside")

print("--------------------")

if not(temp >= 0 and temp <= 30):
    print("the temperature is good today")
    print("go outside")
elif not(temp <0 or temp>30):
    print("the temperature is bad today")
    print("stay inside")