#!/usr/bin/env python3
"""
measure_runtime should
measure the total 
runtime and return it.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime"""
    now = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    return time.time() - now
