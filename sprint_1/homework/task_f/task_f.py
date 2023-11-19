def is_palindrome(line: str) -> bool:
    left = 0
    right = len(line) - 1

    while left < right:
        
        while ord(line[left].upper()) not in range(65, 91) and not line[left].isnumeric():
            left += 1

        while ord(line[right].upper()) not in range(65, 91) and not line[right].isnumeric():
            right -= 1
        
        if line[left].upper() != line[right].upper():
            return False
        
        left += 1
        right -= 1
    
    return True


print(is_palindrome(input().strip()))
