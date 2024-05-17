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
    global ba





while game:









pygame.display.update()

