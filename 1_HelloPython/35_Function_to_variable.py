def hello():
    print ("hello")

print("-----------------------")
hello()
print("-----------------------")
print(hello)
hi = hello        # Przypisujemy adres funkcji hello do hi taki jakby wskaźnik
print(hi)
print("-----------------------")
hi1 = hello
hi1()


print("-----------------------")
say = print     # say ma taki sam adres jak funkcia print czyli może to samo jak print()
say("Whoa! I can't believe this works :O")
say(1+2)

