class MyQueueSized:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.length = 0
        self.head = 0
        self.tail = 0

    def push(self, x):
        if self.length != self.capacity:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.capacity
            self.length += 1
        else:
            print("error")

    def pop(self):
        if self.length == 0:
            return None

        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return x

    @property
    def size(self):
        return self.length

    @property
    def peek(self):
        return self.queue[self.head]


def main():
    steps = int(input().strip())
    queue_size = int(input().strip())

    q = MyQueueSized(queue_size)
    for _ in range(steps):
        line = input().strip().split()
        if len(line) == 2:
            function_name, value = line
            if function_name == "push":
                q.push(int(value))
        else:
            function_name = line[0].strip()
            if function_name == "peek":
                print(q.peek)
            elif function_name == "size":
                print(q.size)
            else:
                print(q.pop())


if __name__ == '__main__':
    main()
