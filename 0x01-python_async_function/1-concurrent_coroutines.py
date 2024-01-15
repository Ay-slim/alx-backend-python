#!/usr/bin/env python3
"""Concurrent coroutines module"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ret_list = []
    for i in range(n):
        ret_list.append(await wait_random(max_delay))
    return sorted(ret_list)
