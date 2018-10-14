import pygame as pg
import math
import time

def text_objects(text, font):
    textSurface = font.render(text, True, font_color)
    return textSurface, textSurface.get_rect()

# Colors
font_color = (255,200,76)
ball_color = (129,102,205)
white = (245,245,245)


w = 1920
h = 1080


radius = 20
width = 0
originX = 1000
originY = 500
flag=0

def circle(time_to_run, quitf=True):

    local_time = time.time()
    pg.init()
    t = 0
    screen = pg.display.set_mode((w,h),pg.FULLSCREEN)
    running = True
    while running:

        if (time.time()-local_time)>= time_to_run:
            running = False

        # for event in pg.event.get():
        #     if event.type == pg.KEYDOWN:
        #         running = False
        x = int(round(originX + math.cos(t)*800))
        y = int(round(originY + math.sin(t)*450))
        t+=0.01
        t %= (360)
        position = (x, y)
        screen.fill(white)
        largeText = pg.font.Font('Raleway-Medium.ttf',60)
        pg.draw.circle(screen,ball_color, position, radius, width)
        TextSurf, TextRect = text_objects("Follow the Dot", largeText)
        TextRect.center = ((950),(500))
        screen.blit(TextSurf, TextRect)
        pg.display.flip()
        milliseconds = 10
        pg.time.delay(milliseconds)

    if quitf:
        pg.display.quit()
        pg.quit()



if __name__ == '__main__':
    circle()
