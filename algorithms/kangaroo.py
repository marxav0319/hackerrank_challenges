import random
import os
import sys

def kangaroo(x1, v1, x2, v2):
    """
    Given the starting positions and velocities of two "kangaroos", determine
    whether the kangaroos will meet at the same ending position within the
    same number of jumps.

    Args:
        x1 <int>: the starting position of the first kangaroo
        v1 <int>: the velocity of the first kangaroo
        x1 <int>: the starting position of the second kangaroo
        v2 <int>: the velocity of the second kangaroo

    Return:
        str: YES or NO
    """
    can_hop = "NO"
    numerator = x2-x1
    denominator = v1-v2
    
    if (denominator > 0):
        if numerator % denominator == 0:
            return "YES"

    return can_hop


def run_test_cases():
    """
    Runs the test cases provided by hackerrank

    Args:
        None

    Returns:
        None
    """
    result = kangaroo(0, 3, 4, 2)
    print(result)

    result = kangaroo(0, 2, 5, 3)
    print(result)

    result = kangaroo(43, 2, 70, 2)
    print(result)
    
    return
    
if __name__ == '__main__':
    run_test_cases()
