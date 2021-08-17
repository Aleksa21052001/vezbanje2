import turtle

screen = turtle.Screen()
screen.setup(750, 750)

my_turtle = turtle.Turtle()

my_turtle.shape('turtle')
my_turtle.color('green')


def move_up():
    x, y = my_turtle.pos()
    my_turtle.goto(x, y+10)


def move_down():
    x, y = my_turtle.pos()
    my_turtle.goto(x, y-10)


def move_left():
    x, y = my_turtle.pos()
    my_turtle.goto(x-10, y)


def move_right():
    x, y = my_turtle.pos()
    my_turtle.goto(x+10, y)


screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

screen.listen()
screen.exitonclick()
