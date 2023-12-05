# ID - 102086917
# Time: O(NlogN)
# Space: O(1)
"""
Принцип работы


Нам дан неотсортированный массив. Мы должны его отсортировать используя быстрый поиск без дополнительной памяти.
Главная идея будет такая же как и в обычном быстром поиске, но с изменением расположения массива вместо хранения его
в отдельным массивах.

a = [10, 4, 5, 1, 0, 11, 2, 4]

Берем два указателя left = 0 и right = len(a) - 1. Берем сравниваемый элемент (pivot). Пусть это будет центральный
элемент pivot = a[mid].

Нам нужно добиться того, что в левой части массива будут элементы меньше pivot, а в правой больше.
Создадим функцию partition, которая будет заниматься этим. Мы будем сдвигать left вперед, если a[left] < pivot. И
сдвигать right назад, если a[right] > pivot. После этого мы меняем местами элементы. Это будет работать в цикле
и мы будет это делать до момента столкновения left и right.

Далее мы возвраащем индекс left, так как после последней смены мест left > right. После этого в главной функции мы
вызываем рекурсивно функцию сортировки, которая будет сортировать леву и правую часть массива.


UPD: Теперь беру рандомный pivot. Применил вместо random.choice random.randrange и заработало!
"""

import random

from typing import Callable, Any


class Student:

    def __init__(self, name: str, score: int, errors: int) -> None:
        self.name = name
        self.score = score
        self.errors = errors

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', score={self.score}, errors={self.errors})"

    def __gt__(self, other: "Student") -> bool:
        return ((self.score > other.score)
                or (self.score == other.score and self.errors < other.errors)
                or (self.score == other.score and self.errors == other.errors and self.name < other.name))

    def __lt__(self, other: "Student") -> bool:
        return ((self.score < other.score)
                or (self.score == other.score and self.errors > other.errors)
                or (self.score == other.score and self.errors == other.errors and self.name > other.name))


def compare_students(student1: Student, student2: Student, reverse: bool = False) -> bool:
    if reverse:
        return student1 < student2

    return student1 > student2


def partition(
        arr: list[Student],
        pivot: Student,
        left: int,
        right: int,
        comparator: Callable[[Any, Any, bool], bool],
        reverse: bool = False
) -> int:
    while left <= right:
        while comparator(pivot, arr[left], reverse):
            left += 1

        while comparator(arr[right], pivot, reverse):
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


def quicksort(
        arr: list[Student],
        left: int,
        right: int,
        comparator: Callable[[Any, Any, bool], bool],
        reverse: bool = False
) -> None:
    if left >= right:
        return

    pivot_idx = random.randrange(left, right)
    pivot = arr[pivot_idx]
    split_index = partition(arr=arr, pivot=pivot, left=left, right=right, comparator=comparator, reverse=reverse)
    quicksort(arr=arr, left=left, right=split_index - 1, comparator=comparator, reverse=reverse)
    quicksort(arr=arr, left=split_index, right=right, comparator=comparator, reverse=reverse)


def sort_students(arr: list, reverse: bool = False) -> None:
    quicksort(arr=arr, left=0, right=len(arr) - 1, comparator=compare_students, reverse=reverse)


def main() -> None:
    n = int(input().strip())
    students = []
    for _ in range(n):
        name, score, errors = input().strip().split()
        score, errors = int(score), int(errors)
        students.append(Student(name=name, score=score, errors=errors))

    sort_students(arr=students, reverse=True)
    for student in students:
        print(student.name)


if __name__ == "__main__":
    main()
