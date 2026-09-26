
class Cursor:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col

    def up(self):
        if self.row > 0:
            self.row -= 1
    def left(self):
        if self.col > 0:
            self.col -= 1
    def right(self, buffer: str):
        if self.col < len(buffer[self.row]) - 1:
            self.col += 1
    def down(self, buffer: str):
        if self.row < len(buffer) - 1:
            self.row += 1
