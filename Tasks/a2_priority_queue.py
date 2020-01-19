"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any, Dict



_queue: Dict = {}


def enqueue(elem: Any, priority: int = 0):
	_queue[priority] = elem





def dequeue() -> Any:
	if _queue:
		return _queue.pop(0)
	"""
	Return element from the beginning of the queue. Should return None if not elements.

	:return: dequeued element
	"""
	return None


def peek(ind: int = 0, priority: int = 0) -> Any:
	if ind in enumerate(_queue):
		return _queue[priority]



	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""



def clear() -> None:
	if _queue:
		_queue.clear()
	"""
	Clear my queue

	:return: None
	"""

