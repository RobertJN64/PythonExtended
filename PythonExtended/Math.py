import math

#region Scaling Functions
def scale(minv, v, maxv, minx, maxx):
    """Maps a number from one range to another"""
    decimal = (v - minv) / (maxv - minv)
    return (decimal * (maxx-minx)) + minx

def unitscale(minv, v, maxv):
    """Scales from -1 to 1"""
    return scale(minv, v, maxv, -1, 1)

def posiscale(minv, v, maxv):
    """Scales from 0 to 1"""
    return scale(minv, v, maxv, 0, 1)
#endregion

#region Conversion functions
def deg(rads):
    """Radians to degrees"""
    return rads * 180 / math.pi

def rad(degs):
    """Degrees to radians"""
    return degs * math.pi/180
#endregion

#region Geo Functions
def distance(x1, y1, x2, y2):
    """Distance between 2 points"""
    return math.sqrt((x1-x2)^2 + (y1-y2)^2)

def pointdistance(pointa, pointb):
    """Distance between 2 points (as tuples)"""
    return distance(pointa[0], pointa[1], pointb[0], pointb[1])
#endregion

#region Angle Functions
def modangle(x):
    """Converts angle to 0 to 360"""
    return x%360

def unitangle(x):
    """Converts angle to -180 to 180"""
    x = x%360
    if x > 180:
        x -= 360
    return x

def getHeading(x1, y1, x2, y2):
    """Gets heading from point 1 to point 2. 0 is north"""
    return deg(math.atan2(x2-x1, y2 - y1))

def getPointHeading(pointa, pointb):
    """Gets heading from pointa to point b. O is north"""
    return getHeading(pointa[0], pointa[1], pointb[0], pointb[1])
#endregion

#region trig
def lawSines(A,B,b):
    """Finds side a given angles A and B and side b"""
    return (math.sin(rad(A)) * b) / math.sin(rad(B))

def lawCosines(A,b,c):
    """Finds side a given angle A and sides b and c"""
    return math.sqrt(math.pow(b,2) + math.pow(c,2) - 2*b*c*math.cos(rad(A)))

def invLawCosines(a,b,c):
    """Calculates angle A given sides a, b, and c"""
    return deg(math.acos((math.pow(b,2) + math.pow(c,2) - math.pow(a,2)) / (2 * b * c)))

