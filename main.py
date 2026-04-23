import pygame
from constants import *
from logger import log_state
from player import *
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    delta = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    counter = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while 1 == 1:
        log_state()
        counter += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


if __name__ == "__main__":
    main()
