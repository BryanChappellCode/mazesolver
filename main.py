from window import Window
from point import Point
from line import Line

def main():

    win = Window(800, 600)

    point_one = Point()
    point_one.x = 0
    point_one.y = 0

    point_two = Point()
    point_two.x = 800
    point_two.y = 600

    line_one = Line(point_one, point_two)

    win.draw_line(line_one, "red")

    win.wait_for_close()


if __name__ == "__main__":
    main()