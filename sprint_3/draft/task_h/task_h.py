def comparator(elem1, elem2):
    first = elem1 + elem2
    second = elem2 + elem1
    return first < second


def solution(arr: list) -> str:
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if comparator(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return "".join(arr)


def main():
    length = int(input().strip())
    numbers = input().strip().split()
    biggest_num = solution(numbers)
    print(biggest_num)


if __name__ == "__main__":
    main()
