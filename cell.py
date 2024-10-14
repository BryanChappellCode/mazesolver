from line import Line
from point import Point


class Cell:

    def __init__(self, x1, y1, x2, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.top_left_point = Point(self.__x1, self.__y1)
        self.top_right_point = Point(self.__x2, self.__y1)
        self.bottom_right_point = Point(self.__x2, self.__y2)
        self.bottom_left_point = Point(self.__x1, self.__y2)
        self.__win = None

    def draw(self, canvas, fill_color):
        
        if self.has_left_wall:
            Line(self.top_left_point, self.bottom_left_point).draw(canvas, fill_color)

        if self.has_right_wall:
            Line(self.top_right_point, self.bottom_right_point).draw(canvas, fill_color)

        if self.has_top_wall:
            Line(self.top_left_point, self.top_right_point).draw(canvas, fill_color)

        if self.has_bottom_wall:
            Line(self.bottom_left_point, self.bottom_right_point).draw(canvas, fill_color)
        

        