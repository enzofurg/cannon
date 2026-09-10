import pyxel


class App:
    def __init__(self):
        self.tempo = 1
        self.screenwidth = 500
        self.screenlength = 600
        pyxel.init(self.screenwidth,self.screenlength, title="Cannon",fps=12)