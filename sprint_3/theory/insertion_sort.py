def insertion_sort(array):
    for i in range(1, len(array)):
        insertion_element = array[i]
        j = i
        while j > 0 and insertion_element < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1

        array[j] = insertion_element

    return array


print(insertion_sort([11, 2, 9, 7, 1, 9]))
