#!/usr/bin/env python3
'''time module to measure an approximate elapsed time'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    now = time.time()
    asyncio.run(wait_n(n, max_delay))
    then = time.time()
    return (then - now) / n
