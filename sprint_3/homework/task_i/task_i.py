def solution(arr: list[int], top: int) -> list:
    count_uni = {}
    for elem in arr:
        count_uni[elem] = 1 + count_uni.get(elem, 0)

    bucket = [[] for _ in range(len(arr) + 1)]
    for elem, count in count_uni.items():
        bucket[count].append(elem)

    result = []
    for nums in reversed(bucket):
        if not nums:
            continue

        nums.sort()
        result.extend(nums)
        if len(result) >= top:
            break

    return result[:top]


def main():
    n = int(input().strip())
    universities = list(map(int, input().strip().split()))
    top = int(input().strip())
    result = solution(universities, top)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
