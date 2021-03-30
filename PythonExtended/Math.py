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
