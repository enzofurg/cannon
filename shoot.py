import pyxel
import math
import random
from crater import Crater


class Shoot:
    def __init__(self, charge, elevation, angle, centrotuple, time):
        self.abstime=time
        self.centrocords = centrotuple
        self.angle = angle
        self.distance= (25*charge)**2 * math.sin(2*elevation) / 9.8
        self.height = 0
        self.hspeed = (25*charge)*math.sin(elevation)
        self.traveltime= time + 2 * (25*charge*math.sin(elevation)) / 9.8
        print(self.traveltime)
        
        self.speed = self.distance / (self.traveltime-time)
        print(self.speed)
        self.cords=(centrotuple[0]+self.distance*math.cos(angle), centrotuple[1]-self.distance*math.sin(angle))
        self.cordstx = centrotuple[0]
        self.cordsty = centrotuple[1]
        
        #self.cordstx = self.centrocords[0] + self.distance * math.cos(self.angle) * (time - self.abstime)/12
        #self.cordsty = self.centrocords[1] - self.distance * math.sin(self.angle) * (time - self.abstime)/12
        
        #print(self.cords)
    def move(self, time):
        self.cordstx += self.speed * math.cos(self.angle)/12
        self.cordsty -= self.speed * math.sin(self.angle)/12
        self.hspeed = self.hspeed - 9.8/12
        self.height += self.hspeed/12
        print(self.hspeed)
        #if self.cordstx>self.cords[0] or self.cordsty<self.cords[1]:
        if time > self.traveltime:
            self.cordstx = self.cords[0]
            self.cordsty = self.cords[1]

    def animate(self, time):
        

        #print(self.cordstx, self.cordsty)

        pyxel.circ(self.cordstx,self.cordsty, 2+abs(self.height/30), 10)
        if time > self.traveltime:

            pyxel.circ(self.cords[0],self.cords[1], 8, 8)
            pyxel.circ(self.cords[0],self.cords[1], 7, 10)
            pyxel.circ(self.cords[0],self.cords[1], 5, 7)
