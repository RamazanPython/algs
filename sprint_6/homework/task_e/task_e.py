def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for edge in graph:
        v1, v2 = edge
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)

    return adj_list


def dfs(vertex: int, component_count: int, adj_list: list, colors: list):
    stack = [vertex]
    while stack:
        v = stack.pop()
        if colors[v] == -1:
            colors[v] = component_count
        for neighbor in adj_list[v]:
            if colors[neighbor] == -1:
                stack.append(neighbor)


def main():
    n, m = list(map(int, input().strip().split()))
    graph = [None] * m
    for i in range(m):
        graph[i] = list(map(int, input().strip().split()))

    colors = [-1] * (n + 1)
    adj_list = get_adjacency_list(n, graph)
    component_count = 1
    for i in range(1, len(colors)):
        if colors[i] == -1:
            dfs(i, component_count, adj_list, colors)
            component_count += 1

    components = {}
    for i in range(1, len(colors)):
        if colors[i] not in components:
            components[colors[i]] = []
        components[colors[i]].append(i)

    res = []
    for component in components.values():
        res.append(" ".join(map(str, component)))

    print(len(components))
    print("\n".join(res))


if __name__ == "__main__":
    main()
