import math
import pygame
import time

def text_objects(text, font):
    textSurface = font.render(text, True, (255,200,76))
    return textSurface, textSurface.get_rect()



def wave(time_to_run, quitf=True):

    local_time = time.time()
    pygame.init()
    screen = pygame.display.set_mode((1920,1080), pygame.FULLSCREEN)
    t = 0
    white = (245,245,245)
    color = (129,102,205)
    running = True

    while running:

        if (time.time()-local_time) >= time_to_run:
            running = False


        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         running = False
        x = t
        y = math.sin(t/50.0) * 500 + 400
        t+=10
        t%=(4 *540)
        y = int(y)
        screen.fill(white)
        pygame.draw.circle(screen, color, (x, y+100), 20)
        largeText = pygame.font.Font('Raleway-Medium.ttf',60)

        # pygame.draw.circle(screen,color, position, radius, width)
        TextSurf, TextRect = text_objects("Follow the Dot", largeText)
        TextRect.center = ((950),(500))
        screen.blit(TextSurf, TextRect)
        pygame.display.flip()
        milliseconds = 30
        pygame.time.delay(milliseconds)

    if quitf:
        pygame.display.quit()
        pygame.quit()


if __name__ == '__main__':
    wave()
