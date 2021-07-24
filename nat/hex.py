import time
import turtle


def setup_turtle():
    # setup your turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.shapesize(1)

    # setup your turtle's home
    t.screen.bgcolor("light blue")
    t.screen.title("My Awesome Hexagon")

    return t


# start here
my_turtle = setup_turtle()

my_turtle.setheading(0)


my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

my_turtle.forward(200)
my_turtle.left(60)
time.sleep(1)

time.sleep(3)
