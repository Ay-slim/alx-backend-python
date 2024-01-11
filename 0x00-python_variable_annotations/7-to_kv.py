#!/usr/bin/env python3
"""Return a tuple module"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to_kv - To kv function
    @k: String arg
    @v: Int or float
    Returns: Tuple of string and float
    """
    return (k, v ** 2)
