import turtle


def create_window(window_name):
    screen = turtle.Screen()
    screen.title(window_name)
    screen.setup(200, 400)
    screen.exitonclick()


create_window("MyWindow")
