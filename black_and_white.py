import math

import pygame

pygame.init()

FPS = 60
W, H = 640, 480

clock = pygame.time.Clock()
display = pygame.display.set_mode((W, H))


class Cube:
    def __init__(self, w=10, h=10, speed=2):
        self.w, self.h = w, h
        self.x, self.y = W // 2, H // 2
        self.angle = 0
        self.speed = speed

    @property
    def pos(self):
        return self.x, self.y

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.x += self.speed * cos_a
            self.y += self.speed * sin_a
        elif key[pygame.K_s]:
            self.x += -self.speed * cos_a
            self.y += -self.speed * sin_a
        elif key[pygame.K_a]:
            self.x += self.speed * sin_a
            self.y += -self.speed * cos_a
        elif key[pygame.K_d]:
            self.x += -self.speed * sin_a
            self.y += self.speed * cos_a
        elif key[pygame.K_LEFT]:
            self.angle -= 0.02
        elif key[pygame.K_RIGHT]:
            self.angle += 0.02


cube = Cube()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    cube.movement()

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 0), (cube.pos[0], cube.pos[1], cube.w, cube.h))
    pygame.draw.line(display, (0, 255, 0), cube.pos, (cube.x + W * math.cos(cube.angle),
                                                      cube.y + W * math.sin(cube.angle)))

    pygame.display.update()
    clock.tick(FPS)
