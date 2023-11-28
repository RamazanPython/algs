"""
Задача:

Даны две строки. Нужно понять, является ли первая строка подпоследовательностью второй. Если да, то функция должна
вернуть True, иначе False.


Принцип работы:

У нас есть две строки subsequence и string. Как понять, что строка subsequence подпоследовательность в string?

Для начала определим, что такое подпоследовательность. Это значит, что в string есть последовательность из subsequence,
но при этом между символами subsequence могут быть любые символы. Главное - это порядок нахождения символов. Пример:

    subsequence: abc
    string: akfkgettretretrebll;ll;;lll;c
            _               _           _

Символы a, b, c присутствуют в строке string и сохраняют порядок. При этом не важно, сколько символов между ними.

Первое, что приходит в голову при проверку. Длина subsequence должна быть меньше или равна string. Если нет, то это
заведомо не подпоследовательность. Далее мы должны пройтись по строке string циклом и проверить, присутствуют ли
в ней символы из subsequence в строгом порядке. Так же нам надо хранить индекс начала строки subsequence.

    subsequence: abc
    string: ____a_________b_________c__________

При прохождении цикла если в строке string есть первый символ из строки subsequence, то увеличивает индекс начала строки
на 1. И так далее мы проходим пока не пройдем весь string, либо весь subsequence. При успешном прохождении в индексе
начала строки у нас будет хранится длина строки subsequence.

"""


def solution(subsequence: str, string: str) -> bool:
    if len(subsequence) > len(string):
        return False

    sub_idx = 0
    str_idx = 0

    while sub_idx < len(subsequence) and str_idx < len(string):
        if string[str_idx] == subsequence[sub_idx]:
            sub_idx += 1

        str_idx += 1

    return sub_idx == len(subsequence)


def main():
    a = input().strip()
    b = input().strip()
    print(solution(a, b))


if __name__ == "__main__":
    main()
