import time
import turtle


def setup_turtle():
    # setup your turtle
    t = turtle.Turtle()

    t.shape("turtle")
    t.shapesize(1)

    # setup your turtle's home
    s = t.getscreen()
    s.bgcolor("light blue")
    s.title("My Awesome Square")
    t.setheading(0)

    return t


# start here
my_turtle = setup_turtle()

my_turtle.forward(200)
my_turtle.left(90)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(90)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(90)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(90)
time.sleep(1)

time.sleep(3)
