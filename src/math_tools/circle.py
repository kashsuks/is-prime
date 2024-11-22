import math

def area(radius: float) -> float:
    """
    Finds the area of the circle given the radius.

    :param radius: Radius of the circle.
    :type radius: float
    :return: area (float)
    """
    if radius < 0:
        return 0
    return math.pi * pow(radius, 2)

def perimeter(radius: float) -> float:
    """
    Finds the area of the circle given the radius.

    :param radius: Radius of the circle.
    :type radius: float
    :return: perimeter (float)
    """
    if radius < 0:
        return 0
    return 2 * math.pi * radius