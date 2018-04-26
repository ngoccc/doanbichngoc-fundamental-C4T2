from Sub_Function import *

speed(0)
color('blue')
for i in range(100):
    import random

    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    Draw_Star(x, y, length)
