import os
import time
import winsound

# from threading import Timer
# from test import hello
#
from eyeris_detector import  EyerisDetector, ImageSource, CascadeClassifier, LucasKanadeTracker

import pygame

from win10toast import ToastNotifier
from threading import Thread

from input import loop as input_loop
from input import WALK_AWAY, PLAY_AROUND, EYE_EX
from circle import circle as circle_game
from wave import wave as wave_game
from counter import timer_screen
from home import display_home
from glare_message import display_glare_message
from close_eyes import close_eye_screen
# STRING CONSTANTS
TITLE = "Rinnegan"
STARTUP_MESS = "The Rinnegan has started !!"
WORK_MESS = "Focus on your work for 25 minutes!!!"
BREAK_MESS = "You deserve a 5 mins break."
BLINK_MESS = "Maintain 10-15 blinks per minute."
LOOKAWAY_MESS = "Gotta look somewhere else for a while!"

LOGO_PATH = './assets/logo.ico'

called = False

# HYPER PARAMETERS
WORK_TIME = 0.5*60
BREAK_TIME = 0.2*60
STARTUP_TIME = 15
NOTIF_TIME = 15

GAME1_TIME = 10
GAME2_TIME = 10
CLOSE_TIME = 10
LOOK_AWAY_TIME = 10
# WORK_TIME = 15
# BREAK_TIME = 5
# STARTUP_TIME = 5
USE_CV = True

# VALUES
global_time = time.time()
last_called = time.time()



# games
games = [circle_game, wave_game]


def alarm(duration=3000, freq=440):
    # duration = 5000  # millisecond
    # freq = 440  # Hz
    winsound.Beep(freq, duration)


def test_glare():
    os.system("turnoff.exe")
    print("WHAt")
    return


def test_startup():
    print("STARTUP SCREEN WILL SHOW")
    #i = input("Press 'q' key to continue: ")
    return



def test_button_screen():
    print("Button screen to be called : ")
    x = input("Press 1. Walk away \n 2. Eye Excercise \n 3. PlayAround \n")
    return x


def call_screen(screen_id):

    if screen_id == 1:
        print("Show other screen with timer")
        timer_screen(BREAK_TIME)


    elif screen_id == 2:

            close_eye_screen(CLOSE_TIME, text="Close your eyes for a minute!", quitf=False)


            games[0](GAME1_TIME, quitf=False)


            close_eye_screen(LOOK_AWAY_TIME, text="Look away from the screen!", quitf=False)

            games[1](GAME2_TIME, quitf=False)

            close_eye_screen(CLOSE_TIME, text="Close your eyes for a minute again!")




    # elif screen_id == 3:
    #     return

    print("This {} screen was called : ".format(screen_id))
    return

def test_break_screen():

    global global_time
    get_screen_value = input_loop(quitf=False)
    if get_screen_value == 3:
        pygame.quit()
    global_time = time.time()
    call_screen(get_screen_value)

    return


def seconds_passed(old):

    return time.time()-old


# Initializations

toaster = ToastNotifier()



# FLAGS

first_run = True
first_five = True
is_break = False
blink_time = 10

blink_times = [4*60, 4*60, 12*60]
ix = 0

# toaster.show_toast("TEST", "TESTSETS T", duration=10)


while True:

    # print("MAIN Controller : ", eyeris_detector.blinks)


    if first_run:
        USE_CV = display_home()
        display_glare_message()
        test_startup()

        if USE_CV:
            eyeris_detector = EyerisDetector(image_source=ImageSource(), classifier=CascadeClassifier(),
                                             tracker=LucasKanadeTracker())
            tx = Thread(target=eyeris_detector.run, args=())
            tx.start()
        os.system("turnoff.exe")
        print("HERE!!!")
        first_run = False


    if USE_CV and seconds_passed(last_called) >= blink_time:

        print(eyeris_detector.blinks)
        if eyeris_detector.blinks < 40:
            print("KEEP BLINKING : ")
            toaster.show_toast(TITLE, BLINK_MESS, icon_path=LOGO_PATH, duration=NOTIF_TIME,threaded=True)

        eyeris_detector.reset_blinks()
        last_called = time.time()
        blink_time = 4*60

    if not USE_CV and seconds_passed(last_called) >= blink_time:

        blink_time = blink_times[ix%3]
        ix+=1
        if ix%3 == 0 and ix!=0:
            toaster.show_toast(TITLE, LOOKAWAY_MESS, icon_path=LOGO_PATH, duration=NOTIF_TIME,threaded=True)
            timer_screen(20)

    if first_five and seconds_passed(global_time) >= STARTUP_TIME:
        print("STARTED !!!")
        toaster.show_toast(TITLE, WORK_MESS, icon_path=LOGO_PATH,duration=NOTIF_TIME,threaded=True)
        first_five = False
        global_time = time.time()

    if seconds_passed(global_time) >= WORK_TIME:
        toaster.show_toast(TITLE, BREAK_MESS, icon_path=LOGO_PATH,duration=NOTIF_TIME,threaded=True)
        print("BREAK !!!")
        is_break = True
        global_time = time.time()
        test_break_screen()


    if seconds_passed(global_time) >= BREAK_TIME and is_break:
        toaster.show_toast(TITLE, WORK_MESS, icon_path=LOGO_PATH,duration=NOTIF_TIME,threaded=True)
        print("WORK!!")
        is_break = False
        global_time = time.time()



# take care of the blink thread if initialized
tx.join()
