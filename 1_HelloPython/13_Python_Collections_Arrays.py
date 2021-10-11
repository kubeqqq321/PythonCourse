# list = used to store multiple items in a single variable
print("~~~~~~~~~~~~~~~~~~")
print("list")
print("~~~~~~~~~~~~~~~~~~")
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

print(food)

food[0] = "sushi"

print("------------------------------")
for x in food:
    print(x)

food.append("ice cream")        #dodaje do listy element
food.remove("hotdog")           #usuwa podany element
food.pop()                      #przenosi ostatni element na pierwszą pozycje
food.insert(0,"cake")           #dodaje element na odpowiedni indeks
food.sort()                     #sortuje alfabetycznie liste
#food.clear()                   #usuwa wszytskie elementy w liście
print("------------------------------")
print(food)
print("------------------------------")
#2D lists - a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

foods = [drinks, dinner, dessert]
print(foods)
print(foods[0][2])
print("------------------------------")





#tuple(krotka) - collection which is ordered and unchangeable used to group
#                together related data
print("~~~~~~~~~~~~~~~~~~")
print("Tuple")
print("~~~~~~~~~~~~~~~~~~")
student = ("Jakub" , 21 , "male")

print(student.count("Jakub"))           #zlicza ile razy występyje dana liczba czy string
print(student.index("male"))            #pokazuje podany index w tuple

print("------------------------------")

for i in student:
    print(i)

print("------------------------------")

if "Jakub" in student:
    print(student[0] + " is here")

print("------------------------------")





#set - collection which is unordered, unindexed. No duplicate values
print("~~~~~~~~~~~~~~~~~~")
print("set")
print("~~~~~~~~~~~~~~~~~~")

utensils = {"fork", "spoon", "knife"}       #narzędzia, przyrządy
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# #utensils.clear()
# utensils.update(dishes)             #dodanie jednego set do drugiego

dinner_table = utensils.union(dishes)

for i in dinner_table:
    print(i)

print("------------------------------")
print(utensils.difference(dishes))      #sprawda czego nie ma w set dishes a co jest w utensils
print("------------------------------")
print(utensils.intersection(dishes))    #sprawdza elementy które się powtarzają






#dictionary - A changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly
#jest szybkie ponieważ używamy tu hashowania poprzez klucz i wartość

print("~~~~~~~~~~~~~~~~~~")
print("dictionary")
print("~~~~~~~~~~~~~~~~~~")

            #klucz : wartość
capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany' : 'Berlin'})
print(capitals.get('Germany'))
print("------------------------------")

capitals.update({'USA' : "Las Vegas"})
print(capitals.get('USA'))
print("------------------------------")

#capitals.pop('China')               #usuwa wybrany przez nas klucz razem z wartością która posiada
#capitals.clear()                    #usuaw wszytsko

print("------------------------------")


print(capitals['Russia'])               #wyświetlamy daną wartość poprzez jej klucz
print(capitals.get('Germany'))          #sprawdzamy czy dany klucz znajduje się w capitals
print(capitals.keys())                  #wyswietla klucze
print(capitals.values())                #wyświetla wartości
print(capitals.items())                 #pokazuje klucze razem z wartościami

print("------------------------------")

for key, value in capitals.items():
    print(key+" : "+value)

print("------------------------------")


