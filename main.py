import pyxel
import math
import random


class Target:
    def __init__(self):
        self.x= random.randint(10,480)
        self.y= random.randint(60,500)
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

#
class Shoot:
    def __init__(self, charge, elevation, angle, centrotuple, time):
        self.centrocords = centrotuple
        self.angle = angle
        self.distance= (25*charge)**2 * math.sin(2*elevation) / 9.8
        self.traveltime= time + 2 * (25*charge*math.sin(elevation)) / 9.8
        print(self.traveltime)
        self.speed = self.distance / self.traveltime
        self.cords=(centrotuple[0]+self.distance*math.cos(angle), centrotuple[1]-self.distance*math.sin(angle))
        self.cordstx = centrotuple[0]
        self.cordsty = centrotuple[1]
        self.timelapse = 0
        #print(self.cords)

    def animate(self, time):
        self.timelapse+=1/12
        self.cordstx = self.centrocords[0] + self.speed*self.timelapse*math.cos(self.angle)
        self.cordsty = self.centrocords[1] - self.speed*self.timelapse*math.cos(self.angle) 
        print(self.cordstx, self.cordsty)
        pyxel.circ(self.cordstx,self.cordsty, 20, 10)
        if time > self.traveltime:
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
        self.tempo = 0
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
        self.tiros = []
        self.alvos = []

        for i in range(5):
            self.alvos.append(Target())
        pyxel.run(self.update, self.draw)


        
    def update(self):
        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and len(self.tiros)<1:
            self.tiros.append(Shoot(self.charge,self.elevationrad,self.anglerad,self.centro, self.tempo))
            for alvos in self.alvos:
                if alvos.hitcheck(self.tiros[0].cords, 10):
                    self.alvos.remove(alvos)
                    #self.tiros=[]
            self.fire=True
        else:
            self.mira=Aim(self.charge,self.elevationrad,self.anglerad,self.centro)
            
        for tiro in self.tiros:
            if tiro.traveltime + 1 < self.tempo:
                self.tiros=[]
        
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
        self.tempo+=1/12
        #print(f"Tempo: {self.tempo}")
        pass
    
    def draw(self):
        pyxel.cls(0)
        pyxel.dither(0.1)
        pyxel.rect(0,0,self.screenwidth, self.screenlength, 1)
        pyxel.dither(0.5)
        pyxel.line(0,self.screenlength-50,self.screenwidth, self.screenlength-50, 8)
        pyxel.line(0,self.screenlength-51,self.screenwidth, self.screenlength-51, 8)
        pyxel.line(0,self.screenlength-52,self.screenwidth, self.screenlength-52, 8)

        pyxel.dither(1)
        for alvos in self.alvos:
            alvos.spawn()
        #self.alvo1.spawn()
        #self.alvo2.spawn()
        #self.alvo3.spawn()
        #print(self.centro)
        if self.fire:
            pyxel.circ(self.cannontip[0],self.cannontip[1],2,10)
            
        else:
            self.mira.animate()
        for tiro in self.tiros:
            tiro.animate(self.tempo)
        #else:
            #pyxel.circb()
        #pyxel.circb(self.centro[0],self.centro[1], 20, 7)
        pyxel.rect(0,self.centro[1],self.screenwidth,self.screenlength,7)
        pyxel.circ(self.centro[0], self.centro[1], 3, 7)
        
        #pyxel.line(self.centro[0], self.centro[1], pyxel.mouse_x, pyxel.mouse_y,7)
        #DESENHO DO CANO
        pyxel.line(self.centro[0], self.centro[1], self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]-1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)
        pyxel.line(self.centro[0]+1,self.centro[1],self.cannontip[0], self.cannontip[1], 7)
        
        #TEXTO
        pyxel.text(10,10,f"Mouse (x,y): {pyxel.mouse_x}, {pyxel.mouse_y}", 7)
        pyxel.text(10,20, f"Angle {self.angle:.2f}°", 7)
        pyxel.text(10,30, f"Elevation: {self.elevation:.1f}",7)
        pyxel.text(10,40, f"Charge: {self.charge}",7)
        pyxel.text(10,50, f"Time: {int(self.tempo)}s",7)
        pass
    
Juego()
