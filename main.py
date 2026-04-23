import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from logger import *
import sys
from shot import *
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    delta = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    
    Player.containers = (drawable, updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    asteroid = AsteroidField()
    print(player.position)
    while 1 == 1:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for object in updatable:
            object.update(delta)
        for ass in asteroids:
            if ass.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit(1)    
        for ass in asteroids:
            for asser in shots:
                if ass.collides_with(asser):
                    log_event("asteroid_shot")
                    ass.split()
                    
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        delta = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
