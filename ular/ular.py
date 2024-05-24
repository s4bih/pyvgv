import pygame
import time

pygame.init()

width,hight=400,300
window_size=(width,hight)
window_title=("snake game")

white=(255,255,255)
black=(0,0,0)

#create the game window
window=pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

#snake class to move the snake and growth
class Snake:
    def __init__(self):
        self.body=[(width//2-i*20,hight//2) for i in range(4)]
        self.direction=(1,0)

    def move(self):
        dx,dy=self.direction
        new_head=(self.body[0][0]+20*dx,self.body[0][1]+20*dy)
        self.body.insert(0,new_head)
        self.body.pop()

    def grow(self):
        dx,dy=self.direction
        new_tail=(self.body[-1][0]+dx*20,self.body[-1][1]+dy*20)
        self.body.append(new_tail)

    def change_direction(self,dx,dy,):
        if (dx,dy) != (-self.direction[0],-self.direction[1]):
            self.direction = (dx,dy)

    def get_head(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]



def main():
    snake=Snake()


    clock=pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(0,-1)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0,1)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(-1,0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(1,0)

        snake.move()
        window.fill(white)
        for pos in snake.get_body():
            pygame.draw.rect(window,black,(pos[0],pos[1],20,20))
        pygame.display.update()
        clock.tick(10)


