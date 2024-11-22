import math

def area(radius: float) -> float:
    """

    Args:
        radius: (float) The radius of the circle

    Returns:
        area: (float) The area of the circle

    """
    if radius < 0:
        return 0
    return math.pi * pow(radius, 2)

def perimeter(radius: float) -> float:
    """

    Args:
        radius: (float) The radius of the circle

    Returns:
        perimeter: (float) The perimeter of the circle
    """
    if radius < 0:
        return 0
    return 2 * math.pi * radius