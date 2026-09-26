
class Cursor:
    def __init__(self, row: int, col: int):
        self.row = row
        self._col = col

    @property
    def col(self):
        return self._col


    @col.setter
    def col(self, col):
        self._col = col


    def up(self, buffer):
        if self.row > 0:
            self.row -= 1
            self._col_clamp(buffer)
    def left(self):
        if self.col > 0:
            self.col -= 1
    def right(self, buffer: str):
        if self.col < len(buffer[self.row]) - 1:
            self.col += 1
    def down(self, buffer: str):
        if self.row < len(buffer) - 1:
            self.row += 1
            self._col_clamp(buffer)


    def _col_clamp(self, buffer: str):
        self.col = min(self.col, len(buffer[self.row]) - 1)
