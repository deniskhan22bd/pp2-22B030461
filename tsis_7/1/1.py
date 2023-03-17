import pygame
import datetime
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("1 task")

image = pygame.image.load(r"tsis_7\1\images\clock.png")
min_arr = pygame.image.load(r"tsis_7\1\images\min.png")
sec_arr = pygame.image.load(r"tsis_7\1\images\sec.png")
angle = 1

date = datetime.datetime.today()
seconds = date.second
minutes = date.minute
print(minutes)
running = True
while running:
    rotated_min = pygame.transform.rotate(min_arr, -50 - (minutes * 6))
    rotated_min_rect = rotated_min.get_rect(center = (700, 525))

    rotated_sec = pygame.transform.rotate(sec_arr, -(6 * seconds))
    rotated_sec_rect = rotated_sec.get_rect(center = (700, 525))

    screen.blit(image, (0, 0))
    screen.blit(rotated_min, rotated_min_rect)
    screen.blit(rotated_sec, rotated_sec_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


    date = datetime.datetime.today()
    seconds = date.second
    minutes = date.minute

    clock.tick(60)
    pygame.display.update()

