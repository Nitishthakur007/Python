import math

def calc(c):
    radius  = c/(2 * math.pi )
    area = ( math.pi * (radius ** 2) )
    Radius = str( round(radius,2))
    Area = str(round(area,2))
    print("(" +Radius + ", " + Area + ")")

calc(8)