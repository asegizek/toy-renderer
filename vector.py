from point import *


class Vec2:

    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def norm(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def norm_squared(self) -> float:
        return (self.x ** 2) + (self.y ** 2)

    def dot(self, other) -> float:
        return (self.x * other.x) + (self.y * other.y)

    def cross(self, other) -> float:
        return (self.x * other.y) - (self.y * other.x)

    def __add__(self, other) -> "Vec2":
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> "Vec2":
        return Vec2(self.x - other.x, self.y - other.y)

    def __iadd__(self, other) -> "Vec2":
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other) -> "Vec2":
        self.x -= other.x
        self.y -= other.y
        return self

    @classmethod
    def point(cls, point: Point2):
        return Vec2(point.x, point.y)

    def __str__(self):
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return f"Vec2<{self.x}, {self.y}> at {hex(id(self))}"




class Vec3:

    def __init__(self, x: float, y: float, z: float):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def norm(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def norm_squared(self) -> float:
        return (self.x ** 2) + (self.y ** 2) + (self.z ** 2)

    def dot(self, other) -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other) -> "Vec3":
        new_x = (self.y * other.z) - (self.z * other.y)
        new_y = (self.z * other.x) - (self.x * other.z)
        new_z = (self.x * other.y) - (self.y * other.x)
        return Vector3(new_x, new_y, new_z)

    def __add__(self, other) -> "Vec3":
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other) -> "Vec3":
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __iadd__(self, other) -> "Vec3":
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other) -> "Vec3":
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self
        
    @classmethod
    def point(cls, point: Point3):
        return Vec3(point.x, point.y, point.z)

    def __str__(self):
        return f"Vec3<{self.x}, {self.y}, {self.z}>"

    def __repr__(self):
        return f"Vec3<{self.x}, {self.y}, {self.z}> at {hex(id(self))}"