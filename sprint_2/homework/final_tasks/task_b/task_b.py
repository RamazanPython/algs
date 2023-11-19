# ID - 96908631
"""
-- ПРИНЦИП РАБОТЫ --
Для решения этой задачи я использовал массив в качестве стека. Так как операции по извлечению и удалению
последнего элемента в динамическом массиве в среднем происходит за О(1) (в худшем за O(n), но благодаря амортизационному
анализу можем считать за O(1)). Функция принимает на выход массив из строк, где каждый элемент - либо операнд,
либо оператор. Я в цикле прохожусь по элементам и проверяю. Если элемент является операндом, то он попадает в стек. Если
элемент - оператор, то я произвожу действия над последними двумя элементами (так как арифметические операции бинарные).
Результат так же кладу в стек. После выхода из цикла у меня в стеке остается один элемент. Его и я отдаю.

-- Временная сложность
O(n) - где n длина входного массива

-- Пространственная сложность
O(k) - где k длина стека. Я назвал k, потому что количество операндов у нас будет меньше, чем всех элементов во входном
массиве (n - длина входного массива). То есть размеры стека и входного массива не могут быть одинаковы.
"""


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int:
    if y == 0:
        raise ZeroDivisionError

    return x // y


def solution(input_array: list[str]) -> int:
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    stack = []
    for elem in input_array:
        if elem not in operators.keys():
            stack.append(int(elem))
            continue

        function = operators.get(elem)
        if function:
            first_operand = stack.pop()
            second_operand = stack.pop()
            stack.append(function(second_operand, first_operand))
        else:
            raise ValueError("Invalid operator")

    return stack.pop()


def main() -> list[str]:
    input_array = input().strip().split()
    return input_array


if __name__ == "__main__":
    input_array = main()
    result = solution(input_array)
    print(result)
