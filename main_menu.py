import pyxel
import math
import random
import game

class MainMenu:
    def __init__(self, game):
        self.game = game

    def update(self):
        if pyxel.btn(pyxel.KEY_RETURN):
            self.game.new_game()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(100, 100, "Lorem Ipsum", 7)