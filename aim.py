import pyxel
import math
import random

class Aim:
    def __init__(self, charge, elevation, angle, centrotuple):
        self.centrotuple=centrotuple
        self.distance= (25*charge)**2 * math.sin(2*elevation) / 9.8
        #print(self.distance)
        self.cords=(centrotuple[0]+self.distance*math.cos(angle), centrotuple[1]-self.distance*math.sin(angle))
        #print(self.cords)
    def draw(self, trueanglerad):
        pyxel.line(self.centrotuple[0],self.centrotuple[1],self.cords[0],self.cords[1], 13)
        pyxel.circb(self.centrotuple[0]+self.distance*math.cos(trueanglerad),self.centrotuple[1]-self.distance*math.sin(trueanglerad), 3, 13)
