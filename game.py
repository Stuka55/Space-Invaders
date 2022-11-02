import pygame as pg
from bunker import Bunkers
from settings import Settings
import game_functions as gf

from laser import Lasers
from alien import Aliens
from ship import Ship
from sound import Sound
from scoreboard import Scoreboard
from button import Button
import sys


class Game:
    def __init__(self, screen, highscore = 0):
        #pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = screen

        #self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Alien Invasion")

        self.sound = Sound(bg_music="sounds/startrek.wav")

        self.scoreboard = Scoreboard(game=self, highscore=highscore)  
        self.lasers = Lasers(settings=self.settings)
        self.ship = Ship(game=self, screen=self.screen, settings=self.settings, sound=self.sound, lasers=self.lasers)
        self.bunkers = Bunkers(game=self,screen=self.screen,settings=self.settings,lasers=self.lasers) #CUT
        self.aliens = Aliens(game=self, screen=self.screen, settings=self.settings, lasers=self.lasers, ship=self.ship, bunkers=self.bunkers)
        
        self.settings.initialize_speed_settings()

    def reset(self):
        print('Resetting game...')
        self.lasers.reset()
        self.ship.reset()
        self.aliens.reset()
        # self.scoreboard.reset()

    def game_over(self):
        print('All ships gone: game over!')
        self.sound.gameover()
        self.aliens.clearFleet()
        #print("high score is: " + str(self.scoreboard.high_score))
        main_menu(self.screen, self.scoreboard.high_score)
        #g.quit()
        #sys.exit()

    def play(self):
        self.sound.play_bg()
        #play_button = Button(msg="PLAY", screen=self.screen, xCoord=400, yCoord=400)
        #play_button.draw_button()
        
        while True:     # at the moment, only exits in gf.check_events if Ctrl/Cmd-Q pressed
            gf.check_events(settings=self.settings, ship=self.ship)
            self.screen.fill(self.settings.bg_color)
            self.ship.update()
            self.aliens.update()
            self.lasers.update()
            self.scoreboard.update()
            self.bunkers.update()#cut
            pg.display.flip()
            

def main_menu(screen, highscore = 0):
    pg.display.set_caption("MENU")
    screen.fill("red")
    #pg.display.flip()
    BG = pg.image.load('images/background.png')
    BG = pg.transform.scale(BG, (1200,800))
    screen.blit(BG, (0,0))
    play_button = Button(msg="PLAY", screen=screen, xCoord=475, yCoord=380)
    highscore_button = Button(msg="HIGHSCORE", screen=screen, xCoord=725, yCoord=380)

    play_button.draw_button()
    highscore_button.draw_button()
    pg.display.flip()

    while True:
        #screen.blit(background, (0,0))
        #screen.blit(pg.image.load('images/explode1.png'),(0,0))
        #play_button.draw_button()

        #MENU_MOUSE_POS = pg.mouse.get_pos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouseX, mouseY = pg.mouse.get_pos()

                if play_button.rect.collidepoint(mouseX,mouseY):
                    g = Game(screen, highscore=highscore)
                    g.play()
                elif highscore_button.rect.collidepoint(mouseX,mouseY):
                    highscore_menu(screen=screen, highscore=highscore)

def highscore_menu(screen, highscore = 0):
    pg.display.set_caption("HIGHSCORE")
    screen.fill("darkblue")
    
    back_button = Button("BACK", screen, 600, 700)
    back_button.draw_button()

    screen_rect = screen.get_rect()

    text_color = (255, 0, 0)
    font = pg.font.SysFont(None, 72)

    score_image = None
    score_rect = None

    score_str = "HIGHSCORE: " + str(highscore)
    score_image = font.render(score_str, True, text_color)

    score_rect = score_image.get_rect()
    score_rect.center = screen_rect.center

    screen.blit(score_image,score_rect)

    pg.display.flip()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                mouseX, mouseY = pg.mouse.get_pos()

                if back_button.rect.collidepoint(mouseX,mouseY):
                    #print("Back button pressed")
                    main_menu(screen=screen, highscore=highscore)
                
        

def main():
    pg.init()
    SCREEN = pg.display.set_mode((1200,800))

    pg.display.set_caption("Hello")
    main_menu(SCREEN)



    #g = Game(SCREEN)
    #g.play()


if __name__ == '__main__':
    main()
