import ctypes
from typing import Any, Generator, Optional


class Array:
    def __init__(self, size: int) -> None:
        if size <= 0:
            raise ValueError("Array size must be a positive integer")
        self._size = size
        self._data = (ctypes.py_object * self._size)()
        self._type: Optional[type] = None
        self.clear()

    def clear(self, value: Optional[Any] = None) -> None:
        if (
            self._type is not None
            and value is not None
            and not isinstance(value, self._type)
        ):
            raise TypeError(f"Expected type {self._type}, got {type(value)}")
        for i in range(self._size):
            self._data[i] = value

    def __len__(self) -> int:
        return self._size

    def __contains__(self, value: Any) -> bool:
        for item in self._data:
            if item == value:
                return True
        return False

    def _check_index(self, index: int) -> None:
        if not 0 <= index < self._size:
            raise IndexError(
                f"Index out of range: {index}. Valid range: 0 to {self._size - 1}"
            )

    def __getitem__(self, index: int) -> Any:
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if self._type is None and value is not None:
            self._type = type(value)
        elif value is not None and not isinstance(value, self._type):
            raise TypeError(f"Expected type {self._type}, got {type(value)}")
        self._check_index(index)
        self._data[index] = value

    def __iter__(self) -> Generator[Any, None, None]:
        yield from self._data

    def __reversed__(self) -> Generator[Any, None, None]:
        yield from reversed(self._data)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({', '.join(map(str, self._data))})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(size={self._size})"
