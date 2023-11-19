from typing import Tuple


# TODO: Refactor

def get_sum(first_number: str, second_number: str) -> str:
    max_number, low_number = get_numbers(first_number, second_number)

    res = ""
    temp = ""
    for i in reversed(range(len(max_number))):
        if max_number[i] == "1" and low_number[i] == "1":
            if temp == "1":
                value = "1"
            else:
                value = "0"

            temp = "1"
            res = value + res
        elif max_number[i] == "0" and low_number[i] == "0":
            if temp == "1":
                value = "1"
                temp = ""
            else:
                value = "0"

            res = value + res
        else:
            if temp == "1":
                value = "0"
                temp = "1"
            else:
                value = "1"

            res = value + res

        if i == 0 and temp == "1":
            res = "1" + res

    res = remove_extra_zeros(res)

    return res


def remove_extra_zeros(res: str) -> str:
    if res[0] != "0":
        return res

    first_non_zero_index = -1
    for i in range(len(res)):
        if res[i] != "0":
            first_non_zero_index = i
            break

    if first_non_zero_index == -1:
        return "0"

    new_res = ""
    for i in range(first_non_zero_index, len(res)):
        new_res += res[i]

    return new_res


def get_numbers(first_number: str, second_number: str) -> tuple[str, str]:
    if len(first_number) == len(second_number):
        return first_number, second_number

    if len(first_number) > len(second_number):
        diff = len(first_number) - len(second_number)
        second_number = "0" * diff + second_number
        return first_number, second_number

    diff = len(second_number) - len(first_number)
    first_number = "0" * diff + first_number
    return second_number, first_number


def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number


first_number, second_number = read_input()
print(get_sum(first_number, second_number))
