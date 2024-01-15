#!/usr/bin/env python3
"""Module for async basics"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random - Async function that waits for a random amount of time
    @max_delay: Int specifiying maximum delay interval
    Returns: Float depicting the random value chosen between 0 and 10
    """
    rand_val = random.uniform(0, max_delay)
    await asyncio.sleep(rand_val)
    return rand_val
