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


UPD: Теперь размер бакетов будет определяться в зависимости от load_factor. При добавлении элемента будет высчитывать
load_factor (количество добавленных элементов деленное на количество бакетов). Если этот парамтер превышает 1.25, то
берется следующий размер их массива простых чисел. При удалении элемента тоже высчитывается заполняемость и при
достижении значения меньше чем 0.5, то произойдет уменьшение бакетов.
"""


class LinkedList:

    def __init__(self, key=None, value=None, next_node=None) -> None:
        self.key = key
        self.value = value
        self.next_node = next_node


class HashTable:

    _GOOD_SIZES = [1, 7, 17, 31, 67, 127, 257, 509, 1021, 2069, 4513, 7853, 14087, 30493, 62473]
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
        return self.size * 2

    def _initialize_buckets(self) -> list:
        return [LinkedList() for _ in range(self.size)]

    def get_hash(self, key):
        return (key * self._Q) % self._R

    def get_index(self, key: int) -> int:
        return self.get_hash(key) % self.size

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
            current_node = bucket.next_node
            while current_node:
                key, value = current_node.key, current_node.value
                self.put(key, value, to_rehash=False)
                current_node = current_node.next_node

    def find_node(self, idx: int, key: int) -> LinkedList | None:
        current_node = self.buckets[idx]
        while current_node:
            if current_node.key == key:
                return current_node
            current_node = current_node.next_node
        return None

    def put(self, key: int, value: int, to_rehash: bool = True) -> None:
        idx = self.get_index(key)
        node = self.find_node(idx, key)
        if node:
            node.value = value
        else:
            new_node = LinkedList(key=key, value=value, next_node=self.buckets[idx].next_node)
            self.buckets[idx].next_node = new_node
            self._current_size += 1
            if to_rehash:
                self._calculate_load_factor()

    def get(self, key: int) -> int | None:
        idx = self.get_index(key)
        node = self.find_node(idx, key)
        return node.value if node else None

    def delete(self, key: int) -> int | None:
        idx = self.get_index(key)
        current_node = self.buckets[idx]
        while current_node.next_node:
            if current_node.next_node.key == key:
                value = current_node.next_node.value
                current_node.next_node = current_node.next_node.next_node
                self._current_size -= 1
                self._calculate_load_factor()
                return value
            current_node = current_node.next_node
        return None


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
