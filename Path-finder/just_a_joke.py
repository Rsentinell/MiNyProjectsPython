# import curses
# from curses import wrapper
#
#
# def main(stdscr):
#     stdscr.clear()
#     stdscr.addstr(0, 5, "Hello world!")
#     stdscr.refresh()
#     stdscr.getch()
#

number = {24, 40, 12, 39, 19, 45, 16}
count = 0
print(number)
for numO in number:
    for index, numI in enumerate(number):
        count += 1
        if numO < numI:
            temp = numO
            number[index] = 0

# wrapper(main)
