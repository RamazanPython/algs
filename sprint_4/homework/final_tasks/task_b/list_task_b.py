from typing import Any


class HashTable:
    # Primes
    _GOOD_SIZES = [1, 7, 17, 31, 67, 127, 257, 509, 1021, 2069, 4513, 7853, 14087, 30493, 62473, 10 ** 5]
    _Q = 10 ** 9 + 7
    _R = 2 ** 64

    def __init__(self) -> None:
        self.size_idx = 0
        self.size = self._get_size()
        self.buckets: list[None | list] = self._initialize_buckets()
        self._max_load_factor = 1.5
        self._min_load_factor = 0.5
        self._current_size = 0

    def _get_size(self):
        if self.size_idx < 0:
            return self._GOOD_SIZES[0]
        if 0 <= self.size_idx < len(self._GOOD_SIZES):
            return self._GOOD_SIZES[self.size_idx]
        return self._GOOD_SIZES[-1]

    def _initialize_buckets(self) -> list:
        return [[] for _ in range(self.size)]

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

            for key, value in bucket:
                self.put(key=key, value=value, to_rehash=False)

    def _find_node_idx(self, idx: int, key: int) -> int | None:
        for node_idx, node in enumerate(self.buckets[idx]):
            if node[0] == key:
                return node_idx

    def put(self, key: int, value: int, to_rehash: bool = True) -> None:
        idx = self._get_index(key)
        node_idx = self._find_node_idx(idx, key)
        if node_idx is not None:
            self.buckets[idx][node_idx] = (key, value)
            return

        self.buckets[idx].append((key, value))
        self._current_size += 1
        if to_rehash:
            self._calculate_load_factor()

    def get(self, key: int) -> int | None:
        idx = self._get_index(key)
        node_idx = self._find_node_idx(idx, key)
        if node_idx is not None:
            return self.buckets[idx][node_idx][1]

    def delete(self, key: int) -> int | None:
        idx = self._get_index(key)
        node_idx = self._find_node_idx(idx, key)
        if node_idx is not None:
            value = self.buckets[idx][node_idx][1]
            self.buckets[idx].pop(node_idx)
            self._current_size -= 1
            self._calculate_load_factor()
            return value


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
