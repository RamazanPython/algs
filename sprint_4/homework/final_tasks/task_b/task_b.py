# ID - 102941481
# Time: O(1)
# Space: O(N)
"""
Принцип работы

Моя хеш таблица использует в качестве размера бакетов 10 ** 5. Для решение коллизий используется метод цепочек.
Принцип работы: если при вычисления индекса ключа оказывается, что в этом бакете уже есть элемент, то вставляемый
элемент добалвяется в конец. Так же при работе программы для оптимизации вывода данных я сначала их собираю в
переменной, а потом разом все вывожу. В качестве хеш функции взял форумлу:
    hash = (key * q) % R (q и R взял из теории)
"""


class LinkedList:

    def __init__(self, key=None, value=None, next_node=None) -> None:
        self.key = key
        self.value = value
        self.next_node = next_node


class HashTable:
    _MAX_LENGTH = 10 ** 5
    _Q = 10 ** 9 + 7
    _R = 2 ** 64

    def __init__(self) -> None:
        self.buckets: list[LinkedList] = [LinkedList() for _ in range(self._MAX_LENGTH)]

    def get_hash(self, key):
        return (key * self._Q) % self._R

    def get_index(self, key: int) -> int:
        return self.get_hash(key) % self._MAX_LENGTH

    def put(self, key: int, value: int) -> None:
        idx = self.get_index(key)
        current_node = self.buckets[idx]
        while current_node.next_node:
            if current_node.next_node.key == key:
                current_node.next_node.value = value
                return
            current_node = current_node.next_node

        current_node.next_node = LinkedList(key=key, value=value)

    def get(self, key: int) -> int | None:
        idx = self.get_index(key)
        current_node = self.buckets[idx]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next_node
        return None

    def delete(self, key: int) -> int | None:
        idx = self.get_index(key)
        current_node = self.buckets[idx]
        while current_node and current_node.next_node:
            if current_node.next_node.key == key:
                value = current_node.next_node.value
                current_node.next_node = current_node.next_node.next_node
                return value
            current_node = current_node.next_node


def main() -> None:
    hash_table = HashTable()
    amount = int(input().strip())
    output = ""
    for _ in range(amount):
        args = input().strip().split()
        if args[0] == "get":
            key = args[1]
            method = getattr(hash_table, "get")
            value = method(int(key))
            output += (str(value) or "None") + "\n"
        elif args[0] == "put":
            key, value = args[1:]
            method = getattr(hash_table, "put")
            method(int(key), int(value))
        elif args[0] == "delete":
            key = args[1]
            method = getattr(hash_table, "delete")
            value = method(int(key))
            output += (str(value) or "None") + "\n"

    print(output, end="")


if __name__ == "__main__":
    main()
