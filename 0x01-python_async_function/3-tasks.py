#!/usr/bin/env python3
"""task_wait_random takes max_delay and returns a asyncio task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """integer max_delay and return a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
