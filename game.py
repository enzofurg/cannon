import pyxel
import math
import random

from main_menu import MainMenu
from level import Level

class Game:
    STATE_MENU = 0
    STATE_LEVEL = 0
    
    

    def __init__(self):
        self.state = STATE_MENU
        self.main_menu = MainMenu(self)
        self.level = Level(STATE_LEVEL)

    def new_game(self):
        self.state = STATE_LEVEL

    def game_over(self):
        self.state = STATE_MENU
    def update(self):
        if self.state == STATE_MENU:
            self.main_menu.update()
        elif self.state == STATE_LEVEL:
            self.level.update()

    def draw(self):
        if self.state == STATE_MENU:
            self.main_menu.draw()
        elif self.state == STATE_LEVEL:
            self.level.draw()
