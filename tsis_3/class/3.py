class Shape:
    lenght = None
    width = None
    
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

class Rectangle(Shape):
    def area(self):
        print(self.lenght * self.width)

s = Rectangle(10, 13)
s.area()
