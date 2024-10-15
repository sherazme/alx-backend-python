#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async """

import asyncio
from typing import List

waitRandom = __import__('0-basic_async_syntax').waitRandom


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn waitRandom n times with the specified max_delay.
    """
    tasks = [asyncio.create_task(waitRandom(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
