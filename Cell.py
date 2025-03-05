from Point import *
from Line import *

class Cell():

    def __init__(self, p1, p2, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = p1.x
        self.x2 = p2.x
        self.y1 = p1.y
        self.y2 = p2.y
        self.win = win
        self.visited = False

    def draw(self):
        if self.has_left_wall:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x1,self.y2)),"black")
        else:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x1,self.y2)),"#d9d9d9")
        if self.has_right_wall:
            self.win.draw_line(Line(Point(self.x2,self.y1),Point(self.x2,self.y2)),"black")
        else:
            self.win.draw_line(Line(Point(self.x2,self.y1),Point(self.x2,self.y2)),"#d9d9d9")
        if self.has_top_wall:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x2,self.y1)),"black")
        else:
            self.win.draw_line(Line(Point(self.x1,self.y1),Point(self.x2,self.y1)),"#d9d9d9")
        if self.has_bottom_wall:
            self.win.draw_line(Line(Point(self.x1,self.y2),Point(self.x2,self.y2)),"black")
        else:
            self.win.draw_line(Line(Point(self.x1,self.y2),Point(self.x2,self.y2)),"#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        if undo:
            self.win.draw_line(Line(self.get_center(),to_cell.get_center()),"gray")
        else:
            self.win.draw_line(Line(self.get_center(),to_cell.get_center()),"red")

    def get_center(self):
        return Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2 )
    