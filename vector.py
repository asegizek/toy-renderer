


class Vector2:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def norm(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def norm2(self) -> float:
        return (self.x ** 2) + (self.y ** 2)

    def dot(self, other: Vector2) -> float:
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other: Vector2) -> float:
        return (self.x * other.y) - (self.y * other.x)




class Vector3:

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def norm(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def norm2(self) -> float:
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)

    def dot(self, other: Vector3) -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other: Vector3) -> Vector3:
        new_x = (self.y * other.z) - (self.z * other.y)
        new_y = (self.z * other.x) - (self.x * other.z)
        new_z = (self.x * other.y) - (self.y * other.x)
        return Vector3(new_x, new_y, new_z)