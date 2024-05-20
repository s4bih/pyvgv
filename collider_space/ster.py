import pygame
import random
import sys

pygame.init()

screenw,screenh=800,600
window=pygame.display.set_mode((screenw,screenh))
pygame.display.set_caption('ster')

background1=pygame.image.load('space_background.jpeg').convert()
background1=pygame.transform.scale(background1,(screenw,screenh))
background2=pygame.transform.scale(background1,(screenw,screenh))

space=pygame.image.load('spaceship.png').convert_alpha()
spacew,spaceh=space.get_size()
spaces=0.15
space=pygame.transform.scale(space,(int(spacew*spaces),int(spaceh*spaces))),int(spacew*spaces),int(spaceh*spaces)

spacex=screenw//2-spacew//2
spacey=screenh-50
spacespeed=5

class asteroid:

    def __init__(self):
        self.x=x
        self.y=y
        self.image=image
        self.scale=scale

        self.image=pygame.transform.scale(self.image,(int(self.image.get_width()*self.scale),int(self.image.get_height()*self.scale)))



    def move(self,speed):
        self.y+=speed

    def draw(self):
        window.blit(self.image,(self.x,self.y))

asteroid_img=pygame.image.load('asteroid.png').convert_alpha()
asteroidw,asteroidh=asteroid_img.get_size()



max_asteroids=0.15
min_asteroids=0.05


asteroids=[]
clock=pygame.time.Clock()
game=True

def close_game():
   pygame.exit()
   pygame.quit()

def update():
    global background1_y,background2_y
    background1_y=(background1_y+1)%screenh
    background2_y=background1_y-screenh
    window.blit(background1,(0,background1_y))
    window.blit(background1,(0,background2_y))

background1_y=0
background2_y= -screenh





while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        spacex-=spacespeed

    if keys[pygame.K_RIGHT]:
        spacex+=spacespeed
        if spacex > screenw-space.get_width:
            spacex=screenw-spacew.get_width

    window.fill((0,0,0))

    update.background()

    window.blit(space,(spacex,spacey))

    if random.randint(1,100)<2:
        a_x=random.randint(30,screenw-30)
        a_s=random.uniform(min_asteroids,max_asteroids)
        astroid=asteroid(a_x,-int(asteroidh*a_s),asteroid_img,a_s)
        asteroids.append(astroid)

    astroid_rect = pygame.Rect(spacex, spacey, space.get_width(), space.get_height())


    for astroid in asteroids:
        astroid.move(1)
        astroid_rect=pygame.Rect(astroid.x,astroid.y,astroid.image.get_width(),astroid.image.get_height())
        astroid.draw(window)

        if astroid_rect.colliderect(astroid_rect):
            close_game()

    astroid=[astroid for astroid in asteroids if astroid.y<screenh]
    pygame.display.update()
    clock.tick(60)


pygame.quit()
sys.exit()










