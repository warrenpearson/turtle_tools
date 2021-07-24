import turtle


def setup_turtle():
    # setup your turtle
    t = turtle.Turtle()

    t.shape("turtle")
    t.shapesize(1)

    # setup your turtle's home
    s = t.getscreen()
    s.bgcolor("light pink")
    s.title("My Awesome Shape")

    t.penup()
    t.setx(-50)
    t.sety(-300)
    t.setheading(0)
    t.pendown()

    return t
