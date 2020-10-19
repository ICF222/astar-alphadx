
class Point():
    x = 0
    y = 0

    def __init__(self, x_ = 0, y_ = 0):
        self.x = x_
        self.y = y_

    def __eq__(self, other):

        return self.x == other.x and self.y == other.y