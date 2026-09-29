
class Window:
    def __init__(self, num_rows: int, num_cols: int, row: int = 0, col: int = 0):
        self.num_rows = num_rows
        self.num_cols =  num_cols
        self.row = row
        self.col = col


    @property
    def bottom(self):
        # return the iindex of the last visible line of the window
        return self.row + (self.num_rows - 1)

    def scroll_up(self, cursor: object):
        if cursor.row == self.row - 1 and self.row > 0:
            self.row -= 1
    def scroll_down(self, cursor: object, buffer: str):
        if cursor.row == self.bottom + 1 and self.bottom < buffer.bottom:
            self.row += 1
    
    
    def translate(self, cursor: object):
        return (cursor.row - self.row, cursor.col - self.col)


    def horizontal_scroll(self, cursor: object):
        left_margin = 5
        right_margin = 2
        visible_cols_per_page = self.num_cols - left_margin - right_margin

        current_cursor_page = cursor.col // max(visible_cols_per_page, 1)
        self.col = max(current_cursor_page * visible_cols_per_page  - left_margin, 0)