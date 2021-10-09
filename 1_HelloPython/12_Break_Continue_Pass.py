#Loop control statements - change a loop execution from its normal sequence
#
# break =       used to terminate the loop entirely
# continue =    skip to te next iteration of the loop
# pass =        does nothing, acts as a placeholder

#break
while True:
    name = input("Enter your name: ")
    if name != "":
        print(name)
        break

print("-----------------------------")

#continue
phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        continue
    print(i,end="")
    
print("")
print("-----------------------------")

#pass
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)




