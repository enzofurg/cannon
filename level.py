import math
import game
import pyxel
import random
from aim import Aim
from shoot import Shoot
from tank import Tank
from target import Target
from charge import Charge
from plane import Plane
from soldier import Soldier
from elevation import Elevation
from crater import Crater


class Level:
    def __init__(self, levelnumber, game):
        self.game = game
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
        self.elevation = Elevation()
        self.charges=Charge()
        self.fire=False
        self.mira = Aim(self.charges.chargenum,self.elevation.elevrad,self.anglerad,self.centro)
        self.craters = []
        self.tiros = []
        self.alvos = []
        self.tanques = []
        self.planes = []
        self.levelnumber=levelnumber
        self.tanques=[]
        self.alvos=[]
        self.planes=[]
        self.planeinfo = (False,(0,0))
        self.soldiers=[]
        self.crateres=[]
        self.cargasinv = 0
        self.tirosinv = 0
        if self.levelnumber == 1:
          self.cargasinv = 180
          self.tirosinv = 60
          for i in range(10):
                self.alvos.append(Target())
        elif self.levelnumber == 2:
            self.cargasinv = 180
            self.tirosinv = 60
            for i in range(10):
                self.tanques.append(Tank())
            for i in range(0):
                self.planes.append(Plane((0,20),self.tempo))
        elif self.levelnumber == 3:
            self.cargasinv = 180
            self.tirosinv = 60
            for i in range(12):
                self.tanques.append(Tank())
            for i in range(3):
                self.planes.append(Plane((0,40),self.tempo))

        for i in range(0):
            self.soldiers.append(Soldier(random.randint(20,480),0))
        self.inimigos = len(self.alvos) + len(self.tanques) + len(self.planes) + len(self.soldiers)

    def fim(self):
        self.game.game_over()

    def update(self):
        self.trueaim = (pyxel.mouse_x, pyxel.mouse_y)

        if (pyxel.btn(pyxel.MOUSE_BUTTON_RIGHT)):
            self.fim()

        for x  in range(20):
            if self.trueaim[0] - self.delayaim[0] > 0.5:
                self.delayaim = (self.delayaim[0]+0.5, self.delayaim[1])
            elif self.trueaim[0] - self.delayaim[0] < -0.5:
                self.delayaim = (self.delayaim[0]-0.5, self.delayaim[1])

            if self.trueaim[1] - self.delayaim[1] > 0.5:
                self.delayaim = (self.delayaim[0], self.delayaim[1]+0.5)
            elif self.trueaim[1] - self.delayaim[1] < -0.5:
                self.delayaim = (self.delayaim[0], self.delayaim[1]-0.5)

        for tiro in self.tiros:
            if tiro.traveltime < self.tempo:
                for alvo in self.alvos:
                    if alvo.hitcheck(tiro.cords,10):
                        self.alvos.remove(alvo)
                for tanque in self.tanques:
                    if tanque.hitcheck(tiro.cords,12):
                        self.tanques.remove(tanque)
                for soldier in self.soldiers:
                    if soldier.hitcheck(tiro.cords,16):
                        self.soldiers.remove(soldier)
                self.craters.append(Crater(tiro.cords))
                self.tiros.remove(tiro)
            tiro.move(self.tempo)

        for soldier in self.soldiers:
            soldier.update()
            if soldier.bordercheck(self.screenlength):
                self.fim()


        for tanque in self.tanques:
            tanque.update()
            if tanque.bordercheck(self.screenlength):
                self.fim()
                
        #for alvo in self.alvos:
            #alvo.update()
        for plane in self.planes:
            if (plane.update(self.tempo)):
                self.planes.remove(plane)
            
            self.planeinfo = plane.spawncheck(self.tempo)
            if self.planeinfo[0]:
                self.soldiers.append(Soldier(self.planeinfo[1][0],self.planeinfo[1][1]))
        for crater in self.crateres:
            crater.update()

        self.fire=False
        #self.elevationrad = self.elevation * math.pi/180
        self.anglerad = abs(math.atan2(((self.centro[1]-self.delayaim[1])),(self.delayaim[0]-self.centro[0])))
        self.trueanglerad = abs(math.atan2(((self.centro[1]-self.trueaim[1])),(self.trueaim[0]-self.centro[0])))

        #IF DO TIRO
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and self.tempo > self.tshot and self.cargasinv>self.charges.chargenum and self.tirosinv>0: 
            self.tiros.append(Shoot(self.charges.chargenum,self.elevation.elevrad,self.anglerad,self.centro, self.tempo))
            self.tshot = self.tempo + 2
            self.cargasinv -= self.charges.chargenum
            self.tirosinv -= 1
            self.fire=True
        elif pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print("lol")
        else:
            self.mira=Aim(self.charges.chargenum,self.elevation.elevrad,self.anglerad,self.centro)
        self.charges.incdec(pyxel.btnp(pyxel.KEY_LEFT),pyxel.btn(pyxel.KEY_RIGHT))
        self.elevation.incdec(pyxel.btn(pyxel.KEY_UP),pyxel.btn(pyxel.KEY_DOWN))
        self.angle = self.anglerad * 180/math.pi
        self.cannontip=((self.centro[0]+(math.cos(self.anglerad)*15*math.cos(self.elevation.elevrad))),(self.centro[1]-(math.sin(self.anglerad)*15*math.cos(self.elevation.elevrad))))
        self.inimigos = len(self.alvos) + len(self.tanques) + len(self.planes) + len(self.soldiers)
        if self.inimigos == 0:
            self.fim()
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

        for plane in self.planes:
            plane.draw()

        for soldier in self.soldiers:
            soldier.draw()

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
        pyxel.text(10,20, f"Ãngulo: {self.angle:12.2f}°", 7)
        pyxel.text(10,30, f"Elevação: {self.elevation.elevangle:.1f}",7)
        pyxel.text(10,40, f"Cargas carregadas: {self.charges.chargenum}",7)
        pyxel.text(10,50, f"Tempo: {int(self.tempo)}s",7)
        #pyxel.text(10,60, f"{self.trueaim} {self.delayaim}", 7)
        pyxel.text(10,60, f"Cargas restantes: {self.cargasinv}", 7)
        pyxel.text(10,70,f"Tiros restantes: {self.tirosinv}", 7)
        pyxel.text(10,80,f"Inimigos: {self.inimigos}", 7)
        #pyxel.text(10,80,f"SPAWNBOOL:{self.planeinfo[0]}",7)

    
        for tiro in self.tiros:
            pyxel.text(10, 70, f"height:{tiro.height:.2f}",7)

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
        