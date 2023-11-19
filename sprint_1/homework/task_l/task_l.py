from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    sum_1 = 0
    sum_2 = 0

    for elem in shorter:
        sum_1 += ord(elem)
    
    for elem in longer:
        sum_2 += ord(elem)
    
    return chr(sum_2 - sum_1)

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
