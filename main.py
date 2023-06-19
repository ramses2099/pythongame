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


class Box:
    def __init__(self, x, y, color):
        self.mass = 10
        self.w, self.h = 32, 32
        self.color = color
        self.rect = pygame.rect.Rect(x, y, self.w, self.h)
        self.position = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleartion = pygame.math.Vector2(0, 0.10)

    def apply_force(self, vec):
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 1)

    def update(self, dt):
        # bounding
        if self.rect.left - self.rect.w < 0 or self.rect.right + self.rect.w > WINDOW_SIZE[0]:
            self.velocity.x *= -1
        if self.rect.top - self.rect.h < 0 or self.rect.bottom + self.rect.h > WINDOW_SIZE[1]:
            self.velocity.y *= -1

        # force
        self.acceleartion.x = self.acceleartion.x / self.mass
        self.acceleartion.y = self.acceleartion.y / self.mass
        # velocity
        self.velocity.x += self.acceleartion.x * dt
        self.velocity.y += self.acceleartion.y * dt
        # position
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
        # pygame rect
        self.rect.x += self.position.x
        self.rect.y += self.position.y


class App:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.objets = []
        self.init_object()

    def random_color(self) -> tuple[int, int, int]:
        r = random.random() * 255
        g = random.random() * 255
        b = random.random() * 255
        return (int(r), int(g), int(b))

    def init_object(self):
        c = self.random_color()
        b = Box(25, 25, c)
        self.objets.append(b)

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

            # draw
            for obj in self.objets:
                obj.update(self.dt)
                obj.draw(self.screen)

            # connect particles
            # self.connect_particle()

            # flip() the display to put your work on screen
            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    App().run()
