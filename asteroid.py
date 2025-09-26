import pygame 
from circleshape import CircleShape
from constants import *
import random



class Asteroid (CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)
    def update(self,dt):
        self.position += self.velocity * dt * 2
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x,self.position.y,new_rad)
        new_ast2 = Asteroid(self.position.x,self.position.y,new_rad)

        new_ast1.velocity = pygame.Vector2.rotate(self.velocity,random.uniform(20,50))*1.2
        new_ast2.velocity = pygame.Vector2.rotate(self.velocity,-random.uniform(20,50))*1.2

