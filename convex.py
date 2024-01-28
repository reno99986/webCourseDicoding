import pygame
from pygame.locals import *
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Grafika Komputer - Cekung')

# Inisiasi Kode RGB Warna yang akan digunakan
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PROJECTION_1 = (255, 0, 0)
PROJECTION_2 = (0, 255, 0)
REAL = (255, 255, 0)
FAKE = (255, 0, 255)

# Inisiasi Font
font = pygame.font.SysFont(None, 20)

# Inisiasi Koordinat Penting
f_coor = (300, 300)
# obj_base = [100, 300]
# obj_top = [100, 200]

# Membuat fungsi DDA untuk menggambar garis
def DDA_line(start, end, color):
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    # Determine number of steps needed
    steps = max(abs(dx), abs(dy))

    # Calculate increments
    if steps != 0:
        inc_x = dx / steps
        inc_y = dy / steps
    else:
        inc_x = inc_y = 0

    # Initialize current position
    x, y = x1, y1

    # Draw each pixel along the line
    for _ in range(int(steps)):
        screen.set_at((int(x), int(y)), color)
        x += inc_x
        y += inc_y

    pygame.display.flip()

    return (x, y)

def DDA_line_projection_0(start, end, color):
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    # Determine number of steps needed
    steps = max(abs(dx), abs(dy))

    # Calculate increments
    if steps != 0:
        inc_x = dx / steps
        inc_y = dy / steps
    else:
        inc_x = inc_y = 0

    # Initialize current position
    x, y = x1, y1

    # Draw each pixel along the line
    while True:
        screen.set_at((int(x), int(y)), color)
        x += inc_x
        y += inc_y

        # If the line reaches the y-axis, stop drawing
        if int(x) >= 400:
            break

    pygame.display.flip()

    return (x, y)

def DDA_line_projection_1(start, end, batas, color):
    x1, y1 = start
    x2, y2 = end

    dx = x2 - x1
    dy = y2 - y1

    # Menentukan total langkah yang dibutuhkan
    steps = max(abs(dx), abs(dy))

    # Menghitung Total Langkah
    if steps != 0:
        inc_x = dx / steps
        inc_y = dy / steps
    else:
        inc_x = inc_y = 0

    # Inisiasi Posisi Awal
    x, y = x1, y1

    # Menggambar setiap pixel yang dilewati dengan warna telah ditentukan
    while True:
        screen.set_at((int(x), int(y)), color)
        x += inc_x
        y += inc_y

        # Kalau mencapai batas, berhenti
        if int(y) == batas:
            break

    pygame.display.flip()

    return (x, y)


# Main loop
running = True
while running:
    obj_top = [100, 200]
    obj_base = [100, 300]
 
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False


        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_w: 
                print("Real Object's height +10 pixels")
                obj_top[1] -= 10 
            elif event.key == pygame.K_s: 
                print("Real Object's height -10 pixels")
                obj_top[1] -= 10 
            elif event.key == pygame.K_a: 
                print("Real Object moves left 10 pixels")
                obj_base[0] -= 10
                obj_top[0] -= 10 
            elif event.key == pygame.K_d: 
                print("Real Object moves right 10 pixels") 
                obj_base[0] += 10
                obj_top[0] += 10 

    screen.fill(WHITE)

    # Render tulisan "f"
    text_surface_f = font.render('f', True, BLACK)
    text_rect_f = text_surface_f.get_rect()
    text_rect_f.center = (300, 296)
    screen.blit(text_surface_f, text_rect_f)


    # Render tulisan "2f"
    text_surface_2f = font.render('2f', True, BLACK)
    text_rect_2f = text_surface_2f.get_rect()
    text_rect_2f.center = (200, 296)
    screen.blit(text_surface_2f, text_rect_2f)

    # Menggambar Koordinat Kartesius
    DDA_line((0, 300), (800, 300), BLACK) # x-axis
    DDA_line((400, 0), (400, 600), BLACK) # y-axis

    # Menggambar Objek
    DDA_line(obj_base, obj_top, REAL)

    # Menggambar Proyeksi Pertama
    DDA_line(obj_top, (400, obj_top[1]), PROJECTION_2)
    proj_0 = DDA_line_projection_0(obj_top, f_coor, PROJECTION_2)
    batas_0 = proj_0[1]

    # Menggambar Proyeksi Kedua
    proj_1 = DDA_line_projection_1((400, obj_top[1]), f_coor, batas_0, PROJECTION_1)
    batas_1 = proj_0[1]
    fake_base = DDA_line(proj_0, proj_1, PROJECTION_1)

    # Menggambar Bayangan
    DDA_line(fake_base, (fake_base[0], 300), FAKE)
 
    time.sleep(0.5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()