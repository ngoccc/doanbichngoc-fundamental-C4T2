class Rectangle:
    width = 0
    length = 0

    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.length * self.width


a = Rectangle(10, 50)
print(a.area())