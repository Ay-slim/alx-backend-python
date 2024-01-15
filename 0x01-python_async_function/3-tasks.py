#!/usr/bin/env python3
"""Tasks task (pun intended) module"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    task_wait_random - Random wait task
    @max_delay: Int. Max delay arg to random_wait
    Returns: Async task
    """
    return asyncio.create_task(wait_random(max_delay))
