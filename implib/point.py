class point():
    #declaration point xyz 3D
    def __init__(self, *args):
        self.X = 0
        self.Y = 0
        self.Z = 0
        self.L = []
        self.dim = 0
        for i, j in enumerate(args):
            self.L.append(j)
            self.dim = i+1
        while self.dim < 3:
            self.L.append(0)
            self.dim += 1
        self.X = self.L[0]
        self.Y = self.L[1]
        self.Z = self.L[2]
    def _avx(self, value):
        self.L[0] += value
    def _avy(self, value):
        self.L[1] += value
    def _avz(self, value):
        self.L[2] += value
    def _xyz(self):
        return (self.L[0], self.L[1], self.L[2])
    def _dim(self):
        return self.dim
    def _avi(self, i, value):
        self.L[i] += value
