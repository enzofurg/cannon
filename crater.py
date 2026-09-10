import pyxel
import math
import random

class Crater:
    def __init__(self, cords):
        self.cords = cords
    def draw(self):
        pyxel.dither(0.5)
        pyxel.circ(self.cords[0], self.cords[1], 5, 13)
        pyxel.dither(1)
