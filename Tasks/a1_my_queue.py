"""
My little Queue
"""
from typing import Any, List

import queue


_queue: List = []

def enqueue(elem: Any) -> None:
	_queue.append(elem)


	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""



def dequeue() -> Any:
	if _queue:
		return _queue.pop(0)


	"""
	Return element from the beginning of the queue. Should return None if no elements.

	:return: dequeued element
	"""



def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	if ind in range(len(_queue)):
		return _queue[ind]

def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	if _queue:
		_queue.clear()


