class Stack:

    def __init__(self):
        self.list = []

    def push(self, elem: int):
        self.list.append(elem)

    def pop(self):
        return self.list.pop()

    @property
    def last(self):
        return self.list[-1] if self.list else None


class StackMaxEffective:

    def __init__(self):
        self.list = []
        self.max_stack = Stack()
        self.max = None

    def pop(self):
        if not self.list:
            return "error"

        self.max_stack.pop()
        self.max = self.max_stack.last
        return self.list.pop()

    def push(self, elem: int):
        if not self.list:
            self.max_stack.push(elem)
        else:
            max_elem = max(self.max_stack.last, elem)
            self.max_stack.push(max_elem)

        self.max = self.max_stack.last
        self.list.append(elem)

    def get_max(self):
        return self.max


def main():
    stack = StackMaxEffective()

    n = int(input())
    for _ in range(n):
        line = input().strip().split()
        if len(line) == 2:
            function_name, value = line
            stack.push(int(value))
        else:
            function_name = line[0].strip()
            if function_name == 'pop':
                result = stack.pop()
                if result == 'error':
                    print(result)
            else:
                print(stack.get_max())


if __name__ == '__main__':
    main()
