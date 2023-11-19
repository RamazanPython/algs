def solution(n: int, brackets: str, is_half: bool = False):
    if not brackets:
        brackets = "("

    if n // len(brackets) == 2:
        is_half = True

    if len(brackets) == n:
        print(brackets)
        return

    if is_half:
        solution(n, brackets + ")", is_half)

    solution(n, brackets + "(", is_half)


def main():
    n = int(input().strip())
    brackets = ""
    solution(n * 2, brackets)


if __name__ == "__main__":
    main()
