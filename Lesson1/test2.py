import turtle

# def init (self, color, pensize, speed):
#     self.color(color)
#     self.pensize(pensize)
#     self.speed(speed)

def star(turtle, n, r):
    """ draw a star of n rays of length d"""
    for k in range(0, n):
        turtle.pendown()
        turtle.forward(r)
        turtle.penup()
        turtle.backward(r)
        turtle.left(360 / n)


def recursive_star(turtle, n, r, depth, f):
    """At each point of the star, draw another smaller star,
    and so on, up to given depth. Rescale the stars by a factor f
    at each generation."""

    if depth == 0:
        star(turtle, n, f * 4)
    else:
        for k in range(0, n):
            turtle.pendown()
            turtle.forward(r)
            recursive_star(turtle, n, f * r, depth - 1, f)
            turtle.penup()
            turtle.backward(r)
            turtle.left(360 / n)

wn = turtle.Screen()
fred = turtle.Turtle()
fred.speed("fastest")
recursive_star(fred, 5, 150, 4, 0.4)
wn.mainloop()