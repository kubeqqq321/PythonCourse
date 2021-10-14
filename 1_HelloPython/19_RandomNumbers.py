import random

x = random.randint(1, 6)
y = random.random()
print(x)


mylist = ['rock' , 'paper', "scissors"]
z = random.choice(mylist)
print(z)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)

