import pygame

pygame.init()

width, height = 900, 700
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

x, y = 25, 25

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if y < height-25 and event.key == pygame.K_DOWN:
                y += 20
            if y > 25 and event.key == pygame.K_UP:
                y -= 20
            if x < width-25 and event.key == pygame.K_RIGHT:
                x += 20
            if x > 25 and event.key == pygame.K_LEFT:
                x -= 20

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)