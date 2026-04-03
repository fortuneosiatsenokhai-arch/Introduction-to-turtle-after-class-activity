import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
pen=turtle.Turtle()
sides=5
angle=72
length=100
for i in range(sides):
    pen.forward(length)
    pen.left(angle)
turtle.done()