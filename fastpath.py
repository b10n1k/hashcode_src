import math

def getDistance(p, p2, p3, p4):
    point_one = math.pow(math.fabs(p-p3), 2)
    point_two = math.pow(math.fabs(p2-p4), 2)
    dis = int(round(math.sqrt(point_one+point_two)))
    return dis

print getDistance(2,3,4,5)
