class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, l, w):
        self.lenght=l
        self.width=w

    def area(self):
        return self.lenght*self.width

rct=Rectangle(5,9)
print(rct.area())