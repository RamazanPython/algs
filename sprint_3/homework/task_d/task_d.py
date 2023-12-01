def solution(greedy: list[int], cookies: list[int]) -> int:
    greedy.sort()
    cookies.sort()

    g_idx = 0
    c_idx = 0

    result = 0
    while g_idx < len(greedy) and c_idx < len(cookies):
        if cookies[c_idx] >= greedy[g_idx]:
            result += 1
            g_idx += 1
        c_idx += 1

    return result


def main():
    n = int(input().strip())
    greedy = list(map(int, input().strip().split()))
    m = int(input().strip())
    cookies = list(map(int, input().strip().split()))
    result = solution(greedy=greedy, cookies=cookies)
    print(result)


if __name__ == "__main__":
    main()
