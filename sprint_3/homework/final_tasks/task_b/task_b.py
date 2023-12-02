import random

from typing import Callable


def comparator(elem1: list, elem2: list):
    name1, score1, errors1 = elem1
    name2, score2, errors2 = elem2

    if score1 > score2:
        return True
    elif score1 == score2:
        if errors1 < errors2:
            return True
        elif errors1 == errors2:
            if name1 < name2:
                return True

    return False


def quick_sort(competitors: list[list[str, int, int]], left, right, comparator: Callable):
    return []


def main():
    n = int(input().strip())
    competitors = []
    for _ in range(n):
        name, score1, score2 = input().strip().split()
        score1, score2 = int(score1), int(score2)
        competitor = [name, score1, score2]
        competitors.append(competitor)

    quick_sort(competitors, 0, len(competitors) - 1, comparator)
    for competitor in competitors:
        print(competitor[0])


if __name__ == "__main__":
    main()
