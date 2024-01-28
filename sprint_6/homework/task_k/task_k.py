import heapq


def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for v1, v2, w in graph:
        adj_list[v1].append((v2, w))
        adj_list[v2].append((v1, w))

    return adj_list


def main():
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    adj_list = get_adjacency_list(n, graph)
    paths = []
    for i in range(1, n + 1):
        shortest_paths = {}
        min_heap = [(0, i)]
        while min_heap:
            w1, v1 = heapq.heappop(min_heap)
            if v1 in shortest_paths:
                continue

            shortest_paths[v1] = w1
            for v2, w2 in adj_list[v1]:
                if v2 not in shortest_paths:
                    heapq.heappush(min_heap, (w1 + w2, v2))

        paths.append(shortest_paths)

    matrix = [[-1 for _ in range(n)] for _ in range(n)]
    for idx in range(1, n + 1):
        for key, value in paths[idx - 1].items():
            matrix[idx - 1][key - 1] = value

    output = []
    for arr in matrix:
        output.append(" ".join(map(str, arr)))

    print("\n".join(output))


if __name__ == "__main__":
    main()
