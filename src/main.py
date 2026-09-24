
import curses

from screen import welcome_screen, file_selector


def main(stdscr) -> None:
    welcome_screen(stdscr)
    file_path = file_selector(stdscr)


if __name__ == "__main__":
    curses.wrapper(main)
