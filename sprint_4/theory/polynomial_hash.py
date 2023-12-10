def calculate_hash(string: str, q: int, mod: int):
    hash_ = 0
    for elem in string:
        hash_ = (hash_ * q + ord(elem)) % mod

    return hash_


print(calculate_hash(string="hash", q=123, mod=100003))
