
class Window:
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols =  num_cols
        self.row = 0
        self.col = 0


    @property
    def bottom(self):
        # return the total visible lines of the window
        return self.row + (self.num_rows - 1)

    def scroll_up(self, cursor: object):
        if cursor.row == self.row - 1 and self.row > 0:
            self.row -= 1
    def scroll_down(self, cursor: object, buffer: str):
        if cursor.row == self.bottom + 1 and self.bottom < len(buffer) - 1:
            self.row += 1
    
    
    def translate(self, cursor: object):
        return (cursor.row - self.row, cursor.col - self.col)