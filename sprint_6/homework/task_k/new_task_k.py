import heapq


def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for v1, v2, w in graph:
        adj_list[v1].append((v2, w))
        adj_list[v2].append((v1, w))
    return adj_list


def find_shortest_paths(start_vertex, adj_list, n):
    shortest_paths = {}
    min_heap = [(0, start_vertex)]
    while min_heap:
        w1, v1 = heapq.heappop(min_heap)
        if v1 in shortest_paths:
            continue

        shortest_paths[v1] = w1
        for v2, w2 in adj_list[v1]:
            if v2 not in shortest_paths:
                heapq.heappush(min_heap, (w1 + w2, v2))
    return shortest_paths


def main():
    n, m = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(m)]
    adj_list = get_adjacency_list(n, graph)

    matrix = [[0 if i == j else -1 for j in range(n)] for i in range(n)]
    for i in range(1, n + 1):
        shortest_paths = find_shortest_paths(i, adj_list, n)
        for key, value in shortest_paths.items():
            matrix[i - 1][key - 1] = value

    print("\n".join(" ".join(map(str, arr)) for arr in matrix))


if __name__ == "__main__":
    main()
