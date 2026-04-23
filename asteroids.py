from circleshape import CircleShape
import pygame
from constants import *
from logger import *
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        rnd = random.uniform(20, 50)
        new1 = self.velocity.rotate(rnd)
        new2 = self.velocity.rotate(-rnd)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        small1 = Asteroid(self.position.x, self.position.y, new_rad)
        small2 = Asteroid(self.position.x, self.position.y, new_rad)
        small1.velocity = new1 * 1.2
        small2.velocity = new2 * 1.2

        