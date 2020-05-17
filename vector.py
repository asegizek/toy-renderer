


class Vector2:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def norm(self):
        return sqrt((self.x ** 2) + (self.y ** 2))

    def norm2(self):
        return (self.x ** 2) + (self.y ** 2)

    def dot(self, other: Vector2):
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other: Vector2):
        return (self.x * other.y) - (self.y * other.x)
