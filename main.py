# this allow us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    alive = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    while alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color='black')
        pygame.display.flip()

if __name__ == "__main__":
    main()