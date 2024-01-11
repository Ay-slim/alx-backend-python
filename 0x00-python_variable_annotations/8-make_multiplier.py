#!/usr/bin/env python3
"""Make multiplier function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier - Make multiplier
    @multiplier: Multiplier to work with
    Return: Returns a function multiplying the arg with a float
    """
    return lambda x: x * multiplier
