# /test/tests_operations

import pytest
from math_tools import operations

def test_add_simple():
    assert operations.add(1, 2) == 3
    assert operations.add( 1400, 268) == 1668
    assert operations.add(1.23, 1.23) == 2.46