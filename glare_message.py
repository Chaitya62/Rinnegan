import pygame as pg


BUTTON_LOC = (840, 450, 250, 75)
orange = (255,200,76)
green  = (107,200,176)

def display_glare_message():
    pg.init()
    width,height=(1920,1080)
    screen = pg.display.set_mode((width,height), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    done = False
    widgets = []

    purple = (129,102,205)
    def text_objects(text, font):
        textSurface = font.render(text, True,purple)
        return textSurface, textSurface.get_rect()


    font = pg.font.Font("Raleway-Medium.ttf", 30)



    flag=0
    while not done:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                done = True
        largeText = pg.font.Font('Raleway-Medium.ttf',30)
        TextSurf, TextRect = text_objects("In the next screen, adjust your screen such that glare is minimum, after adjusting, press space to continue.", largeText)
        TextRect.center = (950,400)
        screen.blit(TextSurf, TextRect)
        TextSurf, TextRect = text_objects("-- Press Space to Continue --", font)
        TextRect.center = (950,800)
        screen.blit(TextSurf, TextRect)

        pg.display.flip()
        screen.fill((255,255,255))
    pg.quit()

# display_warning()
