#!/usr/bin/env python3
"""Async generator module"""


import random
import asyncio
from typing import Iterator


async def async_generator() -> Iterator[int]:
    """
    async_generator - Function to wait for a bit and yield a random int
    Returns: A generator
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
