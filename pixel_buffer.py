import numpy as np

BYTE_MASK = 0xFF
RGB_MASK = 0xFFFFFF

class PixelBuffer:

    def __init__(self, width: int, height: int, fill_color: int=0):
        self.width = width
        self.height = height
        self.buffer = self._create_pixel_buffer(width, height, fill_color)
        

    def _create_pixel_buffer(self, width: int, height: int, fill_color: int) -> np.array:
        fill_color_truncated = fill_color & RGB_MASK
        list_2d = []

        for x in range(width):
            list_2d.append([fill_color_truncated] * height)

        return np.array(list_2d, dtype=np.int32)

    
    def fill(self, color: int):
        color_truncated = color & RGB_MASK
        self.buffer.fill(color_truncated)


    def fill_rect(self, x: int, y: int, width: int, height: int, color: int):
        color_truncated = color & RGB_MASK
        x_start = max(x, 0)
        y_start = max(y, 0)
        x_end = x + width
        y_end = y + height
        self.buffer[x_start:x_end, y_start:y_end] = color_truncated


    def fill_pixel(self, x: int, y: int, color: int):
        color_truncated = color & RGB_MASK

        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            self.buffer[x, y] = color_truncated

