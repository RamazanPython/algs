# ID - 104459097
# Time: O(NlogN)
# Space: O(N) - так как нужен массив для хранения отсортированных данных + глубина рекурсии
"""
Принцип работы:

Перед сортировкой мы должны создать приоритетную кучу. В вершине кучи будет участник, у которого либо больше всех очков,
либо при равенстве очков меньше всех ошибок, либо же у кого имя в алфавитном порядке стоит первее.

Для создания двоичной кучи нам нужен метод sift_up. Он нужен, чтобы сохранялась целостность нашей кучи. То есть в
вершине должен быть самый успешный участник соревнований. Ниже те кто чуть хуже и так далее.

После мы создаем массив для хранения отсортированных данных. Тут уже нужен метод sift_down. Он нужен при удалении из
очереди максимального элемента. При удалении вершины кучи мы ставим на ее место последний элемент. Далее мы попарно
сравниваем два соседних элемента и меняем местами добавленный элемент с наибольшим. Рекурсивно продолжаем пока условие
верно.

После в нашем новом массиве будет храниться отсортированные данные
"""


def comparator(item_1: list[str, int, int], item_2: list[str, int, int]):
    return ((item_1[1] > item_2[1])
            or (item_1[1] == item_2[1] and item_1[2] < item_2[2])
            or (item_1[1] == item_2[1] and item_1[2] == item_2[2] and item_1[0] < item_2[0]))


def sift_up(heap, index):
    if index == 1:
        return

    parent_index = index // 2
    if comparator(heap[index - 1], heap[parent_index - 1]):
        heap[parent_index - 1], heap[index - 1] = heap[index - 1], heap[parent_index - 1]
        sift_up(heap, parent_index)


def heap_add(heap: list, item: list[str, int, int]):
    index = len(heap) + 1
    heap.append(item)
    sift_up(heap, index)


def sift_down(heap, index):
    left = 2 * index + 1
    right = 2 * index + 2
    if len(heap) <= left:
        return

    index_largest = right if right < len(heap) and comparator(heap[right], heap[left]) else left
    if comparator(heap[index_largest], heap[index]):
        heap[index], heap[index_largest] = heap[index_largest], heap[index]
        sift_down(heap, index_largest)


def pop_max(heap):
    result = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 0)
    return result


def heap_sort(competitors: list[list[str, int, int]]):
    heap = []
    for item in competitors:
        heap_add(heap, item)

    sorted_array = [None] * len(heap)
    idx = 0
    while heap:
        max_val = pop_max(heap)
        sorted_array[idx] = max_val
        idx += 1

    return sorted_array


def main():
    n = int(input())
    competitors = []
    for _ in range(n):
        name, score, penalty = input().strip().split()
        score, penalty = int(score), int(penalty)
        competitors.append([name, score, penalty])

    sorted_arr = heap_sort(competitors)
    names = []
    for elem in sorted_arr:
        names.append(elem[0])

    print("\n".join(names))


if __name__ == "__main__":
    main()
