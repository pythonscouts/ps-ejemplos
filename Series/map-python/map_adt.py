from typing import Any, Iterator, Mapping, Optional, Sequence, Tuple


class Map:
    """Implement a Map (associative array) abstract data type."""

    def __init__(
        self, mapping: Optional[Mapping[Any, Any]] = None, /, **kwargs
    ) -> None:
        self._keys: list[Any] = []
        self._values: list[Any] = []
        self.__update(mapping, **kwargs)

    def keys(self) -> Iterator[Any]:
        """Return an iterator over the keys of map."""
        yield from self._keys

    __iter__ = keys

    def values(self) -> Iterator[Any]:
        """Return an iterator over the values of map."""
        yield from self._values

    def items(self) -> Iterator[Tuple[Any, Any]]:
        """Return an iterator that yields key-value tuples."""
        yield from zip(self._keys, self._values)

    __items = items

    def update(self, other: Optional[Mapping[Any, Any]] = None, /, **kwargs) -> None:
        """Update map with items from other."""
        if other is not None:
            for key, value in other.items():
                self[key] = value
        if kwargs:
            for key, value in kwargs.items():
                self[key] = value

    __update = update

    def set_default(self, key: Any, default: Optional[Any] = None, /) -> Any:
        """Insert a key-default pair into map if key doesn't exist.

        Return the value for key if key is in the map, else default.
        """
        try:
            return self[key]
        except KeyError:
            self[key] = default
            return default

    def pop(self, key: Any) -> Any:
        """Remove a key-value pair and return the value."""
        try:
            index = self._keys.index(key)
        except ValueError:
            raise KeyError(f"{key}") from None
        self._keys.remove(key)
        return self._values.pop(index)

    def popitem(self) -> Tuple[Any, Any]:
        """Remove and return a key-value pair as a tuple."""
        try:
            return self._keys.pop(), self._values.pop()
        except IndexError:
            raise KeyError("popitem from empty Map") from None

    def clear(self) -> None:
        """Remove all the items from map."""
        self._keys.clear()
        self._values.clear()

    @classmethod
    def fromkeys(cls, iterable: Sequence, value: Optional[Any] = None, /) -> "Map":
        """Return a new Map with keys from iterable and values from value."""
        mapping = cls()
        for key in iterable:
            mapping[key] = value
        return mapping

    def get(self, key: Any, default: Optional[Any] = None) -> Any:
        """Return the value for key if key is in the map, else default."""
        try:
            return self[key]
        except KeyError:
            return default

    def __getitem__(self, key: Any) -> Any:
        try:
            index = self._keys.index(key)
        except ValueError:
            raise KeyError(f"{key}") from None
        return self._values[index]

    def __setitem__(self, key: Any, value: Any) -> None:
        hash(key)
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __eq__(self, other: "Map") -> bool:
        if other.__class__ is not self.__class__:
            return False
        if len(self) != len(other):
            return False
        other_items = list(other.__items())
        for item in self.__items():
            if item not in other_items:
                return False
        return True

    def __contains__(self, key: Any) -> bool:
        return key in self._keys

    def __len__(self) -> int:
        return len(self._keys)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({dict(zip(self._keys, self._values))})"

    def __str__(self) -> str:
        return f"{dict(zip(self._keys, self._values))}"

    def __delitem__(self, key: Any) -> None:
        try:
            index = self._keys.index(key)
        except ValueError:
            raise KeyError(f"{key}") from None
        del self._keys[index]
        del self._values[index]

    def __reversed__(self) -> Iterator:
        yield from reversed(self._keys)
