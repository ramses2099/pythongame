import random
import math
import pygame

WINDOW_SIZE = (1280, 720)


class Particle:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = random.uniform(0, (math.pi * 2))
        self.color = color
        self.radius = random.random() * math.pi * 6

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius, 1)

    def update(self, dt):
        if self.x + self.radius > WINDOW_SIZE[0] or self.x - self.radius < 0:
            self.vx *= -1
        if self.y + self.radius > WINDOW_SIZE[1] or self.y - self.radius < 0:
            self.vy *= -1
        self.x += math.sin(self.angle) * self.vx * dt
        self.y -= math.cos(self.angle) * self.vy * dt
