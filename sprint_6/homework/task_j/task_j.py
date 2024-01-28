def convert_to_adjacency_list(vertex_amount: int, graph: list[list[int]]):
    adj_list = {i: [] for i in range(1, vertex_amount + 1)}

    for v1, v2 in graph:
        adj_list[v1].append(v2)

    return adj_list


def top_sort(vertex: int, adj_list: dict, stack: list, colors: list):
    colors[vertex] = "grey"

    for neighbour in adj_list[vertex]:
        if colors[neighbour] == "white":
            top_sort(neighbour, adj_list, stack, colors)

    colors[vertex] = "black"
    stack.append(vertex)


def main():
    n, m = list(map(int, input().strip().split()))
    graph = []
    for _ in range(m):
        v1, v2 = list(map(int, input().strip().split()))
        graph.append([v1, v2])

    adj_list = convert_to_adjacency_list(n, graph)
    colors = ["white"] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        if colors[i] == "white":
            top_sort(i, adj_list, stack, colors)

    print(" ".join(map(str, reversed(stack))))


if __name__ == "__main__":
    main()
