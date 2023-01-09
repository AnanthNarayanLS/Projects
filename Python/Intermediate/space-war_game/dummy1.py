
import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))
background = pygame.image.load("background.jpg")


running = True
while running:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
