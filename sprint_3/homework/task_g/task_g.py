def solution(arr: list[int], k: int) -> None:
    count_nums = [0] * k
    for elem in arr:
        count_nums[elem] += 1

    index = 0
    for value in range(k):
        for amount in range(count_nums[value]):
            arr[index] = value
            index += 1


def main():
    n = int(input())
    nums = list(map(int, input().strip().split()))
    solution(nums, 3)
    print(" ".join(map(str, nums)))


if __name__ == "__main__":
    main()
