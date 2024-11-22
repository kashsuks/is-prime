import math

def area(radius: float) -> float:
    """
    Finds the area of the circle given the radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: The area of the circle.
    """
    
    return math.pi * (radius ** 2)

def perimeter(radius: float) -> float:
    """
    Finds the perimeter (circumference) of the circle given the radius.

    Args:
        radius (float): Radius of the circle.

    Returns:
        float: The perimeter of the circle.
    """
    
    return 2 * math.pi * radius
