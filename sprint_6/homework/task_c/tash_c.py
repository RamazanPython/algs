def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for edge in graph:
        v1, v2 = edge
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    for v in adj_list:
        v.sort(reverse=True)

    return adj_list


def dfs(start_vertex: int, adj_list: list[list[int]]):
    stack = [start_vertex]
    visited = set()
    res = []
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            res.append(vertex)
            visited.add(vertex)
            for neighbor in adj_list[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)

    return res


def main() -> None:
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    start_vertex = int(input().strip())
    adj_list = get_adjacency_list(n, graph)
    res = dfs(start_vertex, adj_list)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
