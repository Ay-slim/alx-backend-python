#!/usr/bin/env python3
"""Task wait module"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n - Function to execute the wait_random function a given number of times asynchronously
    @n: Int number of times to run the wait_random function
    @max_delay: Int argument to the wait_random function
    Returns: List of floats
    """
    ret_list = []
    for i in range(n):
        ret_list.append(await asyncio.create_task(wait_random(max_delay)))
    return sorted(ret_list)
