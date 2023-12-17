from typing import Any


class Node:

    def __init__(self, key: Any, value: Any, next_node: Any = None, prev_node: Any = None):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __repr__(self):
        return f"Node(key={self.key}, value={self.value}, next_node={self.next_node})"


class LinkedList:

    def __init__(self, head: Node = None):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def append_left(self, key: Any, value: Any):
        node = Node(key=key, value=value, next_node=self.head, prev_node=None)
        if self.head:
            self.head.prev_node = node

        self.head = node
        if not self.tail:
            self.tail = self.head
        self.size += 1

    def append_right(self, key: Any, value: Any):
        if not self.tail:
            self.append_left(key, value)
            return

        node = Node(key=key, value=value, next_node=None, prev_node=self.tail)
        self.tail.next_node = node
        self.tail = node
        self.size += 1

    def find(self, key: Any) -> Node | None:
        if self.size == 0:
            return

        for elem in self:
            if elem.key == key:
                return elem

        return None

    def delete(self, key: Any) -> Node | None:
        node = self.find(key)
        if not node:
            return

        prev_node = node.prev_node
        next_node = node.next_node
        if prev_node:
            prev_node.next_node = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev_node = prev_node
        else:
            self.tail = prev_node

        self.size -= 1
        return node


class HashTable:
    # Primes
    _GOOD_SIZES = [1, 7, 17, 31, 67, 127, 257, 509, 1021, 2069, 4513, 7853, 14087, 30493, 62473, 10 ** 5]
    _Q = 10 ** 9 + 7
    _R = 2 ** 64

    def __init__(self) -> None:
        self.size_idx = 0
        self.size = self._get_size()
        self.buckets: list[None | LinkedList] = self._initialize_buckets()
        self._max_load_factor = 2
        self._min_load_factor = 0.5
        self._current_size = 0

    def _get_size(self):
        if self.size_idx < 0:
            return self._GOOD_SIZES[0]
        if 0 <= self.size_idx < len(self._GOOD_SIZES):
            return self._GOOD_SIZES[self.size_idx]
        return self._GOOD_SIZES[-1]

    def _initialize_buckets(self) -> list:
        return [None] * self.size

    def _get_hash(self, key) -> int:
        return (key * self._Q) % self._R

    def _get_index(self, key: Any) -> int:
        return self._get_hash(key) % self.size

    def _calculate_load_factor(self) -> None:
        curr_load_factor = self._current_size / self.size
        if curr_load_factor >= self._max_load_factor:
            self._rehash(increase=True)
        elif curr_load_factor <= self._min_load_factor and self.size_idx != 0:
            self._rehash(increase=False)

    def _rehash(self, increase: bool = True) -> None:
        prev_size_idx = self.size_idx
        if increase:
            self.size_idx += 1
        else:
            self.size_idx -= 1

        # If reached max size
        next_size = self._get_size()
        if next_size >= self._GOOD_SIZES[-1]:
            self.size_idx = prev_size_idx
            return

        self.size = next_size
        old_buckets = self.buckets
        self._current_size = 0
        self.buckets = self._initialize_buckets()
        for bucket in old_buckets:
            if bucket is None:
                continue

            for node in bucket:
                self.put(key=node.key, value=node.value, to_rehash=False)

    def put(self, key: int, value: int, to_rehash: bool = True) -> None:
        idx = self._get_index(key)
        if self.buckets[idx] is None:
            llist = LinkedList()
            self.buckets[idx] = llist
        else:
            llist = self.buckets[idx]

        node = llist.find(key)
        if node:
            node.value = value
            return

        llist.append_right(key=key, value=value)
        self._current_size += 1
        if to_rehash:
            self._calculate_load_factor()

    def get(self, key: int) -> int | None:
        idx = self._get_index(key)
        if self.buckets[idx] is None:
            return
        node = self.buckets[idx].find(key)
        return getattr(node, "value", None)

    def delete(self, key: int) -> int | None:
        idx = self._get_index(key)
        if self.buckets[idx] is None:
            return

        node = self.buckets[idx].delete(key)
        if not node:
            return

        self._current_size -= 1
        self._calculate_load_factor()
        return node.value


def main() -> None:
    hash_table = HashTable()
    amount = int(input().strip())
    output = []
    for _ in range(amount):
        args = input().strip().split()
        method = getattr(hash_table, args[0])
        if args[0] in ("get", "delete"):
            key = args[1]
            value = method(int(key))
            output.append(str(value) or "None")
        elif args[0] == "put":
            key, value = args[1:]
            method(int(key), int(value))

    print("\n".join(output))


if __name__ == "__main__":
    main()
