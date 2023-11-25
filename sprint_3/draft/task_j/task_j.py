def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)


def main():
    length = int(input().strip())
    arr = list(map(int, input().strip().split()))
    bubble_sort(arr)


if __name__ == "__main__":
    main()
