
import curses

from console_explorer import browse_for_file


def home_window(stdscr) -> None:
    stdscr.clear()
    stdscr.addstr("Welcome to qwerty!")
    stdscr.addstr("\n\nWould you like to open an existing file?")
    stdscr.addstr("\nPress O to open an existing file\nPress any other key to open a new file")
    stdscr.refresh()

    while True:
        key = stdscr.getkey()

        if key == 'O' or 'o':
            # temporarily return to shell-terminal
            curses.def_prog_mode()
            curses.reset_shell_mode()
            file_path = choose_file_window(stdscr)
            curses.reset_prog_mode()
            break
        else:
            file_path = None
            break


def choose_file_window(stdscr):
    return browse_for_file(existence_required=True)