#!/usr/bin/env python3
"""
Helper function for pagination.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for the range of items
    on a specific page based on the page number and page size.
    Parameters:
    - page (int): the page number, 1-indexed.
    - page_size (int): the number of items per page.
    Returns:
    Tuple[int, int]: a tuple containing the start and end indices.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
