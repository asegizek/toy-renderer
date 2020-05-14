import numpy as np
import pygame
from pixel_buffer import PixelBuffer
from canvas import Canvas2D

HEIGHT = 480
WIDTH = 640

N=0


pixel_buffer = PixelBuffer(WIDTH, HEIGHT)

canvas = Canvas2D(WIDTH, HEIGHT, pixel_buffer)



fill_color = 0x0000FF
R = 255
G = 0
B = 0

GREEN_UP = 0
RED_DOWN = 1
BLUE_UP = 2
GREEN_DOWN = 3
RED_UP = 4
BLUE_DOWN = 5

COLOR_STATE = GREEN_UP

def update_color():
    global COLOR_STATE, R, G, B
    next_state = COLOR_STATE
    if COLOR_STATE == GREEN_UP:
        G += 1
        if G == 255:
            next_state = RED_DOWN
    elif COLOR_STATE == RED_DOWN:
        R -= 1
        if R == 0:
            next_state = BLUE_UP
    elif COLOR_STATE == BLUE_UP:
        B += 1
        if B == 255:
            next_state = GREEN_DOWN
    elif COLOR_STATE == GREEN_DOWN:
        G -= 1
        if G == 0:
            next_state = RED_UP
    elif COLOR_STATE == RED_UP:
        R += 1
        if R == 255:
            next_state = BLUE_DOWN
    elif COLOR_STATE == BLUE_DOWN:
        B -= 1
        if B == 0:
            next_state = GREEN_UP
    
    COLOR_STATE = next_state

def pack_color_bits(r, g, b):
    r_byte = r & 0xFF
    g_byte = g & 0xFF
    b_byte = b & 0xFF
    return (r_byte << 16) | (g_byte << 8) | b_byte        

cached_surface = None
def getFrame():
    global pixel_buffer, N, fill_color, canvas
    global R, G, B


    update_color()


    # list2d = make_2d_list(WIDTH, HEIGHT, pack_color_bits(R, G, B))
    # pixel_array = np.array(list2d, dtype=np.int32)
    # pixel_array[100:200, 100:200] = 0
    pixel_buffer.fill(pack_color_bits(R,G,B))
    # pixel_array.buffer[0:0, 400:800] = 0
    pixel_buffer.fill_rect(-2, 400, 2, 400, 0xFF)
    pixel_buffer.fill_pixel(639, 479, 0xFF)
    canvas.draw_line(600, 200, 200, 200, 0x00FF00)
    return pixel_buffer.buffer


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Serious Work - not games")
done = False
clock = pygame.time.Clock()

# Get a font for rendering the frame number
basicfont = pygame.font.SysFont(None, 32)

while not done:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

    # Clear screen to white before drawing 
    screen.fill((255, 150, 255))

    # Get a numpy array to display from the simulation
    npimage=getFrame()

    # Convert to a surface and splat onto screen offset by border width and height
    # surface = pygame.surfarray.pixels2d(npimage)
    # screen.blit(surface, (border, border))
    if cached_surface is None:
        cached_surface = pygame.Surface((WIDTH, HEIGHT))
    # surface = pygame.Surface((WIDTH, HEIGHT))
    pygame.surfarray.blit_array(cached_surface, npimage)
    screen.blit(cached_surface, (0, 0))



    # Display and update frame counter
    # text = basicfont.render('Frame: ' + str(N), True, (255, 0, 0), (255, 255, 255))
    # screen.blit(text, (0, HEIGHT+border))
    N = N + 1

    pygame.display.flip()
    clock.tick(60)