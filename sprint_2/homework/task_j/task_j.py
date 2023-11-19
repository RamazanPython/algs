class Node:

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item

    def __str__(self):
        return str(self.value)


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def put(self, x):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            self.tail.next = node
            self.tail = node

        self._size += 1

    def get(self):
        if self.head is None:
            return "error"

        elem = self.head
        next_item = self.head.next
        self.head = next_item
        self._size -= 1
        return elem

    @property
    def size(self):
        return self._size

    def print_queue(self):
        node = self.head
        while node:
            print(node, end=" -> ")
            node = node.next

        print("None")


def main():
    q = Queue()
    steps = int(input().strip())
    for _ in range(steps):
        line = input().strip().split()
        if len(line) == 2:
            function_name, value = line
            if function_name == "put":
                q.put(int(value))
        else:
            function_name = line[0].strip()
            if function_name == "get":
                error = q.get()
                if error:
                    print(error)
            elif function_name == "size":
                print(q.size)


if __name__ == '__main__':
    main()
