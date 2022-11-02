import pygame as pg 
# import pygame.font

class Scoreboard:
    def __init__(self, game, highscore = 0): 
        self.score = 0
        self.level = 0
        #self.high_score
        self.high_score = highscore
        
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None

        self.high_score_image = None
        self.high_score_rect = None
        
        self.prep_score()

    def increment_score(self, value): 
        self.score += value
        self.prep_score()

    def prep_score(self):
        if self.score >= self.high_score:
            self.high_score = self.score 
        
        score_str = "Score: " + str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        highScore_str = "Highscore: " + str(self.high_score)
        self.high_score_image = self.font.render(highScore_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

        # display high score
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = 20
        self.high_score_rect.top = 20

    def reset(self):
        if self.score >= self.high_score:
            self.high_score = self.score 
        #print("sdfghjklkjhgfdrghjklkjhgfdfghjkljhgfds" + str(self.high_score))
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        self.draw()

    def draw(self): 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)