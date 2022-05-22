import Point_Class
from Point_Class import Point as Point2D, Point3D
from turtle import *

point_list = [
    Point2D(2, 5), Point2D(3, 7), Point2D(9, 0),
    Point2D(3, 6), Point2D(5, 5), Point2D(1, 9),
    Point2D(4, 0), Point2D(8, 8), Point2D(0, 2)
]

current_point = point_list[0]
point_not_on_track = point_list.copy()
point_on_track = [current_point]
point_not_on_track.remove(current_point)

while point_not_on_track:
    current_point = current_point.nearest_point(point_not_on_track)
    point_not_on_track.remove(current_point)
    point_on_track.append(current_point)

print([(point.x, point.y) for point in point_on_track])

# Printing Track Point on Turtle
penup()
ht()
for i, point in enumerate(point_on_track):
    goto(point.x*50, point.y*50)
    if not i:
        pendown()
    dot()
done()
