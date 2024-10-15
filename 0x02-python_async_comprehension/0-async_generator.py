#!/usr/bin/env python3
""" 
asynchronous generator function that yields random float 
between 0 and 10 after one second delay for 10 iterations
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Returns Asynchronous generator object that can be used in an
    awaitable context.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
