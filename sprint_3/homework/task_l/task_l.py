def bicyle_search(input_list: list[int], price: int, left: int, right: int):
    if right <= left:
        return -1

    mid = (left + right) // 2
    if price <= input_list[mid]:
        prev_index = mid - 1
        if input_list[prev_index] >= price and prev_index >= 0:
            return bicyle_search(input_list, price, left, mid)

        return mid + 1
    else:
        return bicyle_search(input_list, price, mid + 1, right)


def process_input() -> tuple[list[int], int]:
    length = int(input().strip())
    input_list = list(map(int, input().strip().split()))
    price = int(input().strip())
    return input_list, price


def main() -> None:
    input_list, price = process_input()
    first_day = bicyle_search(input_list, price, 0, len(input_list))
    second_day = bicyle_search(input_list, price * 2, 0, len(input_list))
    print(first_day, second_day)


if __name__ == "__main__":
    main()
