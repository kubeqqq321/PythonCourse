#slicing - create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start:stop:step]

name = "Jakub Marciniak"

first_name = name[:5]
last_name = name[6:]
funky_name = name[::2]
reversed_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

silce = slice(7,-4)     #->start , stop<-
print(website1[silce])
print(website2[silce])




