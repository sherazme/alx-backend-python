#!/usr/bin/env python3
""" The basics of async """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """  use the regular function syntax """
    t = create_task(wait_random(max_delay))
    return t
