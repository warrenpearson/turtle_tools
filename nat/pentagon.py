import time
from my_turtle import setup_turtle

# start here
my_turtle = setup_turtle()

counter = 0

while counter < 5:
    my_turtle.forward(200)
    my_turtle.left(72)
    counter = counter + 1
    time.sleep(1)

time.sleep(3)
