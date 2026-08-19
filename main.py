import pyxel
import math
import random


class Target:
    def __init__(self):
        self.x= random.randint(10,480)
        self.y= random.randint(60,500)
    def spawn(self):
        pyxel.circb(self.x, self.y, 1, 8)
        pyxel.circb(self.x, self.y, 2, 7)
        pyxel.circb(self.x, self.y, 3, 8)
        pyxel.circb(self.x, self.y, 4, 7)
        pyxel.circb(self.x, self.y, 5, 8)
#
class Shoot:
    def __init__(self, charge, elevation, angle, centrotuple):
        self.distance= (25*charge)**2 * math.sin(2*elevation) / 9.8
        #print(self.distance)
        self.cords=(centrotuple[0]+self.distance*math.cos(angle), centrotuple[1]-self.distance*math.sin(angle))
        #print(self.cords)
    def hitcheck(self):
        if (pyxel.pget(self.cords[0], self.cords[1])) == 7 or (pyxel.pget(self.cords[0], self.cords[1])) == 8:
            print("Acerto")
        pass
    def animate(self):
        pyxel.circ(self.cords[0],self.cords[1], 5, 10)

class Aim:
    def __init__(self, charge, elevation, angle, centrotuple):
        self.centrotuple=centrotuple
        self.distance= (25*charge)**2 * math.sin(2*elevation) / 9.8
        #print(self.distance)
        self.cords=(centrotuple[0]+self.distance*math.cos(angle), centrotuple[1]-self.distance*math.sin(angle))
        #print(self.cords)
    def animate(self):
        pyxel.line(self.centrotuple[0],self.centrotuple[1],self.cords[0],self.cords[1], 13)
        pyxel.circb(self.cords[0],self.cords[1], 3, 13)

class Juego:
    def __init__(self):
        self.screenwidth = 500
        self.screenlength = 600
        pyxel.init(self.screenwidth,self.screenlength, title="Cannon",fps=12)
        self.centro=(self.screenwidth/2,self.screenlength-20)
        self.cannontip=(0,0)
        #self.vetor=(0,0)
        self.anglerad=0
        self.angle = 0
        self.elevation = 30
        self.elevationrad = 0
        self.charge=1
        self.fire=False
        self.alvo1=Target()
        self.alvo2=Target()
        self.alvo3=Target()
        pyxel.run(self.update, self.draw)


        
    def update(self):
        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
            self.tiro=Shoot(self.charge,self.elevationrad,self.anglerad,self.centro)
            self.tiro.hitcheck()
            self.fire=True
        else:
            self.mira=Aim(self.charge,self.elevationrad,self.anglerad,self.centro)
        if pyxel.btn(pyxel.KEY_UP):
            if (self.elevation + 0.5) > 45:
                self.elevation = 45
            else:
                self.elevation+=0.5
        if pyxel.btn(pyxel.KEY_DOWN):
            if (self.elevation - 0.5) < 15:
                self.elevation = 15
            else:
                self.elevation-=0.5
                #
        if pyxel.btn(pyxel.KEY_RIGHT):
            if(self.charge+1)>3:
                self.charge=3
            else:
                self.charge+=1
        if pyxel.btn(pyxel.KEY_LEFT):
            if(self.charge-1)<1:
                self.charge=1
            else:
                self.charge-=1
        
        
        #pyxel.mouse(True)
        #self.vetor=((pyxel.mouse_x - 60),(pyxel.mouse_y -60))
        self.anglerad = abs(math.atan2(((self.centro[1]-pyxel.mouse_y)),(pyxel.mouse_x-self.centro[0])))
        self.angle = self.anglerad * 180/math.pi
        self.cannontip=((self.centro[0]+(math.cos(self.anglerad)*15*math.cos(self.elevationrad))),(self.centro[1]-(math.sin(self.anglerad)*15*math.cos(self.elevationrad))))
        #print(self.vetor)
        #self, charge, elevation, angle, centrox, centroy
        #print(pyxel.mouse_wheel)
        pass
    
    def draw(self):
        pyxel.cls(0)
        pyxel.dither(0.1)
        pyxel.rect(0,0,self.screenwidth, self.screenlength, 1)
        pyxel.dither(1)
        self.alvo1.spawn()
        self.alvo2.spawn()
        self.alvo3.spawn()
        #print(self.centro)
        if self.fire:
            pyxel.circ(self.cannontip[0],self.cannontip[1],2,10)
            self.tiro.animate()
        else:
            self.mira.animate()
        #else:
            #pyxel.circb()
        #pyxel.circb(self.centro[0],self.centro[1], 20, 7)
        pyxel.rect(0,self.centro[1],self.screenwidth,self.screenlength,7)
        pyxel.circ(self.centro[0], self.centro[1], 3, 7)
        
        #pyxel.line(self.centro[0], self.centro[1], pyxel.mouse_x, pyxel.mouse_y,7)
        #Cano:
        pyxel.line(self.centro[0], self.centro[1], self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]-1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]+1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)
        

        pyxel.text(10,10,f"Mouse (x,y): {pyxel.mouse_x}, {pyxel.mouse_y}", 7)
        pyxel.text(10,20, f"Angle {self.angle:.2f}°", 7)
        pyxel.text(10,30, f"Elevation: {self.elevation:.1f}",7)
        pyxel.text(10,40, f"Charge: {self.charge}",7)
        pass
    
Juego()