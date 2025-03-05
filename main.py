from Window import Window
from Point import *
from Line import *
from Cell import *
from Maze import *

def main():
    win = Window(800, 600)
    num_cols = 12
    num_rows = 10
    m1 = Maze(10, 10, num_rows, num_cols, 20, 20,win)
    m1.solve()
    win.wait_for_close()


main()