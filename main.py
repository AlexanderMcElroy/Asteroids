# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
pygame.init()
clock = pygame.time.Clock()  # This properly creates a new Clock object 
dt = 0

def main():
    print(f"Starting asteroids!\nScreen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               return 

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0  # Convert milliseconds to seconds


if __name__ == "__main__":
    main()    
