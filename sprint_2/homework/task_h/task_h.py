def is_correct_bracket_seq(brackets: str):
    stack = []
    mapping = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    for elem in brackets:
        if elem in ["(", "{", "["]:
            stack.append(elem)
            continue

        last_bracket = stack.pop() if stack else ""
        if last_bracket != mapping[elem]:
            return False

    return len(stack) == 0


def read_input():
    line = input().strip()
    return line


brackets = read_input().strip()
print(is_correct_bracket_seq(brackets))
