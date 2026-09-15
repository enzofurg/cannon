import math

import pyxel
import random
from aim import Aim
from shoot import Shoot
from tank import Tank
from target import Target

class Level:
    def __init__(self, levelnumber):
        
        self.screenwidth = 500
        self.screenlength = 600
        self.centro = (self.screenwidth/2,self.screenlength-20)
        self.tempo = 1
        self.trueaim = (pyxel.mouse_x, pyxel.mouse_y)
        self.delayaim = self.trueaim
        self.tshot = 1
        self.cannontip=(0,0)
        self.anglerad=0
        self.trueanglerad = 0
        self.angle = 0
        self.elevation = 30
        self.elevationrad = 0
        self.charge=1
        self.fire=False
        self.mira = Aim(self.charge,self.elevationrad,self.anglerad,self.centro)
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
        #for alvo in self.alvos:
            #alvo.update()
        for crater in self.crateres:
            crater.update()

        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        self.trueanglerad = abs(math.atan2(((self.centro[1]-self.trueaim[1])),(self.trueaim[0]-self.centro[0])))
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.tempo > self.tshot: 
            self.tiros.append(Shoot(self.charge,self.elevationrad,self.anglerad,self.centro, self.tempo))
            self.tshot = self.tempo + 2
            self.fire=True
        else:
            self.mira=Aim(self.charge,self.elevationrad,self.anglerad,self.centro)

        self.angle = self.anglerad * 180/math.pi
        self.cannontip=((self.centro[0]+(math.cos(self.anglerad)*15*math.cos(self.elevationrad))),(self.centro[1]-(math.sin(self.anglerad)*15*math.cos(self.elevationrad))))
        self.tempo += 1/12



    def draw(self):
        
        pyxel.cls(0)
        pyxel.dither(0.1)
        pyxel.rect(0,0,self.screenwidth, self.screenlength, 1)
        pyxel.dither(0.5)
        pyxel.line(0,self.screenlength-50,self.screenwidth, self.screenlength-50, 8)
        pyxel.line(0,self.screenlength-51,self.screenwidth, self.screenlength-51, 8)
        pyxel.line(0,self.screenlength-52,self.screenwidth, self.screenlength-52, 8)

        for crater in self.craters:
            crater.draw()

        pyxel.dither(1)
        for alvos in self.alvos:
            alvos.draw()

        for tanque in self.tanques:
            tanque.draw()

        if self.fire:
            pyxel.circ(self.cannontip[0],self.cannontip[1],2,10)
            
        else:
            #self.mira.draw(self.trueanglerad)
            self.mira.draw(self.trueanglerad)
            
        for tiro in self.tiros:
            tiro.draw(self.tempo)


        pyxel.rect(0,self.centro[1],self.screenwidth,self.screenlength,7)
        pyxel.circ(self.centro[0], self.centro[1], 3, 7)
        
        #pyxel.line(self.centro[0], self.centro[1], pyxel.mouse_x, pyxel.mouse_y,7)
        #DESENHO DO CANO
        pyxel.line(self.centro[0], self.centro[1], self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]-1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]+1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)

        #pyxel.circb(self.trueaim[0],self.trueaim[1], 3, 13)
        
        #TEXTO
        pyxel.text(10,10,f"Mouse (x,y): {pyxel.mouse_x}, {pyxel.mouse_y}", 7)
        pyxel.text(10,20, f"Angle {self.angle:12.2f}°", 7)
        pyxel.text(10,30, f"Elevation: {self.elevation:.1f}",7)
        pyxel.text(10,40, f"Charge: {self.charge}",7)
        pyxel.text(10,50, f"Time: {int(self.tempo)}s",7)
        pyxel.text(10,60, f"{self.trueaim} {self.delayaim}", 7)
        for tiro in self.tiros:
            pyxel.text(10, 60, f"height:{tiro.height:.2f}",7)
        for tanque in self.tanques:
            if tanque.bordercheck(self.screenlength):
                pyxel.rect(0,0,self.screenwidth,self.screenlength,8)
        if self.tshot>self.tempo:
            pyxel.rect(self.cannontip[0], self.cannontip[1]-20, 40*((self.tshot-self.tempo)/2),5,10)
        pyxel.mouse(True)
#PRÉ PASTE
        #pyxel.cls(0)
        #if self.levelnumber == 0:
        #    pyxel.text(10,10, "TESTE", 7)
        #for tanque in self.tanques:
        #    tanque.draw()
        #for alvo in self.alvos:
        #    alvo.draw()
        #for crater in self.crateres:
        #    crater.draw()
        