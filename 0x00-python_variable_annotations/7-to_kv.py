#!/usr/bin/env python3
"""
   function to_kv annotations
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to_kv arguments that returns a tuple """
    return k, float(v**2)
