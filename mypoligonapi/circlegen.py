from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from math import cos, sin, pi, hypot

def create_polygon_n(puntos_n):
    point_array = []
    center = [0,0]
    angle = 2*pi/puntos_n
    radius = 100
    # point_on_circle(angle)
    # print(angle)
    # print(cos(angle))
    for i in range(puntos_n):
        x = center[0] + (radius * round(cos(angle*i),2))
        y = center[1] + (radius * round(sin(angle*i),2))
        point_array.append([x,y])
        # print(x,y)
    x1 = point_array[0][0]
    y1 = point_array[0][1]
    x2= point_array[1][0]
    y2 = point_array[1][1]
    print(x1,y1)
    print(x2,y2)
    distance = hypot(x2 - x1, y2 - y1)
    print(point_array)
    print(distance)

# print(point_on_circle())
create_polygon_n(3)