
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


    def split(self, cursor: object):
        row, col = cursor.row, cursor.col

        if self.lines == []:
            self.lines.append('')

        line = self.lines.pop(row)

        line_split_before = line[:cursor.col]
        line_split_after = line[cursor.col:]

        self.lines.insert(row, line_split_after)
        self.lines.insert(row, line_split_before)


    def delete(self, cursor: object):
        row, col = cursor.row, cursor.col

        if row == self.bottom and col == len(self.lines[row]): # stop if the cursor is the last position in the buffer
            return

        if self.lines != []:
            line = self.lines.pop(row)

            if col < len(line):
                new_line = line[:col] + line[col + 1:]

                self.lines.insert(row, new_line)
            else:
                next_line = self.lines[row]

                new_line = line + next_line

                self.lines.insert(row, new_line)
                del self.lines[row + 1]


    def __len__(self):
        return len(self.lines)


    def __getitem__(self, key: int):
        return self.lines[key]