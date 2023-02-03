class Shape:
    def area(self):
        pass

class Square(Shape):
    lenght = None
    def __init__(self, lenght):
        self.lenght = lenght
        self.area()

    def area(self):
        print(self.lenght * self.lenght)
    
s = Square(13)
