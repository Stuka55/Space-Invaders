import pygame as pg
from pygame.sprite import Sprite,Group
from laser import Lasers

class Bunker(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pg.image.load('images/bunker.png')
        self.image = pg.transform.scale(self.image, (150,48))
        self.rect = self.image.get_rect()

        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        self.draw()

    def draw(self):
        image = self.image
        rect = image.get_rect()

        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image,rect)

class Bunkers:
    def __init__(self, game, screen, settings, lasers: Lasers):
        self.game = game
        self.bunkers = Group()
        self.screen = screen
        self.lasers = lasers.lasers
        self.settings = settings
        self.create_bunkers()

    def create_bunkers(self):
        self.create_bunker(182, 700)
        self.create_bunker(460, 700)
        self.create_bunker(742, 700)
        self.create_bunker(1024, 700)

    def create_bunker(self, x, y):
        print("BUNKER CREATED")
        bunker = Bunker(self.screen, self.settings)

        bunker.rect.centerx = x
        bunker.rect.centery = y

        self.bunkers.add(bunker)

    def check_collision(self):
        collisions = pg.sprite.groupcollide(self.bunkers, self.lasers, False, True)
        if collisions:
            for laser in collisions:
                laser.remove()

    def update(self):
        self.check_collision()
        for bunker in self.bunkers.sprites():
            bunker.update()

    def draw(self):
        for bunker in self.bunkers.sprite():
            bunker.draw()

        
