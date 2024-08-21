#!/usr/bin/env python3
"""
Task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    start = page_size * (page - 1)
    end = start + page_size
    return (start, end)
