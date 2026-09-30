
import curses

from window import Window

from cursor import Cursor

from buffer import Buffer


def move_right(cursor: object, buffer: object, window: object):
    cursor.right(buffer)
    window.scroll_down(cursor, buffer)
    window.horizontal_scroll(cursor)


def editor(stdscr, file_path: str | None) -> None:
    if file_path is None:
        file_path = "Untitled.py"
        buffer = Buffer([])
    else:
            with open(file_path, 'r') as file:
                buffer = Buffer(file.read().splitlines())

    window = Window(curses.LINES - 1, curses.COLS - 1)
    cursor = Cursor(0, 0)

    while True:
        stdscr.erase()

        for row, line in enumerate(buffer[window.row: window.row + window.num_rows]):
            if row == cursor.row - window.row and window.col > 0:
                line = '←' + line[window.col + 1:]
            if len(line) > window.num_cols:
                line = line[:window.num_cols - 1] + '→'
            stdscr.addstr(row, 0, line)

        stdscr.move(*window.translate(cursor))

        key = stdscr.getkey()

        if key == "KEY_F(1)":
            break

        elif key == "KEY_UP":
            cursor.up(buffer)
            window.scroll_up(cursor)
            window.horizontal_scroll(cursor)
        elif key == "KEY_LEFT":
            cursor.left(buffer)
            window.scroll_up(cursor)
            window.horizontal_scroll(cursor)
        elif key == "KEY_RIGHT":
            if buffer.lines != []:
                move_right(cursor, buffer, window)
        elif key == "KEY_DOWN":
            cursor.down(buffer)
            window.scroll_down(cursor, buffer)
            window.horizontal_scroll(cursor)

        elif key in ("\n", "\r"):
            buffer.split(cursor)
            move_right(cursor, buffer, window)
        elif key in ("KEY_DELETE", "\x04"):
            buffer.delete(cursor)

        else:
            if len(key) < 3 and ord(key) == 27:
                raise SystemExit(0)
            buffer.insert(cursor, key)
            
            for character in key:
                move_right(cursor, buffer, window)
        
        
        stdscr.refresh()

    # implement saving logic
