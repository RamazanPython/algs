def reverse_sorted_arr(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] < arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def semisort(arr):
    if len(arr) < 2:
        return

    left = 0
    right = len(arr) - 1
    pivot = arr[right]

    while True:
        while arr[left] <= pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left > right:
            break

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    semisort(arr[:right])
    semisort(arr[left:])

    return arr


def partition(items, left, right, pivot):
    while left <= right:

        while items[left] < pivot:
            left += 1

        while items[right] > pivot:
            right -= 1

        if left <= right:
            items[left], items[right] = items[right], items[left]
            left += 1
            right -= 1

    return left


def sort(items, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    pivot = items[mid]
    split_index = partition(items, left, right, pivot)
    sort(items, left, split_index - 1)
    sort(items, split_index, right)


# arr = list(range(20))
arr = [10, 4, 5, 1, 0, 11, 2, 4]

# print(reverse_sorted_arr(arr))
sort(arr, left=0, right=len(arr) - 1)
print("*" * 100)
print(arr)
