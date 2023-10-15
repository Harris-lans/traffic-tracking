from vector import Vector

class Car:
    def __init__(self, position: Vector, direction: Vector) -> None:
        self.position = position
        self.direction = direction