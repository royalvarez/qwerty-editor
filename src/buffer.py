
class Buffer:
    def __init__(self, lines: list[str]):
        self.lines = lines


    @property
    def bottom(self):
        return len(self) - 1


    def insert(self, cursor: object, input_key: str):
        row, col = cursor.row, cursor.col
        if self.lines != []:
            line = self.lines.pop(row)

            new_line = line[:cursor.col] + input_key + line[cursor.col:]
            self.lines.insert(row, new_line)
        else:
            self.lines.append(input_key)


    def __len__(self):
        return len(self.lines)


    def __getitem__(self, key: int):
        return self.lines[key]