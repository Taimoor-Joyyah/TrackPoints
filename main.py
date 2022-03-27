import Point_Class
from Point_Class import Point as Point2D, Point3D

point_list = [
    Point3D(2, 5, 7), Point3D(3, 7, 9), Point3D(9, 0, 3),
    Point3D(3, 6, 5), Point3D(5, 5, 0), Point3D(1, 9, 3),
    Point3D(4, 0, 1), Point3D(8, 8, 9), Point3D(0, 2, 0)
]

current_point = point_list[0]
point_not_on_track = point_list.copy()
point_on_track = [current_point]
point_not_on_track.remove(current_point)

while point_not_on_track:
    current_point = current_point.nearest_point(point_not_on_track)
    point_not_on_track.remove(current_point)
    point_on_track.append(current_point)

print([(point.x, point.y, point.z) for point in point_on_track])

print(point_on_track[0].distance(point_on_track[1]))
print(point_on_track[1].distance(point_on_track[2]))
print(point_on_track[2].distance(point_on_track[3]))
print(point_on_track[3].distance(point_on_track[4]))