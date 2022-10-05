import curses
from curses import wrapper
import queue
import time

mazeOUT = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", "#", "#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", "#", "#", "#", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#", "#", "#", " ", " ", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]
counter = 0


def print_maze(maze, stdscr, path=[]):
    print(path)
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j*2, "X", RED)
            else:
                stdscr.addstr(i, j*2, value, BLUE)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j

def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        curent_pos, path = q.get()
        row, col = curent_pos

        stdscr.clear()
        # print(mazeOUT)
        print_maze(maze, stdscr, path)
        time.sleep(0.1)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)

def find_neighbors(maze, row, col):
    neighbors = []
    global counter
    counter += 1
    print(counter)


    if row > 0: # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze): # DOWN
        neighbors.append((row + 1, col))
    if col > 0: # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]): # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    find_path(mazeOUT, stdscr)
    stdscr.getch()



wrapper(main)
