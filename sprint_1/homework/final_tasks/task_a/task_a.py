# ID - 95864620
# Time: O(N) - two loops
# Space: O(N) - extra data type for result

def solution(streets: list) -> str:
    result = [0] * len(streets)

    # left -> right
    zero_index = len(streets)
    for i in range(len(streets)):
        if streets[i] == 0:
            zero_index = i

        result[i] = abs(i - zero_index)

    # right -> left
    zero_index = len(streets) * 2
    for i in reversed(range(len(streets))):
        if streets[i] == 0:
            zero_index = i

        result[i] = min(result[i], abs(i - zero_index))

    return " ".join(map(str, result))


def read_input() -> list[int]:
    n = int(input())
    streets = list(map(int, input().strip().split()))
    return streets


# Comment for unittests
streets = read_input()
print(solution(streets))
