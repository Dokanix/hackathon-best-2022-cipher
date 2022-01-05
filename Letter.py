from cv2 import sqrt


class Letter:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def distance_to_letter(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def y_distance_to_letter(self, other):
        return abs(self.y - other.y)

    def x_distance_to_letter(self, other):
        return abs(self.x - other.x)

    def __lt__(self, other):
        return self.x < other.x
