def solution(arr: list[int], top: int) -> list:
    count_uni = {}
    for elem in arr:
        if elem not in count_uni:
            count_uni[elem] = 1
        else:
            count_uni[elem] += 1


    return []


def main():
    n = int(input().strip())
    universities = list(map(int, input().strip().split()))
    top = int(input().strip())
    result = solution(universities, top)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
