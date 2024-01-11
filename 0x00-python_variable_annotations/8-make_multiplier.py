#!/usr/bin/env python3
"""Make multiplier function module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
