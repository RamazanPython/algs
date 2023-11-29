def merge_sort(array: list):
    if len(array) == 1:
        return array

    middle = len(array) // 2
    left_array = merge_sort(array[0: middle])
    right_array = merge_sort(array[middle:])

    result = [0] * len(array)
    l, r, k = 0, 0, 0
    while l < len(left_array) and r < len(right_array):
        if left_array[l] <= right_array[r]:
            result[k] = left_array[l]
            l += 1
        else:
            result[k] = right_array[r]
            r += 1

        k += 1

    while l < len(left_array):
        result[k] = left_array[l]
        k += 1
        l += 1

    while r < len(right_array):
        result[k] = right_array[r]
        r += 1
        l += 1

    return result


array = [9, 8, 2, 5, 1, 7, 4]
test_array = array[:]
test_array.sort()
print(merge_sort(array) == test_array)
