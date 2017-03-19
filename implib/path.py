#path.py is unused in programm looking for delete

from implib import point
#import numpy as np
from implib import bresenham

class path():
    def __init__(self):
        self.PathPoints = []
        self.Start = point()
        self.End = point()
        self.Operation = False
        self.sizepapo = len(self.PathPoints)
        self.Pat = []
        self.bres = bresenham(self.start, self.end)

    def _resizepapo(self):
        self.sizepapo = len(self.PathPoints)

    def _setconfig(self, S, E, W):
        self.Start = S
        self.End = E
        if W == 'T':
            self.Operation = True
        elif W == 'F':
            self.Operation = False

    def _changeoperation(self):
        self.Operation = not self.Operation

    def _printpathpoints(self):
        for i in self.PathPoints:
            print (i.X, i.Y, i.Z)

    def _resetlist(self):
        self.PathPoints = []
        self.Operation = False
        self.Pat = []

    #def _bresenham(self):
    #def _optimise(self):


    def _startx(self):
        #Application of _bresenham function
        self._bresenham()
        #Application of _optimise function
        self._optimise()
