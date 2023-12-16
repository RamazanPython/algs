from typing import Any


class Node:

    def __init__(self, key: Any, value: Any):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, key: Any, value: Any) -> None:
        new_node = Node(key, value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find(self, key: Any) -> Node | None:
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def remove(self, key: Any) -> Node | None:
        current = self.head
        previous = None
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = previous
                return current
            previous = current
            current = current.next
        return None


class HashTable:

    _GOOD_SIZES = [1, 7, 17, 31, 67, 127, 257, 509, 1021, 2069, 4513, 7853]
    _Q = 10 ** 9 + 7
    _R = 2 ** 64

    def __init__(self) -> None:
        self.size_idx = 0
        self.size = self._get_size(self.size_idx)
        self.buckets = self._initialize_buckets()
        self._max_load_factor = 1.25
        self._min_load_factor = 0.5
        self._current_size = 0

    def _get_size(self, size_idx: int):
        if self.size_idx < 0:
            return self._GOOD_SIZES[0]
        if 0 <= size_idx < len(self._GOOD_SIZES):
            return self._GOOD_SIZES[size_idx]
        return self._next_prime(self.size * 2)

    def _initialize_buckets(self) -> list:
        return [LinkedList() for _ in range(self.size)]

    def get_hash(self, key):
        return (key * self._Q) % self._R

    def get_index(self, key: Any) -> int:
        return hash(key) % self.size

    def _calculate_load_factor(self) -> None:
        curr_load_factor = self._current_size / self.size
        if curr_load_factor >= self._max_load_factor:
            self._rehash(increase=True)
        elif curr_load_factor <= self._min_load_factor and self.size_idx != 0:
            self._rehash(increase=False)

    def _rehash(self, increase: bool = True):
        if increase:
            self.size_idx += 1
        else:
            self.size_idx -= 1

        self.size = self._get_size(self.size_idx + 1)
        old_buckets = self.buckets
        self._current_size = 0
        self.buckets = self._initialize_buckets()
        for bucket in old_buckets:
            current = bucket.head
            while current:
                self.put(current.key, current.value, to_rehash=False)
                current = current.next

    def _add_pair(self, idx: int, key: Any, value: Any, to_rehash: bool = True) -> None:
        self.buckets[idx].add(key, value)
        self._current_size += 1
        if to_rehash:
            self._calculate_load_factor()

    def _delete_pair(self, idx: int, key: Any) -> Any | None:
        node = self.buckets[idx].remove(key)
        if not node:
            return

        self._current_size -= 1
        self._calculate_load_factor()
        return node.value

    def put(self, key: Any, value: int, to_rehash: bool = True) -> None:
        idx = self.get_index(key)
        pair_node = self.buckets[idx].find(key)
        if pair_node:
            pair_node.value = value
        else:
            self._add_pair(idx, key, value, to_rehash)

    def get(self, key: Any) -> int | None:
        idx = self.get_index(key)
        pair_node = self.buckets[idx].find(key)
        return pair_node.value if pair_node else None

    def delete(self, key: Any) -> int | None:
        idx = self.get_index(key)
        return self._delete_pair(idx, key)


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
