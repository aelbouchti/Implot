from path.py import path
from tools.py import tools_point,tools_2d

class code():
    def __init__(self):
        self.Code = ''
        self.CheckPoints = []
        self.OperativePaths = []
        self.PointByPointRoad = []
        self.Tool = tools_point()
    def _code(self):
        code = ''
        for i in range(0, len(self.CheckPoints)):
            a, b, c = self.CheckPoints[i]._xyz()
            code += str(self.OperativePaths[i])
            code += '.' + str(a) + '.' +str(b) + '.' + str(c)
        self.Code = code

    def _decodedata(self, code):
        pp = []
        op = []
        self.Code = code
        recode = code.split('.')
        for i in range(0, len(recode), 4):
            pp += [point(int(recode[i]), int(recode[i+1]), int(recode[i+2]))]
            op += [recode[i+3]]
        self.CheckPoints = pp
        self.OperativePaths = op

    def _encodelist(self, M, N):
        self.CheckPoints = M
        self.OperativePaths = N
        self._code()

    def _ben_ben(self):
        l = len(self.CheckPoints)
        for i in range(l-1):
            ##########
            self.PointByPointRoad += Tool._optimise(Tool._brenseham(self.CheckPoints[i], self.CheckPoints[i+1]))
