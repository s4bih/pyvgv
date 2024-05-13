import pygame
from pygame.locals import QUIT

pygame.init()

window_width, window_height = 800, 600
brush=20

white=(255, 255, 255)
black=(0, 0, 0)
gray=(128, 128, 128)
red=(255, 0, 0)

window=pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("paling")

drawing=False
brush_size=2
min=1
max=100
brush_color=black
penghapus=False
last=None

canvas=pygame.Surface((window_width, window_height-brush))
canvas.fill(white)

tollbar=pygame.Surface((window_width, brush))
tollbar.fill(gray)

run=True
while run:
    tollbar.fill(gray)
    font=pygame.font.SysFont(None, 30)
    pen_text=font.render("pen", True, black)
    eraser_text=font.render("eraser", True, black)
    big_pen_text=font.render("+", True, black)
    small_pen_text=font.render("-", True, black)
    tollbar.blit(pen_text, (10, 10))
    tollbar.blit(eraser_text, (10, 50))
    tollbar.blit(big_pen_text, (10, 90))
    tollbar.blit(small_pen_text, (10, 130))

    color_button_g=20
    color_button_h=20
    black_button=pygame.draw.circle(tollbar,black,(240,25),color_button_g//2)
    red_button=pygame.draw.circle(tollbar,red,(240,25),color_button_g//2)

    window.fill(white)

    window.blit(0,tollbar)