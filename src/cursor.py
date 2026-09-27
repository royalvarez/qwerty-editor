
class Cursor:
    def __init__(self, row: int, col: int, col_hint: int | None = None):
        self.row = row
        self._col = col
        self._col_hint = col if col_hint is None else col_hint

    @property
    def col(self):
        return self._col


    @col.setter
    def col(self, col: int):
        self._col = col
        self._col_hint = col


    def up(self, buffer):
        if self.row > 0:
            self.row -= 1
            self._col_clamp(buffer)
    def left(self, buffer: str):
        if self.col > 0:
            self.col -= 1
        elif self.col == 0 and self.row != 0:
            self.up(buffer)
            self._col = len(buffer[self.row]) - 1
    def right(self, buffer: str):
        if self.col < len(buffer[self.row]) - 1:
            self.col += 1
        elif self.col == len(buffer[self.row]) - 1 and self.row != len(buffer) - 1:
            self.down(buffer)
            self._col = 0
    def down(self, buffer: str):
        if self.row < len(buffer) - 1:
            self.row += 1
            self._col_clamp(buffer)


    def _col_clamp(self, buffer: str):
        self._col = min(self._col_hint, len(buffer[self.row]) - 1)
