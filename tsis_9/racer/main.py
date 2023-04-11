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
        self.image = pygame.Surface((50, 100))
        self.image.fill("Blue")
        self.rect = self.image.get_rect(center = (400, 700))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.left > 155:
            self.rect.move_ip(-5, 0)
        if keys[pygame.K_d] and self.rect.right < W - 155:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 100))
        self.image.fill("Red")
        self.rect = self.image.get_rect(center = (random.randint(200, W - 200), 75))

    def update(self):
        if self.rect.y < H - 20:
            self.rect.y += Speed
        else:
            self.rect.center = (random.randint(200, W - 200), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill("Yellow")
        self.rect = self.image.get_rect(center = (random.randint(200, W - 200), 700))
    def update(self):
       self.image.fill("Yellow")
       self.rect.center = (random.randint(200, W - 200), 700)

def game_over():
    game_over_music = pygame.mixer.Sound(r"tsis_9\racer\music\gameover.wav")
    game_over_music.play()
    time.sleep(0.1)
    screen.fill("RED")
    screen.blit(big_font.render("Game Over", True, "Black"), (200, 350))
    pygame.display.update()
    for entity in all_sprites:
        entity.kill()
    time.sleep(1.5)
    pygame.quit()

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

# Randomly generating coins with different weights on the road
weight = random.choice([1, 3, 5])
w = small_font.render(str(weight), True, "Black")
w_rect = w.get_rect(center = (15, 15))
C1.image.blit(w, w_rect)

#Game Loop
running = True
while running:
    #Screen
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, "white", (150, 0), (150, H), 10)
    pygame.draw.line(screen, "white", (W - 150, 0), (W - 150, H), 10)
    Score = small_font.render(f"Score:{SCORE}", True, "Red")
    screen.blit(Score, (640, 0))

    #Moves and Re-draws all Sprites
    
    #To be run if collision occurs between Player and Enemy and Player and Coin
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over()

    #Randomly generating coins with different weights on the road
    if pygame.sprite.spritecollideany(P1, coins):
        SCORE += weight
        coins.update()
        weight = random.choice([1, 3, 5])
        w = small_font.render(str(weight), True, "Black")
        w_rect = w.get_rect(center = (15, 15))
        C1.image.blit(w, w_rect)
        Speed += 0.2

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.update()
    screen.blit(C1.image, C1.rect)


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    pygame.display.update()