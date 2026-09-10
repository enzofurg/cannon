import pyxel
import math
import random

class Target:
    def __init__(self):
        self.x= random.randint(10,480)
        self.y= random.randint(60,400)
    def spawn(self):
        pyxel.circ(self.x, self.y, 4, 8)
        pyxel.circ(self.x, self.y, 3, 7)
        pyxel.circ(self.x, self.y, 2, 8)
        pyxel.circ(self.x, self.y, 1, 7)
        pyxel.circ(self.x, self.y, 0, 8)
    def hitcheck(self, hitcords, radius):
        #if (pyxel.pget(self.cords[0], self.cords[1])) == 7 or (pyxel.pget(self.cords[0], self.cords[1])) == 8:
            #print("Acerto")
        self.hitdistance = math.sqrt((self.x-hitcords[0])**2 + (self.y-hitcords[1])**2)
        if self.hitdistance <= radius:
            print("Acerto")
            return True
        else:
            return False