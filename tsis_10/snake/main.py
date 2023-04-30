import random
import pygame
import time
import psycopg2
pygame.init()

# db 
SCORE = 0
name = ""
while True:
    name = input("Enter your name: ")
    if name != "":
        break

connection = psycopg2.connect(
host="localhost",
database="postgres",
user="postgres",
password="123"
) 

cur = connection.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS scores(
            name VARCHAR(50) PRIMARY KEY,
            score INT);""")


#level map
walls = []

#const vars
FPS = 8
LEVEL = 0
FONT = pygame.font.SysFont("Verdana", 20, True)
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
Block = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
Block.fill("Grey")

class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)
        self.surf = pygame.Surface((BLOCK_SIZE, BLOCK_SIZE))
        self.surf_rect = self.surf.get_rect(center = (BLOCK_SIZE / 2, BLOCK_SIZE / 2))
    def draw(self, w, w_rect):
        self.surf.fill("Green")
        self.surf.blit(w, w_rect)
        SCREEN.blit(self.surf, (self.location.x * BLOCK_SIZE, self.location.y * BLOCK_SIZE))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            )
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)

def game_over():
    SCREEN.fill("BLACK")
    GameOver = FONT.render("Game Over", True, "red")
    GameOver_rect = GameOver.get_rect(center = (400, 400))
    SCREEN.blit(GameOver, GameOver_rect)
    pygame.display.flip()
    game_over_music = pygame.mixer.Sound("tsis_9\snake\gameover.wav")
    game_over_music.play()
    time.sleep(1.5)
    pygame.quit()
    quit()

def foodinsnake(x, y):
    for i in snake.body:
        if (x, y) in (i.x, i.y):
            return False
    return True

# Randomly generating coins with different weights on the road
weight = random.choice([1, 3, 5])
w = FONT.render(str(weight), True, "Black")
w_rect = w.get_rect(center = (BLOCK_SIZE / 2, BLOCK_SIZE / 2))

def save():
    cur.execute(f"SELECT score FROM scores WHERE name = '{name}'")
    scores = cur.fetchone()
    cur.execute(f"SELECT name FROM scores WHERE name = '{name}'")
    data = cur.fetchone()
    if data is not None:
        if scores[0] < SCORE:
            cur.execute(f"UPDATE scores SET score = {SCORE} WHERE name = '{name}'")
    else:
        cur.execute(f"INSERT INTO scores (name, score) VALUES ('{name}', {SCORE})")
        
    connection.commit()
    cur.close()
    connection.close()

def pause(cond):
    while cond:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cond = False


# vars
running = True
snake = Snake()
blocks = []
food = Food(random.randint(1, WIDTH // BLOCK_SIZE - 2), random.randint(1, WIDTH // BLOCK_SIZE - 2))
dx, dy = 0, 0
curr_key = None
curr_score = 0
timer = 0
levelupscore = 10
while running:
    SCREEN.fill(BLACK)
    #block.draw()
    Score = FONT.render(f"Score:{SCORE}", True, "red")
    Level = FONT.render(f"Level:{LEVEL}", True, "red")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and curr_key != "S":
                dx, dy = 0, -1
                curr_key = "W"
            elif event.key == pygame.K_s and curr_key != "W":
                dx, dy = 0, +1
                curr_key = "S"
            elif event.key == pygame.K_d and curr_key != "A":
                dx, dy = 1, 0
                curr_key = "D"
            elif event.key == pygame.K_a and curr_key != "D":
                dx, dy = -1, 0
                curr_key = "A"
            if event.key == pygame.K_SPACE:
                pause(True)
  
    #checking border
    if snake.body[0].x <= 0:
        save()
        game_over()
    if snake.body[0].x >= 19:
        save()
        game_over()
    if snake.body[0].y >= 19:
        save()
        game_over()
    if snake.body[0].y <= 0:
        save()
        game_over()
    
    #moving
    snake.move(dx, dy)

    # checking collision 
    if snake.check_collision(food):
        timer = 0
        curr_score += 1
        SCORE += weight 
        snake.body.append(
            Point(snake.body[-1].x, snake.body[-1].y)
        )
        while True:
            food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
            if (food.location.x, food.location.y) not in walls and foodinsnake(food.location.x, food.location.y):
                break

        weight = random.choice([1, 3, 5])
        w = FONT.render(str(weight), True, "Black")
        w_rect = w.get_rect(center = (BLOCK_SIZE / 2, BLOCK_SIZE / 2))
    else:
        timer += 1
        if timer == 40:
            timer = 0
            food.location.x = random.randint(1, WIDTH // BLOCK_SIZE - 2)
            food.location.y = random.randint(1, HEIGHT // BLOCK_SIZE - 2)
        for body in snake.body[1:]:
            if snake.body[0].x == body.x and snake.body[0].y == body.y:
                save()
                game_over()

    # level and speed
    if SCORE >= levelupscore:
        LEVEL += 1
        FPS += 1
        levelupscore = levelupscore * 2
        walls.append((random.randint(1, 10), random.randint(10, 20)))
        walls.append((random.randint(1, 10), random.randint(10, 20)))

    if LEVEL >= 1:
        for i in walls:
            SCREEN.blit(Block, (i[0] * BLOCK_SIZE, i[1] * BLOCK_SIZE))
            if snake.body[0].x == i[0] and snake.body[0].y == i[1]:
                save()
                game_over()

    # draw
    for i in blocks:
        i.draw()
    snake.draw()
    food.draw(w, w_rect)
    draw_grid()
    SCREEN.blit(Score, (0, 0))
    SCREEN.blit(Level, (0, 20))

    pygame.display.flip()
    clock.tick(FPS)

print("GAGAGAGG")
