from collections import deque
from typing import Any, Iterable, Iterator, Optional


class Stack:
    """Implement a Stack (LIFO) abstract data type."""

    def __init__(
        self,
        iterable: Optional[Iterable[Any]] = None,
        /,
    ) -> None:
        self._data: deque = deque()
        if iterable is not None:
            self._data.extend(iterable)

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._data.append(item)

    def pop(self) -> Any:
        """Remove and return an item from the top of the stack."""
        try:
            return self._data.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None

    def top(self) -> Any:
        """Return the item at the top of the stack."""
        try:
            return self._data[-1]
        except IndexError:
            raise IndexError("top from an empty stack") from None

    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise."""
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
