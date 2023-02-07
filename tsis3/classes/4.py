import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def show(self):
        return self.x, self.y


    def move(self, x, y):
        self.x += x
        self.y += y


    def dist(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)

p1 = Point(2, 3)
p2 = Point(3, 3)

p1.show()
p2.show()

p1.move(5, -4)
p1.show()

p1.dist(p2)