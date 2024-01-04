class HeapQueue:

    def __init__(self, max_size: int):
        self.max_size: int = max_size
        self.queue: list = [None] * (max_size + 1)
        self.current_idx: int = 0

    def is_full(self) -> bool:
        return self.current_idx == self.max_size

    def is_empty(self) -> bool:
        return self.current_idx == 0

    def compare(self, left_idx: int, right_idx: int, less: bool = True) -> bool:
        if less:
            return self.queue[left_idx] < self.queue[right_idx]
        return self.queue[left_idx] > self.queue[right_idx]

    def swap(self, left_idx: int, right_idx: int):
        self.queue[left_idx], self.queue[right_idx] = self.queue[right_idx], self.queue[left_idx]

    def enqueue(self, value: int):
        if self.is_full() or self.current_idx * 2 > self.max_size:
            raise OverflowError("Queue is full")

        self.current_idx += 1
        self.queue[self.current_idx] = value
        self.swim(self.current_idx)

    def swim(self, child: int):
        parent = child >> 1
        while child > 1 and self.compare(parent, child):
            self.swap(child, parent)
            child = parent
            parent = parent >> 1

    def dequeue(self):
        if self.is_empty():
            return ValueError("Queue is empty")

        max_elem = self.queue[1]
        self.queue[1] = self.queue[self.current_idx]
        self.queue[self.current_idx] = None
        self.current_idx -= 1

        return max_elem

    def sink(self, parent: int):
        while 2 * parent <= self.current_idx:
            child = 2 * parent
            if child < self.current_idx and self.compare(child, child + 1):
                child += 1

            if not self.compare(parent, child):
                break

            self.swap(child, parent)
            parent = child
