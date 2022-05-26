import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1000,528))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((255,255,255))

    color = 0,0,0
    width = 5
    pygame.draw.line(screen,color,(100,100),(500,300),width)

    pygame.display.update()
