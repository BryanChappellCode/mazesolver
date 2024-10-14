from tkinter import Tk, BOTH, Canvas
from line import Line
from cell import Cell

class Window():

    def __init__(self, width , height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title = "Root Widget"
        self.canvas = Canvas()
        self.canvas.pack()
        self.window_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):

        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.window_running = True

        while self.window_running:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_cell(self, cell: Cell, fill_color="black"):

        cell.draw(self.canvas, fill_color)


