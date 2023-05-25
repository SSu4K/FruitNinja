class Blade:
    def __init__(self, max_points):
        self.max_points = max_points
        self._points = [[int, int]]*max_points
        for point in self._points:
            point[0]=0
            point[1]=0
    
    def add_point(self, point):
        self._points.pop(0)
        self._points.append(point)
    
    def get_points(self):
        return self._points
    
