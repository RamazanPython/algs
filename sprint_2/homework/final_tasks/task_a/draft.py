class Node:

    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return f"{self.data})"


class LinkedList:

    def __init__(self, max_size: int):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.max_size = max_size
        self.size = 0

    def _add_head(self, data):
        node = Node(data=data)
        self.head = node
        self.tail = node
        self.size += 1

    @property
    def is_full(self):
        return self.size == self.max_size

    @property
    def is_empty(self):
        return self.size == 0

    def add_right(self, data):
        if self.size + 1 > self.max_size:
            raise OverflowError()

        if self.head is None:
            self._add_head(data)
            return

        new_tail = Node(data=data, prev_node=self.tail, next_node=None)
        self.tail.next_node = new_tail
        self.tail = new_tail
        self.size += 1

    def add_left(self, data):
        if self.size + 1 > self.max_size:
            raise OverflowError()

        if self.head is None:
            self._add_head(data)
            return

        new_head = Node(data=data, prev_node=None, next_node=self.head)
        self.head.prev_node = new_head
        self.head = new_head
        self.size += 1

    def print(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next_node
        print(None)


class Deque:

    def __init__(self, max_size: int):
        self.max_size = max_size
        self.deque = LinkedList(max_size)

    def push_front(self):
        pass
