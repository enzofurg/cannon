import pyxel
import math
import random

class Tank:
    def __init__(self):
        self.x = random.randint(10,480)
        self.y = random.randint(40,70)
    def hitcheck(self, hitcords, radius):
        self.hitdistance = math.sqrt((self.x-hitcords[0])**2 + (self.y-hitcords[1])**2)
        if self.hitdistance <= radius:
            print("Acerto")
            return True
        else:
            return False
    def bordercheck(self, screenlength):
        if self.y>= screenlength -50:
            return True
        else:
            return False
    def draw(self):
        pyxel.rect(self.x-3,self.y-5,7,11,11)
        pyxel.dither(0.5)
        #pyxel.rect(self.x-3,self.y-5,7,11,0)
        pyxel.dither(1)
        pyxel.circ(self.x,self.y,2,3)
        pyxel.line(self.x,self.y,self.x,self.y+12,11)
        pyxel.circ(self.x,self.y+12,1,11)
        
    def update(self):
        self.y+=1/12 * 2