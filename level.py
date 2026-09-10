import math

import pyxel
import random
from aim import Aim
from shoot import Shoot
from tank import Tank
from target import Target

class Level:
    def __init__(self, levelnumber):

        self.trueaim = (pyxel.mouse_x, pyxel.mouse_y)
        self.delayaim = self.trueaim
        self.tshot = 1
        self.cannontip=(0,0)
        self.anglerad=0
        self.angle = 0
        self.elevation = 30
        self.elevationrad = 0
        self.charge=1
        self.fire=False
        self.craters = []
        self.tiros = []
        self.alvos = []
        self.tanques = []
        
        self.levelnumber=levelnumber
        self.tanques=[]
        self.alvos=[]
        self.crateres=[]
        
        if self.levelnumber == 0:
          for i in range(10):
                self.alvos.append(Target())
        elif self.levelnumber == 1:
            for i in range(10):
                self.tanques.append(Tank())

    def update(self):
        self.trueaim = (pyxel.mouse_x, pyxel.mouse_y)

        for x  in range(20):
            if self.trueaim[0] - self.delayaim[0] > 0.5:
                self.delayaim = (self.delayaim[0]+0.5, self.delayaim[1])
            elif self.trueaim[0] - self.delayaim[0] < -0.5:
                self.delayaim = (self.delayaim[0]-0.5, self.delayaim[1])

            if self.trueaim[1] - self.delayaim[1] > 0.5:
                self.delayaim = (self.delayaim[0], self.delayaim[1]+0.5)
            elif self.trueaim[1] - self.delayaim[1] < -0.5:
                self.delayaim = (self.delayaim[0], self.delayaim[1]-0.5)


        for tanque in self.tanques:
            tanque.update()
        for alvo in self.alvos:
            alvo.update()
        for crater in self.crateres:
            crater.update()

        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.tempo > self.tshot: 
            self.tiros.append(Shoot(self.charge,self.elevationrad,self.anglerad,self.centro, self.tempo))
            self.tshot = self.tempo + 2
            self.fire=True
        else:
            self.aim=Aim(self.charge,self.elevationrad,self.anglerad,self.centro)



    def draw(self):
        pyxel.cls(0)
        if self.levelnumber == 0:
            pyxel.text(10,10, "TESTE", 7)
        for tanque in self.tanques:
            tanque.draw()
        for alvo in self.alvos:
            alvo.draw()
        for crater in self.crateres:
            crater.draw()
        