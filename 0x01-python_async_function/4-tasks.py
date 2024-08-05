#!/usr/bin/env python3
"""Execute multiple coroutines"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays"""
    f_delays = [task_wait_random(max_delay) for _ in range(n)]
    f_delays = asyncio.as_completed(f_delays)
    delays = [await delay for delay in f_delays]
    return delays
