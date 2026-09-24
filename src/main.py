
import curses

from screen import welcome_screen, file_selector

from editor import editor


def main(stdscr) -> None:
    welcome_screen(stdscr)
    file_path = file_selector(stdscr)
    editor(stdscr, file_path)


if __name__ == "__main__":
    curses.wrapper(main)
