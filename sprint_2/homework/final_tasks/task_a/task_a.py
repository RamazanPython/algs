# ID - 97291030
"""
-- ПРИНЦИП РАБОТЫ --

Я реализовал структуру данных дек на кольцевом буфере. Основную идею я взял из теории в 8 уроке, где была реализована
очередь. В отличие от обычной очереди дек позволяет и добавлять, и извлекать элементы с обоих концов. По сути дек
поддерживает как FIFO, так и LIFO. Основной критерий при реализации дека - все операции должны быть выполнены за О(1).
Я реализовал 4 основных метода:
- push_back(x) - добавление в конец дека
- push_front(x) - добавление в начало дека
- pop_back() - удаление элемента с конца дека
- pop_front() - удаление элемента с начала


-- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
Все операции работают за О(1) благодаря тому, что у нас начало и конец дека - это индексы, которые меняют свое
расположение. В отличие от того же массива, где операции удаление с начала занимают O(n) времени, в моей реализации
начало и конец - это указатели. Помимо указателей на начало и конец моя реализация дека ограничена по количеству
элементов. Это позволяет экономить память и гибко управлять указателями.

Если простыми словами, то у нас есть массив длины n. У нас есть указатели head и tail. Они имеют одинаковый индекс 0.
При добавлении элемента в конец дека (push_back) указатель tail всегда будет на шаг впереди добавленного элемента и
будет указывать на свободный слот (где стоит None). При добавлении в начало (push_front) head будет идти в обратном
направлении (head - 1) и указывать на первый элемент в деке. Так же важно, что при добавлении элемента в дек у нас
есть атрибут size и метод _check_deque_length, который не позволяет добавить элементы сверх нормы. => таким образом,
head - указывает всегда на начало дека и идет в обратном направлении, tail - на шаг впереди последнего элемента =>
мы можем за O(1) достать либо первый, либо последний элементы. Благодаря методы _get_index мы можем быстро получить
нужным нам индекс, который не будет превышать размер массива.

-- Временная сложность
- push_back(x) - O(1)
- push_front(x) - O(1)
- pop_back() - O(1)
- pop_front() - O(1)

-- Пространственная сложность
O(n), где n - размер дека.

UPD: Добавил новые методы: _one_step_back, _one_step_forward. Добавил новый параметр в функцию _get_index

"""
from typing import Any


class Deque:

    def __init__(self, max_size: int) -> None:
        self.max_size: int = max_size
        self.deque: list = [None] * max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    @property
    def is_full(self) -> bool:
        return self.size == self.max_size

    def _get_index(self, index: int, value: int) -> int:
        return (index + value) % self.max_size

    def _one_step_back(self, index: int) -> int:
        return self._get_index(index, -1)

    def _one_step_forward(self, index: int) -> int:
        return self._get_index(index, 1)

    def _check_deque_length(self) -> None:
        if self.is_full:
            raise OverflowError("deque is overflowed")

    def _check_is_empty(self) -> None:
        if self.is_empty:
            raise IndexError("deque is empty")

    def push_back(self, elem: Any) -> None:
        self._check_deque_length()

        self.deque[self.tail] = elem
        self.tail = self._one_step_forward(self.tail)
        self.size += 1

    def push_front(self, elem: Any) -> None:
        self._check_deque_length()

        self.head = self._one_step_back(self.head)
        self.deque[self.head] = elem
        self.size += 1

    def pop_back(self) -> Any:
        self._check_is_empty()

        self.tail = self._one_step_back(self.tail)
        elem = self.deque[self.tail]
        self.deque[self.tail] = None
        self.size -= 1
        return elem

    def pop_front(self) -> Any:
        self._check_is_empty()

        elem = self.deque[self.head]
        self.deque[self.head] = None
        self.head = self._one_step_forward(self.head)
        self.size -= 1
        return elem


def main():
    attempts = int(input().strip())
    max_size = int(input().strip())
    deque = Deque(max_size=max_size)
    for _ in range(attempts):
        input_string = input().strip().split()
        try:
            if len(input_string) == 1:
                method = getattr(deque, input_string[0])
                print(method())
            else:
                method_name, value = input_string
                method = getattr(deque, method_name)
                method(value)
        except (IndexError, OverflowError):
            print("error")
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    main()
