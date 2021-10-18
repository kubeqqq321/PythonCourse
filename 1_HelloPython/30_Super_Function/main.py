# super() - Function used to give access to the methods of a parent class.
#           Returns a temporary object of a parent class when used

from square import Square
from cube import Cube


sqr = Square(3,3)
cub = Cube(3,3,3)

print("Square area = "+ str(sqr.area()))
print("Cube volume = "+ str(cub.volume()))
