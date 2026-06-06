from operator import add, sub
from typing import Any, Callable, NamedTuple, Self, Tuple


class Size(NamedTuple):
    """Represents a matrix size as a tuple (rows, cols)."""

    rows: int
    cols: int


class Matrix:
    """Represent a numeric matrix as an m x n rectangular grid."""

    def __init__(self, rows: int, cols: int, default: int = 0) -> None:
        self._rows = rows
        self._cols = cols
        self._data = [[default] * cols for _ in range(rows)]

    @property
    def rows(self) -> int:
        """Return the number of rows."""
        return self._rows

    @rows.setter
    def rows(self, value: int) -> None:
        """Raise AttributeError when trying to assign rows."""
        raise AttributeError("can't set 'rows'")

    @property
    def cols(self) -> int:
        """Return the number of columns."""
        return self._cols

    @cols.setter
    def cols(self, value: int) -> None:
        """Raise AttributeError when trying to assign cols."""
        raise AttributeError("can't set 'cols'")

    @property
    def size(self) -> Size:
        """Return the matrix size as a (rows, cols) tuple."""
        return Size(self.rows, self.cols)

    @size.setter
    def size(self, value: Tuple[int, int]) -> None:
        """Raise AttributeError when trying to assign size."""
        raise AttributeError("can't set 'size'")

    def _validate_index(self, index: Tuple[int, int]) -> Tuple[int, int]:
        """Validate an index and return it as a (row, col) tuple."""
        if not isinstance(index, tuple) or len(index) != 2:
            raise IndexError("index must be a tuple of two integers")
        row, col = index
        if not (0 <= row < self.rows):
            raise IndexError(
                f"row index out of range: {row}. Valid range: 0 to {self.rows - 1}"
            )
        if not (0 <= col < self.cols):
            raise IndexError(
                f"column index out of range: {col}. Valid range: 0 to {self.cols - 1}"
            )
        return row, col

    def scale_by(self, scalar: int) -> None:
        """Scale the matrix by a scalar."""
        for i, row in enumerate(self._data):
            for j, _ in enumerate(row):
                self[i, j] *= scalar

    def transpose(self) -> Self:
        """Return the transpose of the current matrix."""
        transposed = type(self)(self.cols, self.rows)
        transposed._data = [list(row) for row in zip(*self._data)]
        return transposed

    def add(self, other: Self) -> Self:
        """Return the sum of this matrix and another matrix."""
        return self.__add__(other)

    def __add__(self, other: Self) -> Self:
        return self._compute(other, operation=add)

    def _compute(self, other: Self, operation: Callable) -> Self:
        if other.__class__ is not self.__class__:
            raise TypeError("expected a Matrix object")
        if other.size != self.size:
            raise ValueError("invalid matrix size")
        matrix = type(self)(self._rows, self._cols)
        for i, row in enumerate(self._data):
            for j, _ in enumerate(row):
                matrix[i, j] = operation(self[i, j], other[i, j])
        return matrix

    def subtract(self, other: Self) -> Self:
        """Return the difference between this matrix and another."""
        return self.__sub__(other)

    def __sub__(self, other: Self) -> Self:
        return self._compute(other, operation=sub)

    def multiply(self, other: Self) -> Self:
        """Return the product of this matrix and another matrix."""
        return self.__mul__(other)

    def __mul__(self, other: Self) -> Self:
        if other.__class__ is not self.__class__:
            raise TypeError("expected a Matrix object")
        if self.cols != other.rows:
            raise ValueError("invalid matrix size")
        matrix = type(self)(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(other.rows):
                    matrix[i, j] += self[i, k] * other[k, j]
        return matrix

    @classmethod
    def from_list_of_lists(cls, iterable: list[list[Any]], /) -> Self:
        """Return a new matrix built from a list of lists."""
        if len(set(len(row) for row in iterable)) > 1:
            raise ValueError("invalid matrix size")
        matrix = cls(rows=len(iterable), cols=len(iterable[0]))
        for i, rows in enumerate(iterable):
            for j, value in enumerate(rows):
                matrix[i, j] = value
        return matrix

    def __getitem__(self, index: Tuple[int, int]) -> Any:
        row, col = self._validate_index(index)
        return self._data[row][col]

    def __setitem__(self, index: Tuple[int, int], value: Any) -> None:
        row, col = self._validate_index(index)
        self._data[row][col] = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(rows={self._rows}, cols={self._cols})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({' '.join(str(row) for row in self._data)})"
