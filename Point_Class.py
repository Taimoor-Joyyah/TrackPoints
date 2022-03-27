class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, point):
        return (((point.x - self.x) ** 2) + ((point.y - self.y) ** 2)) ** 0.5

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
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def distance(self, point):
        return ((Point.distance(self, point) ** 2) + ((point.z - self.z) ** 2)) ** 0.5
