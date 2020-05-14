from pixel_buffer import PixelBuffer

RGB_MASK = 0xFFFFFF

class Canvas2D:

    def __init__(self, width: int, height: int, pixel_buffer: PixelBuffer):
        self.width = width
        self.height = height
        self.pixel_buffer = pixel_buffer


    def draw_point(self, x: int, y: int, color: int):
        self.pixel_buffer.fill_pixel(x, y, color)
    

    def draw_line(self, x0: int, y0: int, x1: int, y1: int, color: int):
        if x0 == x1:
            y_start = min(y0, y1)
            y_end = max(y0, y1)
            for y in range(y_start, y_end + 1):
                self.pixel_buffer.fill_pixel(x0, y, color)

        if y0 == y1:
            x_start = min(x0, x1)
            x_end = max(x0, x1)
            for x in range(x_start, x_end + 1):
                self.pixel_buffer.fill_pixel(x, y0, color)


    def draw_rect(self, x: int, y: int, width: int, height: int, color: int):
        self.pixel_buffer.fill_rect(x, y, width, height, color)

    
