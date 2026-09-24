
import curses

from console_explorer import browse_for_file


def welcome_screen(stdscr) -> None:
    stdscr.erase()
    stdscr.addstr("\n    Welcome to qwerty!")
    stdscr.refresh()


def file_selector(stdscr) -> str:
    stdscr.addstr("\n\nWould you like to open an existing file?")
    stdscr.addstr("\nPress O to open an existing file\nPress any other key to open a new file")
    stdscr.refresh()

    while True:
        key = stdscr.getkey()

        if key in ('O', 'o'):
            # temporarily return to shell-terminal
            curses.def_prog_mode()
            curses.reset_shell_mode()
            file_path = choose_file_window(stdscr)
            curses.reset_prog_mode()
            break
        else:
            file_path = None
            break
    return file_path


def choose_file_window(stdscr):
    return browse_for_file(existence_required=True)