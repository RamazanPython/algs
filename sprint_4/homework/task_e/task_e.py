def get_longest_substring(string: str) -> int:
    length = 0
    left = 0
    unique = set()
    for right in range(len(string)):
        while string[right] in unique:
            unique.remove(string[left])
            left += 1

        unique.add(string[right])
        length = max(length, right - left + 1)

    return length


def main() -> None:
    string = input().strip()
    length = get_longest_substring(string)
    print(length)


if __name__ == "__main__":
    main()
