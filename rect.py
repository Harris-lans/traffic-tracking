from vector import Vector

class Rect:
  def __init__(self, position: Vector, width: int, height: int) -> None:
    """
    Initialize a rectangle with given coordinates and dimensions.

    Parameters:
        x (float): The x-coordinate of the top-left corner of the rectangle.
        y (float): The y-coordinate of the top-left corner of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

    Returns:
        None
    """
    self.position = position
    self.width = width
    self.height = height

  def get_centroid(self):
    """
    Get the centroid (center) coordinates of the rectangle.

    Returns:
        Tuple[float, float]: A tuple containing the x and y coordinates of the centroid.
    """
    return Vector(self.position.x + (self.width / 2), self.position.y + (self.height / 2))
  
  @staticmethod
  def is_rect_within_rect(outer_rect, inner_rect, percentage_threshold: float = 100):
    """
    Check if the inner rectangle is at least a certain percentage within the outer rectangle.

    Parameters:
        outer_rect (Rect): The outer rectangle.
        inner_rect (Rect): The inner rectangle to be checked.
        percentage_threshold (float): The minimum percentage of the inner rectangle area within the outer rectangle.

    Returns:
        bool: True if the inner rectangle's area is greater than or equal to the specified percentage of the
              outer rectangle's area; False otherwise.
    """
    # Calculate the area of the outer and inner rectangles
    area_outer = outer_rect.width * outer_rect.height
    area_inner = inner_rect.width * inner_rect.height

    # Calculate the intersection area between the two rectangles
    x_overlap = max(0, min(outer_rect.position.x + outer_rect.width, inner_rect.position.x + inner_rect.width) - max(outer_rect.position.x, inner_rect.position.x))
    y_overlap = max(0, min(outer_rect.position.y + outer_rect.height, inner_rect.position.y + inner_rect.height) - max(outer_rect.position.y, inner_rect.position.y))
    intersection_area = x_overlap * y_overlap

    # Calculate the percentage of the inner rectangle area within the outer rectangle
    percentage_within = intersection_area / area_inner * 100

    # Return True if the percentage is greater than or equal to the threshold
    return percentage_within >= percentage_threshold
  
  @staticmethod
  def is_point_within_rect(point: Vector, rect):
    """
    Check if the inner rectangle is at least a certain percentage within the outer rectangle.

    Parameters:
        outer_rect (Rect): The outer rectangle.
        inner_rect (Rect): The inner rectangle to be checked.
        percentage_threshold (float): The minimum percentage of the inner rectangle area within the outer rectangle.

    Returns:
        bool: True if the inner rectangle's area is greater than or equal to the specified percentage of the
              outer rectangle's area; False otherwise.
    """
    return point.x >= rect.position.x and point.x <= rect.position.x + rect.width and point.y >= rect.position.y and point.y <= rect.position.y + rect.height
