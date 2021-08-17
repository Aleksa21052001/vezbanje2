import turtle


def create_turtle(x, y):
    t = turtle.Turtle()

    t.shape('turtle')
    t.color('green')
    t.penup()
    t.goto(x, y)

    return t


screen = turtle.Screen()
create_turtle(100,200)
screen.exitonclick()
