
import pygame as pg

def display_home():

    pg.init()
    width,height=(1920,1080)
    screen = pg.display.set_mode((width,height), pg.FULLSCREEN)
    screen_rect = screen.get_rect()
    done = False
    widgets = []
    red = (247,132,138)
    purple = (129,102,205)

    def text_objects(text, font):
        textSurface = font.render(text, True,purple )
        return textSurface, textSurface.get_rect()

    BUTTON_LOC = (840, 450, 125, 75)
    BUTTON1_LOC = (975, 450, 125, 75)
    orange = (255,200,76)
    grey = (173, 173, 166)
    green  = (107,200,176)
    font = pg.font.Font("Raleway-Medium.ttf", 30)
    clock = pg.time.Clock()


    flag = -1
    while not done:
        # for event in pg.event.get():
        #     if event.type == pg.KEYDOWN:
        #         done = True
        largeText = pg.font.Font('Raleway-Medium.ttf',80)
        TextSurf, TextRect = text_objects("Welcome to Rinnegan!", largeText)
        TextRect.center = (950,200)
        screen.blit(TextSurf, TextRect)
        button  = pg.Rect(BUTTON_LOC)
        button1 = pg.Rect(BUTTON1_LOC)
        TextSurf, TextRect = text_objects("Enable Blink Tracking?", font)
        TextRect.center = (960,400)
        screen.blit(TextSurf, TextRect)
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("HERE !!!!")
                    if button.collidepoint(event.pos):
                        print("ALSO HERE!!!!!")
                        flag = 1
                    if button1.collidepoint(event.pos):
                        print("NO BUTTON CLICKED")
                        flag = 0
            if event.type == pg.KEYDOWN:
                done = True



        new_game_text = font.render("Yes", False, (255,255,255))
        new_game_text1 = font.render("No", False, (255,255,255))

        if flag == -1:
            pg.draw.rect(screen, grey,(BUTTON_LOC))
            pg.draw.rect(screen, grey, (BUTTON1_LOC))

        if flag==1:
            pg.draw.rect(screen, green,(BUTTON_LOC))
            pg.draw.rect(screen, grey, (BUTTON1_LOC))
            # new_game_rect1 = new_game_text1.get_rect(center=button1.center)
            # new_game_rect = new_game_text.get_rect(center=button.center)

        if flag == 0:
            pg.draw.rect(screen, grey,(BUTTON_LOC))
            pg.draw.rect(screen, red, (BUTTON1_LOC))

        new_game_rect1 = new_game_text1.get_rect(center=button1.center)
        new_game_rect = new_game_text.get_rect(center=button.center)


        # pg.draw.rect(screen, (255, 0, 0), (BUTTON1_LOC))
        # new_game_rect1 = new_game_text.get_rect(center=button1.center)

        screen.blit(new_game_text1, new_game_rect1)
        screen.blit(new_game_text, new_game_rect)
        font1 = pg.font.Font('Raleway-Medium.ttf',30)
        TextSurf, TextRect = text_objects("-- Press Space to Continue --", font1)
        TextRect.center = (950,800)
        screen.blit(TextSurf, TextRect)
        pg.display.flip()
        screen.fill((255,255,255))

        # clock.tick(60)

    return flag


if __name__ == '__main__':
    display_home()
