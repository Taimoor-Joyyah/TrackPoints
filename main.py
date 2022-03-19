import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        return math.sqrt(math.pow((point.x - self.x), 2) + math.pow((point.y - self.y), 2))

    def nearest_point(self, point_list):
        near_point = point_list[0]
        for index, point in enumerate(point_list):
            if index:
                if self.distance(point) < self.distance(near_point):
                    near_point = point
        return near_point

    def point_distance(self, end_point, point_on_track):
        previous_point = self
        total_distance = 0
        for index, point in enumerate(point_on_track[point_on_track.index(self):]):
            if index:
                total_distance += point.distance(previous_point)
                previous_point = point
            if point is end_point:
                return total_distance


class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def distance(self, point):
        return math.sqrt(math.pow(Point.distance(self, point), 2) + math.pow((point.z - self.z), 2))


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
print(point_on_track[4].distance(point_on_track[5]))
print(point_on_track[0].point_distance(point_on_track[5], point_on_track))