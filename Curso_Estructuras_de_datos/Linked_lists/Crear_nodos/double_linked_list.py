from typing import Iterable
from typing import Optional
from typing import Union

from nodos import TwoWayNode


class DoubleLinkedList:

    _head: Optional[TwoWayNode]

    _size: int

    def __init__(self, *items):
        """Initializes a double linked list."""

        self._head = None
        self._size = 0

        if len(items) > 0 and isinstance(items[0], Iterable):
            items = items[0]

        for item in items:
            self.append(item)

    @property
    def size(self) -> int:
        """Returns the size of the list."""

        return self._size

    def append(self, data: object):
        """Appends a node to the end of the list.

        Time complexity: O(n)
        """

        new_node = TwoWayNode(data)

        if self._head is None:
            self._head = new_node
        else:
            current = self._head

            while current.next is not None:
                current = current.next

            current.next = new_node
            new_node.previous = current

        self._size += 1

    def itervalues(self):
        """Iterates over the list."""

        current = self._head

        while current is not None:
            yield current.value
            current = current.next

    def iteritems(self):
        """Iterates over the list."""

        current = self._head

        while current is not None:
            yield current
            current = current.next

    def insert(self, index: int, value: object):
        """Inserts item before index.

        Time complexity: O(n)

        Args:
            index: The index to insert the item before.
            value: The value to insert.
        Returns:
            None
        """

        if index < 0:
            index = self._size + index

        if index > self._size - 1:
            raise IndexError('Index out of range')

        if index == 0:
            self._head = TwoWayNode(value, self._head)

        else:
            for idx, item in enumerate(self):
                if idx == index:
                    new_node = TwoWayNode(value)
                    new_node.next = item

                    item.previous.next = new_node
                    item.previous = new_node
                    break

        self._size += 1

        return None

    def index(self, target: object) -> int:
        """Returns the index of the value.

        Raises ValueError if the value is not in the list.

        Time complexity: O(n)

        Args:
            target: The value to find the index of.

        Returns:
            int: The index of the value.
        """

        item: TwoWayNode
        for index, item in enumerate(self):
            if item.value == target:
                return index

        raise ValueError('Value not found')

    def clear(self):
        """Clears the list."""

        self._head = None
        self._size = 0

    def replace(self, old_value: object, new_value: object):
        """Replaces the old value with the new value.

        Raises ValueError if the value is not in the list.

        Time complexity: O(n)

        Args:
            old_value: The value to replace.
            new_value: The new value.

        Returns:
            None
        """

        item: TwoWayNode
        for item in self:
            if item.value == old_value:
                item.value = new_value
                return None

        raise ValueError('Value not found')

    def pop(self, raw: bool = False) -> Union[object, TwoWayNode]:
        """Removes the last item and returns it.

        Time complexity: O(n)

        Args:
            raw: If True, returns the node instead of the value.

        Returns:
            object: The last item.
        """

        if self._head is None:
            raise IndexError('List is empty')

        item: TwoWayNode
        for item in self:
            pass

        if item.previous is not None:
            item.previous.next = None

        self._size -= 1

        if raw:
            return item

        return item.value

    def remove(self, target: object):
        """Removes the target from the list.

        Raises ValueError if the value is not in the list.

        Time complexity: O(n)

        Args:
            target: The value to remove.

        Returns:
            None
        """

        item: TwoWayNode
        for item in self:
            if item.value == target:
                if item.previous is not None:
                    item.previous.next = item.next

                if item.next is not None:
                    item.next.previous = item.previous

                self._size -= 1

                return None

        raise ValueError('Value not found')

    def reverse(self):
        """Reverses the double linked list.

        Time complexity: O(n)
        """

        temp = None
        current = self._head

        # Swap next and previous for all nodes of the list
        while current is not None:
            temp = current.previous
            current.previous = current.next
            current.next = temp
            current = current.previous

        # Before changing the head, check for the cases like empty list
        if temp is not None:
            self._head = temp.previous

    def __getitem__(self, index: int) -> object:
        """Returns the item at the index.

        Raises IndexError if the index is out of range.

        Time complexity: O(n)

        Args:
            index: The index to get the item at.

        Returns:
            object: The item at the index.
        """

        if index < 0:
            index = self._size + index

        if index > self._size - 1:
            raise IndexError('Index out of range')

        item: TwoWayNode
        for idx, item in enumerate(self):
            if idx == index:
                return item.value

        return None

    def __setitem__(self, index: int, value: object):
        """Sets the item at the index.

        Raises IndexError if the index is out of range.

        Time complexity: O(n)

        Args:
            index: The index to set the item at.
            value: The value to set.

        Returns:
            None
        """

        if index < 0:
            index = self._size + index

        if index > self._size - 1:
            raise IndexError('Index out of range')

        if index == 0:
            self._head.value = value

        else:

            item: TwoWayNode
            for idx, item in enumerate(self):
                if idx == index:
                    item.value = value

                    break

        return None

    def __iter__(self):
        return self.iteritems()

    def __len__(self) -> int:
        """Returns the size of the list."""

        return self._size

    def __delitem__(self, index: int):
        """Deletes the item at the index.

        Raises IndexError if the index is out of range.

        Time complexity: O(n)

        Args:
            index: The index to delete the item at.

        Returns:
            None
        """

        if index < 0:
            index = self._size + index

        if index > self._size - 1:
            raise IndexError('Index out of range')

        if index == 0:
            self._head = self._head.next

        else:

            item: TwoWayNode
            for idx, item in enumerate(self):
                if idx == index:
                    if item.previous is not None:
                        item.previous.next = item.next

                    if item.next is not None:
                        item.next.previous = item.previous

                    self._size -= 1

                    break

        return None
