# class Ten_Class:
# thuoc tinh - variable
# phuong thuc - ham con
# example

class HCN:
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def chuvi(self):
        c = (self.height + self.width) * 2
        return c


# Tao
a1 = HCN(10, 100)
a2 = HCN(30, 100)
print(a1.chuvi())
print(a2.chuvi())
