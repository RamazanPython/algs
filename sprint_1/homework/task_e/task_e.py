def get_longest_word(line: str) -> str:
    current_line = ""
    max_line = ""
    
    for ch in line:
        if ch != " ":
            current_line += ch
            continue
        
        max_line = get_max_line(current_line, max_line)
        current_line = ""

    return get_max_line(current_line, max_line)

def get_max_line(current_line: str, max_line: str):
    if len(current_line) > len(max_line):
        return current_line

    return max_line


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
