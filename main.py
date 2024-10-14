from window import Window
from point import Point
from line import Line
from cell import Cell
from constants import CELL_WIDTH, GRID_SIZE

def main():

    win = Window(800, 600)

    grid = []

    for i in range(1, GRID_SIZE + 1):
        row = []
        for j in range(1, GRID_SIZE + 1):
            row.append(Cell(j * CELL_WIDTH, i * CELL_WIDTH, j * CELL_WIDTH + CELL_WIDTH, i * CELL_WIDTH + CELL_WIDTH))
            
        grid.append(row)

 
    for row in grid:
        for cell in row:
            win.draw_cell(cell)
    

    win.wait_for_close()


if __name__ == "__main__":
    main()