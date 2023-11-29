def insertion_sort(array: list[int]):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = item_to_insert
        print('step {}, sorted {} elements: {}'.format(i, i + 1, array))

    return array


print(insertion_sort([11, 2, 9, 7, 1, 9]))
