def solution(n, k):
    if n == 0 or n == 1:
        return 1

    a, b = 1, 1
    mod = 10 ** k

    for _ in range(2, n + 1):
        a, b = b, (a + b) % mod

    return b


def main():
    n, k = list(map(int, input().strip().split()))
    return n, k


if __name__ == "__main__":
    n, k = main()
    print(solution(n, k))
