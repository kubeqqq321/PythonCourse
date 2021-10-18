# multiple inheritance - when a child class is derived from than one parent class

class Prey:    #ofiara

    def flee(self):             #uciekać
        return "This animal flees"


class Predator:     # lowca

    def hunt(self):
        return "This animal is hunting"



class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey , Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

print("rabbit.flee(): " + str(rabbit.flee()))
print("hawk.hunt(): " +str(hawk.hunt()))
print("fish.hunt(): " +str(fish.hunt()))
print("fish.flee(): " +str(fish.flee()))








