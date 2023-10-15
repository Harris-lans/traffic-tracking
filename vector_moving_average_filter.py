from vector import Vector

class VectorMovingAverageFilter:
    def __init__(self, window_size):
        self.window_size = window_size
        self.data = []

    def smoothen_value(self, value: Vector) -> Vector:
        self.data.append(value)

        if len(self.data) > self.window_size:
            self.data.pop(0)

        return sum(self.data, Vector(0, 0)) / len(self.data)