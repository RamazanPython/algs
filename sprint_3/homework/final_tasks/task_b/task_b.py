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
    while True:
        while comparator(pivot, arr[left], reverse):
            left += 1

        while comparator(arr[right], pivot, reverse):
            right -= 1

        if left >= right:
            return right + 1

        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def sort_students(
        arr: list[Student],
        left: int,
        right: int,
        comparator: Callable[[Any, Any, bool], bool],
        reverse: bool = False
) -> None:
    length = right - left + 1
    if length < 2:
        return

    pivot = random.choice(arr)
    split_index = partition(arr=arr, pivot=pivot, left=left, right=right, comparator=comparator, reverse=reverse)
    sort_students(arr=arr, left=left, right=split_index - 1, comparator=comparator, reverse=reverse)
    sort_students(arr=arr, left=split_index, right=right, comparator=comparator, reverse=reverse)


def main() -> None:
    n = int(input().strip())
    students = []
    for _ in range(n):
        name, score, errors = input().strip().split()
        score, errors = int(score), int(errors)
        students.append(Student(name=name, score=score, errors=errors))

    sort_students(arr=students, left=0, right=len(students) - 1, comparator=compare_students, reverse=True)
    for student in students:
        print(student.name)


if __name__ == "__main__":
    main()
