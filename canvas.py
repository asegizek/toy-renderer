from pixel_buffer import PixelBuffer
from utils import sign
from vector import Vec2
from point import Point2

RGB_MASK = 0xFFFFFF


class Canvas2D:

    def __init__(self, width: int, height: int, pixel_buffer: PixelBuffer):
        self.width = width
        self.height = height
        self.pixel_buffer = pixel_buffer


    def draw_point(self, x: int, y: int, color: int):
        self.pixel_buffer.fill_pixel(x, y, color)


    def draw_line_naive(self, x0: int, y0: int, x1: int, y1: int, color: int):
        """
        Bresenham algorithm
        """
        if x0 == x1:
            y_start = min(y0, y1)
            y_end = max(y0, y1)
            for y in range(y_start, y_end + 1):
                self.pixel_buffer.fill_pixel(x0, y, color)
            return

        if y0 == y1:
            x_start = min(x0, x1)
            x_end = max(x0, x1)
            for x in range(x_start, x_end + 1):
                self.pixel_buffer.fill_pixel(x, y0, color)
            return

        dx = x1 - x0
        dy = y1 - y0
        # (x_start, y_start) = (x0, y0) if x0 < x1 else (x1, y1)
        # (x_end, y_end) = (x1, y1) if x0 < x1 else (x0, y0)
        m = float(dy) / dx
        b = y0 - (m * x0)
        # b = y_start - (m * x_start)

        if abs(m) <= 1:
            x_start = min(x0, x1)
            x_end = max(x0, x1)
            for x in range(x_start, x_end + 1):
                y = int(round(m*x + b))
                self.pixel_buffer.fill_pixel(x, y, color)
                
        else:
            # print("ELSE")
            y_start = min(y0, y1)
            y_end = max(y0, y1)
            for y in range(y_start, y_end + 1):
                x = int(round((y - b) / m))
                self.pixel_buffer.fill_pixel(x, y, color)


    def draw_line(self, x0: int, y0: int, x1: int, y1: int, color: int):
        """
        Bresenham algorithm
        """
        dx = x1 - x0
        dy = y1 - y0

        if abs(dx) >= abs(dy):
            # x-driving axis
            x_start = min(x0, x1)
            x_end = max(x0, x1)
            y = y0 if x0 < x1 else y1
            dy = dy if x0 < x1 else -dy
            eps = abs(dy) - abs(dx)

            for x in range(x_start, x_end + 1):
                self.pixel_buffer.fill_pixel(x, y, color)
                if eps >= 0:
                    y += sign(dy)
                    eps -= abs(dx)
                eps += abs(dy)
        else:
            # y-driving axis
            y_start = min(y0, y1)
            y_end = max(y0, y1)
            x = x0 if y0 < y1 else x1
            dx = dx if y0 < y1 else -dx
            eps = abs(dx) - abs(dy)

            for y in range(y_start, y_end + 1):
                self.pixel_buffer.fill_pixel(x, y, color)
                if eps >= 0:
                    x += sign(dx)
                    eps -= abs(dy)
                eps += abs(dx)


    def draw_rect(self, x: int, y: int, width: int, height: int, color: int):
        self.pixel_buffer.fill_rect(x, y, width, height, color)

    
    def draw_triangle(self, p0: Point2, p1: Point2, p2: Point2, color: int):
        self.draw_line(p0.x, p0.y, p1.x, p1.y, 0)
        self.draw_line(p1.x, p1.y, p2.x, p2.y, 0)
        self.draw_line(p2.x, p2.y, p0.x, p0.y, 0)

        min_x = min(p0.x, p1.x, p2.x)
        min_y = min(p0.y, p1.y, p2.y)
        max_x = max(p0.x, p1.x, p2.x)
        max_y = max(p0.y, p1.y, p2.y)

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                test_point = Point2(x, y)
                if self._point_within_triangle(test_point, p0, p1, p2):
                    self.pixel_buffer.fill_pixel(x, y, color)

    
    def _point_within_triangle(self, test_point: Point2, p0: Point2, p1: Point2, p2: Point2) -> bool:
        # Find barycentric coordinates.
        A = Vec2.point(p0)
        B = Vec2.point(p1)
        C = Vec2.point(p2)
        P = Vec2.point(test_point)

        AB = B - A
        AC = C - A
        BC = C - B
        AP = P - A
        BP = P - B

        # (miniscule optimization) Note  triangle areas are usually the cross product of two sides divided by 2
        #but in this case since i am dividing the subtriangle areas by the whole triangle
        #area the 2's would cancel out

        # Double area of triangle.
        ABC = abs(AB.cross(AC))

        # Find signed double areas of subtriangles.
        flip = 1 if AC.cross(AB) > 0 else -1
        ABP = flip * (AP.cross(AB))
        BCP = flip * (BP.cross(BC))
        CAP = flip * (AC.cross(AP))

        # Find barycentric coordinates.
        phi_A = BCP / ABC
        phi_B = CAP / ABC
        phi_C = ABP / ABC

        # Check that the values are within the triangle. If point is outside triangle then one
        # of these barycentric coordinates would be negative.
        within_A = phi_A >= 0.0
        within_B = phi_B >= 0.0
        within_C = phi_C >= 0.0

        return within_A and within_B and within_C