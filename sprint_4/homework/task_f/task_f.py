def solution(words) -> list:
    res = {}

    for i in range(len(words)):
        count = [0] * 26

        for c in words[i]:
            count[ord(c) - ord('a')] += 1

        if tuple(count) in res:
            res[tuple(count)].append(i)
        else:
            res[tuple(count)] = [i]

    return list(res.values())


def main() -> None:
    amount = int(input().strip())
    words = input().strip().split()
    groups = solution(words)
    for elem in groups:
        print(" ".join(map(str, elem)))


if __name__ == "__main__":
    main()
