from typing import List

def factorize(number: int) -> List[int]:
    result = []
    i = 2
    while i * i <= number:
        if number % i == 0:
            result.append(i)
            number //= i
        else:
            i = i + 1
    
    if number > 1:
        result.append(number)
    
    return result

result = factorize(int(input()))
print(" ".join(map(str, result)))