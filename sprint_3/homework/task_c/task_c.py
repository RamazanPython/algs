def solution(a: str, b: str) -> bool:
    a_idx = 0
    b_idx = 0

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] == b[b_idx]:
            a_idx += 1

        b_idx += 1

    return a_idx == len(a)


def main():
    a = input().strip()
    b = input().strip()
    print(solution(a, b))


if __name__ == "__main__":
    main()
