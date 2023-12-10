def solution(rounds: list[int]) -> int:
    score_map = {0: 1, 1: -1}
    prefix_sum_length = len(rounds) + 1
    prefix_sum = [0] * prefix_sum_length
    for i in range(len(rounds)):
        score = score_map.get(rounds[i])
        prefix_sum[i + 1] = prefix_sum[i] + score

    print(prefix_sum)
    max_length = 0
    # {score: index}
    score_indices = {}
    for round_number in range(len(prefix_sum)):
        score = prefix_sum[round_number]
        if score not in score_indices:
            score_indices[score] = round_number
        else:
            start_idx = score_indices[score]
            max_length = max(max_length, round_number - start_idx)

    return max_length


def main() -> None:
    amount = int(input().strip())
    rounds = list(map(int, input().strip().split()))
    max_round = solution(rounds)
    print(max_round)


if __name__ == "__main__":
    main()
