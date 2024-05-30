import pygame
import time
import random
import math

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
    def __init__(self,speed):
        self.body=[(width//2-i*20,hight//2) for i in range(4)]
        self.direction=(1,0)
        self.speed=speed

    def move(self):
        head = self.get_head()
        new_head = (head[0] + self.direction[0] * 20, head[1] + self.direction[1] * 20)

        if new_head[1] >= hight:
            new_head = (new_head[0], 0)
        elif new_head[1] < 0:
            new_head = (new_head[0], hight - 20)

        if new_head[0] >= width:
            new_head = (0, new_head[1])
        elif new_head[0] < 0:
            new_head = (width - 20, new_head[1])

        self.body.insert(0, new_head)
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

    def Speed(self,speed):
        self.speed=speed

class Food:
    def __init__(self):
        self.pos=(random.randint(10,width-10),random.randint(10,hight-10))

    def respawn(self):
        self.pos = (random.randint(10, width - 10), random.randint(10, hight - 10))

    def get_position(self):
        return self.pos

def distance(pos1,pos2):
    return math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)

def intro():
    font_l=pygame.font.Font(None,50)
    font_s=pygame.font.Font(None,30)

    game_n=font_l.render("SNAKE GAME",True,black)
    slow_b=font_s.render("SLOW",True,black)
    normal_b=font_s.render("NORMAL",True,black)
    fast_b=font_s.render("FAST",True,black)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type==pygame.MOUSEBUTTONDOWN:
                x,y=pygame.mouse.get_pos()
                if 100<x<200 and 150<y<200:
                    return"slow"
                if 100<x<200 and 100<y<150:
                    return"normal"
                if 100<x<200 and 50<y<100:
                    return"fast"

        window.fill(white)
        window.blit(game_n,(width//1-game_n.get_width() ,hight//1-game_n.get_height()))
        window.blit(slow_b,(100,150))
        window.blit(normal_b,(100,100))
        window.blit(fast_b,(100,50))
        pygame.display.update()






def main():
    speed_level=intro()
    if speed_level == "slow":
        speed_level=10
    elif speed_level == "normal":
        speed_level=15
    else:
        speed_level=20
    snake=Snake(speed_level)
    food=Food()

    score=0
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
        head=snake.get_head()

        if distance(head,food.get_position())<=20:
            snake.grow()
            food.respawn()
            score+=1
        if head in snake.get_body():
            font=pygame.font.Font(None,50)
            text=font.render("GAME OVER",True,black)
            window.blit(text,(width//2-text.get_width()//2,hight//2-text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(2)
            pygame.quit()
        if score>=10:
            font=pygame.font.Font(None,50)
            text=font.render("YOU WIN",True,black)
            window.blit(text,(width//2-text.get_width()//2,hight//2-text.get_height()//2))
            pygame.display.update()
            pygame.time.delay(1000)
            pygame.quit()
        window.fill(white)
        #draw snake and snake body is black
        for de in snake.body:

            pygame.draw.rect(window,black,(de[0],de[1],20,20))

            # draw food
            pygame.draw.circle(window, black, food.get_position(), 10)


        font=pygame.font.Font(None,30)
        text=font.render("Score: "+str(score),True,black)
        window.blit(text,(10,10))
        pygame .display.update()
        clock.tick(speed_level)






main()

