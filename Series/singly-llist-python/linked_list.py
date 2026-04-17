from typing import Any, Iterable, Iterator, Optional


class Node:
    """Node of a linked list."""

    def __init__(self, data: Any) -> None:
        self.next: Optional["Node"] = None
        self.data = data

    def __repr__(self) -> str:
        return str(self.data)


class LinkedList:
    """Implement a singly linked list abstract data type."""

    def __init__(self, data: Optional[Iterable[Any]] = None, /) -> None:
        self.head: Optional[Node] = None
        self._length: int = 0
        if data is not None:
            data_as_list = list(data)
            if (length := len(data_as_list)) > 0:
                head, *rest = data_as_list
                self._length = length
                self.head = Node(data=head)
                node = self.head
                for value in rest:
                    node.next = Node(data=value)
                    node = node.next

    def append_left(self, value: Any) -> None:
        """Add a node holding value to the left end of the linked list."""
        node = Node(data=value)
        node.next = self.head
        self.head = node
        self._length += 1

    def append(self, value: Any) -> None:
        """Add a node holding value to the right end of the linked list."""
        node = Node(data=value)
        if self.head is None:
            self.head = node
        else:
            # Traverse the list to reach the last node
            for last_node in self:
                pass
            last_node.next = node
        self._length += 1

    def insert(self, index: int, value: Any) -> None:
        """Insert a node holding value at index."""
        if self.head is None or index == 0:
            self.append_left(value)
            return
        previous_node = self.head
        for i, current_node in enumerate(self):
            if i == index:
                node = Node(data=value)
                previous_node.next = node
                node.next = current_node
                self._length += 1
                return
            previous_node = current_node
        raise IndexError("index out of range")

    def remove(self, value: Any) -> None:
        """Remove the node holding value."""
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            self._length -= 1
            return
        previous_node = self.head
        for current_node in self:
            if current_node.data == value:
                previous_node.next = current_node.next
                self._length -= 1
                return
            previous_node = current_node
        raise IndexError(f"{value} doesn't exist")

    def reverse(self) -> None:
        """Reverse the list in place."""
        if self.head is None:
            return
        previous: Optional[Node] = None
        current: Optional[Node] = self.head
        next_node: Optional[Node] = current.next
        while current:
            current.next = previous
            previous = current
            current = next_node
            if next_node:
                next_node = next_node.next
        self.head = previous

    def __iter__(self) -> Iterator:
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:
        data = [node.data for node in self]
        return f"{self.__class__.__name__}({data})"

    def __str__(self) -> str:
        data = [str(node.data) for node in self]
        data.append("None")
        if len(data) == 1:
            return f"HEAD({data[0]})"
        return f"HEAD({data[0]}) -> " + " -> ".join(data[1:])

    def __len__(self) -> int:
        return self._length
