# Time: O(N)
# Space: O(N)
def compare(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        return "NO"

    hash1 = {}
    hash2 = {}

    for ch1, ch2 in zip(str1, str2):
        hash1[ch1] = 1 + hash1.get(ch1, 0)
        hash2[ch2] = 1 + hash2.get(ch2, 0)

    for value1, value2 in zip(hash1.values(), hash2.values()):
        if value1 != value2:
            return "NO"

    return "YES"


def main() -> None:
    str1 = input().strip()
    str2 = input().strip()
    print(compare(str1, str2))


if __name__ == "__main__":
    main()
