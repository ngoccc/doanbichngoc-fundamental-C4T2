from turtle import *


# [1]
def Print_Out():
    for i in range(3):
        print("Hello world")


# [2]
def Sum(a, b):
    print(a + b)


# [3]
def Draw_Square(Length, Color):
    color(Color)
    for i in range(4):
        forward(Length)
        left(90)


# [5]
def Draw_Star(x, y, length):
    penup()
    setpos(x, y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)


# [7]
def Remove_Dollar_Sign(s):
    return s.replace("$", "")


# [9]
def Get_Even_List(l):
    return [x for x in l if x % 2 == 0]


# [10]
def Is_Inside(l1, l2):
    return l2[0] <= l1[0] <= l2[0] + l2[2] and l2[1] <= l1[1] <= l2[3]

