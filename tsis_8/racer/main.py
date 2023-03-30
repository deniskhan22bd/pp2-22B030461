import pygame
import random
import time

pygame.init()

#Vars
W, H = 800, 800
FPS = 60
Speed = 10
SCORE = 0

#Display, font
screen = pygame.display.set_mode((W, H))
background = pygame.Surface((W, H))
big_font = pygame.font.SysFont("Verdana", 70)
small_font = pygame.font.SysFont("Verdana", 30)

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"tsis_8\racer\images\car1.png"), (80, 150))
        self.rect = self.image.get_rect(center = (400, 700))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 150:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_d] and self.rect.right < W - 150:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"tsis_8\racer\images\car2.png"), (80, 150))
        self.rect = self.image.get_rect(center = (random.randint(200, W - 200), 75))

    def update(self):
        if self.rect.y < H - 20:
            self.rect.y += Speed
        else:
            self.rect.center = (random.randint(200, W - 200), 75)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"tsis_8\racer\images\coin.png"), (40, 40))
        self.rect = self.image.get_rect(center = (random.randint(200, W - 200), 700))
    def update(self):
       self.rect.center = (random.randint(200, W - 200), 700)

#Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Game Loop
running = True
while running:
    #Screen
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, "white", (150, 0), (150, H), 10)
    pygame.draw.line(screen, "white", (W - 150, 0), (W - 150, H), 10)
    Score = small_font.render(f"Score:{SCORE}", True, "Red")
    screen.blit(Score, (0, 0))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.update()
    screen.blit(C1.image, C1.rect)

    #To be run if collision occurs between Player and Enemy and Player and Coin
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)
        screen.fill("RED")
        screen.blit(big_font.render("Game Over", True, "Black"), (200, 350))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()

    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += 1
        Speed += 0.5
        coins.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()