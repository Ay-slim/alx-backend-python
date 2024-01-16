#!/usr/bin/env python3
"""Async comprehension list"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension - Async comprehension function
    Return: A list of floats
    """
    return [i async for i in async_generator()]
