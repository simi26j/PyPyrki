from pyrka import Pyrka


class Board:

    pyrkas = []

    def __init__(self, size):
        if size > 1:
            for i in range(size):
                if i == 0:
                    self.pyrkas.append(Pyrka(row=0, position=0))
                # else:
                    # for p in range(i+2):
                        # self.pyrkas[i].append(Pyrka(row=i, position=p))
