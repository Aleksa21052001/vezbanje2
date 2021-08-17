import turtle


def create_turtle(x, y):
    t = turtle.Turtle()

    t.shape('turtle')
    t.color('green')
    t.penup()
    t.goto(x, y)

    return t


def create_turtles_corner(width, height):
    t1 = create_turtle(-width/2, height/2)
    t2 = create_turtle(-width / 2, -height/2)
    t3 = create_turtle(width / 2, height/2)
    t4 = create_turtle(width / 2, -height/2)


screen = turtle.Screen()
screen.setup(550, 550)
create_turtles_corner(500, 500)
screen.exitonclick()
