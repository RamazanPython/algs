def solution(n: int) -> list[str]:
    stack = []
    result = []

    def backtrack(open_n: int, close_n: int):
        if open_n == close_n == n:
            result.append("".join(stack))
            return

        if open_n < n:
            stack.append("(")
            backtrack(open_n + 1, close_n)
            stack.pop()

        if close_n < open_n:
            stack.append(")")
            backtrack(open_n, close_n + 1)
            stack.pop()

    backtrack(0, 0)
    return result


def main():
    n = int(input().strip())
    brackets = solution(n)
    for bracket in brackets:
        print(bracket)


if __name__ == "__main__":
    main()
