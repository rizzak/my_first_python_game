import random

import pygame

from main import collide


class Kolobok(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed = 30
        self.group = group

    def update(self, *args, **kwargs) -> None:
        self.rect.x += random.choice([0, 0, self.speed, -self.speed])
        self.rect.y += random.choice([0, 0, self.speed, -self.speed])
        if self.rect.right > args[0]:
            self.rect.right = args[0]
            self.speed *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed *= -1
        if self.rect.bottom > args[1]:
            self.rect.bottom = args[1]
            self.speed *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed *= -1

        collided = pygame.sprite.spritecollideany(self, self.group, collide)

        if collided:
            print('collided')
            # Kolobok(self.rect.x, self.rect.y, "img/kolobok.png", self.group)

