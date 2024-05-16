import pygame
from pygame.locals import QUIT

pygame.init()

window_width, window_height = 800, 600
brush=40



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
    tollbar.blit(pen_text, (40, 20))
    tollbar.blit(eraser_text, (80, 20))
    tollbar.blit(big_pen_text, (200, 20))
    tollbar.blit(small_pen_text, (160, 20))

    color_button_g=20
    color_button_h=20
    black_button=pygame.draw.circle(tollbar,black,(240,25),color_button_g//2)
    red_button=pygame.draw.circle(tollbar,red,(280,25),color_button_g//2)

    window.fill(white)

    window.blit(canvas, (0,brush))
    window.blit(tollbar, (0,0))


    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if event.pos[1] <= brush:
               pen_rect=pen_text.get_rect(topleft=(40, 20))
               ereser_rect=eraser_text.get_rect(topleft=(80, 20))
               decrease_rect=eraser_text.get_rect(topleft=(120, 20))
               increase_rect=eraser_text.get_rect(topleft=(150, 20))


               if pen_rect.collidepoint(event.pos):
                   drawing=False

               elif ereser_rect.collidepoint(event.pos):
                   drawing=True

               elif decrease_rect.collidepoint(event.pos):
                   if brush_size > min:
                       brush_size-=1
               elif increase_rect.collidepoint(event.pos):
                   if brush_size < max:
                       brush_size+=1
               elif black_button.collidepoint(event.pos):
                   brush_color=black
               elif red_button.collidepoint(event.pos):
                   brush_color=red

            else:
             drawing=True
             last_pos=event.pos
        elif event.type==pygame.MOUSEMOTION:
            if drawing and not penghapus:
               pygame.draw.line(canvas, brush_color, last, event.pos, brush_size)
               last=event.pos
        elif event.type==pygame.MOUSEBUTTONUP:
            drawing=False

    pygame.display.flip()

pygame.quit()






















































