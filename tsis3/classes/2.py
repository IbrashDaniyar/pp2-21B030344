class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.lenght=int(input())

    def area(self):
        return self.lenght*self.lenght

sqr=Square()
print(sqr.area())