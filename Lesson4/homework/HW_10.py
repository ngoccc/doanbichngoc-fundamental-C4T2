import math
from turtle import *

speed(0)
penup()
setposition(-200, 50)
pendown()
#N
left(90)
forward(100)
right(180 - 45)
forward(100 * math.sqrt(2))
left(180 - 45)
forward(100)
penup()
print(position())

#G
setposition (30,130)
pendown()
for i in range(3):
    left(45)
    forward(20*math.sqrt(2))
    left(45)
    forward(60)
left(45)
forward(20*math.sqrt(2))
left(45)
forward(20)
penup()
setposition(10,90)
pendown()
right(90)
forward(40)
penup()

#O
setposition(160, 130)
pendown()
left(90)
for i in range(4):
    left(45)
    forward(20*math.sqrt(2))
    left(45)
    forward(60)
penup()

#C
setposition(290, 130)
pendown()
for i in range(3):
    left(45)
    forward(20*math.sqrt(2))
    left(45)
    forward(60)
left(45)
forward(20*math.sqrt(2))
penup()
#.
setposition(110, 30)

n = input("")
