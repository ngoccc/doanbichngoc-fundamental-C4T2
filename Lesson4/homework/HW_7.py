class Rectangle:

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.height * self.width


a = Rectangle(10, 50)
print(a.area())
