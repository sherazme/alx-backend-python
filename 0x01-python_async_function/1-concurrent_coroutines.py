#!/usr/bin/env python3
"""
execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn waitRandom n times with the specified max_delay
    """
    j = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    e = [await task for task in asyncio.as_completed(j)]
    return e
