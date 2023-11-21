phone_symbols = {
    "2": 'abc',
    "3": 'def',
    "4": 'ghi',
    "5": 'jkl',
    "6": 'mno',
    "7": 'pqrs',
    "8": 'tuv',
    "9": 'wxyz',
}


def solution(digits: str, result: list, idx: int = 0, curr_str: str = ""):
    if len(curr_str) == len(digits):
        result.append(curr_str)
        return

    symbols = phone_symbols.get(digits[idx])
    for symbol in symbols:
        solution(digits, result, idx + 1, curr_str + symbol)


def main():
    n = input().strip()
    res = []
    solution(n, res)
    format_res = " ".join(res)
    print(format_res)


if __name__ == "__main__":
    main()
