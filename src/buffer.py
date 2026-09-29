
class Buffer:
    def __init__(self, lines: list[str]):
        self.lines = lines


    def __len__(self):
        return len(self.lines)


    def __getitem__(self, key: int):
        return self.lines[key]