
import curses

from windows import home_window

def main(stdscr) -> None:
    file_path = home_window(stdscr)




if __name__ == "__main__":
    curses.wrapper(main)
