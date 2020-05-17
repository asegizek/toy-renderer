from pixel_buffer import PixelBuffer
from utils import sign

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

    
