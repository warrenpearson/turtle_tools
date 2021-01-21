import time
import turtle

# Simple script to allow the transform of a triangle
# by shifting its coordinates by the user-supplied
# x and y values.

# This just sets up the little white screen 
board = turtle.Turtle()

# TODO: draw a quadrant
# TODO: express the transform as (x,y)

def draw_a_triangle(): 
  # draw a line of length 100
  board.forward(100)
  time.sleep(0.5)

  # rotate the arrow through 120 degrees left
  board.left(120)
  time.sleep(0.5)

  board.forward(100)
  time.sleep(0.5)
 
  board.left(120)
  time.sleep(0.5)

  board.forward(100)
  time.sleep(0.5)

draw_a_triangle() 
board.left(120)

board.penup()
x = input("How much x should I add? ")
board.forward(int(x))

board.left(90)

y = input("How much y should I add? ")
board.forward(int(y))

board.right(90)
 
board.pendown()

draw_a_triangle()
 
turtle.done()
