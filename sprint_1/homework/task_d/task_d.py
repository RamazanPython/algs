from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    if len(temperatures) == 1:
        return 1
    
    days_count = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i] > temperatures[i - 1] and temperatures[i] > temperatures[i + 1]:
            days_count += 1
    
    days_count += int(temperatures[0] > temperatures[1]) + int(temperatures[-1] > temperatures[-2])
    
    return days_count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
