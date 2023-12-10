def polynomial_hash(string: str, base: int, m: int):
    hash_ = 0
    for ch in string:
        code = ord(ch)
        hash_ = (hash_ * base + code) % m
    return hash_


def main() -> None:
    base = int(input().strip())
    m = int(input().strip())
    string = input().strip()
    print(polynomial_hash(string, base, m))


if __name__ == "__main__":
    main()
