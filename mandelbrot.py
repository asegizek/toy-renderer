def get_mandelbrot_frame():
    MANDELBROT_MAX_ITERATION = 256
    x_view_min = -2
    x_view_max = 0.5
    y_view_min = -1
    y_view_max = 1

    x_view_width = x_view_max - x_view_min
    y_view_width = y_view_max - y_view_min

    global canvas
    
    for x in range(0, WIDTH):
        for y in range(0, HEIGHT):
            x_frac = float(x) / WIDTH
            y_frac = float(y) / HEIGHT # I should flip y but since mandelbrot is symmetrical along x-axis i won't bother
            
            x_view = lerp(x_view_min, x_view_max, x_frac)
            y_view = lerp(y_view_min, y_view_max, y_frac)

            c = complex(x_view, y_view)
            z = 0
            pixel_color = 0x0

            for i in range(MANDELBROT_MAX_ITERATION):
                if abs(z) > 2:
                    # pixel_color = 0xFFFFFF
                    break
                z = (z*z) + c
            
            mag = abs(z)
            if mag >= 2:
                canvas.draw_point(x, y, 0xFFFFFF)
            else:
                mag_frac = mag / 2
                color_strength = int(mag_frac * 255)
                color = (color_strength << 16) | (color_strength << 8) | color_strength
                canvas.draw_point(x, y, color)

    return canvas.pixel_buffer.buffer