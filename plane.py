import pyxel
import math
import random

class Plane:
    def __init__(self):
        self.fpoint = (random.randint(-500,-30),random.randint(0,420))
        self.spoint = (random.randint(530,1000),random.randint(0,420))
   
    def draw(self):
        pyxel.dither(0.7)
        pyxel.line(self.fpoint[0],self.fpoint[1],self.spoint[0],self.spoint[1], 14)
        pyxel.dither(1)
    #def update(self):
        #self.y+=1/12