import pygame #type:ignore
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return None
        new_angle = random.uniform(20, 50)
        asteroid1_velocity = self.velocity.rotate(new_angle)
        asteroid2_velocity = self.velocity.rotate(-new_angle)
        asteroids_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1],asteroids_radius)
        asteroid2 = Asteroid(self.position[0], self.position[1],asteroids_radius)
        asteroid1.velocity = asteroid1_velocity * 1.2
        asteroid2.velocity = asteroid2_velocity * 1.2