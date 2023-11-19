def is_power_of_four(number: int) -> bool:
    limit = number // 2
    for i in range(limit + 1):
        if 4 ** i == number:
            return True
        if 4 ** i > number:
            return False
    
    return False


print(is_power_of_four(int(input())))
