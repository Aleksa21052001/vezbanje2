import turtle


def create_window(file_path):
    f = open(file_path)
    config = f.read()
    f.close()

    config_data = config.split(",")

    screen = turtle.Screen()
    screen.title(config_data[2])
    screen.setup(int(config_data[0]), int(config_data[1]))

    return  screen


screen = create_window("window_config.txt")
screen.exitonclick()
