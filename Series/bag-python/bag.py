from collections import Counter
from collections.abc import Iterable, Iterator
from random import choice as _choice
from typing import Any, Optional


class Bag:
    """Implement a Bag (multiset) abstract data type."""

    def __init__(self, iterable: Optional[Iterable[Any]] = None, /) -> None:
        self._data: list[Any] = []
        if iterable is not None:
            self._data.extend(iterable)

    def add(self, value: Any) -> None:
        """Add an object to the Bag."""
        self._data.append(value)

    def remove(self, value: Any) -> None:
        """Remove an object from the Bag."""
        try:
            self._data.remove(value)
        except ValueError:
            raise ValueError(f"{value} not in {self.__class__.__name__}") from None

    def count(self, value: Any) -> int:
        """Count the number of times an object appears in the Bag."""
        return self._data.count(value)

    def clear(self) -> None:
        """Remove all the objects from the Bag."""
        self._data.clear()

    def pop(self) -> Any:
        """Remove and return an item from the right end of the Bag."""
        try:
            return self._data.pop()
        except IndexError:
            raise IndexError("pop from empty bag") from None

    def randpop(self) -> Any:
        """Remove and return a random item from the Bag."""
        try:
            value: Any = _choice(self._data)
        except IndexError:
            raise IndexError("randpop from empty bag") from None
        self._data.remove(value)
        return value

    def as_counter(self) -> Counter:
        """Return a Counter from the objects in the Bag."""
        try:
            return Counter(self._data)
        except TypeError:
            raise

    def __len__(self) -> int:
        return len(self._data)

    def __contains__(self, value: Any) -> bool:
        return value in self._data

    def __iter__(self) -> Iterator:
        yield from self._data

    def __reversed__(self) -> Iterator:
        yield from reversed(self._data)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self._data})"

    __str__ = __repr__
