#!/usr/bin/env python3
"""
Server class and helper function for pagination.
"""

import csv
import math
from typing import List, Tuple, Dict, Optional


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset (a list of rows).
        Parameters:
        - page (int): the page number, 1-indexed.
        - page_size (int): the number of items per page.
        Returns:
        List[List]: a list of rows corresponding to the requested page.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index] if start_index < len(dataset) \
            else []

    def get_hyper(
            self, page: int = 1, page_size: int = 10
    ) -> Dict[str, Optional[int]]:
        """
        Returns a dictionary with pagination information.
        Parameters:
        - page (int): the page number, 1-indexed.
        - page_size (int): the number of items per page.
        Returns:
        Dict: A dictionary with pagination information.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
