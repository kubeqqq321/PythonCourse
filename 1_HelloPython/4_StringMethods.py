name = "Jakub Marciniak"

print(len(name))                #pokazuje dlugosc name
print(name.find("r"))           #pokazuje index na którym występuje szukana literka
print(name.capitalize())        #powiększa pierwsza litere jak w zdaniu
print(name.upper())             #zamienia litery na duże
print(name.lower())             #zamienia litery na małe
print(name.isdigit())           #jeżeli nasz string jest liczbą tzn "123" = True jeżeli jednak litery będzie to False
print(name.isalpha())           #sprawdza czy string jest bez żadnych liczb
print(name.count("k"))          #liczy ile w stringu występuje dana wartość
print(name.replace("a" , "u"))  #zamienia w stringu coś na coś
print(name*3)                   #wyświetla string kilka razy