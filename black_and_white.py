import pygame

pygame.init()

FPS = 60
clock = pygame.time.Clock()

W, H = 640, 480

display = pygame.display.set_mode((W, H))

# cube = pygame.draw.rect(display, (0, 255, 0), [640//2, 480//2, 10, 10])
x = 100
y = 100
while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    key = pygame.key.get_pressed()
    cube = pygame.rect.Rect(x, y, 10, 10)
    if key[pygame.K_LEFT] and cube.left > 0:
        x -= 2
    elif key[pygame.K_RIGHT] and cube.right < W:
        x += 2
    elif key[pygame.K_UP] and cube.top > 0:
        y -= 2
    elif key[pygame.K_DOWN] and cube.bottom < H:
        y += 2

    display.fill((0, 0, 0))
    pygame.draw.rect(display, (0, 255, 0), cube)
    pygame.display.update()
