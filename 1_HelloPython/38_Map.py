# ---------------------------------------------------------------------------------------------------------------
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)


store_euros = [("shirt", 20.00),
               ("pants", 25.00),
               ("jacket", 50.00),
               ("socks", 10.00)]

to_zloty = lambda data: (data[0], data[1] * 4.59)
to_dollar = lambda data: (data[0], data[1] * 1.16)

store_pln = list(map(to_zloty, store_euros))
store_dollar = list(map(to_dollar, store_euros))

for i in store_pln:
    print(i)

print("-----------------------------------")

for i in store_dollar:
    print(i)
