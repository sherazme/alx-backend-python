#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """

import asyncio
from typing import List

waitRandom = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn waitRandom n times with the specified max_delay.
    """
    tasks = = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(tasks)
