#!/usr/bin/env python3
"""Execute multiple coroutines"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """async routine"""
    f_delays = [wait_random(max_delay) for _ in range(n)]
    f_delays = asyncio.as_completed(f_delays)
    delays = [await delay for delay in f_delays]
    return delays
