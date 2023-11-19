# ID - 95864754
# Time: O(N) - two loops
# Space: O(N) - extra data structure for counting numbers

def solution(k: int, numbers: list) -> int:
    count_numbers = [0] * 9
    for i in range(len(numbers)):
        count_numbers[numbers[i] - 1] += 1

    result = 0
    max_keys = k * 2
    for i in range(len(count_numbers)):
        if count_numbers[i] == 0:
            continue
        if max_keys >= count_numbers[i]:
            result += 1

    return result


def read_input() -> tuple[int, list]:
    k = int(input())
    numbers = []
    for _ in range(4):
        input_string = input()
        for elem in input_string:
            if elem.isnumeric():
                numbers.append(int(elem))
    return k, numbers


k, numbers = read_input()
print(solution(k, numbers))
