# ID - 103231402
# Time: O(1)
# Space: O(N)
"""
Принцип работы

Моя хеш таблица использует в качестве размера бакетов 10 ** 5. Для решение коллизий используется метод цепочек.
Принцип работы: если при вычисления индекса ключа оказывается, что в этом бакете уже есть элемент, то вставляемый
элемент добалвяется в конец. Так же при работе программы для оптимизации вывода данных я сначала их собираю в
переменной, а потом разом все вывожу. В качестве хеш функции взял форумлу:
    hash = (key * q) % R (q и R взял из теории)


UPD: Я сдаюсь. Мой первый вариант без рехеширования с нерзряженными бакетами неотрефакторинный работает быстрее
и потребляет меньше памяти, чем этот вариант. Я не знаю как дальше оптимизировать это. Потрачено в районе 20 попыток
в контесте и улучшений нет
"""

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

    def __init__(self, size: int) -> None:
        self.size = size
        self.buckets: list[None | LinkedList] = self._initialize_buckets()
        self._max_load_factor = 2
        self._min_load_factor = 0.5
        self._current_size = 0

    def _initialize_buckets(self) -> list:
        return [None] * self.size

    def _get_index(self, key: Any) -> int:
        return hash(key) % self.size

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

        return node.value


def main() -> None:
    size = int(input().strip())
    hash_table = HashTable(size)
    output = []
    for _ in range(size):
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
