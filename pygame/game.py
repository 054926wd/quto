import sys
import pygame
pygame.init()
size = width,heigth = 320,240
screen = pygame.display.set_mode(size)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()