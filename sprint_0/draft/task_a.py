def solution(numbers: list, k: int) -> list:
    """
        Скользяшее среднее
    """
    pass

def read_input() -> list[int]:
    k = int(input())
    numbers = list(map(int, input().strip().split()))
    return k, numbers


# Comment for unittests
k, numbers = read_input()
print(solution(numbers, k))
