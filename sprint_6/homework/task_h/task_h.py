def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for edge in graph:
        v1, v2 = edge
        adj_list[v1].append(v2)

    for v in adj_list:
        v.sort(reverse=True)

    return adj_list


def dfs(start_vertex: int, adj_list: list[list[int]]):
    visited = set()
    stack = [start_vertex]
    while stack:
        v = stack.pop()
        visited.add(v)
        for neighbor in adj_list[v]:
            if neighbor not in visited:
                stack.append(neighbor)

    return []


def main() -> None:
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    start_vertex = 1
    adj_list = get_adjacency_list(n, graph)
    res = dfs(start_vertex, adj_list)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
