class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"Node(value={self.value})"


class Queue:

    def __init__(self):
        self.first = None
        self.last = None

    def is_empty(self):
        return self.first is None

    def enqueue(self, value):
        if self.first is None:
            self.first = self.last = Node(value=value)
        else:
            self.last.next = Node(value=value)
            self.last = self.last.next

    def dequeue(self):
        if self.is_empty():
            raise RuntimeError("Queue is empty")

        value = self.first.value
        self.first = self.first.next
        return value

    def __iter__(self):
        node = self.first
        while node:
            yield node
            node = node.next

    def __repr__(self):
        result = []
        for elem in self:
            result.append(f"{elem} -> ")

        result.append("None")
        return "".join(result)


if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)

    print(queue)
