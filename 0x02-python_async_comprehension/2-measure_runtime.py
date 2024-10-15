#!/usr/bin/env python3
'''
provide asynchronous function that measures the runtime
of running 4 instances of async_comprehension function
'''
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
     Returns The runtime of the async_comprehension function in seconds.
    '''
    startTime = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - startTime
