import math

#returns a circle drawn parametrically by varying theta (deg)
def PCircle(center,radius,thetastep):
    circleObj = []
    for theta in range(int(360/thetastep)):
        theta = theta*thetastep
        dVector = [math.cos(theta*math.pi/180),math.sin(theta*math.pi/180)]
        circleObj.append((int(radius*dVector[0]+center[0]),int(radius*dVector[1]+center[1])))
    return circleObj

#returns a circle drawn by varying x and y depending on the current gradient
def CCircle(center,radius):
    index = [1,1,-1,-1]
    points = []
    for n in range(int((math.ceil(1/math.sqrt(2)))*radius)):
        m = int(math.ceil(math.sqrt(radius**2-n**2)))
        for i in range(4):
            yco = index[(i%4)]
            xco = index[((i+1)%4)]
            points.append((yco*n+center[0],xco*m+center[1]))
            points.append((yco*m+center[0],xco*n+center[1]))
    return points

#returns an array of points connecting 2 lines without gaps
def drawLine(p1,p0):
    if p0 == p1:
        return [p0,p1]
    points = []
    dy = p1[1]-p0[1]
    dx = p1[0]-p0[0]
    if abs(dy)>abs(dx):
        direction = [dx/abs(dy),dy/abs(dy)]
        steps = range(abs(dy))
    else:
        direction = [dx/abs(dx),dy/abs(dx)]
        steps = range(abs(dx))
    for step in steps:
        y = int(p0[1]+step*direction[1])
        x = int(p0[0]+step*direction[0])
        points.append((x,y))
    return points

#returns an array of points containing a regular polygon
def polyReg(center,radius,sides):
    points = []
    corners = PCircle(center,radius,360/sides)
    for index in range(sides):
        line = drawLine(corners[index],corners[(index+1)%sides])
        for point in line:
            points.append(point)
    return points

