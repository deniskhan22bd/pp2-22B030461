import math

class Point:
    x = None
    y = None
    new_x = None
    new_y = None


    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Your coordinate: x =", self.x, "y =", self.y)
    
    def move(self):
        print("Your move:")
        self.new_x = int(input("x = ")) + self.x
        self.new_y = int(input("y = ")) + self.y
        print("new x =", self.new_x, "new y =", self.new_y)

    def dist(self):
        self.d = math.sqrt((self.new_x - self.x) ** 2 + (self.new_y - self.y) ** 2)
        print("distance =",self.d)
        

a = Point(10, 3)
a.show()
a.move()
a.dist()