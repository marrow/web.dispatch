from collections import deque
from pathlib import Path, PurePosixPath


class NoDefault(object):
	__slots__ = []
	
	def __repr__(self):
		return "<no default>"

nodefault = NoDefault()  # Sentinel value.


def ipeek(d):
	"""Iterate through a deque, popping elements from the left after they have been seen."""
	last = None
	
	# We eat trailing slashes.  No sir, can't say we like 'em.
	while d and d[-1] == '':
		d.pop()
	
	while d:
		yield last, d[0]
		last = d.popleft()


def prepare_path(path):
	if isinstance(path, str):
		path = PurePosixPath(path)
	
	if isinstance(path, Path):
		path = deque(path.parts[1 if path.root else 0:])
	else:
		path = deque(path)
