#from implib import bresenham
from implib import point
from maths import sqrt
class tools_point():

    def __init__(self):
        self.functions = []

    def _equal_point(a,b):
        return a.X == b.X, a.Y == b.Y, a.Z == b.Z

    def _give_function_point(a,b):
        pass

    def _dist_point(a, b, c):
        pass

    def _derivate_point(q, p):
        pass

class tools_algebra():
    def __init__(self):
        self.functions = []

    def _pgcd (a,b):
        while a%b == 0:
            a, b = b, a%b
        return b

    def _factorise(a, b):
        if pgcd(a, b) == 1:
            return a, b
        return a/pgcd(a, b), b/pgcd(a, b)

    def _isprime(a):
        if a%2 == 0:
            return False
        for i in range(3,sqrt(a)+1):
            if a%i==0:
                return False
        return True

class tools_decrypt():
    def __init__(self):
        self.functions = []

    def _decrypt(ch):
        l = ch.split('.')
        p=l[1].split('-')
        return l[0], [int(i) for i in p], int(l[2]), int(l[3])

class tools_2d():
    def __init__(self):
        self.functions = []

    def _derivate(p,q):
      return q.X-p.X, q.X-p.X

    def _bresenhampath(p, q):
		""" Bresenham's Algorithm for Line
			Start and End are Point() classes
			Ouput: Modifying the pathpoints to bresenhams points
		"""
		x1, y1 = p.X, p.Y
		x2, y2 = q.X, q.Y
		#Calculating differentials dx,dy
		dx = x2-x1
		dy = y2-y1
		#defining if Line passing threw start and end is steep or not
		is_steep = abs(dy) > abs(dx)
		if is_steep:
			x1, y1 = y1, x1
			x2, y2 = y2, x2
		#swapping points if its necessary
		swapped = False
		if x1 > x2:
			x1, x2 = x2, x1
			y1, y2 = y2, y1
			swapped = True
		#recalculating dx,dy
		dx = x2-x1
		dy = y2-y1
		#Calculating Error
		error = int(dx/2.0)
		#ystep is -1 or +1
		ystep = 1 if y1 < y2 else -1
		y = y1
		points = []
		for x in range(x1, x2+1):
			coord = point(y, x) if is_steep else point(x, y)
			points.append(coord)
			error -= abs(dy)
			if error < 0:
				y += ystep
				error += dx
        if swapped:
            points.reverse()
		return points

    def _wich_dir():
        a, b = derivate(p, q)
        if self._vector_dir(p, q)[0] == self._vector_dir(p, q)[1]:
            if a>0:
                return 1, 1
            return -1, -1
        else:
            if a>0:
                return 1, -1
            return -1,1
            
    def _vector_dir(p, q):
        return [i>0 for i in self._derivate(p, q)]
