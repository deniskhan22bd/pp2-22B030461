import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
sound = [
    pygame.mixer.Sound(r"tsis_7\2\sounds\mixkit-keyboard-typing-1386.wav"),
    pygame.mixer.Sound(r"tsis_7\2\sounds\mixkit-little-birds-singing-in-the-trees-17.wav"),
    pygame.mixer.Sound(r"tsis_7\2\sounds\mixkit-tick-tock-clock-timer-1045.wav")
]
sound_name = [
    "Keyboard typing",
    "Birds singing",
    "Tick tock clock"
]
sound_cnt = 0

myfont = pygame.font.SysFont("comicsansms", 30)

playmusic = myfont.render("Press Space to play music", True, (0, 128, 0))
nextmusic = myfont.render("Press D to play next music", True, (0, 128, 0))
stopmusic = myfont.render("Press S to stop music", True, (0, 128, 0))
previousmusic = myfont.render("Press A to play previous music", True, (0, 128, 0))


musis_on = False

running = True
while running:
    screen.blit(background, (0, 0))
    screen.blit(playmusic, (50, 0))
    screen.blit(nextmusic, (50, 100))
    screen.blit(stopmusic, (50, 200))
    screen.blit(previousmusic, (50, 300))
    screen.blit(myfont.render(f"Music name : {sound_name[sound_cnt]}", True, (0, 128, 0)), (50, 400))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not musis_on:
                musis_on = True
                sound[sound_cnt].play()
            elif event.key == pygame.K_d:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt += 1
                if sound_cnt >= len(sound):
                    sound_cnt = 0
                sound[sound_cnt].play()
            elif event.key == pygame.K_s:
                musis_on = False
                sound[sound_cnt].stop()
            elif event.key == pygame.K_a:
                musis_on = True
                sound[sound_cnt].stop()
                sound_cnt -= 1
                if sound_cnt < 0:
                    sound_cnt = len(sound) - 1
                sound[sound_cnt].play()

    pygame.display.update()