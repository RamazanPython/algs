def sort(array: list):
    array.sort()


def solution(array: list):
    sort(array)

    result = [array[0]]
    for i in range(1, len(array)):
        last_end = result[-1][-1]
        if last_end >= array[i][0]:
            result[-1][-1] = max(array[i][-1], last_end)
        else:
            result.append(array[i])

    return result


def main():
    n = int(input().strip())
    array = []
    for _ in range(n):
        inner_array = list(map(int, input().strip().split()))
        array.append(inner_array)

    result = solution(array)
    for elem in result:
        print(" ".join(map(str, elem)))


if __name__ == "__main__":
    main()
