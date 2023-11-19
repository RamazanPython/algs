def get_sum(number_list: list[int], k: int) -> str:
    k_list = to_list_form(k)
    number_list = number_list[::-1]

    max_len = max(len(number_list), len(k_list))
    shift = 0
    result = []
    for i in range(max_len):
        first_number = number_list[i] if i < len(number_list) else 0
        second_number = k_list[i] if i < len(k_list) else 0
        temp = first_number + second_number + shift
        shift = temp // 10
        result.append(temp % 10)

    if shift > 0:
        result.append(1)

    return " ".join(str(elem).strip() for elem in result[::-1])


def to_list_form(number: int) -> list:
    arr = []
    while number != 0:
        remainder = number % 10
        arr.append(remainder)
        number = number // 10

    return arr


def read_input() -> tuple[list[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k


number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
