import pyxel
import math
import random
#ARGH!!!

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

class Soldier:
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
        pyxel.rect(self.x,self.y,2,2,6)
    def move(self):
        self.y+=1/12

#
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
        self.soldados = []

        for i in range(25):
            self.alvos.append(Target())

        for i in range(0):
            self.soldados.append(Soldier())
        pyxel.run(self.update, self.draw)




        
    def update(self):
        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) and len(self.tiros)<1:
            self.tiros.append(Shoot(self.charge,self.elevationrad,self.anglerad,self.centro, self.tempo))

            self.fire=True
        else:
            self.mira=Aim(self.charge,self.elevationrad,self.anglerad,self.centro)

        for soldado in self.soldados:
            soldado.move()
            
        for tiro in self.tiros:
            if tiro.traveltime < self.tempo:
                for alvo in self.alvos:
                    if alvo.hitcheck(tiro.cords,10):
                        self.alvos.remove(alvo)
                for soldado in self.soldados:
                    if soldado.hitcheck(tiro.cords,10):
                        self.soldados.remove(soldado)
                self.tiros.remove(tiro)
        
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
        for tiro in self.tiros:
            tiro.move(self.tempo)
        
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

        for soldado in self.soldados:
            soldado.draw()

        if self.fire:
            pyxel.circ(self.cannontip[0],self.cannontip[1],2,10)
            
        else:
            self.mira.animate()
            
        for tiro in self.tiros:
            tiro.animate(self.tempo)


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
        for tiro in self.tiros:
            pyxel.text(10, 60, f"height:{tiro.height:.2f}",7)
        for soldado in self.soldados:
            if soldado.bordercheck(self.screenlength):
                pyxel.rect(0,0,self.screenwidth,self.screenlength,8)
        pass
    
Juego()
