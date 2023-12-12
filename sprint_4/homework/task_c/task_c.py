def get_prefix_hash_sum(string: str, base: int, mod: int) -> list:
    prefix_hash_sum_length = len(string) + 1
    prefix_hash_sum = [0] * prefix_hash_sum_length
    prefix_hash_sum[1] = ord(string[0])
    for i in range(2, prefix_hash_sum_length):
        prefix_hash_sum[i] = (prefix_hash_sum[i - 1] * base + ord(string[i - 1])) % mod

    return prefix_hash_sum


def fast_power(num: int, power: int) -> int:
    s, v, c = 1, power, num
    while v > 0:
        if v % 2 == 1:
            s = s * c
        v = v >> 1
        c = c * c
    return s


def main() -> None:
    base = int(input().strip())
    mod = int(input().strip())
    string = input().strip()
    amount = int(input().strip())
    borders = []
    max_power = 0
    for _ in range(amount):
        l, r = list(map(int, input().strip().split()))
        current_power = r - l + 1
        if current_power > max_power:
            max_power = current_power
        borders.append([l, r])

    powers = [1] * (max_power + 1)
    for i in range(1, max_power + 1):
        powers[i] = (powers[i - 1] * base) % mod

    hashes = get_prefix_hash_sum(string, base, mod)
    for border in borders:
        l, r = border
        power = r - l + 1
        power_value = powers[power]
        result = (hashes[r] + mod - hashes[l - 1] * power_value % mod) % mod
        print(result)


if __name__ == "__main__":
    main()
