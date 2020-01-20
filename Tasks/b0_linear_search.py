"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

def min_search(arr: Sequence) -> int:
	min = arr[0]
	ind_position = 0
	for ind, el in enumerate(arr):
		if el<min:
			min = el
			ind_position = ind
	return ind_position

