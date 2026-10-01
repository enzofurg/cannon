import pyxel
import math
import random

class Plane:
    def __init__(self):
        self.fpoint = (random.randint(-40,-30),random.randint(0,420))
        self.spoint = (random.randint(530,540),random.randint(0,420))
        if self.fpoint[1] < self.spoint[1]:
            self.anglerad = math.atan2(self.spoint[1]-self.fpoint[1],self.spoint[0]-self.fpoint[0])
            self.planetip = (self.fpoint[0]+math.cos(self.anglerad)*10,self.fpoint[1]+math.sin(self.anglerad)*10)
            self.wing1 = (self.fpoint[0]+math.cos(self.anglerad + math.pi/2)*5, self.fpoint[1]+math.sin(self.anglerad+math.pi/2)*5)
            self.wing2 = (self.fpoint[0]+math.cos(self.anglerad - + math.pi/math.pi/2)*5, self.fpoint[1]+math.sin(self.anglerad-math.pi/2)*5)
        else:
            self.anglerad = math.atan2(self.fpoint[1]-self.spoint[1],self.fpoint[0]-self.spoint[0])
            self.planetip = (self.spoint[0]+math.cos(self.anglerad)*10,self.spoint[1]+math.sin(self.anglerad)*10)
            self.wing1 = (self.spoint[0]+math.cos(self.anglerad + math.pi/2)*5, self.spoint[1]+math.sin(self.anglerad+math.pi/2)*5)
            self.wing2 = (self.spoint[0]+math.cos(self.anglerad - math.pi/2)*5, self.spoint[1]+math.sin(self.anglerad-math.pi/2)*5)

    def update(self):
        self.increment = (math.cos(self.anglerad)*(1/12)*12,math.sin(self.anglerad)*(1/12)*12)
        self.planetip = (self.planetip[0]+self.increment[0],self.planetip[1]+self.increment[1])
        self.wing1 = (self.wing1[0]+self.increment[0],self.wing1[1]+self.increment[1])
        self.wing2 = (self.wing2[0]+self.increment[0],self.wing2[1]+self.increment[1])

   
    def draw(self):
       # pyxel.text(100,100, str(self.anglerad*180/math.pi),8)

        pyxel.tri(self.planetip[0],self.planetip[1],self.wing1[0],self.wing1[0],self.wing2[0],self.wing2[1],8)
        pyxel.dither(0.7)
        pyxel.line(self.fpoint[0],self.fpoint[1],self.spoint[0],self.spoint[1], 14)
        pyxel.dither(1)
    #def update(self):
        #self.y+=1/12