# /tests/tests_circle.py

import pytest
from math_tools import circle

def test_area_integer_radius():
    assert circle.area(1) == 3.141592653589793
    assert circle.area(2) == 12.566370614359172
    assert circle.area(3) == 28.274333882308138

def test_perimeter_integer_radius():
    assert circle.perimeter(1) == 6.283185307179586
    assert circle.perimeter(2) == 12.566370614359172
    assert circle.perimeter(3) == 18.84955592153876

def test_area_zero_radius():
    assert circle.area(0) == 0

def test_perimeter_zero_radius():
    assert circle.perimeter(0) == 0

def test_area_negative_radius():
    assert circle.area(-4) == 0

def test_perimeter_negative_radius():
    assert circle.perimeter(-4) == 0
