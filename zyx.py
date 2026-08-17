import pyxel
import math

class Juego:
    def __init__(self):
        self.screenwidth = 200
        self.screenlength = 300
        pyxel.init(self.screenwidth,self.screenlength, title="Cannon",fps=12)
        self.centro=(self.screenwidth/2,self.screenlength-20)
        self.cannontip=(0,0)
        #self.vetor=(0,0)
        self.anglerad=0
        self.angle = 0
        self.elevation = 15
        self.elevationrad = 0
        self.fire=False
        pyxel.run(self.update, self.draw)

        
    def update(self):
        self.fire=False
        self.elevationrad = self.elevation * math.pi/180
        if pyxel.btn(pyxel.KEY_SPACE):
            self.fire=True
        if pyxel.btn(pyxel.KEY_UP):
            if (self.elevation + 0.5) > 45:
                self.elevation = 45
            else:
                self.elevation+=0.5
        if pyxel.btn(pyxel.KEY_DOWN):
            if (self.elevation - 0.5) < 5:
                self.elevation = 5
            else:
                self.elevation-=0.5
        
        pyxel.mouse(True)
        #self.vetor=((pyxel.mouse_x - 60),(pyxel.mouse_y -60))
        self.anglerad = abs(math.atan2(((self.centro[1]-pyxel.mouse_y)),(pyxel.mouse_x-self.centro[0])))
        self.angle = self.anglerad * 180/math.pi
        self.cannontip=((self.centro[0]+(math.cos(self.anglerad)*28*math.cos(self.elevationrad))),(self.centro[1]-(math.sin(self.anglerad)*28*math.cos(self.elevationrad))))
        #print(self.vetor)
        print(pyxel.mouse_wheel)
        pass
    
    def draw(self):
        pyxel.cls(0)
        #print(self.centro)
        if self.fire:
            pyxel.circ(self.cannontip[0],self.cannontip[1],2,10)
        #pyxel.circb(self.centro[0],self.centro[1], 20, 7)
        pyxel.rect(0,self.centro[1],self.screenwidth,self.screenlength,7)
        pyxel.circ(self.centro[0], self.centro[1], 3, 7)
        
        #pyxel.line(self.centro[0], self.centro[1], pyxel.mouse_x, pyxel.mouse_y,7)
        pyxel.line(self.centro[0], self.centro[1], self.cannontip[0], self.cannontip[1], 7)
        pyxel.text(10,10,f"Mouse (x,y): {pyxel.mouse_x}, {pyxel.mouse_y}", 7)
        pyxel.text(10,20, f"Angle {self.angle:.2f}°", 7)
        pyxel.text(10,30, f"Elevation {self.elevation:.1f}",7)
        pass
    
Juego()