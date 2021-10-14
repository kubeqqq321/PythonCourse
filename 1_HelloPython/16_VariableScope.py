# scope - the region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version od a variable can be created


name = "Jakub"      #global scope (available inside & ouside functions)


def display_name():
    name = "JPM"    #local scope (available only iside this function)
    print(name)


display_name()
print(name)

