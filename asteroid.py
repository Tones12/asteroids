import pygame
import random
from circleshape import CircleShape
from logger import log_event
from constants import *

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        split_angle = random.uniform(20, 50)
        asteroid_1_velocity = self.velocity.rotate(split_angle)
        asteroid_2_velocity = self.velocity.rotate(-split_angle)
        old_radius = self.radius
        self.radius = old_radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.radius)
        new_asteroid_1.velocity = asteroid_1_velocity * 1.2
        new_asteroid_2.velocity = asteroid_2_velocity * 1.2


