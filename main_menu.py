import pyxel
import math
import random
import game

class MainMenu:
    def __init__(self, game):
        self.levelnum = 1
        self.game = game

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.levelnum += 1
            if self.levelnum > 3:
                self.levelnum = 3
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.levelnum -= 1
            if self.levelnum < 1:
                self.levelnum = 1
        if pyxel.btn(pyxel.KEY_RETURN):
            self.game.new_game(self.levelnum)

    def draw(self):
        pyxel.cls(0)
        pyxel.text(100, 100, "Cannon", 7)
        pyxel.text(100,120,f"SELECIONE O NÍVEL: {self.levelnum}",7)