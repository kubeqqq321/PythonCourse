from rectangle import Rectangle


class Square(Rectangle):
    # def __init__(self,Square_length , Square_width):
    #     self.length = Square_length
    #     self.width = Square_width

    def __init__(self, Square_length, Square_width):
        super().__init__(Square_length, Square_width)

    def area(self): 
        return self.length * self.width
