from math import sqrt

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, val):
        self.width = val

    def set_height(self, val):
        self.height = val

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2*self.height + 2*self.width

    def get_diagonal(self):
        return sqrt((self.height **2) + (self.width ** 2))

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                picture += "*"*self.width + "\n"
            return picture

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def get_amount_inside(self, other):
        dim1 = self.width // other.width
        dim2 = self.height // other.height
        return dim1 * dim2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_width(self, length):
        self.set_height(length)

    def set_height(self, length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self.set_height(length)

    def __str__(self):
        return f"Square(side={self.width})"
