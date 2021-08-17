import turtle


def create_window(window_name, width, height):
    screen = turtle.Screen()
    screen.title(window_name)
    screen.setup(width, height)
    screen.exitonclick()


create_window("MyWindow", 400, 350)
