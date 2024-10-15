#!/usr/bin/env python3
""" 
asynchronous generator function that yields random float 
between 0 and 10 after one second delay for 10 iterations
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Returns Asynchronous generator object that can be used in an
    awaitable context.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
