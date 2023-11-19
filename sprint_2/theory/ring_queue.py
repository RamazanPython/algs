class Queue:

    def __init__(self, size: int):
        self.queue = [None] * size
        self.max_n = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1

    def pop(self):
        if self.is_empty():
            return

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x


if __name__ == "__main__":
    q = Queue(3)
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.queue)
    q.push(10)
    q.push(11)
