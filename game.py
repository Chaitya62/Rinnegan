import pygame, sys
import pyautogui
import time


#Initiate pygame
pygame.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)

color = [WHITE, BLACK, RED, YELLOW]

width, height = pyautogui.size()

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


cnt = 0

game_over = False
while not game_over:

    # XXX draw all the objects here

    # overlays.draw(screen)
    screen.fill(color[cnt%4])
    cnt+=1
    pygame.display.flip()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            pressed_key = event.key
            game_over = True

#
# #Set up main menu window
# while True:
#     pygame.display.set_caption("Test")
#     window.fill(color[-1])
#
#     keys=pygame.key.get_pressed()
#
#     if keys[ord('q')] == 1:
#         break
#
#     cnt+=1
#
#     time.sleep(1/30)
#     # title = pygame.image.load('title.bmp')
#     # start = pygame.image.load('enter.bmp')
#     # blank = pygame.image.load('blank.bmp')
#     # window.blit(title, (100, 200))
#     pygame.display.flip()
