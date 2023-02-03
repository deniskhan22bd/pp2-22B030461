class Shape:
    def area(self):
        pass

class Square(Shape):
    lenght = None
    def __init__(self, lenght = 0):
        self.lenght = lenght
        self.area()

    def area(self):
        print(self.lenght * self.lenght)
    
s1 = Square()
s2 = Square(10)