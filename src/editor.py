
import curses

from window import Window

from cursor import Cursor


def editor(stdscr, file_path: str | None) -> None:
    if file_path is None:
        file_path = "Untitled.py"
        buffer = []
    else:
            with open(file_path, 'r') as file:
                text = file.read()
                buffer = text.split("\n")

    window = Window(curses.LINES - 1, curses.COLS)
    cursor = Cursor(0, 0)

    while True:
        stdscr.erase()

        for row, line in enumerate(buffer[:window.num_rows]):
            stdscr.addstr(row, 0, line[:window.num_cols])

        stdscr.move(cursor.row, cursor.col)

        key = stdscr.getkey()

        if key == "KEY_F(1)":
            break

        elif key == "KEY_UP":
            cursor.up(buffer)
        elif key == "KEY_LEFT":
            cursor.left(buffer)
        elif key == "KEY_RIGHT":
            if buffer != []:
                cursor.right(buffer)
        elif key == "KEY_DOWN":
            cursor.down(buffer)

        else:
            if len(key) < 3 and ord(key) == 27:
                raise SystemExit(0)
        stdscr.refresh()

    # implement saving logic
