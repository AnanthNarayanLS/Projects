
import pygame
from pygame.locals import *
from pygame import mixer
import time
import random

back_color = (186, 44, 230)
size = 20

class Cherry:
    def __init__(self,parent_screen):
        self.cherry = pygame.image.load("requirements/cherry.jpg").convert()
        self.parent_screen=parent_screen
        self.x=size*4
        self.y=size*4

    def draw(self):
        self.parent_screen.blit(self.cherry, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0,33)*size
        self.y = random.randint(0,18)*size

class Snake:

    def __init__(self,parent_screen,length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("requirements/block.png").convert()
        self.x = [size]*length
        self.y = [size]*length
        self.direction = 'down'

    def increse_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        self.parent_screen.fill((186, 44, 230))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        self.draw()


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("ANANTH NARAYAN LS here!!!!")

        self.surface = pygame.display.set_mode((1366, 768))
        self.surface.fill((186, 44, 230))
        self.snake = Snake(self.surface , 1)
        self.snake.draw()
        self.cherry = Cherry(self.surface)
        self.cherry.draw()

    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def play(self):
        self.snake.walk()
        self.cherry.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_collision(self.snake.x[0],self.snake.y[0],self.cherry.x,self.cherry.y):
            self.snake.increse_length()
            self.cherry.move()

        for i in range(3,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "gameover"

    def show_gameover(self):
        self.surface.fill(back_color)
        font = pygame.font.SysFont('arial',30)
        line1 = font.render(f"Python score : {self.snake.length}",True,(255,255,255))
        self.surface.blit(line1,(200,300))
        print("\n")
        line2 = font.render("TO PLAY AGAIN HIT ENTER ELSE HIT ESCAPE",True,(255,255,255))
        self.surface.blit(line2,(200,350))
        pygame.display.flip()


    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Python score : {self.snake.length}",True,(255,255,255))
        self.surface.blit(score,(1100,10))

    def reset(self):
        self.snake = Snake(self.surface , 1)
        self.cherry = Cherry(self.surface)

    def run(self):
        running=True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
                        if event.key == K_UP:
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                        if event.key == K_RIGHT:
                            self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_gameover()
                pause = True
                self.reset()

            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.run()





