
class code():
    def __init__(self):
        self.Code = ''
        self.CheckPoints = []
        self.OperativePaths = []

    def _code(self):
        code = ''
        for i in range(0, len(self.CheckPoints)):
            a, b, c = self.CheckPoints[i]._xyz()
            code += str(self.OperativePaths[i])
            code += '.' + str(a) + '.' +str(b) + '.' + str(c)
        self.Code=code

    def _decodedata(self,code):
        pp = []
        op = []
        recode = code.split('.')
        for i in range(0,len(recode),4):
            pp += [ Point(int(recode[i]), int(recode[i+1]), int(recode[i+2]))]
            op += [recode[i+3]]
        self.CheckPoints = pp
        self.OperativePaths = op

    def _encodelist(self, M, N):
        self.CheckPoints = M
        self.OperativePaths = N
        self._code()
