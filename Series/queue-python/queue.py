from collections import deque
from typing import Any, Iterable, Iterator, Optional


class Queue:
    """Implement a Queue (FIFO) abstract data type."""

    def __init__(self, data: Optional[Iterable[Any]] = None, /) -> None:
        self._data: deque = deque()
        if data is not None:
            self._data.extend(data)

    def enqueue(self, item: Any) -> None:
        """Add items to the right end of the queue."""
        self._data.append(item)

    def dequeue(self) -> Any:
        """Remove and return an item from the front of the queue."""
        try:
            return self._data.popleft()
        except IndexError:
            raise IndexError("dequeue from an empty queue") from None

    def front(self) -> Any:
        """Return the item at the beginning of the queue."""
        try:
            return self._data[0]
        except IndexError:
            raise IndexError("front from an empty queue") from None

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of item."""
        try:
            self._data.remove(item)
        except ValueError:
            raise ValueError(
                f"{self.__class__.__name__}.remove(x): x not found"
            ) from None

    def is_empty(self) -> bool:
        """Return True if the queue is empty, False otherwise."""
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, item: Any) -> bool:
        return item in self._data

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({list(self._data)})"

    __str__ = __repr__

    def __iter__(self) -> Iterator:
        yield from self._data

    def __reversed__(self) -> Iterator:
        yield from reversed(self._data)
