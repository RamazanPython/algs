def valid_borders(a: int, b: int, c: int) -> bool:
    return a < b + c and b < a + c and c < a + b


def solution(borders: list[int]) -> int:
    if len(borders) < 3:
        return 0

    borders.sort(reverse=True)

    for i in range(len(borders) - 2):
        if valid_borders(borders[i], borders[i + 1], borders[i + 2]):
            return borders[i] + borders[i + 1] + borders[i + 2]

    return 0


def main():
    n = int(input().strip())
    borders = list(map(int, input().strip().split()))
    print(solution(borders))


if __name__ == "__main__":
    main()
