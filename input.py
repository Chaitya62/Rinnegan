import pygame




width, height = (1920,1080)
# bg = pygame.image.load("hero.png")


WALK_AWAY = 1
EYE_EX =  2
PLAY_AROUND = 3

def text_objects(text, font):
    textSurface = font.render(text, True, green)
    return textSurface, textSurface.get_rect()


# bg = pygame.image.load("hero.png")

width, height = (1920,1080)


purple = (129,102,205)
orange = (255,200,76)
green  = (107,200,176)
white  = (255,255,255)

pygame.init()
BUTTON_LOC = (1610, 200, 300, 150)
BUTTON1_LOC = (1610, 400, 300, 150)
BUTTON2_LOC = (1610, 600, 300, 150)

def loop(quitf=True):
    pygame.init()
    screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
    font = pygame.font.Font("Raleway-Medium.ttf", 30)
    clock = pygame.time.Clock()
    button  = pygame.Rect(BUTTON_LOC)
    button1 = pygame.Rect(BUTTON1_LOC)
    button2 = pygame.Rect(BUTTON2_LOC)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if quitf:
                        pygame.quit()
                    if button.collidepoint(event.pos):
                        input = WALK_AWAY
                    if button1.collidepoint(event.pos):
                        input = EYE_EX
                    if button2.collidepoint(event.pos):
                        input = PLAY_AROUND

                    return input

                    # print(input)


        screen.fill(white)

        pygame.draw.rect(screen, purple, button)
        pygame.draw.rect(screen, orange, button1)
        pygame.draw.rect(screen, green, button2)
        img = pygame.image.load('activity.png')
        screen.blit(img, (300,250))
        new_game_text = font.render("Walk Away", False, white)
        new_game_rect = new_game_text.get_rect(center=button.center)
        new_game_text1 = font.render("Eye Exercise", False, white)
        new_game_rect1 = new_game_text.get_rect(center=button1.center)
        new_game_text2 = font.render("Play Around", False, white)
        new_game_rect2 = new_game_text.get_rect(center=button2.center)

        screen.blit(new_game_text, new_game_rect)
        screen.blit(new_game_text1, new_game_rect1)
        screen.blit(new_game_text2, new_game_rect2)

        mouse = pygame.mouse.get_pos()
        if 1610+300 > mouse[0] > 0 and 200+150 > mouse[1] > 200:
            pygame.draw.rect(screen, (52,29,114),(BUTTON_LOC))
            screen.blit(new_game_text, new_game_rect)
        elif 1610+300 > mouse[0] > 0 and 400+150 > mouse[1] > 400:
            pygame.draw.rect(screen, (249, 173, 0),(BUTTON1_LOC))
            screen.blit(new_game_text1, new_game_rect1)
        elif 1610+300 > mouse[0] > 0 and 600+150 > mouse[1] > 600:
            pygame.draw.rect(screen, (49, 132, 111),(BUTTON2_LOC))
            screen.blit(new_game_text2, new_game_rect2)

        # font1 = pygame.font.Font("Raleway-Medium.ttf", 120)
        # TextSurf, TextRect = text_objects("Choose An Activity", font1)
        # TextRect.center = (1300,500)
        # screen.blit(TextSurf, TextRect)
        pygame.display.update()

        clock.tick(30)



if __name__ == '__main__':
    loop()
    pygame.quit()
