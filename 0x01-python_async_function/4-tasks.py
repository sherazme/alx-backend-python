#!/usr/bin/env python3
""" The basics of async """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    alter it into a new function task_wait_n
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    return [await t for t in asyncio.as_completed(task)]
