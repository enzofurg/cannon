import pyxel
import math


class Elevation:
    def __init__(self):
        self.elevangle = 30
        self.elevrad = self.elevangle * math.pi/180
        self.min = 15
        self.max = 45
    def incdec(self,up,down):
        if down:
            self.elevangle -= 0.5
        elif up:
            self.elevangle += 0.5
        if self.elevangle < self.min:
            self.elevangle = self.min
        elif self.elevangle > self.max:
            self.elevangle = self.max
        self.elevrad = self.elevangle * math.pi/180
