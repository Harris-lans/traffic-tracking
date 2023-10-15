import math

class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Overload the + operator to perform vector addition.

        Parameters:
            other (Vector): The other vector to be added.

        Returns:
            Vector: The result of the vector addition.
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Overload the - operator to perform vector subtraction.

        Parameters:
            other (Vector): The other vector to be subtracted.

        Returns:
            Vector: The result of the vector subtraction.
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        """
        Overload the * operator to perform scalar multiplication.

        Parameters:
            scalar (float): The scalar value to multiply the vector.

        Returns:
            Vector: The result of the scalar multiplication.
        """
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float):
        """
        Overload the / operator to perform scalar division.

        Parameters:
            scalar (float): The scalar value to divide the vector.

        Returns:
            Vector: The result of the scalar division.
        """
        return Vector(self.x / scalar, self.y / scalar)

    def __eq__(self, other):
        """
        Overload the == operator to perform vector equality check.

        Parameters:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if both vectors have the same x and y values; False otherwise.
        """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """
        Overload the != operator to perform vector inequality check.

        Parameters:
            other (Vector): The other vector to compare.

        Returns:
            bool: True if either x or y values of the vectors are different; False otherwise.
        """
        return not self.__eq__(other)

    def is_zero(self):
        return self.x == 0 and self.y == 0

    @staticmethod
    def normalize(vector):
        """
        Normalize the input vector.

        Parameters:
            vector (Vector): The input vector to be normalized.

        Returns:
            Vector: The normalized vector.
        """
        magnitude = Vector.magnitude(vector)
        return vector / magnitude

    @staticmethod
    def magnitude(vector):
        """
        Calculate the magnitude (length) of the input vector.

        Parameters:
            vector (Vector): The input vector.

        Returns:
            float: The magnitude of the vector.
        """
        return math.sqrt(vector.x**2 + vector.y**2)

    @staticmethod
    def distance(vector1, vector2):
        """
        Calculate the distance between two vectors.

        Parameters:
            vector1 (Vector): The first vector.
            vector2 (Vector): The second vector.

        Returns:
            float: The distance between the two vectors.
        """
        return Vector.magnitude(vector2 - vector1)

    @staticmethod
    def dot_product(vector1, vector2):
        """
        Calculate the dot product between two vectors.

        Parameters:
            vector1 (Vector): The first vector.
            vector2 (Vector): The second vector.

        Returns:
            float: The dot product of the two vectors.
        """
        return vector1.x * vector2.x + vector1.y * vector2.y

    @staticmethod
    def cross_product(vector1, vector2):
        """
        Calculate the cross product between two vectors in 2D.

        Parameters:
            vector1 (Vector): The first vector.
            vector2 (Vector): The second vector.

        Returns:
            float: The cross product of the two vectors.
        """
        return vector1.x * vector2.y - vector1.y * vector2.x

    @staticmethod
    def angle_between(vector1, vector2):
        """
        Find the angle (in degrees) between two vectors.

        Parameters:
            vector1 (Vector): The first vector.
            vector2 (Vector): The second vector.

        Returns:
            float: The angle between the two vectors in degrees.
        """
        dot_product = Vector.dot_product(vector1, vector2)
        magnitude_product = Vector.magnitude(vector1) * Vector.magnitude(vector2)

        if magnitude_product == 0:
            raise ValueError("Cannot compute angle for zero magnitude vector.")

        cos_theta = dot_product / magnitude_product
        theta_rad = math.acos(max(-1, min(1, cos_theta)))  # Ensure the value is in valid range for acos
        return math.degrees(theta_rad)
