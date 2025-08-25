# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import random
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    #initialize pygame
    pygame.init()
    
    # create a window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # create a clock object to manage the frame rate
    clock = pygame.time.Clock()

    # groups to hold game objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #create the object in the groups
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    # create the player object
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    asteroid_field = AsteroidField()

    dt = 0

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
        
            for shot in shots:
                if asteroid.collide(shot):
                    shot.kill()
                    asteroid.split()

        # set screen to black
        screen.fill("black")

        # draw all objects
        for object in drawable:
            object.draw(screen)
        #refresh the display
        pygame.display.flip()
        
        # manage frame rate
        dt = clock.tick(60) / 1000  # Limit to 60 frames per second


if __name__ == "__main__":
    main()
