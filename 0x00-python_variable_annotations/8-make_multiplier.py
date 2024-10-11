#!/usr/bin/env python3
""" functions"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes float multiplier as argument,
    returns function that multiplies float number by multiplier
    """
    def multi(n: float) -> float:
        """ multiplies float number by multiplier """
        return float(n * multiplier)

    return multi
