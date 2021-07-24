import time
import turtle


# setup your turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.shapesize(3)

# setup your turtle's home
my_turtle.screen.bgcolor("yellow")
my_turtle.screen.title("My Awesome Turtle")

# # move your turtle a bit
# time.sleep(1)
my_turtle.setheading(0)

my_turtle.forward(200)
my_turtle.setheading(90)
# time.sleep(1)
my_turtle.forward(200)
my_turtle.setheading(180)
# time.sleep(1)
my_turtle.forward(200)
my_turtle.setheading(270)
# time.sleep(1)
my_turtle.forward(200)
#
# # Nat
my_turtle.forward(200)
my_turtle.setheading(45)
my_turtle.forward(200)

my_turtle.setheading(135)
my_turtle.forward(200)

turtle.done()
