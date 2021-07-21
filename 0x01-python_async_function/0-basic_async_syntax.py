#!/usr/bin/env python3
'''
asynchronous coroutine
'''
import random
import asyncio



async def wait_random(max_delay: int = 10) -> float:
    n = random.random() * max_delay
    await asyncio.sleep(n)
    return n
