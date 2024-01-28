def get_adjecency_matrix(vertex_amount: int, graph: list[list[int]]):
    matrix = [
        [0] * vertex_amount
        for _ in range(vertex_amount)
    ]
    for edge in graph:
        v1, v2 = edge
        matrix[v1 - 1][v2 - 1] = 1

    return matrix


def main() -> None:
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    matrix = get_adjecency_matrix(n, graph)
    res = [None] * n
    for idx, arr in enumerate(matrix):
        res[idx] = " ".join(map(str, arr))

    print("\n".join(res))


if __name__ == "__main__":
    main()
