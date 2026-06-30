from circleshape import CircleShape
from constants import BOMB_RADIUS
from shot import Shot
import pygame

class Bomb(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, BOMB_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, BOMB_RADIUS, 3)

    