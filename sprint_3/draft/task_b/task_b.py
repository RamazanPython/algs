def solution(nums: str) -> list[str]:
    phone_numbers = {
        "2": 'abc',
        "3": 'def',
        "4": 'ghi',
        "5": 'jkl',
        "6": 'mno',
        "7": 'pqrs',
        "8": 'tuv',
        "9": 'wxyz'
    }
    result = []

    def backtrack(idx: int, new_str: str = ""):
        if len(nums) == len(new_str):
            result.append(new_str)
            return

        num = nums[idx]
        symbols = phone_numbers.get(num)
        if not symbols:
            return

        for symbol in symbols:
            backtrack(idx + 1, new_str + symbol)

    backtrack(0)
    return result


def main():
    nums = input().strip()
    result = solution(nums)
    print(result)


if __name__ == "__main__":
    main()
