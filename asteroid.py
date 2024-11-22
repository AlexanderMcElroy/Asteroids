import pygame
from circleshape import CircleShape
import random
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        super().__init__(position.x, position.y, radius)
        self.velocity = velocity
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(random_angle)
        new_velocity2 = self.velocity.rotate(-random_angle)
   
                    # Calculate new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

                # Then create the new asteroids with this new_radius...

        asteroid1 = Asteroid(
            position=self.position,  # use current asteroid's position
            radius=new_radius,       # use the smaller radius we calculated
            velocity=(new_velocity1 * 1.2))  # speed up the rotated velocity
            

        for group in self.groups():
                group.add(asteroid1)
        
        asteroid2 = Asteroid(
            position=self.position,  # use current asteroid's position
            radius=new_radius,       # use the smaller radius we calculated
            velocity=(new_velocity2 * 1.2))
            

        for group in self.groups():
                group.add(asteroid2)

