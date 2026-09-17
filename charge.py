import pyxel


class Charge:
    def __init__(self):
        self.chargenum = 1
        self.min = 1
        self.max = 3
    def incdec(self,left,right):
        if left:
            self.chargenum -= 1
        elif right:
            self.chargenum += 1
        if self.chargenum < self.min:
            self.chargenum = self.min
        elif self.chargenum > self.max:
            self.chargenum = self.max

