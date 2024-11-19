# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
pygame.init()

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
       
if __name__ == "__main__":
    main()    
