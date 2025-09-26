from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfeild import AsteroidField

import pygame 


def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group() 
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids,drawable,updatable)

    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroidf = AsteroidField()
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)    
        for obj in asteroids:
            if obj.col_det(player):
                print("Game over!")
                exit(0)
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
