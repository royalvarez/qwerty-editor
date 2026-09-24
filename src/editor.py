
import curses


def editor(stdscr, file_path: str | None) -> None:
    if file_path is None:
        pass
    else:
        pass
    
    while True:
        stdscr.erase()

        key = stdscr.getkey()

        if key == "KEY_F(1)":
            break
        else:
            if len(key) < 3 and ord(key) == 27:
                raise SystemExit(0)
        stdscr.refresh()

    # implement saving logic
