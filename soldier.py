import pyxel
import math
import random

class Soldier:
    def __init__(self, x, y):
        self.dx = x
        self.x = x
        self.y = y
        self.intime = random.randint(1,6) + random.random()
    def hitcheck(self, hitcords, radius):
        self.hitdistance = math.sqrt((self.x-hitcords[0])**2 + (self.y-hitcords[1])**2)
        if self.hitdistance <= radius:
            return True
        else:
            return False
    def bordercheck(self, screenlength):
        if self.y>= screenlength -50:
            return True
        else:
            return False
    def draw(self):
        pyxel.circ(self.x,self.y, 3, 4)
        
    def update(self):
        self.intime += 1/12
        self.x = self.dx + 6*math.cos(self.intime)
        self.y+=1/12 * 3