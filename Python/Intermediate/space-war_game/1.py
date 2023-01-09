import pygame
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 500))

score=0

# background
background=pygame.image.load('background.jpg')

mixer.music.load('mainSong.mp3')
mixer.music.play(-1)

# logo and caption
pygame.display.set_caption("AVENGERS")
icon=pygame.image.load('caplogo.png')
pygame.display.set_icon(icon)

# player
playerimg=pygame.image.load('chaur.png')
playerx=370
playery=380
playerx_change=0

# enemy
enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemy=6
for i in range(num_of_enemy):
    enemyimg.append(pygame.image.load('ghost1.png'))
    enemyx.append(random.randint(0, 735))
    enemyy.append(random.randint(50, 150))
    enemyx_change.append(0.3)
    enemyy_change.append(40)

# bullet
bulletimg=pygame.image.load('pokiball.png')
bulletx=0
bullety=380
bulletx_change=0
bullety_change=1
bullet_state='ready'

score_value=0
font=pygame.font.SysFont('freesansbold.ttf', 32)
textx=10
texty=10

over_font = pygame.font.SysFont('freesansbold.ttf',64)

def game_over():
    over =over_font.render("GAME OVER !!", True, (255, 255, 255))
    screen.blit(over, (200,150))
    mixer.music.load('gameover.wav')
    mixer.music.play()

def show_score(x, y):
    score=font.render(f"SCORE : {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state='fire'
    screen.blit(bulletimg, (x+16, y+10))


def iscollision(enemyx, enemyy, bulletx, bullety):
    distance=math.sqrt((math.pow(enemyx-bulletx, 2))+(math.pow(enemyy-bullety, 2)))
    if distance<27:
        return True
    return False


running=True
while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                playerx_change=-0.4
            if event.key==pygame.K_UP:
                playerx_change=0.4
            if event.key==pygame.K_LEFT:
                playerx_change=-0.4
            if event.key==pygame.K_RIGHT:
                playerx_change=0.4
            if event.key==pygame.K_SPACE:
                if bullet_state=='ready':
                    bullet_sound = mixer.Sound('shoot2.wav')
                    bullet_sound.play()

                    bulletx=playerx
                    fire(bulletx, bullety)

    playerx+=playerx_change

    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736

    for i in range(num_of_enemy):

        if enemyy[i] > 300:
            for j in range(num_of_enemy):
                enemyy[j] = 2000
            game_over()
            break

        enemyx[i]+=enemyx_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=0.3
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i]>=736:
            enemyx_change[i]=-0.3
            enemyy[i]+=enemyy_change[i]

        collision=iscollision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            collide_sound=mixer.Sound('collide.wav')
            collide_sound.play()
            bullety=380
            bullet_state='ready'
            score_value+=1
            enemyx[i]=random.randint(0, 735)
            enemyy[i]=random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    if bullety<=0:
        bullety=380
        bullet_state='ready'

    if bullet_state=='fire':
        fire(bulletx, bullety)
        bullety-=bullety_change

    player(playerx, playery)
    show_score(textx, texty)
    pygame.display.update()
