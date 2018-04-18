import turtle
wn = turtle.Screen() # Set up the window and its attributes
wn.bgcolor("black")
wn.title("Tess & Alex")

tess = turtle.Turtle() # Create tess and set some attributes
alex = turtle.Turtle()

def init (self, color, pensize, speed):
    self.color(color)
    self.pensize(pensize)
    self.speed(speed)
# def draw(self):
#     for i in range(1000):
#         self.forward(i)
#         self.right(180-60+1)
init(alex, "red", 6, 0)
init(tess, "white", 2, 0)
# draw(alex)
# draw(tess)
# for i in range(1000):
#     alex.forward(i)
#     tess.forward(i)
#     alex.right(180-60+1)
#     tess.right(180-60+1)
# for i in range(1000):
#     alex.circle(50)
#     alex.left(10)
#     tess.circle(50)
#     tess.left(10)
for i in range(100):
    alex.forward(100)
    tess.forward(100)
    alex.left(108)
    tess.left(108)
alex.setposition(60,60)
tess.setposition(60,60)
for i in range(100):
    alex.forward(100)
    tess.forward(100)
    alex.left(100)
    tess.left(100)

wn.mainloop()