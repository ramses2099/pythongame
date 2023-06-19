# Example file showing a circle moving on screen
import math
import random

import pygame

TITLE = "TEST GAME"
WINDOW_SIZE = (1280, 720)
FPS = 60
BLACK = (0, 0, 0)
RED = (255, 30, 70)
BLUE = (10, 20, 200)
GREEN = (50, 230, 40)
WHITE = (255, 255, 255)
DISTANCE = 100


class Particle:
    def __init__(self, x, y, vx, vy, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = random.random() * math.pi * 6

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def update(self, dt):
        if self.x + self.radius > WINDOW_SIZE[0] or self.x - self.radius < 0:
            self.vx *= -1
        if self.y + self.radius > WINDOW_SIZE[1] or self.y - self.radius < 0:
            self.vy *= -1
        self.x += self.vx * dt
        self.y += self.vy * dt


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.arry_particle = []
        self.numberofparticle = 200
        self.init_particle()  # init all particle

    def random_color(self) -> tuple[int, int, int]:
        r = random.random() * 255
        g = random.random() * 255
        b = random.random() * 255
        return (int(r), int(g), int(b))

    def init_particle(self):
        for i in range(self.numberofparticle):
            x = random.random() * WINDOW_SIZE[0]
            y = random.random() * WINDOW_SIZE[1]
            vx = random.random() * 5
            vy = random.random() * 7
            p = Particle(x, y, vx, vy, self.random_color())
            self.arry_particle.append(p)

    def connect_particle(self):
        for i in range(len(self.arry_particle)):
            for j in range((i + 1), len(self.arry_particle)):
                dx = self.arry_particle[i].x - self.arry_particle[j].x
                dy = self.arry_particle[i].y - self.arry_particle[j].y
                d = math.hypot(dx, dy)
                if d < DISTANCE:
                    p1x = self.arry_particle[i].x
                    p1y = self.arry_particle[i].y
                    p2x = self.arry_particle[j].x
                    p2y = self.arry_particle[j].y
                    pygame.draw.line(self.screen, WHITE, (p1x, p1y), (p2x, p2y), 2)

    def run(self):
        while self.running:
            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            self.dt = self.clock.tick(FPS) * .001 * FPS
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill(BLACK)

            # update
            for particle in self.arry_particle:
                particle.update(self.dt)

            # draw
            for particle in self.arry_particle:
                particle.draw(self.screen)
            # connect particles
            self.connect_particle()

            # flip() the display to put your work on screen
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
