def solution(number: int) -> int:
    if number == 0 or number == 1:
        return 1

    first, second = 1, 1
    for i in range(2, number + 2):
        first, second = second, first + second
    return first


def main():
    number = int(input().strip())
    return number


if __name__ == "__main__":
    number = main()
    print(solution(number))
