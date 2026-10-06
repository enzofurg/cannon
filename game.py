#import pyxel
import math
import random

from main_menu import MainMenu
from level import Level

class Game:

    def __init__(self):
        self.state = "menu"
        self.levelnum = 1
        self.main_menu = MainMenu(self)
        self.levels=[Level(self.levelnum, self)]
        #self.level = Level(self.levelnum, self)

    def new_game(self):
        self.state = "level"
        self.levelnum = 1
        self.levels=[Level(self.levelnum, self)]

    def game_over(self):
        self.state = "menu"
        self.levelnum = 0
        self.levels=[]
    def update(self):
        if self.state == "menu":
            self.main_menu.update()
        elif self.state == "level":
            #self.level.update()
            self.levels[0].update()

    def draw(self):
        if self.state == "menu":
            self.main_menu.draw()
        elif self.state == "level":
            #self.level.draw()
            self.levels[0].draw()
