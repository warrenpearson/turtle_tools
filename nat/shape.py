import time
from my_turtle import setup_turtle

# start here
my_turtle = setup_turtle()

counter = 0
length = 30
sides = 40
angle = 360 / sides

while counter < sides:
    my_turtle.forward(length)
    my_turtle.left(angle)
    counter = counter + 1
    time.sleep(1)

time.sleep(3)
