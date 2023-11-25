def bubble_sort(arr: list):
    swapped = False
    never_swapped = True
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                never_swapped = False
                if not swapped:
                    swapped = True

        if swapped:
            print(" ".join(map(str, arr)))
            swapped = False

    if never_swapped:
        print(" ".join(map(str, arr)))


def main():
    length = int(input().strip())
    arr = list(map(int, input().strip().split()))
    bubble_sort(arr)


if __name__ == "__main__":
    main()
