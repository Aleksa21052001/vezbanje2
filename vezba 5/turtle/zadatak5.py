import turtle


def create_turtle(x, y, shape='turtle', color='green'):
    t = turtle.Turtle()

    t.shape(shape)
    t.color(color)
    t.penup()
    t.goto(x, y)

    return t


screen = turtle.Screen()

t1 = create_turtle(200, -200, 'square', 'red')
t2 = create_turtle(-200, 200, 'circle', 'black')
t3 = create_turtle(200, 200, color='orange')
t4 = create_turtle(-200, -200)

screen.exitonclick()
