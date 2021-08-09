from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import generics

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from mypoligon.models import *

from rest_framework.permissions import IsAuthenticated

# Create Polygon points from number of Points Function
def create_polygon_n(puntos_n):
    from shapely.geometry import Point
    from shapely.geometry.polygon import Polygon
    from math import cos, sin, pi, hypot

    point_array = []
    center = [0, 0]
    angle = 2 * pi / puntos_n
    radius = 100
    for i in range(puntos_n):
        x = center[0] + (radius * round(cos(angle * i), 2))
        y = center[1] + (radius * round(sin(angle * i), 2))
        point_array.append([x, y])
        # print(x,y)
    x1 = point_array[0][0]
    y1 = point_array[0][1]
    x2 = point_array[1][0]
    y2 = point_array[1][1]
    # print(x1,y1)
    # print(x2,y2)
    distance = hypot(x2 - x1, y2 - y1) * puntos_n
    print(point_array)
    print(distance)
    return point_array, distance


# Create a Polygon in the database and create its Points
class Create_polygon(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        puntos_n = request.data.get("puntos_n")
        puntos_n = int(puntos_n)
        point_array, distance = create_polygon_n(puntos_n)
        Poligon.objects.create(number_points=puntos_n, distance=distance)
        my_id = Poligon.objects.filter(number_points=puntos_n)
        my_id = my_id[len(my_id) - 1].id
        for i in range(puntos_n):
            # print(i)
            # print(point_array[i][0])
            Points.objects.create(
                poligon_id_id=my_id,
                point_x=point_array[i][0],
                point_y=point_array[i][1],
            )

        diccionario = {"id": my_id, "distance": distance, "Points": point_array}
        return Response(diccionario)


# Return a List of all the Polygons in the database
class List_polygon(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        lista = []
        allPolygons = Poligon.objects.all()
        allPolygonslen = len(allPolygons)
        for ii in range(allPolygonslen):
            id = ii
            myPolygon = allPolygons[ii].id
            number_points = allPolygons[ii].number_points
            myPoints = Points.objects.filter(poligon_id=myPolygon)
            if len(myPoints) > 0:
                for i in range(number_points):
                    point_array.append([myPoints[i].point_x, myPoints[i].point_y])
            else:
                point_array = []
            diccionario = {
                "id": myPolygon,
                "distance": allPolygons[ii].distance,
                "Points": point_array,
            }

            lista.append(diccionario)

            point_array = []

        return Response(lista)


# Return the Polygon from the id
class Find_polygon(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        id = request.data.get("id")
        myPolygon = Poligon.objects.get(id=id)
        number_points = myPolygon.number_points
        myPoints = Points.objects.filter(poligon_id=id)
        point_array = []
        for i in range(number_points):
            point_array.append([myPoints[i].point_x, myPoints[i].point_y])

        diccionario = {
            "id": id,
            "distance": myPolygon.distance,
            "Points": point_array,
        }
        return Response(diccionario)


# Verify if a point is within the Polygon
class Verify_point(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        from shapely.geometry import Point, Polygon

        id = request.data.get("id")
        x = request.data.get("x")
        y = request.data.get("y")
        myPolygon = Poligon.objects.get(id=id)
        number_points = myPolygon.number_points
        myPoints = Points.objects.filter(poligon_id=id)
        point_array = []
        for i in range(number_points):
            point_array.append((myPoints[i].point_x, myPoints[i].point_y))
        # Create Point objects
        p1 = Point(float(x), float(y))
        # Create a Polygon
        poly = Polygon(point_array)
        diccionario = {"id": id, "Dentro de Polígono": p1.within(poly)}
        return Response(diccionario)
