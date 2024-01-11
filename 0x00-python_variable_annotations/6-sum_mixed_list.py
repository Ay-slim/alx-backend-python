#!/usr/bin/env python3
"""Sum mixed list function module"""


from typing import List


def sum_mixed_list(mxd_lst: List[float | int]) -> float:
    """
    sum_mixed_list - Sums a mixed list of floats
    @mxd_lst: List of mixed floats and integers
    Return: Float
    """
    return sum(mxd_lst)
