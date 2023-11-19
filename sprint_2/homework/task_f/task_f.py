class StackMax:

    def __init__(self):
        self.list = []

    def pop(self):
        if not self.list:
            return "error"
        return self.list.pop()

    def push(self, elem: int):
        self.list.append(elem)

    def get_max(self):
        if not self.list:
            return None
        return max(self.list)


def main():
    stack = StackMax()

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
