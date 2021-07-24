import time
import turtle
import sys


def setup_turtle():
    # setup your turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(1)
    t.screen.screensize(500,500)

    # setup your turtle's home
    t.screen.bgcolor("light blue")
    t.screen.title("My Awesome Square")
    t.penup()
    t.setx(-50)
    t.sety(-300)
    time.sleep(1)
    t.setheading(0)
    t.pendown()


    return t


# start here
my_turtle = setup_turtle()

length = int(sys.argv[1])
sides = int(sys.argv[2])
angle = int(sys.argv[3])

counter = 0

while counter < sides:
    my_turtle.forward(length)
    my_turtle.left(angle)
    counter = counter + 1
    time.sleep(0.2)

time.sleep(3)
