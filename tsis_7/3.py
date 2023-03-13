import pygame

clock = pygame.time.Clock()

pygame.init()

screen = pygame.display.set_mode((600, 600))
background = pygame.Surface((600, 600))
background.fill("white")
pygame.display.set_caption("task 3")

pos_x = 200
pos_y = 200
move = 20

keys = pygame.key.get_pressed()


running = True
while running:
    clock.tick(60)

    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, "Red", (pos_x, pos_y), 25)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and pos_x < 600 - 40:
        pos_x += move
    elif keys[pygame.K_LEFT] and pos_x > 0 + 40:
        pos_x -= move
    elif keys[pygame.K_DOWN] and pos_y < 600 - 40:
        pos_y += move
    elif keys[pygame.K_UP] and pos_y > 0 + 40:
        pos_y -= move


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        else:
            event.dict.keys()

    pygame.display.update()