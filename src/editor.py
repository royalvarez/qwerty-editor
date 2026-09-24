
import curses


def editor(stdscr, file_path: str | None) -> None:
    if file_path is None:
        file_path = "Untitled.py"
        buffer = []
    else:
        with open(file_path, 'r') as file:
            text = file.read()
            buffer = text.split("\n")

    while True:
        stdscr.erase()

        for row, line in enumerate(buffer):
            stdscr.addstr(row, 0, line)

        key = stdscr.getkey()

        if key == "KEY_F(1)":
            break
        else:
            if len(key) < 3 and ord(key) == 27:
                raise SystemExit(0)
        stdscr.refresh()

    # implement saving logic
