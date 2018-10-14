import pygame
import time as tl
import winsound
from pygame import *
import sys




s = None

def alarm(duration=3000, freq=440):
    global s
    # duration = 5000  # millisecond
    # freq = 440  # Hz
    # winsound.Beep(freq, duration)

    mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
    WAVFILE = './music.wav'
    s = pygame.mixer.Sound(WAVFILE)

    # pygame.init()

    ch = s.play()



def text_objects(text, font):
    textSurface = font.render(text, True, (255,200,76))
    return textSurface, textSurface.get_rect()


def format(num):

    if num <= 9:
        return '0'+str(num)

    return str(num)

def close_eye_screen(count_till, text, quitf=True):
    pygame.init()
    width, height = 1920,1080
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    running = True
    largeText = pygame.font.Font('Raleway-Medium.ttf',110)
    message_text = pygame.font.Font('Raleway-Medium.ttf', 65)



    mess = ""
    is_alarm = False

    while running:


        minutes = int(count_till/60)
        seconds = int(count_till%60)

        screen.fill((255, 255, 255))

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if count_till <= 0:
                    running = False



        TextSurf, TextRect = None, None

        if count_till == 0:
            mess = "Press any key to continue"
            if not is_alarm:
                alarm()
                is_alarm = True
            TextSurf, TextRect = text_objects(mess, message_text)

        else:
            mess = format(minutes)+":"+format(seconds)
            TextSurf, TextRect = text_objects(mess, largeText)
            count_till-=1

        # pygame.draw.circle(screen,color, position, radius, width)
        MessSurf, MessRect = text_objects(text, message_text)

        MessRect.center = (950, 300)
        TextRect.center = ((950),(500))
        screen.blit(TextSurf, TextRect)
        screen.blit(MessSurf, MessRect)

        pygame.display.flip()
        tl.sleep(1)


    s.stop()
    if quitf:
        pygame.quit()



if __name__ == '__main__':
    close_eye_screen(3, "Alarm")