class triangleSolver:
    def __init__(self):
        #sides
        self.a = None
        self.b = None
        self.c = None

        #angles
        self.A = None
        self.B = None
        self.C = None

        #temp
        self.tempangle = 0
        self.tempside = 0

        #config
        self.tol = 0.0001

        #diagnostics
        self.output = "No Solve Method Attempted"

    def reset(self):
        # sides
        self.a = None
        self.b = None
        self.c = None

        # angles
        self.A = None
        self.B = None
        self.C = None

    def safe(self, new, current):
        if current is None:
            return True
        if abs(new - current) < self.tol:
            return True
        else:
            return False

    def errorCheck(self):
        if (self.a is not None and self.A is not None and
            self.b is not None and self.B is not None and
            self.c is not None and self.C is not None):
            if abs(self.A + self.B + self.C - 180) > self.tol:
                self.output = "Angles do not add to 180"
                return False
            if (self.a + self.b < self.c or
                self.b + self.c < self.a or
                self.c + self.a < self.b):
                self.output = "Sides do not form a triangle"
                return False
        else:
            self.output = "Missing info"
            return False
        self.output = "Passed error check"
        return True

    def solveSSS(self):
        """High reliability solving method that uses law of cosines"""
        #check if sss can be used
        if self.a is None or self.b is None or self.c is None:
            self.output = "SSS can't be used, missing side"
            return False
        #angle A
        self.tempangle = invLawCosines(self.a, self.b, self.c)
        if self.safe(self.tempangle, self.A):
            self.A = self.tempangle
        else:
            self.output = "Error setting angle A"
            return False

        self.tempangle = invLawCosines(self.b, self.c, self.a)
        if self.safe(self.tempangle, self.B):
            self.B = self.tempangle
        else:
            self.output = "Error setting angle B"
            return False

        self.tempangle = invLawCosines(self.c, self.a, self.b)
        if self.safe(self.tempangle, self.C):
            self.C = self.tempangle
        else:
            self.output = "Error setting angle C"
            return False

        self.output = "SSS sucessful"
        return True

    def solveSAS(self):
        """Solves triangle using SAS with law of cosines. Relies on SSS solving"""
        if self.a is None and self.A is not None and self.b is not None and self.c is not None:
            #side a
            self.tempside = lawCosines(self.A, self.b, self.c)
            if self.safe(self.tempside, self.a):
                self.a = self.tempside
            else:
                self.output = "SAS failed, error side a"
                return False

        elif self.b is None and self.B is not None and self.a is not None and self.c is not None:
            #side b
            self.tempside = lawCosines(self.B, self.a, self.c)
            if self.safe(self.tempside, self.b):
                self.b = self.tempside
            else:
                self.output = "SAS failed, error side b"
                return False

        elif self.c is None and self.C is not None and self.a is not None and self.b is not None:
            #side c
            self.tempside = lawCosines(self.C, self.a, self.b)
            if self.safe(self.tempside, self.c):
                self.c = self.tempside
            else:
                self.output = "SAS failed, error side c"
                return False

        else:
            self.output = "SAS failed, not enough information"
            return False

        self.solveSSS()
        self.output = "SAS finished"
        return True

    def solveASA(self):
        """Solve triangle using ASA (or AAS), relies on law of sines"""
        if self.A is None and self.B is not None and self.C is not None:
            self.A = 180 - self.B - self.C
        elif self.B is None and self.C is not None and self.A is not None:
            self.B = 180 - self.A - self.C
        elif self.C is None and self.A is not None and self.B is not None:
            self.C = 180 - self.A - self.B
        elif self.A is not None and self.B is not None and self.C is not None:
            pass #all angles are fine
        else:
            self.output = "ASA failed, missing information"
            return False

        if self.a is None:
            self.tempside = lawSines(self.A, self.B, self.b)
            if self.safe(self.tempside, self.a):
                self.a = self.tempside
            else:
                self.output = "ASA failed, side a error"
                return False
        if self.b is None:
            self.tempside = lawSines(self.B, self.C, self.C)
            if self.safe(self.tempside, self.b):
                self.b = self.tempside
            else:
                self.output = "ASA failed, side b error"
                return False
        if self.c is None:
            self.tempside = lawSines(self.C, self.A, self.a)
            if self.safe(self.tempside, self.c):
                self.c = self.tempside
            else:
                self.output = "ASA failed, side c error"
                return False
        self.output = "ASA or AAS solved successfully"
        return True

    def solve(self):
        """Attempts to solve the triangle, returns True if succesful"""
        #check if triangle can be solved
        if self.solveSSS() and self.errorCheck():
            self.output = "SSS solved"
            return True
        elif self.solveSAS() and self.errorCheck():
            self.output = "SAS solved"
            return True
        elif self.solveASA() and self.errorCheck(): #also handles AAS cases
            self.output = "ASA solved"
            return True
        elif not self.errorCheck():
            self.output = "Solving failed - invalid triangle"
        else:
            self.output = "Solving failed - not enough information"
            return False

    def SSS(self, s1, s2, s3):
        """Configure triangle using Side Side Side"""
        self.a = s1
        self.b = s2
        self.c = s3

    def SAS(self, s1, a, s2):
        """Configure triangle using SAS. Centered around angle B"""
        self.a = s1
        self.B = a
        self.c = s2

    def ASA(self, a1, s, a2):
        """Configure triangle using ASA. Centered around side b"""
        self.A = a1
        self.b = s
        self.C = a2

#endregion
