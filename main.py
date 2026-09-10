import pyxel
import math
import random
from game import Game

class App:
    def __init__(self):
        self.tempo = 1
        self.screenwidth = 500
        self.screenlength = 600
        pyxel.init(self.screenwidth,self.screenlength, title="Cannon",fps=12)

        self.game = Game()

        pyxel.run(self.update,self.draw)
        pass

    def update(self):
        self.game.update()
        pass

    def draw(self):
        self.game.draw()

        pass