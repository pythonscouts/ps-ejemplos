from typing import Any, Iterator, Optional, Sequence


class Node:
    """Node of a doubly linked list."""

    def __init__(self, data: Any) -> None:
        self.data = data
        self.previous: Optional[Node] = None
        self.next: Optional[Node] = None

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data={self.data})"

    def __eq__(self, other: "Node") -> bool:
        if other.__class__ is not self.__class__:
            raise TypeError("Node object expected")
        return self.data == other.data


class DoublyLinkedList:
    """Implement a doubly linked list abstract data type."""

    def __init__(self, iterable: Optional[Sequence[Any]] = None, /) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._length: int = 0
        if iterable is not None and (length := len(iterable)) > 0:
            head, *rest = iterable
            self._length = length
            self.head = Node(data=head)
            current = self.head
            for value in rest:
                current.next = Node(data=value)
                previous = current
                current = current.next
                current.previous = previous
            self.tail = current

    def append_left(self, value: Any) -> None:
        """Add a node holding value to the left end of the list."""
        node = Node(data=value)
        if self.head is not None:
            node.next = self.head
            self.head.previous = node
        else:
            self.tail = node
        self.head = node
        self._length += 1

    def append(self, value: Any) -> None:
        """Add a node holding value to the right end of the list."""
        node = Node(data=value)
        if self.tail is not None:
            node.previous = self.tail
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._length += 1

    def remove(self, value: Any) -> None:
        """Remove the node holding value."""
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            if self.head is not None:
                self.head.previous = None
            else:
                self.tail = None
            self._length -= 1
            return
        if self.tail.data == value:
            self.tail = self.tail.previous
            if self.tail is not None:
                self.tail.next = None
            self._length -= 1
            return
        previous_node = self.head
        for node in self:
            if node.data == value:
                next_node = node.next
                previous_node.next = next_node
                if next_node is not None:
                    next_node.previous = previous_node
                self._length -= 1
                return
            previous_node = node
        raise IndexError(f"{value} doesn't exist")

    def insert(self, index: int, value: Any) -> None:
        """Insert a node holding value at index."""
        if self.head is None or index == 0:
            self.append_left(value)
            return
        previous_node = self.head
        for i, current in enumerate(self):
            if i == index:
                node = Node(data=value)
                previous_node.next = node
                node.next = current
                node.previous = previous_node
                current.previous = node
                self._length += 1
                return
            previous_node = current
        raise IndexError("index out of range")

    def __repr__(self) -> str:
        data = [node.data for node in self]
        return f"{self.__class__.__name__}({data})"

    def __str__(self) -> str:
        data = [str(node.data) for node in self]
        data.append("None")
        if len(data) == 1:
            return f"HEAD({data[0]})"
        return f"HEAD({data[0]}) <-> " + " <-> ".join(data[1:])

    def __iter__(self) -> Iterator:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __reversed__(self) -> Iterator:
        node = self.tail
        while node is not None:
            yield node
            node = node.previous

    def __len__(self) -> int:
        return self._length
