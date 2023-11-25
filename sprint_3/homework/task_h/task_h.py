from functools import cmp_to_key


def comparator(a: str, b: str):
    if a + b > b + a:
        return 1
    return -1


def solution(arr: list[str]) -> str:
    arr.sort(key=cmp_to_key(comparator), reverse=True)
    return "".join(arr)


def main():
    length = int(input().strip())
    nums = list(input().strip().split())
    biggest_num = solution(nums)
    print(biggest_num)


if __name__ == '__main__':
    main()
