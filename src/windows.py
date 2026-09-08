
import curses


def home_window(stdscr) -> None:
    stdscr.clear()
    stdscr.addstr("Welcome to qwerty!")
    stdscr.addstr("\nPlease press any key to continue")
    stdscr.refresh()
    stdscr.getkey()
