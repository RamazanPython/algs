def get_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = [[] for _ in range(vertex_amount + 1)]
    for v1, v2 in graph:
        adj_list[v1].append(v2)
        adj_list[v2].append(v1)
    return adj_list


def dfs(vertex: int, component_count: int, adj_list: list, colors: list, components: dict):
    stack = [vertex]

    while stack:
        v = stack.pop()
        if colors[v] == -1:
            colors[v] = component_count
            components[component_count].append(v)
            for neighbor in adj_list[v]:
                if colors[neighbor] == -1:
                    stack.append(neighbor)


def main():
    n, m = map(int, input().strip().split())
    graph = [list(map(int, input().strip().split())) for _ in range(m)]

    colors = [-1] * (n + 1)
    adj_list = get_adjacency_list(n, graph)
    components = {}
    component_count = 1

    for i in range(1, n + 1):
        if colors[i] == -1:
            components[component_count] = []
            dfs(i, component_count, adj_list, colors, components)
            components[component_count].sort()
            component_count += 1

    output = []
    for comp in components.values():
        output.append(" ".join(map(str, comp)))

    print(len(components))
    print("\n".join(output))


if __name__ == "__main__":
    main()
