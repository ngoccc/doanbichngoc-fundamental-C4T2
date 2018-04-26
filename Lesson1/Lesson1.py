from turtle import*
shape("turtle")
speed(0)
for i in range(100):
    for j in range(4):
        forward(100)
        left(90)

    if (i % 6 == 1): color('red')
    if (i % 6 == 2): color('orange')
    if (i % 6 == 3): color('yellow')
    if (i % 6 == 4): color('green')
    if (i % 6 == 5): color('blue')
    if (i % 6 == 0): color('purple')

    left(11)
# for i in range(360):
#     forward(1)
#     left(1)
#     color('red')
n = input("")