'''
Hoang Le
Maze Generator
Depth First Search Recursive Backtracker
https://en.wikipedia.org/wiki/Maze_generation_algorithm
'''

import tkinter as tk
import random
import time

HEIGHT = 800
WIDTH = 800
w = 20
cols = int(WIDTH / w) - 2
rows = int(HEIGHT / w) - 2
grid = None
canvas = None
TOP = 0; LEFT = 1; BOTTOM = 2; RIGHT = 3
N = (-1, 0); E = (0, 1); W = (0, -1); S = (1, 0)
DIRECTIONS = [N, E, W, S]

def run():
    global canvas, grid
    root = tk.Tk()
    root.title("Maze Generator Algorithm")
    canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
    canvas.configure(background = 'gray')
    canvas.pack()
    grid = [[Cell((i,j)) for j in range(rows)] for i in range(cols)]
    createMaze()
    root.mainloop()

def createMaze():
    stack = []
    current = grid[0][0]
    while True:
        for i in range(cols):
            for j in range(rows):
                grid[i][j].display()
        current.visited = True
        current.highlight()
        neighbors = current.unvisited_neighbors()
        if neighbors:
            n = random.choice(neighbors)
            stack.append(current)
            removeWall(current, n)
            current = n
        elif stack:
            current = stack.pop()
        canvas.update()

def removeWall(c1, c2):
    di = c1.position[0] - c2.position[0]
    dj = c1.position[1] - c2.position[1]
    if di == -1:
        c1.walls[RIGHT] = False
        c2.walls[LEFT] = False
    elif di == 1:
        c1.walls[LEFT] = False
        c2.walls[RIGHT] = False

    if dj == -1:
        c1.walls[BOTTOM] = False
        c2.walls[TOP] = False
    elif dj == 1:
        c1.walls[TOP] = False
        c2.walls[BOTTOM] = False

class Cell():

    def __init__(self, position):
        self.position = position
        self.walls = [True, True, True, True]
        self.visited = False

    def display(self):
        i, j = self.position
        i = w + i * w
        j = w + j * w
        canvas.create_rectangle(i, j, i + w, j + w, fill = "pink", outline = "")
        if self.visited:
            canvas.create_rectangle(i, j, i + w, j + w, fill = "white", outline = "")
        if self.walls[TOP]:
            canvas.create_line(i, j, i + w, j, fill = "black", width = 1)
        if self.walls[LEFT]:
            canvas.create_line(i, j, i, j + w, fill = "black", width = 1)
        if self.walls[RIGHT]:
            canvas.create_line(i + w, j, i + w, j + w, fill = "black", width = 1)
        if self.walls[BOTTOM]:
            canvas.create_line(i, j + w, i + w, j + w, fill = "black", width = 1)

    def highlight(self):
        i, j = self.position
        i = w + i * w
        j = w + j * w
        canvas.create_rectangle(i, j, i + w, j + w, fill = "yellow", outline = "")

    def unvisited_neighbors(self):
        n = []
        for direction in DIRECTIONS:
            i = self.position[0] + direction[0]
            j = self.position[1] + direction[1]
            if i in range(0, cols) and j in range(0, rows) and not grid[i][j].visited:
                n.append(grid[i][j])
        return n 
run()
