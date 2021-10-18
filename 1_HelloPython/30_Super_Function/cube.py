from rectangle import Rectangle


class Cube(Rectangle):

    height = 0

    # def __init__(self, Cube_length, Cube_width , Cube_height):
    #     self.length = Cube_length
    #     self.width = Cube_width
    #     self.height= Cube_height

    def __init__(self, Cube_length, Cube_width, Cube_height):
        super().__init__(Cube_length,Cube_width)
        self.height = Cube_height

    def volume(self):
        return self.height * self.width * self.length
