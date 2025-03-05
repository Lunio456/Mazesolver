import random
import time
from Cell import *

class Maze():

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self.create_cells()
        self.break_entrance_and_exit()
        if seed is not None:
            random.seed(seed)
        self.break_walls_r(0,0)
        self.reset_cells_visited()

    def create_cells(self):
        for i in range(self.num_cols):
            self.cells.append([])
            for j in range(self.num_rows):
                cell = Cell(Point(self.x1 + self.cell_size_x*i,self.y1 + self.cell_size_y*j),
                                           Point(self.x1 + self.cell_size_x*(i+1),self.y1 + self.cell_size_y*(j+1)),
                                           self.win)
                self.cells[i].append(cell)
                if self.win != None:
                    self.draw_cell(i,j)
    
    def draw_cell(self, i, j):
        self.cells[i][j].draw()
        self.animate()

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].draw()
        self.cells[-1][-1].has_bottom_wall = False
        self.cells[-1][-1].draw()
    
    def animate(self):
        self.win.redraw()
        time.sleep(0.01)

    def break_walls_r(self,i,j):
        self.cells[i][j].visited = True
        while True:
            to_visit = []
            if self.cells[min(i+1,self.num_cols-1)][j].visited == False:
                to_visit.append((i+1,j))
            if self.cells[max(i-1,0)][j].visited == False:
                to_visit.append((i-1,j))
            if self.cells[i][min(j+1,self.num_rows-1)].visited == False:
                to_visit.append((i,j+1))
            if self.cells[i][max(j-1,0)].visited == False:
                to_visit.append((i,j-1))
            if len(to_visit) == 0:
                return
            if len(to_visit) == 1:
                index = 0
            else:
                index = random.randrange(0,len(to_visit),1)
            if to_visit[index][0] > i:
                self.cells[i][j].has_right_wall = False
                self.cells[i+1][j].has_left_wall = False
                self.cells[i][j].draw()
                self.cells[i+1][j].draw()
            if to_visit[index][0] < i:
                self.cells[i][j].has_left_wall = False
                self.cells[i-1][j].has_right_wall = False
                self.cells[i][j].draw()
                self.cells[i-1][j].draw()
            if to_visit[index][1] > j:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j+1].has_top_wall = False
                self.cells[i][j].draw()
                self.cells[i][j+1].draw()
            if to_visit[index][1] < j:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j-1].has_bottom_wall = False
                self.cells[i][j-1].draw()
                self.cells[i][j].draw()
            self.animate()
            self.break_walls_r(to_visit[index][0],to_visit[index][1])
    
    def reset_cells_visited(self):
        for column in self.cells:
            for cell in column:
                cell.visited = False
    
    def solve(self):
        return self.solve_r(0,0)

    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        if self.cells[min(i+1,self.num_cols-1)][j].visited == False and self.cells[i][j].has_right_wall == False:
            self.cells[i][j].draw_move(self.cells[min(i+1,self.num_cols-1)][j])
            if self.solve_r(i+1,j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[min(i+1,self.num_cols-1)][j],True)
        if self.cells[max(i-1,0)][j].visited == False and self.cells[i][j].has_left_wall == False:
            self.cells[i][j].draw_move(self.cells[max(i-1,0)][j])
            if self.solve_r(i-1,j):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[max(i-1,0)][j],True)
        if self.cells[i][min(j+1,self.num_rows-1)].visited == False and self.cells[i][j].has_bottom_wall == False:
            self.cells[i][j].draw_move(self.cells[i][min(j+1,self.num_rows-1)])
            if self.solve_r(i,j+1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][min(j+1,self.num_rows-1)],True)
        if self.cells[i][max(j-1,0)].visited == False and self.cells[i][j].has_top_wall == False:
            self.cells[i][j].draw_move(self.cells[i][max(j-1,0)])
            if self.solve_r(i,j-1):
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][max(j-1,0)],True)
        return False

