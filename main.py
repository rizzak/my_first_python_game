import random

import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

W, H = 400, 400

display = pygame.display.set_mode((W, H))
pygame.display.set_caption("My First Game")

bg_surf = pygame.image.load("img/bg.jpg").convert()

kolobki = pygame.sprite.Group()


class Kolobok(pygame.sprite.Sprite):
    def __init__(self, x, y, surf, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(surf).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)
        self.speed_x = 3
        self.speed_y = 3
        self.group = group

    def update(self, *args, **kwargs) -> None:
        # self.rect.x += random.choice([0, 0, self.speed, -self.speed])
        # self.rect.y += random.choice([0, 0, self.speed, -self.speed])
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > args[0]:
            self.rect.right = args[0]
            self.speed_x *= -1
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x *= -1
        if self.rect.bottom > args[1]:
            self.rect.bottom = args[1]
            self.speed_y *= -1
        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_y *= -1

        collided = pygame.sprite.spritecollideany(self, self.group, collide)

        if collided:
            print('collided')
            Kolobok(self.rect.x, self.rect.y, "img/kolobok.png", self.group)


# just a helper function that wraps pygame.sprite.collide_mask
# to prevent a sprite from colliding with itself
def collide(a, b):
    if a == b:
        return False
    return pygame.sprite.collide_mask(a, b)


def create_kolobok(w, h, group, count=1):
    for _ in range(count):
        Kolobok(w, h, "img/kolobok.png", group)


# def new_born_kolobok():
#     for kolobok in kolobki:
#         if kolobok.rect.colliderect()

create_kolobok(W // random.randint(0, 4), H // random.randint(0, 100), kolobki, 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.blit(bg_surf, (0, 0))
    kolobki.draw(display)
    pygame.display.update()

    clock.tick(FPS)

    kolobki.update(W, H)
