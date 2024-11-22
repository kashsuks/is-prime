import math

def area(radius: float) -> float:
    """
    Finds the area of the circle given the radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: The area of the circle. Returns 0 if radius is negative.
    """
    if radius < 0:
        return 0
    # Using exact value that matches the test expectation
    return math.pi * pow(radius, 2)

def perimeter(radius: float) -> float:
    """
    Finds the perimeter (circumference) of the circle given the radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: The perimeter of the circle. Returns 0 if radius is negative.
    """
    if radius < 0:
        return 0
    return 2 * math.pi * radius