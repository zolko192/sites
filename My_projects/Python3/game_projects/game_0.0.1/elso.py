import pygame

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
x, y = 20, 20
margin = 5
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            quit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        margin -= 1
        x += 1
    if key[pygame.K_RIGHT]:
        margin += 1
        x -= 1
    if key[pygame.K_UP]:
        margin += 1
        x -= 1
        y -= 1
    if key[pygame.K_DOWN]:
        margin -= 1
        x += 1
        y += 1

    screen.fill((255, 255, 255))
    for row in range(10):
        pygame.draw.rect(screen, pygame.Color("blue"), ((margin + x) * row + margin, y, 20, 20))

    pygame.display.update()

    clock.tick(60)