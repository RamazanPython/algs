def solution(numbers: list, k: int):
    result = []

    current_sum = sum(numbers[:k])
    current_avg = round(current_sum / k, 2)
    result.append(current_avg)
    for i in range(len(numbers) - k):
        current_sum -= numbers[i]
        current_sum += numbers[i + k]
        current_avg = round(current_sum / k, 2)
        result.append(current_avg)

    return result


def read_input() -> list[int]:
    k = int(input())
    numbers = list(map(int, input().strip().split()))
    return k, numbers


# Comment for unittests
k, numbers = read_input()
print(solution(numbers, k))

