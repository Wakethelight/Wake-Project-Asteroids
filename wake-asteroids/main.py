# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player(x = SCREEN_WIDTH // 2, y = SCREEN_HEIGHT // 2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.draw(screen)
        screen.fill("black") 
        pygame.display.flip()

        dt = clock.tick(60) / 1000  # Limit to 60 frames per second


if __name__ == "__main__":
    main()
