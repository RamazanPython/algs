def to_binary(number: int) -> str:
    result = ""
    while number != 0:
        reminder = number % 2
        number //= 2
        result = str(reminder) + result
    return result or "0"

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
