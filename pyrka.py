class Pyrka:

    def __init__(self, row, position):
        self.marked = False
        self.row = row
        self.position = position

    def mark(self):
        self.marked = True
