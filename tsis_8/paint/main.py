import pygame

pygame.init()

H = 800
W = 800
screen = pygame.display.set_mode((H, W))
screen.fill("White")
color = "Red"
mode = "Pen"
pos = ()
points = []
rect_w = 0
rect_h = 0
def eraser(pos):
    pygame.draw.circle(screen, "White", pos, 15)

def pen(pos, color):
    pygame.draw.circle(screen, color, pos, 5)

class Rectangle():
    def __init__(self):
        pass

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = "Red"
            elif event.key == pygame.K_g:
                color = "Green"
            elif event.key == pygame.K_b:
                color = "Blue"

            if event.key == pygame.K_1:
                mode = "Circle"
            elif event.key == pygame.K_2:
                mode = "Pen"
            elif event.key == pygame.K_3:
                mode = "Rect"
            elif event.key == pygame.K_4:
                mode = "Eraser"

        if event.type == pygame.MOUSEBUTTONDOWN and mode == "Circle":
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen, color, pos, 30)
        elif event.type == pygame.MOUSEBUTTONDOWN and mode == "Rect":
            pos = pygame.mouse.get_pos()
            pygame.draw.rect(screen, color, (pos[0], pos[1], 80, 60))

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0] == True:
            pos = pygame.mouse.get_pos()
            if mode == "Pen":
                pen(pos, color)
            if mode == "Eraser":
                eraser(pos)

    pygame.display.flip()